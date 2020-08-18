from common.audio_commons.chunking_conversion_util import ChunkingConversionUtil
from common.audio_commons.snr_util import SNR
from common.audio_commons.transcription_clients import get_transcription_clients

def get_audio_commons(initlization_dict):
    audio_commons_dict = {}

    audio_commons_dict['chunking_conversion'] = ChunkingConversionUtil.get_instance()
    audio_commons_dict['snr_util'] = SNR.get_instance()
    audio_commons_dict['transcription_clients'] = get_transcription_clients()
