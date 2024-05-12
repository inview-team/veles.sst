import io
import string

from domain.command import CommandRepository, Command
from faster_whisper import WhisperModel


class FasterWhisperRepository(CommandRepository):

    def __init__(self):
        self.model = WhisperModel("large-v3", device="cuda", compute_type="int8_float16", download_root="../cache")

    def get_by_bytes(self, payload: bytes) -> Command:
        audio_file = io.BytesIO(payload)
        segments, info = self.model.transcribe(audio=audio_file, language="ru")

        output_text = ""
        for segment in segments:
            output_text += segment.text

        return Command(text=output_text)
