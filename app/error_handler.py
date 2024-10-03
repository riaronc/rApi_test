import logging
import ssl

import httpx
from starlette.responses import JSONResponse

from app import app


@app.exception_handler(ssl.SSLWantReadError)
async def handle_ssl_error(request, exc):
    logging.debug(request)
    logging.error(f"{exc}")
    return JSONResponse(
        status_code=400,
        content={"Internal SSL read error"},
    )


@app.exception_handler(httpx.ReadTimeout)
async def handle_timeout_error(request, exc):
    logging.debug(request)
    logging.error(f"{exc}")
    return JSONResponse(
        status_code=400,
        content={"Request timeout"},
    )
