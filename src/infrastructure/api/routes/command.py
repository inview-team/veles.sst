import time

from fastapi import APIRouter, UploadFile, HTTPException, Request
from usecases.command import CommandUseCases

router = APIRouter(prefix="/commands", )
usecases = None

@router.post("")
async def execute_command(file: UploadFile, request: Request):
    start_time = time.time()
    token = request.headers.get("authorization")
    session_id = request.headers.get("session-id")
    print(file.headers)
    print(session_id, token)
    try:
        command = usecases.execute(session_id, token, file.file.read())
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    end_time = time.time()
    print(end_time-start_time)
    return {'command': command}

