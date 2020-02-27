import grpc

# import the generated classes
from grpc_services_demo.user.grpc_services_demo.protos import user_pb2, user_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50053')

# create a stub (client)
stub = user_pb2_grpc.UserStub(channel)

# create a valid request message
userSearch = user_pb2.UserRequest(search_term="Rodolfo")

# make the call
response = stub.Search(userSearch)

# et voilà
print(response)
