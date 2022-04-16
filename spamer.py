import sre_compile
import pyautogui as pg
import time
import transliterate
import pyperclip as pc

time.sleep(8)
#i = (transliterate.translit("может", reversed=True))
#a=1007
#while a>=0:
#       a=a-7
#       s=7
#       pg.write(f'{a}-{s}')
#       pg.press('Enter')

i = pc.paste()
for s in range(1000):
        # pg.write(f'{i}')
        pg.hotkey('ctrl','v')
        pg.press('Enter')