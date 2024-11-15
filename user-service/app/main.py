from fastapi import FastAPI
from routers.routes import router
from core.config import settings
from db import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await init_db()
    yield


app = FastAPI(title="User Service", lifespan=lifespan)

# Include API routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=settings.HOST,
                port=settings.PORT, reload=True)
