#!/usr/bin/env python

import faust

app = faust.App(
    'grpc_services_with_kafka_demo',
    broker='kafka://localhost:9092',
)

search_results = app.topic('search_results')


@app.agent(search_results)
async def list_results(terms):
    async for term in terms:
        print(f'Consuming the search_results topics with search results: {term}')


if __name__ == '__main__':
    app.main()
