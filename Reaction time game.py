from gpiozero import LED, Button
from time import sleep, time
from random import randint

btn = Button(4)
led = LED(17)

while True:
    sleep(randint(1,10))
    led.on()
    start = time()
    btn.wait_for_press()
    end = time()
    led.off()
    print(end - start)

        
    
    
