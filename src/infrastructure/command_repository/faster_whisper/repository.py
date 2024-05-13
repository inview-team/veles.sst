import io

from domain.command import CommandRepository, Command
from faster_whisper import WhisperModel


class FasterWhisperRepository(CommandRepository):

    def __init__(self, mode: str):
        if mode == "gpu":
            self.device = "cuda"
            self.compute_type = "int8_float16"
        else:
            self.device = "cpu"
            self.compute_type = "int8"

        self.model = WhisperModel("large-v3", device=self.device, compute_type=self.compute_type, download_root="/app/cache")

    def get_by_bytes(self, payload: bytes) -> Command:
        audio_file = io.BytesIO(payload)
        segments, info = self.model.transcribe(audio=audio_file, language="ru")

        output_text = ""
        for segment in segments:
            output_text += segment.text

        return Command(text=output_text)
