from django.http.response import JsonResponse
from datetime import datetime
import asyncio
import aiohttp


url = 'https://api.coingate.com/v2/rates/merchant/USD/RUB'


async def get_async_current_usd() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, allow_redirects=True) as response:
            now = datetime.utcnow().strftime('%H:%M:%S')
            res = await response.text()
            data = {
                "time": now,
                "USD": "1",
                "RUB": res,
            }
            return data

async def main():
    latest = []
    id_counter = 1
    for _ in range(10):
        result = await get_async_current_usd()
        result["id"] = id_counter
        id_counter += 1
        print(result)
        latest.append(result)
        await asyncio.sleep(3)
    return latest

if __name__ == "__main__":
    asyncio.run(main())

async def get(request):
    data = await main()
    return JsonResponse({"data": data})

