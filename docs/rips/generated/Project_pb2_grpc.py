# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Case_pb2 as Case__pb2
import Definitions_pb2 as Definitions__pb2
import PdmObject_pb2 as PdmObject__pb2


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
                )
        self.GetSelectedCases = channel.unary_unary(
                '/rips.Project/GetSelectedCases',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseInfoArray.FromString,
                )
        self.GetAllCaseGroups = channel.unary_unary(
                '/rips.Project/GetAllCaseGroups',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseGroups.FromString,
                )
        self.GetAllCases = channel.unary_unary(
                '/rips.Project/GetAllCases',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=Case__pb2.CaseInfoArray.FromString,
                )
        self.GetCasesInGroup = channel.unary_unary(
                '/rips.Project/GetCasesInGroup',
                request_serializer=Case__pb2.CaseGroup.SerializeToString,
                response_deserializer=Case__pb2.CaseInfoArray.FromString,
                )
        self.GetPdmObject = channel.unary_unary(
                '/rips.Project/GetPdmObject',
                request_serializer=Definitions__pb2.Empty.SerializeToString,
                response_deserializer=PdmObject__pb2.PdmObject.FromString,
                )


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
        return grpc.experimental.unary_unary(request, target, '/rips.Project/GetCurrentCase',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/rips.Project/GetSelectedCases',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseInfoArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/rips.Project/GetAllCaseGroups',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseGroups.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/rips.Project/GetAllCases',
            Definitions__pb2.Empty.SerializeToString,
            Case__pb2.CaseInfoArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/rips.Project/GetCasesInGroup',
            Case__pb2.CaseGroup.SerializeToString,
            Case__pb2.CaseInfoArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/rips.Project/GetPdmObject',
            Definitions__pb2.Empty.SerializeToString,
            PdmObject__pb2.PdmObject.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
