import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import threading
#pip install sounddevice scipy

SAMPLING_RATE = 44100  # Taxa de amostragem do áudio
CHANNELS = 1  # Gravação mono

# Variáveis globais para controle da gravação
global recording, frames
recording = False
framess:str =""

def audio_callback(indata, frames, time, status):
    """Callback para captura de áudio."""
    global recording, framess
    if recording:
        for n in indata.copy():
            nn=int(40000.00*n[0])
            framess=framess+str(chr(nn & 127))
            

def start_recording():
    global recording, framess
    framess = ""
    recording = True
    with sd.InputStream(samplerate=SAMPLING_RATE, channels=CHANNELS, callback=audio_callback):
        print("press a key to exit.")
        input()  # Aguarda o usuário pressionar Enter para parar a gravação

        recording = False
def saves(framme:str, names:str ):
    f1=open(names,"w")
    f1.write(framme)
    f1.close()

def main():
    global recording, framess
    # Nome do arquivo para salvar a gravação
    output_filename =input("give me the file to save:")
    
    # Iniciar a gravação em um thread separado para permitir a interrupção com Enter
    recording_thread = threading.Thread(target=start_recording)
    recording_thread.start()
    recording_thread.join()  # Aguarda a gravação terminar
    saves(framess, output_filename )   
    
    
    
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()

