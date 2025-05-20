import httpx
import random
from proxy import load_random_proxy

async def safe_request(method, url, **kwargs):
    proxies = [load_random_proxy() for _ in range(5)]
    for proxy in proxies:
        try:
            async with httpx.AsyncClient(proxies=f"http://{proxy}", timeout=10) as client:
                response = await client.request(method, url, **kwargs)
                response.raise_for_status()
                return response
        except Exception:
            continue
    raise Exception("All proxy attempts failed")
