# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import Case_pb2 as Case__pb2
import Definitions_pb2 as Definitions__pb2
import PdmObject_pb2 as PdmObject__pb2

GRPC_GENERATED_VERSION = '1.63.2'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in Project_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ProjectStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCurrentCase = channel.unary_unary(
                '/rips.Project/GetCurrentCase',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseRequest.FromString,
                _registered_method=True)
        self.GetSelectedCases = channel.unary_unary(
                '/rips.Project/GetSelectedCases',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseInfoArray.FromString,
                _registered_method=True)
        self.GetAllCaseGroups = channel.unary_unary(
                '/rips.Project/GetAllCaseGroups',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseGroups.FromString,
                _registered_method=True)
        self.GetAllCases = channel.unary_unary(
                '/rips.Project/GetAllCases',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseInfoArray.FromString,
                _registered_method=True)
        self.GetCasesInGroup = channel.unary_unary(
                '/rips.Project/GetCasesInGroup',
                request_serializer=Case__pb2.CaseGroup.SerializeToString,
                response_deserializer=Case__pb2.CaseInfoArray.FromString,
                _registered_method=True)
        self.GetPdmObject = channel.unary_unary(
                '/rips.Project/GetPdmObject',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=PdmObject__pb2.PdmObject.FromString,
                _registered_method=True)


class ProjectServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCurrentCase(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelectedCases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllCaseGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllCases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCasesInGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPdmObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCurrentCase': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentCase,
                    request_deserializer=Definitions__pb2.Empty.FromString,
                    response_serializer=Case__pb2.CaseRequest.SerializeToString,
            ),
            'GetSelectedCases': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelectedCases,
                    request_deserializer=Definitions__pb2.Empty.FromString,
                    response_serializer=Case__pb2.CaseInfoArray.SerializeToString,
            ),
            'GetAllCaseGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCaseGroups,
                    request_deserializer=Definitions__pb2.Empty.FromString,
                    response_serializer=Case__pb2.CaseGroups.SerializeToString,
            ),
            'GetAllCases': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllCases,
                    request_deserializer=Definitions__pb2.Empty.FromString,
                    response_serializer=Case__pb2.CaseInfoArray.SerializeToString,
            ),
            'GetCasesInGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCasesInGroup,
                    request_deserializer=Case__pb2.CaseGroup.FromString,
                    response_serializer=Case__pb2.CaseInfoArray.SerializeToString,
            ),
            'GetPdmObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPdmObject,
                    request_deserializer=Definitions__pb2.Empty.FromString,
                    response_serializer=PdmObject__pb2.PdmObject.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rips.Project', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Project(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCurrentCase(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/rips.Project/GetCurrentCase',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseRequest.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSelectedCases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/rips.Project/GetSelectedCases',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseInfoArray.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllCaseGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/rips.Project/GetAllCaseGroups',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseGroups.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllCases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/rips.Project/GetAllCases',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseInfoArray.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCasesInGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/rips.Project/GetCasesInGroup',
            Case__pb2.CaseGroup.SerializeToString,
            Case__pb2.CaseInfoArray.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPdmObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/rips.Project/GetPdmObject',
            Definitions__pb2.Empty.SerializeToString,
            PdmObject__pb2.PdmObject.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
