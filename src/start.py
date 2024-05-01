import os

import infrastructure.api.server
import usecases.command
from infrastructure.command_repository.faster_whisper.repository import FasterWhisperRepository


def main() -> None:
    command_repository = FasterWhisperRepository()
    command_usecases = usecases.command.CommandUseCases(command_repository)
    api_server = infrastructure.api.server.APIServer(command_usecases)
    api_server.start()


if __name__ == "__main__":
    main()
    os._exit(1)
