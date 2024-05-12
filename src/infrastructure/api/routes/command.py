import time

from fastapi import APIRouter, UploadFile
from usecases.command import CommandUseCases

router = APIRouter(prefix="/commands", )
usecases: CommandUseCases | None = None

@router.post("")
async def execute_command(file: UploadFile):
    start_time = time.time()
    token = file.headers.get("authorization")
    session_id = file.headers.get("session-id")
    command = usecases.execute(session_id, token, file.file.read())
    end_time = time.time()
    print(end_time-start_time)
    return {'command': command}

