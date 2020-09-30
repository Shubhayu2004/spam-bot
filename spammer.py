import pyautogui, time
time.sleep(5)
a = open('spamming','r')
for i in a:
  pyautogui.typewrite(i)
  pyautogui.press('enter')
