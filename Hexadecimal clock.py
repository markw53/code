import time

def decimal_to_hexadecimal(decimal_value):
    return hex(decimal_value).split('x')[-1].upper()

def get_hexadecimal_time():
    current_time = time.localtime()
    hours_hex = decimal_to_hexadecimal(current_time.tm_hour)
    minutes_hex = decimal_to_hexadecimal(current_time.tm_min)
    seconds_hex = decimal_to_hexadecimal(current_time.tm_sec)
    return hours_hex.zfill(2), minutes_hex.zfill(2), seconds_hex.zfill(2)

while True:
    hours, minutes, seconds = get_hexadecimal_time()
    hexadecimal_time = f"{hours}:{minutes}:{seconds}"
    print(hexadecimal_time, end='\r')
    time.sleep(1)
