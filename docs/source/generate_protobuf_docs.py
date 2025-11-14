#!/usr/bin/env python3
"""
Script to generate Protocol Buffer documentation from .proto files.

This script parses .proto files from the docs/proto directory and generates
RST documentation for inclusion in Sphinx documentation.

Usage:
    python generate_protobuf_docs.py

The script will update docs/source/ProtobufStructures.rst with current proto definitions.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional


class ProtoMessage:
    """Represents a Protocol Buffer message."""
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.fields: List[Dict] = []
        self.is_oneof = False


class ProtoEnum:
    """Represents a Protocol Buffer enum."""
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.values: List[Tuple[str, int, str]] = []


class ProtoService:
    """Represents a Protocol Buffer service."""
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.methods: List[Dict] = []


class ProtoParser:
    """Parser for Protocol Buffer .proto files."""

    def __init__(self, proto_dir: Path):
        self.proto_dir = proto_dir
        self.messages: Dict[str, List[ProtoMessage]] = {}
        self.enums: Dict[str, List[ProtoEnum]] = {}
        self.services: Dict[str, List[ProtoService]] = {}

    def parse_all_files(self):
        """Parse all .proto files in the proto directory."""
        if not self.proto_dir.exists():
            print(f"Warning: Proto directory {self.proto_dir} does not exist")
            return

        proto_files = sorted(self.proto_dir.glob("*.proto"))
        for proto_file in proto_files:
            self.parse_file(proto_file)

    def parse_file(self, proto_file: Path):
        """Parse a single .proto file."""
        print(f"Parsing {proto_file.name}...")

        with open(proto_file, 'r', encoding='utf-8') as f:
            content = f.read()

        file_key = proto_file.stem
        self.messages[file_key] = []
        self.enums[file_key] = []
        self.services[file_key] = []

        # Remove comments and get leading comments
        lines = content.split('\n')
        cleaned_lines = []
        comment_buffer = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith('//'):
                # Store comment for next declaration
                comment_text = stripped[2:].strip()
                comment_buffer.append(comment_text)
            else:
                cleaned_lines.append((line, ' '.join(comment_buffer)))
                comment_buffer = []

        # Parse messages
        self._parse_messages(cleaned_lines, file_key)

        # Parse enums
        self._parse_enums(cleaned_lines, file_key)

        # Parse services
        self._parse_services(cleaned_lines, file_key)

    def _parse_messages(self, lines: List[Tuple[str, str]], file_key: str):
        """Parse message definitions."""
        i = 0
        while i < len(lines):
            line, comment = lines[i]

            # Match message declaration
            msg_match = re.search(r'message\s+(\w+)\s*\{', line)
            if msg_match:
                msg_name = msg_match.group(1)
                msg = ProtoMessage(msg_name, comment)

                # Parse fields
                i += 1
                brace_count = 1
                while i < len(lines) and brace_count > 0:
                    field_line, field_comment = lines[i]

                    if '{' in field_line:
                        brace_count += field_line.count('{')
                    if '}' in field_line:
                        brace_count -= field_line.count('}')

                    if brace_count == 0:
                        break

                    # Parse field: type name = number;
                    field_match = re.search(
                        r'(optional|repeated|required)?\s*(\w+)\s+(\w+)\s*=\s*(\d+)',
                        field_line
                    )
                    if field_match:
                        modifier = field_match.group(1) or ''
                        field_type = field_match.group(2)
                        field_name = field_match.group(3)

                        msg.fields.append({
                            'name': field_name,
                            'type': field_type,
                            'modifier': modifier,
                            'description': field_comment
                        })

                    i += 1

                self.messages[file_key].append(msg)

            i += 1

    def _parse_enums(self, lines: List[Tuple[str, str]], file_key: str):
        """Parse enum definitions."""
        i = 0
        while i < len(lines):
            line, comment = lines[i]

            enum_match = re.search(r'enum\s+(\w+)\s*\{', line)
            if enum_match:
                enum_name = enum_match.group(1)
                enum_obj = ProtoEnum(enum_name, comment)

                i += 1
                while i < len(lines):
                    enum_line, enum_comment = lines[i]

                    if '}' in enum_line:
                        break

                    # Parse enum value: NAME = number;
                    value_match = re.search(r'(\w+)\s*=\s*(\d+)', enum_line)
                    if value_match:
                        value_name = value_match.group(1)
                        value_num = int(value_match.group(2))
                        enum_obj.values.append((value_name, value_num, enum_comment))

                    i += 1

                self.enums[file_key].append(enum_obj)

            i += 1

    def _parse_services(self, lines: List[Tuple[str, str]], file_key: str):
        """Parse service definitions."""
        i = 0
        while i < len(lines):
            line, comment = lines[i]

            service_match = re.search(r'service\s+(\w+)\s*\{', line)
            if service_match:
                service_name = service_match.group(1)
                service = ProtoService(service_name, comment)

                i += 1
                while i < len(lines):
                    method_line, method_comment = lines[i]

                    if '}' in method_line:
                        break

                    # Parse rpc method: rpc MethodName (RequestType) returns (ResponseType);
                    method_match = re.search(
                        r'rpc\s+(\w+)\s*\(\s*(\w+)\s*\)\s*returns\s*\(\s*(\w+)\s*\)',
                        method_line
                    )
                    if method_match:
                        method_name = method_match.group(1)
                        request_type = method_match.group(2)
                        response_type = method_match.group(3)

                        service.methods.append({
                            'name': method_name,
                            'request': request_type,
                            'response': response_type,
                            'description': method_comment
                        })

                    i += 1

                self.services[file_key].append(service)

            i += 1


class RstGenerator:
    """Generate RST documentation from parsed proto data."""

    # Mapping of proto types to Python types
    TYPE_MAP = {
        'string': 'str',
        'int32': 'int',
        'int64': 'int',
        'uint32': 'int',
        'uint64': 'int',
        'sint32': 'int',
        'sint64': 'int',
        'fixed32': 'int',
        'fixed64': 'int',
        'sfixed32': 'int',
        'sfixed64': 'int',
        'bool': 'bool',
        'float': 'float',
        'double': 'float',
        'bytes': 'bytes',
    }

    # Important messages to highlight
    IMPORTANT_MESSAGES = [
        'SimulatorTableData',
        'SimulatorCompdatEntry',
        'SimulatorWelspecsEntry',
        'SimulatorTableRequest',
        'Vec3d',
        'Vec3i',
        'CellCenters',
        'CellCorners',
    ]

    def __init__(self, parser: ProtoParser):
        self.parser = parser

    def generate(self, output_file: Path):
        """Generate complete RST documentation."""
        content = self._generate_header()
        content += self._generate_overview()
        content += self._generate_important_structures()
        content += self._generate_all_structures()
        content += self._generate_usage_examples()
        content += self._generate_footer()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Generated documentation: {output_file}")

    def _generate_header(self) -> str:
        return """Protocol Buffer Data Structures
