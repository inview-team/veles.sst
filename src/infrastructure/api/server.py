import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.DEBUG)

from usecases.command import CommandUseCases
from . import routes

def get_app(usecases: CommandUseCases) -> FastAPI:
    app = FastAPI()
    routes.command.usecases = usecases
    origins = [
        "*"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Add the HTTP methods you want to support
        allow_headers=["*"],  # Allow all headers (change as needed)
    )

    app.include_router(routes.command.router, prefix="/api/v1")

    return app


class APIServer:
    _SERVER_PORT = 30001

    def __init__(
        self,
        usecases: CommandUseCases
    ):
        self.usecases = usecases

    def start(self) -> None:
        config = uvicorn.Config(
            get_app(self.usecases),
            host="0.0.0.0",
            port=self._SERVER_PORT,
            log_level="debug",
        )
        uvicorn.Server(config).run()