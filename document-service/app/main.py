from fastapi import FastAPI
from routers.document import router
from core.config import settings
from models import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await init_db()
    yield


app = FastAPI(title="Document Service", lifespan=lifespan)

# Include document API router
app.include_router(router, prefix="/api")
print(settings.PORT, __name__)
if __name__ == "__main__":
    import uvicorn
    print(settings.PORT)
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
