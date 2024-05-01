import io

from domain.command import CommandRepository, Command
from faster_whisper import WhisperModel


class FasterWhisperRepository(CommandRepository):

    def __init__(self):
        self.model = WhisperModel("large-v3", device="cpu", compute_type="int8")

    def get_by_bytes(self, payload: bytes) -> Command:
        audio_file = io.BytesIO(payload)
        segments, info = self.model.transcribe(audio=audio_file)
        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

        output_text = ""
        for segment in segments:
            output_text += segment.text

        return Command(text=output_text)
