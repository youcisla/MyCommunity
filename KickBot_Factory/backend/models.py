import aiosqlite

async def init_db():
    async with aiosqlite.connect("db.sqlite3") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            username TEXT,
            password TEXT,
            verified INTEGER
        )
        """)
        await db.commit()

async def save_account(email, username, password, verified):
    async with aiosqlite.connect("db.sqlite3") as db:
        await db.execute("""
        INSERT INTO accounts (email, username, password, verified)
        VALUES (?, ?, ?, ?)
        """, (email, username, password, verified))
        await db.commit()
