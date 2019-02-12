import pyautogui
import time
import random


def randomize_coords(x, y, offset):
    rx = random.randint(x-offset, x+offset)
    ry = random.randint(y-offset, y+offset)
    return (rx, ry)


def superheat():
    for i in range(27):
        # moves to the spell in the spell book and clicks
        pyautogui.moveTo(randomize_coords(1556, 825, 2),
                         duration=random.uniform(1.0, 1.6))
        time.sleep(random.uniform(0.2, 0.8))
        pyautogui.click(randomize_coords(1556, 825, 2),
                        duration=random.uniform(0.1, 0.3))
        # selects the bottom right ore and clicks
        #time.sleep(random.uniform(0.8, 1.1))
        pyautogui.moveTo(randomize_coords(1594, 977, 3),
                         duration=random.uniform(1.0, 1.4))
        time.sleep(random.uniform(0.2, 0.7))
        pyautogui.click(randomize_coords(1594, 977, 3),
                        duration=random.uniform(0.1, 0.3))
        time.sleep(random.uniform(1.0, 1.4))


def bank_loot():
    # move to and click banker
    time.sleep(0.8)
    pyautogui.moveTo(randomize_coords(638, 429, 1),
                     duration=random.uniform(1.4, 1.9))
    time.sleep(random.randint(3, 6))
    pyautogui.click(randomize_coords(638, 429, 1),
                    duration=random.uniform(0.1, 0.3))
    time.sleep(random.randint(5, 7))
    # move to and click item to deposit
    pyautogui.moveTo(randomize_coords(1510, 762, 2),
                     duration=random.uniform(1.0, 1.6))
    pyautogui.click(randomize_coords(1510, 762, 2),
                    duration=random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.8, 1.3))
    # move to and click item to withdraw
    pyautogui.moveTo(randomize_coords(673, 289, 2),
                     duration=random.uniform(1.0, 1.6))
    pyautogui.click(randomize_coords(673, 289, 2),
                    duration=random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.8, 1.3))
    # close the bank window
    pyautogui.moveTo(randomize_coords(927, 70, 3),
                     duration=random.uniform(1.0, 1.6))
    pyautogui.click(randomize_coords(927, 70, 3),
                    duration=random.uniform(0.2, 0.5))
    time.sleep(random.uniform(0.8, 1.4))


try:

    for i in range(7):
        superheat()
        bank_loot()
        # print(randomize_coords(1555, 833))
        # time.sleep(random.uniform(1.0, 3.6))

except KeyboardInterrupt:
    print('shutting down')
