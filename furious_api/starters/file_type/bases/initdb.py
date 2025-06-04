from app.core.database import Base, engine


async def create_tables():        
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_tables())