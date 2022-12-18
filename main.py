import pygame
import time
import wave
import threading
import pyaudio
from time import time, sleep
import RPi.GPIO as GPIO
import gc

from pysoundLooper import loopingThread


#initialize global variables and a pyaudio instance
GPIO.setmode(GPIO.BOARD)
buttonPin = 16
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 512
WAVE_OUTPUT_FILENAME = 0

device_index = 1
players = []

audio = pyaudio.PyAudio()


def looper_start(file, player_list): 
    var=loopingThread(file)
    player_list.append(var)
    var.start()



#print("----------------------record device list---------------------")
info = audio.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (audio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            #print("Input Device id ", i, " - ", audio.get_device_info_by_host_api_device_index(0, i).get('name'), "- " )
            if audio.get_device_info_by_host_api_device_index(0, i).get('name') == " USB PnP Sound Device: Audio (hw:1,0) ":
                device_index = i
print("-------------------------------------------------------------")
print("recording via index "+str(device_index))


print("Input bpm:")
bpm = int(input())

delta = 60/bpm
while True:
    buttonState = True
    
    '''print("Input number of measures to be recorded:")
    measure_num = int(input())
    record_seconds = (60/bpm)*(measure_num*4)'''
    
    
    print("Press the button to record:")
    while buttonState:
        buttonState = GPIO.input(buttonPin)
    #else:
    '''goal = time()
    for i in range(4):
        print(time() - goal)
        if i == 0:
            pygame.mixer.Sound('clicks/strong_beat.wav').play()
        else:
            pygame.mixer.Sound('clicks/strong_beat.wav').play()
        goal += delta
        gc.collect()
        sleep(goal - time())'''
    print('recording started')
    
    stream = audio.open(format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,input_device_index = device_index,
        frames_per_buffer=CHUNK)
    Recordframes = []
    #recording keeps going for the duration specified above
    while buttonState == False:
        buttonState = GPIO.input(buttonPin)
        data = stream.read(CHUNK)
        Recordframes.append(data)
        
    '''for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        Recordframes.append(data)'''
    

    print ("recording stopped")
    stream.stop_stream()
    stream.close()
    
    #create the wave file for the recording
    waveFile = wave.open(str(WAVE_OUTPUT_FILENAME) + '.wav', 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(Recordframes))
    waveFile.close()
    
    #loop the wave file
    looper_start(str(WAVE_OUTPUT_FILENAME) + '.wav', players)
    WAVE_OUTPUT_FILENAME+=1
                    

