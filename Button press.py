from gpiozero import LED, Button
from time import sleep

btn = Button(4)
led = LED(17)

while True:
    if btn.is_pressed:
        led.on()
        sleep(5)
        led.off()

        
    
    
