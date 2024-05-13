import time

from fastapi import APIRouter, UploadFile, HTTPException
from usecases.command import CommandUseCases

router = APIRouter(prefix="/commands", )
usecases = None

@router.post("")
async def execute_command(file: UploadFile):
    start_time = time.time()
    token = file.headers.get("authorization")
    session_id = file.headers.get("session-id")
    try:
        command = usecases.execute(session_id, token, file.file.read())
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    end_time = time.time()
    print(end_time-start_time)
    return {'command': command}

