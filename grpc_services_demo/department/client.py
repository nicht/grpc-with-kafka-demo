import grpc

# open a gRPC channel
from grpc_services_demo.department.grpc_services_demo.protos import department_pb2_grpc, department_pb2

# import the generated classes

channel = grpc.insecure_channel('localhost:50052')

# create a stub (client)
stub = department_pb2_grpc.DepartmentStub(channel)

# create a valid request message
departmentSearch = department_pb2.DepartmentRequest(search_term="Rodolfo")

# make the call
response = stub.Search(departmentSearch)

# et voilà
print(response)
