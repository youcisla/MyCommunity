import httpx
import random
import string

def generate_email():
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{prefix}@1secmail.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

async def is_username_available(username):
    url = f"https://kick.com/api/v1/signup/verify/username?username={username}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.status_code == 200

async def create_account(email, username, password, dob):
    url = "https://kick.com/api/v1/signup"
    payload = {
        "email": email,
        "username": username,
        "password": password,
        "dob": dob,
        "agree_to_terms": True
    }
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=payload)
        return r.status_code == 200
