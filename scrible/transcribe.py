from dataclasses import dataclass
from typing import Dict, Callable


@dataclass
class AudioSource:
    name: str
    uri: str
    format: str
    language: str


@dataclass
class TranscribeResult:
    created_job: Dict
    notify: Callable[[], str]


class AsyncTranscriber:
    def start_transcription_job(
        self,
        TranscriptionJobName: str,
        Media: Dict[str, str],
        MidiaFormat: str,
        LanguageCode: str,
    ):
        raise NotImplementedError

    def get_transcription_job(self, TranscriptionJobName: str):
        raise NotImplementedError


def transcribe(client: AsyncTranscriber, source: AudioSource):
    created_job = client.start_transcription_job(
        TranscriptionJobName=source.name,
        Media={"MediaFileUri": source.uri},
        MediaFormat=source.format,
        LanguageCode=source.language,
    )

    def notify():
        status = client.get_transcription_job(source.name)
        return status["TranscriptionJob"]["TranscriptionJobStatus"]

    return TranscribeResult(created_job, notify)
