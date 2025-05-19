from fastapi import FastAPI
from create_account import generate_email, generate_username, generate_password, is_username_available, create_account
from email_checker import get_verification_link
from models import init_db, save_account
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/create")
async def create():
    email = generate_email()
    username = generate_username()
    while not await is_username_available(username):
        username = generate_username()
    password = generate_password()
    dob = "1995-01-01"
    success = await create_account(email, username, password, dob)
    verified = 0
    if success:
        link = await get_verification_link(email)
        if link:
            async with httpx.AsyncClient() as client:
                await client.get(link)
                verified = 1
    await save_account(email, username, password, verified)
    return {
        "email": email,
        "username": username,
        "password": password,
        "verified": bool(verified)
    }