=================================

.. note::
   This page is automatically generated from the Protocol Buffer definition files.
   Last updated: Generated by ``generate_protobuf_docs.py``

"""

    def _generate_overview(self) -> str:
        return """Overview
--------

ResInsight uses Protocol Buffers (protobuf) for efficient data serialization and communication between Python and the ResInsight application via gRPC. The protobuf definitions define the structure of data that can be exchanged with ResInsight.

The generated Python classes from these protobuf files are used as return types and parameters in many rips API methods.

Source Files
~~~~~~~~~~~~

The Protocol Buffer definition files (.proto) are automatically downloaded from the `ResInsight repository <https://github.com/OPM/ResInsight/tree/dev/GrpcInterface/GrpcProtos>`_ and stored in the ``docs/proto`` directory.

The generated Python files are located in ``docs/rips/generated/`` and include:

"""

    def _generate_important_structures(self) -> str:
        """Generate documentation for important/commonly used structures."""
        content = "\nKey Data Structures\n-------------------\n\n"
        content += "These are the most commonly used Protocol Buffer structures in the ResInsight Python API.\n\n"

        for msg_name in self.IMPORTANT_MESSAGES:
            for file_key, messages in self.parser.messages.items():
                for msg in messages:
                    if msg.name == msg_name:
                        content += self._format_message(msg, file_key, is_important=True)

        return content

    def _generate_all_structures(self) -> str:
        """Generate documentation for all structures organized by file."""
        content = "\nComplete Structure Reference\n-----------------------------\n\n"

        for file_key in sorted(self.parser.messages.keys()):
            if not self.parser.messages[file_key] and not self.parser.enums[file_key]:
                continue

            # File header
            file_title = f"{file_key}.proto"
            content += f"\n{file_title}\n"
            content += "~" * len(file_title) + "\n\n"

            # Messages
            for msg in self.parser.messages[file_key]:
                if msg.name not in self.IMPORTANT_MESSAGES:
                    content += self._format_message(msg, file_key, is_important=False)

            # Enums
            for enum in self.parser.enums[file_key]:
                content += self._format_enum(enum)

            # Services
            for service in self.parser.services[file_key]:
                content += self._format_service(service)

        return content

    def _format_message(self, msg: ProtoMessage, file_key: str, is_important: bool) -> str:
        """Format a message as RST."""
        content = f"\n{msg.name}\n"
        content += ("^" if is_important else "\"") * len(msg.name) + "\n\n"

        if msg.description:
            content += f"{msg.description}\n\n"

        content += f"**Source:** ``{file_key}.proto``\n\n"

        if msg.fields:
            # Separate required and optional fields
            required_fields = [f for f in msg.fields if f['modifier'] != 'optional']
            optional_fields = [f for f in msg.fields if f['modifier'] == 'optional']
            repeated_fields = [f for f in msg.fields if f['modifier'] == 'repeated']

            if required_fields:
                content += "**Attributes:**\n\n"
                for field in required_fields:
                    if field['modifier'] != 'repeated':
                        content += self._format_field(field)

            if repeated_fields:
                content += "\n**Repeated Fields:**\n\n"
                for field in repeated_fields:
                    content += self._format_field(field)

            if optional_fields:
                content += "\n**Optional Attributes:**\n\n"
                for field in optional_fields:
                    content += self._format_field(field)

        content += "\n"
        return content

    def _format_field(self, field: Dict) -> str:
        """Format a field as RST."""
        python_type = self.TYPE_MAP.get(field['type'], field['type'])

        if field['modifier'] == 'repeated':
            python_type = f"list[{python_type}]"
        elif field['modifier'] == 'optional':
            python_type = f"{python_type} | None"

        desc = f" - {field['description']}" if field['description'] else ""
        return f"* ``{field['name']}`` ({python_type}){desc}\n"

    def _format_enum(self, enum: ProtoEnum) -> str:
        """Format an enum as RST."""
        content = f"\n{enum.name}\n"
        content += "\"" * len(enum.name) + "\n\n"

        if enum.description:
            content += f"{enum.description}\n\n"

        if enum.values:
            content += "**Values:**\n\n"
            for name, value, desc in enum.values:
                desc_text = f" - {desc}" if desc else ""
                content += f"* ``{name}`` = {value}{desc_text}\n"

        content += "\n"
        return content

    def _format_service(self, service: ProtoService) -> str:
        """Format a service as RST."""
        content = f"\n{service.name} Service\n"
        content += "\"" * (len(service.name) + 8) + "\n\n"

        if service.description:
            content += f"{service.description}\n\n"

        if service.methods:
            content += "**Methods:**\n\n"
            for method in service.methods:
                desc = f" - {method['description']}" if method['description'] else ""
                content += f"* ``{method['name']}({method['request']}) -> {method['response']}``{desc}\n"

        content += "\n"
        return content

    def _generate_usage_examples(self) -> str:
        return """
