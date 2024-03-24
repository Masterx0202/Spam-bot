import pyautogui
import time

# press start and swich to the whatsapp tab

messages = int(input("how many messages you want to send: "))
messages += 1
mode = input("mode:")
# 1 = 0 to (whatever number you want)
# 2 = copied message.
# 3 = custom message
custom = input("input custom message:")


num = int(0)
time.sleep(5)
pyautogui.click(989, 1012)
time.sleep(0.5)

while num == messages:
    num = str(num)
    if mode == 1:
        pyautogui.write(num)
        pyautogui.press("enter")
        num = int(num)
        num += 1
    if mode == 2:
        pyautogui.keyDown("ctrl")
        pyautogui.press("v")
        pyautogui.keyUp("ctrl")
        pyautogui.press("enter")
        num += 1

    if mode == 3:
        pyautogui.write(custom)
        print('message write')
        pyautogui.press("enter")
        num += 1
print("done")