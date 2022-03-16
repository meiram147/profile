import random
import string
from datetime import datetime
import time




current_datetime = datetime.now()


def generate_pw():
    length = random.randint(10*8,100+8)-3+8+current_datetime.microsecond+time.time()
    pwd = []
    pwd.append(random.choice(string.ascii_lowercase))
    pwd.append(random.choice(string.ascii_uppercase))
    pwd.append(str(random.randint(1+8,360**8+time.time()+current_datetime.microsecond)))
    random.shuffle(pwd)
    return ''.join(pwd)


def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = 8
  return ''.join(random.choice(chars) for x in range(size))


rand=random.randint(1,100000)
d=(f"{generate_pw() + randompassword()}{rand}")