Usage Examples
--------------

Working with SimulatorTableData
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :meth:`rips.WellPath.completion_data` method returns a ``SimulatorTableData`` object containing well completion information:

.. code-block:: python

    import rips

    # Connect to ResInsight
    resinsight = rips.Instance.find()
    project = resinsight.project

    # Get a case
    case = project.cases()[0]

    # Get well path
    well_path = project.well_paths()[0]

    # Get completion data
    completion_data = well_path.completion_data(case.id)

    # Access COMPDAT entries
    for compdat_entry in completion_data.compdat:
        print(f"Well: {compdat_entry.well_name}")
        print(f"  Grid location: i={compdat_entry.grid_i}, j={compdat_entry.grid_j}")
        print(f"  K layers: {compdat_entry.upper_k} to {compdat_entry.lower_k}")
        print(f"  Status: {compdat_entry.open_shut_flag}")
        if compdat_entry.HasField('transmissibility'):
            print(f"  Transmissibility: {compdat_entry.transmissibility}")
        if compdat_entry.HasField('diameter'):
            print(f"  Diameter: {compdat_entry.diameter}")

    # Access WELSPECS entries
    for welspecs_entry in completion_data.welspecs:
        print(f"Well: {welspecs_entry.well_name}")
        print(f"  Group: {welspecs_entry.group_name}")
        print(f"  Phase: {welspecs_entry.phase}")
        print(f"  Grid location: i={welspecs_entry.grid_i}, j={welspecs_entry.grid_j}")
        if welspecs_entry.HasField('bhp_depth'):
            print(f"  BHP Depth: {welspecs_entry.bhp_depth}")

