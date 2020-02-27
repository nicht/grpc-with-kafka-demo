import time
from concurrent import futures

import grpc

# import the generated classes
from grpc_services_demo.user.grpc_services_demo.protos import user_pb2_grpc

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# to add the defined class to the server
user_pb2_grpc.add_UserServicer_to_server(
    user_pb2_grpc.UserServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
