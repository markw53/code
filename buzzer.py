from gpiozero import BUZZER
from time import sleep

buz1 = BUZZER(15)

buz1.on()
sleep(1)
buz1.off()

