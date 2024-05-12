from abc import ABC, abstractmethod

class Command:
    def __init__(
        self,
        text: str
    ):
        self.text: str = text


class CommandRepository(ABC):

    @abstractmethod
    def get_by_bytes(self, payload: bytes) -> Command:
        raise NotImplementedError

class CommandExecutor(ABC):

    @abstractmethod
    def execute_command(self, session_id: str, token: str, command: str) -> bool:
        raise NotImplementedError