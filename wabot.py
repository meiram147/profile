from turtle import pos
import pyautogui as pg 
import pyperclip
import post as ps

while True:
    if ps.s == 0:
        pg.moveTo(1385,902, duration=0.25)
        pg.click(1385, 902, button = 'left')
        pg.click(1385, 902, button = 'left')
        pg.mouseDown(button='left')
        pg.moveTo(1800, 902, duration=0.25)
        pg.mouseUp(button='left')
        pg.hotkey('ctrl', 'c')
        s = pyperclip.paste()
        pg.moveTo(1800, 1000, duration=0.25)
        pg.click(1800, 1000, button = 'left')
    
        if s == "Хуй":
            z = "хавать хочу погнали в магаз"
            p = pyperclip.copy(z)
        if s == "Да":
            z = "иди нхуй я пошел в магаз"
            p = pyperclip.copy(z)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('enter')
    if ps.s == 1:
        pg.moveTo(1385,902, duration=0.25)
        pg.click(1385, 902, button = 'left')
        pg.click(1385, 902, button = 'left')
        pg.mouseDown(button='left')
        pg.moveTo(1800, 902, duration=0.25)
        pg.mouseUp(button='left')
        pg.hotkey('ctrl', 'c')
        s = pyperclip.paste()
        pg.moveTo(1800, 1000, duration=0.25)
        pg.click(1800, 1000, button = 'left')
    
        if s == "Хуй":
            z = "хавать хочу погнали в магаз"
            p = pyperclip.copy(z)
        if s == "Да":
            z = "иди нхуй я пошел в магаз"
            p = pyperclip.copy(z)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('enter')
    else:
        print("errrr")