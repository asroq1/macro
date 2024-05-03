# from pynput import keyboard
# import pyautogui
# import sys
# import keyboard

# def click(x, y):
#     while not exit_event.is_set():
#         pyautogui.click(x, y)

# def exit_program(e):
#     raise KeyboardInterrupt
#     # sys.exit()

# def main():
#     x=122
#     y=444
#     pyautogui.PAUSE = 0.5

#     keyboard.add_hotkey('esc', exit_program)

#     try:
#         while True:
#             click(x, y)
#             # keyboard.wait('esc')
#     except KeyboardInterrupt:
#         print("프로그램이 종료됩니다.")
#         sys.exit()

# if __name__ == "__main__":
#     main()

import keyboard
import pyautogui
import threading

def click(x, y):
    while not exit_event.is_set():
        pyautogui.click(x, y)

def main():
    global exit_event
    exit_event = threading.Event()

    x=414
    y=1528
    pyautogui.PAUSE = 0.1

    click_thread = threading.Thread(target=click, args=(x, y))
    click_thread.start()

    keyboard.wait('esc')
    exit_event.set()

    click_thread.join()
    print("프로그램이 종료됩니다.")

if __name__ == "__main__":
    main()