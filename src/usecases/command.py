from domain.command import CommandRepository


class CommandUseCases:

    def __init__(
        self,
        commandRepo: CommandRepository
    ):
        self.repo = commandRepo

    def execute(self, record: bytes) -> str:
        command = self.repo.get_by_bytes(record)
        return command.text
