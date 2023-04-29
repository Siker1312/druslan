import random
import time

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    

def gen_help():
    return("Привет! Хочешь посмотреть все команды? Напиши - $help") 

def gen_time(timeeee=1):
    if timeeee==1:
        for x in range( 0, -1):
            x=10800
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            time.sleep(1)
            if seconds >= 1:
                return(f"{hours:02}:{minutes:02}:{seconds:02}")
            if seconds == 0 and minutes == 0 and hours == 0:
                timeeee=0
