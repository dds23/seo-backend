import json
from app.godaddy.api import router as godaddy_router
from app.google.api import router as google_router
from app.moz.api import router as moz_router
from fastapi import FastAPI, Request
from app.utils.common import CustomException
from fastapi.responses import JSONResponse

from . import __title__, __version__, __description__

api = FastAPI(
    title=__title__,
    description=__description__,
    version=__version__,
)

api.include_router(godaddy_router)
api.include_router(google_router)
api.include_router(moz_router)


@api.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message},
    )


with open("openapi.json", "w") as f:
    f.write(json.dumps(api.openapi(), indent=4))
