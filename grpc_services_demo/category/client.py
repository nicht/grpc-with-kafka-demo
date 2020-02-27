import grpc

# import the generated classes
from grpc_services_demo.category.grpc_services_demo.protos import category_pb2, category_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = category_pb2_grpc.CategoryStub(channel)

# create a valid request message
categorySearch = category_pb2.CategoryRequest(search_term="Rodolfo")

# make the call
response = stub.Search(categorySearch)

# et voilà
print(response)
