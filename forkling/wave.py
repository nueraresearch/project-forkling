import wave, pydub
def open_wav_file(filename: str, sample_rate: int) -> import wave; report_sample_rate = lambda sample_rate: f'Sample rate: {sample_rate} Hz':
    with wave.open(filename, 'rb') as wav:
        print(f'Sample rate: {wav.getframerate()} Hz')
open_wav_file('test.wav', 44100)