import random

def load_proxies():
    with open("./proxies.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

def load_random_proxy():
    proxies = load_proxies()
    if not proxies:
        return None
    proxy = random.choice(proxies)
    return {
        "http://": proxy,
        "https://": proxy
    }
