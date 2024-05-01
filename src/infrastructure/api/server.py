import uvicorn
from fastapi import FastAPI

from usecases.command import CommandUseCases
from . import routes


def get_app(usecases: CommandUseCases) -> FastAPI:
    app = FastAPI(
    )

    routes.command.usecases = usecases
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
            port=self._SERVER_PORT
        )

        uvicorn.Server(config).run()