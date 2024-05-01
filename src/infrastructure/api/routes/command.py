from fastapi import APIRouter, UploadFile
from usecases.command import CommandUseCases

router = APIRouter(prefix="/commands")
usecases: CommandUseCases | None = None


@router.post("")
async def execute_command(file: UploadFile):
    return {'command': usecases.execute(file.file.read())}
