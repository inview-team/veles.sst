import string

from domain.command import CommandRepository, CommandExecutor


class CommandUseCases:

    def __init__(
        self,
        commandRepo: CommandRepository,
        commandExec: CommandExecutor
    ):
        self.repo = commandRepo
        self.executor = commandExec

    def execute(self, session_id: str, token: str, record: bytes) -> str:
        command = self.repo.get_by_bytes(record)
        input_text = command.text.lower()
        text = input_text.translate(input_text.maketrans("", "", string.punctuation))
        isSended = self.executor.execute_command(session_id, token, text)
        if not isSended:
            return ""
        return command.text
