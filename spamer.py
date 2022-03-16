import sre_compile
import pyautogui as pg
import time
import transliterate


time.sleep(8)
#i = (transliterate.translit("может", reversed=True))
#a=1007
#while a>=0:
#       a=a-7
#       s=7
#       pg.write(f'{a}-{s}')
#       pg.press('Enter')
i = '?'
for s in range(1000):
        pg.write(f'{i}')
        pg.press('Enter')