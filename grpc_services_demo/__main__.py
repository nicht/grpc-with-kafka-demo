from concurrent.futures import ThreadPoolExecutor as PoolExecutor

import asyncio
import grpc

# import the generated classes
from grpc_services_demo.category.grpc_services_demo.protos import category_pb2, category_pb2_grpc
from grpc_services_demo.department.grpc_services_demo.protos import department_pb2, department_pb2_grpc
from grpc_services_demo.user.grpc_services_demo.protos import user_pb2, user_pb2_grpc

# open a gRPC channel
category_channel = grpc.insecure_channel('localhost:50051')
department_channel = grpc.insecure_channel('localhost:50052')
user_channel = grpc.insecure_channel('localhost:50053')

# create a stub (client)
stub_category = category_pb2_grpc.CategoryStub(category_channel)
stub_department = department_pb2_grpc.DepartmentStub(department_channel)
stub_user = user_pb2_grpc.UserStub(user_channel)


def async_calls(position):
    category_search = category_pb2.CategoryRequest(search_term="Rodolfo")
    department_search = department_pb2.DepartmentRequest(search_term="Rodolfo")
    user_search = user_pb2.UserRequest(search_term="Rodolfo")

    department_response = stub_department.Search(department_search)
    user_response = stub_user.Search(user_search)
    category_response = stub_category.Search(category_search)

    print('Called them all, times: {}'.format(position))


# create a thread pool of 4 threads
with PoolExecutor(max_workers=4) as executor:
    # distribute the 1000 URLs among 4 threads in the pool
    # _ is the body of each page that I'm ignoring right now
    for _ in executor.map(async_calls, [0] * 150): ...
