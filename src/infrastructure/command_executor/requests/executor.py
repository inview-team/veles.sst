import requests

from domain.command import CommandExecutor


class RequestsCommandExecutor(CommandExecutor):

    def __init__(self, assistant_address: str):
        self._assistant_address = assistant_address

    def execute_command(self, session_id: str, token: str, command: str) -> bool:
        url = f"{self._assistant_address}/api/v1/action"
        headers = {
            "Authorization": token
        }

        body = {
            "session_id": session_id,
            "action": command,
        }

        response = requests.post(url, json=body, headers=headers)

        if response.status_code != requests.codes.ok:
            return False
        return True
