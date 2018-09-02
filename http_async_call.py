import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            'https://webhook.site/#/f8394573-d4cf-4d0e-92d2-72471d6df362/b0498fcd-9ed3-47be-8914-3e7c9566f938/0'
        )
        for i in range(3)
    ]
    for response in await asyncio.gather(*futures):
        print(response.headers.get('Date'))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())



