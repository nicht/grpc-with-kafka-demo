import time
from concurrent import futures

import grpc

# import the generated classes
from grpc_services_demo.category.grpc_services_demo.protos import category_pb2_grpc

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
category_pb2_grpc.add_CategoryServicer_to_server(
    category_pb2_grpc.CategoryServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
