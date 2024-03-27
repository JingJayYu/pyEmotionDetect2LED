import serial  
from time import sleep

COM_PORT = '/dev/cu.usbmodem14101'  
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

def run(emotionList):
    try:
        while True:
            emotion = emotionList[0]
            match emotion:
                case "angry":
                    ser.write(bytearray([1]))  
                case "disgust": 
                    ser.write(bytearray([2]))    
                case "fear": 
                    ser.write(bytearray([3])) 
                case "happy": 
                    ser.write(bytearray([4]))
                case "sad": 
                    ser.write(bytearray([5]))
                case "neutral": 
                    ser.write(bytearray([6]))
                case "surprise":
                    ser.write(bytearray([7]))
                case "NoDetect":
                    ser.write(bytearray([0]))
    finally:
            ser.write(bytearray([0]))
            ser.close()