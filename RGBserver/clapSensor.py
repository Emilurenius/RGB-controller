import time, datetime
import RPi.GPIO as GPIO
import requests

def clamp (value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value

clapSensor = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clapSensor, GPIO.IN)

try:
    while True:
        if GPIO.input(clapSensor):
            print("Clap detected")
            claps = 1
            time.sleep(0.5)
            startTime = datetime.datetime.now().timestamp()
            print("Started waiting for double clap:", startTime)

            while datetime.datetime.now().timestamp() - startTime < 1:
                if GPIO.input(clapSensor):
                    print("Double clap!")
                    claps += 1
                    #response = requests.get("http://localhost:3000/lightstate?toggle=change")
                    #print(response.text)
                    break
            time.sleep(0.3)

            startTime = datetime.datetime.now().timestamp()
            print("Waiting for third clap")
            while datetime.datetime.now().timestamp() - startTime < 0.3:
                if GPIO.input(clapSensor):
                    print("triple clap!")
                    claps += 1
                    break
            time.sleep(0.3)

            startTime = datetime.datetime.now().timestamp()
            print("Waiting for fourth clap")
            while datetime.datetime.now().timestamp() - startTime < 0.3:
                if claps == 2:
                    break
                if GPIO.input(clapSensor):
                    print("DAMN! Four claps!")
                    claps += 1
                    break
            
            if claps == 2:
                response = requests.get("http://localhost:3000/lightstate?toggle=change")
                print(response.text)
            elif claps == 3:
                currentBR = requests.get("http://localhost:3000/br").text
                if int(currentBR) <= 1000:
                    newBR = str(int(currentBR) + 100)
                    newBR = str(clamp(int(newBR), 0, 1000))
                    response = requests.get(f"http://localhost:3000/rgb?br={newBR}")
                    print("Changed brightness to", newBR)
            elif claps == 4:
                currentBR = requests.get("http://localhost:3000/br").text
                if int(currentBR) >= 0:
                    newBR = str(int(currentBR) - 100)
                    newBR = str(clamp(int(newBR), 0, 1000))
                    response = requests.get(f"http://localhost:3000/rgb?br={newBR}")
                    print("Changed brightness to", newBR)


finally:
    GPIO.cleanup()