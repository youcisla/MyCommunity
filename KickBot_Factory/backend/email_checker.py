import asyncio
import re
from utils import safe_request

async def get_verification_link(email):
    login = email.split('@')[0]
    domain = email.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"

    for _ in range(30):
        r = await safe_request("GET", url)
        if r.status_code == 200 and r.json():
            msg_id = r.json()[0]["id"]
            msg_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
            msg = await safe_request("GET", msg_url)
            link = re.search(r'https://kick\.com/verify-email\?token=\S+', msg.text)
            if link:
                return link.group(0)
        await asyncio.sleep(2)
    return None
