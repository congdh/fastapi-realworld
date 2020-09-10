import uvicorn
from fastapi import FastAPI

from app.api import api
from app.db import base_class  # noqa
from app.db import session

app = FastAPI()

base_class.Base.metadata.create_all(bind=session.engine)

app.include_router(api.api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
