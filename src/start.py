import os

import infrastructure.api.server
import usecases.command
from infrastructure.command_repository.faster_whisper.repository import FasterWhisperRepository
from infrastructure.command_executor.requests.executor import RequestsCommandExecutor
from utils import environment as env


def main() -> None:
    command_repository = FasterWhisperRepository(env.SERVICE_MODE)
    command_executor = RequestsCommandExecutor(env.ASSISTANT_URL)
    command_usecases = usecases.command.CommandUseCases(command_repository, command_executor)
    api_server = infrastructure.api.server.APIServer(command_usecases)
    api_server.start()


if __name__ == "__main__":
    main()
    os._exit(1)
