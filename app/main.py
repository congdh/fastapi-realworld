import uvicorn
from fastapi import FastAPI, Header, HTTPException

from app.api import api
from app.db import base_class, session  # noqa

app = FastAPI()

base_class.Base.metadata.create_all(bind=session.engine)


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(
    api.api_router,
    prefix="/api"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
