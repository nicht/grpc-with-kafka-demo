#!/usr/bin/env python

import faust

app = faust.App(
    'grpc_services_with_kafka_demo',
    broker='kafka://localhost:9092',
)

search_results = app.topic('search_results')
department_consumer = app.topic('department')


@app.agent(department_consumer)
async def search(terms):
    async for term in terms:
        print(f'Consuming the department topics with the search term: {term.get("search_term")}')
        await populate_search_results()


async def populate_search_results():
    await search_results.send(
        value={'department_name': 'Department test', 'department_id': '12345678', 'user_id': '1234'})


if __name__ == '__main__':
    app.main()