Working with Optional Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many protobuf messages contain optional fields. Use the ``HasField()`` method to check if an optional field is set:

.. code-block:: python

    # Check if optional field is set before accessing
    if entry.HasField('saturation'):
        saturation_value = entry.saturation
    else:
        saturation_value = None

    # Or use getattr with a default value
    saturation = getattr(entry, 'saturation', None)

Working with Vec3d and Vec3i
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many protobuf messages use ``Vec3d`` (3D double vector) or ``Vec3i`` (3D integer vector) for coordinates:

.. code-block:: python

    # Vec3d example (cell centers, coordinates)
    cell_centers = grid.cell_centers()
    for center in cell_centers.centers:
        print(f"Center: x={center.x}, y={center.y}, z={center.z}")

    # Vec3i example (grid indices)
    grid_dims = grid.dimensions()
    print(f"Grid dimensions: i={grid_dims.i}, j={grid_dims.j}, k={grid_dims.k}")
"""

    def _generate_footer(self) -> str:
        return """
See Also
--------

* :doc:`rips` - Main API documentation
* :doc:`GeneratedClasses` - Auto-generated class documentation
* :doc:`PythonExamples` - Python code examples

External Resources
~~~~~~~~~~~~~~~~~~

* `Protocol Buffers Documentation <https://protobuf.dev/>`_
* `gRPC Python Documentation <https://grpc.io/docs/languages/python/>`_
* `ResInsight Source Repository <https://github.com/OPM/ResInsight>`_
"""


def main():
    """Main function."""
    # Get paths
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent
    proto_dir = docs_dir / 'proto'
    output_file = script_dir / 'ProtobufStructures.rst'

    print("=" * 60)
    print("Generating Protocol Buffer Documentation")
    print("=" * 60)
    print(f"Proto directory: {proto_dir}")
    print(f"Output file: {output_file}")
    print()

    # Parse proto files
    parser = ProtoParser(proto_dir)
    parser.parse_all_files()

    # Generate RST documentation
    generator = RstGenerator(parser)
    generator.generate(output_file)

    print()
    print("=" * 60)
    print("Documentation generation complete!")
    print("=" * 60)


if __name__ == '__main__':
    main()
