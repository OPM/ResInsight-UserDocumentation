# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import SimulationWell_pb2 as SimulationWell__pb2


class SimulationWellStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSimulationWellStatus = channel.unary_unary(
                '/rips.SimulationWell/GetSimulationWellStatus',
                request_serializer=SimulationWell__pb2.SimulationWellRequest.SerializeToString,
                response_deserializer=SimulationWell__pb2.SimulationWellStatus.FromString,
                )
        self.GetSimulationWellCells = channel.unary_unary(
                '/rips.SimulationWell/GetSimulationWellCells',
                request_serializer=SimulationWell__pb2.SimulationWellRequest.SerializeToString,
                response_deserializer=SimulationWell__pb2.SimulationWellCellInfoArray.FromString,
                )


class SimulationWellServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSimulationWellStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimulationWellCells(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimulationWellServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSimulationWellStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimulationWellStatus,
                    request_deserializer=SimulationWell__pb2.SimulationWellRequest.FromString,
                    response_serializer=SimulationWell__pb2.SimulationWellStatus.SerializeToString,
            ),
            'GetSimulationWellCells': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimulationWellCells,
                    request_deserializer=SimulationWell__pb2.SimulationWellRequest.FromString,
                    response_serializer=SimulationWell__pb2.SimulationWellCellInfoArray.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rips.SimulationWell', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimulationWell(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSimulationWellStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.SimulationWell/GetSimulationWellStatus',
            SimulationWell__pb2.SimulationWellRequest.SerializeToString,
            SimulationWell__pb2.SimulationWellStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSimulationWellCells(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rips.SimulationWell/GetSimulationWellCells',
            SimulationWell__pb2.SimulationWellRequest.SerializeToString,
            SimulationWell__pb2.SimulationWellCellInfoArray.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
