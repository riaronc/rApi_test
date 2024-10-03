import logging

import dotenv
import uvicorn


from app import app


if __name__ == '__main__':

    logging.info("Loaded .env.stage file")
    uvicorn.run("main:app", port=6016, reload=True)
