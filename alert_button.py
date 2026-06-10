import time
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False
while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        response = requests.post("https://api.telegram.org/bot8290178819:AAG1-MSLQgwyn5OfCI27paceIR-WeGbvUGM/sendMessage",
 json={"chat_id": "8956398548", "text": "Someone pressed the alert button!"})
        print("Someone pressed the alert button!\n")
        print(response.status_code)
        button_pressed = True
    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False
    time.sleep(0.1)
