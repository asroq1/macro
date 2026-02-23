import keyboard
import pyautogui
import threading
import time
import sys
import os

def click():
    # 클릭 함수에서 x, y 좌표를 받지 않고 매번 현재 마우스 위치를 사용
    while not exit_event.is_set():
        try:
            # 현재 마우스 위치에서 클릭
            current_x, current_y = pyautogui.position()
            pyautogui.click(current_x, current_y)
            # 짧은 시간 대기하여 CPU 사용량 감소 및 ESC 키 감지 개선
            time.sleep(0.01)
        except Exception as e:
            print(f"클릭 오류: {e}")
            break

def exit_handler(e=None):
    print("ESC 키가 눌렸습니다. 프로그램을 종료합니다...")
    exit_event.set()
    # 강제 종료를 위해 현재 프로세스 종료
    os._exit(0)

def main():
    global exit_event
    exit_event = threading.Event()

    # 초기 마우스 위치 저장 (참고용)
    initial_x, initial_y = pyautogui.position()
    print(f"시작 마우스 위치: x={initial_x}, y={initial_y}")
    
    pyautogui.PAUSE = 0.1

    # ESC 키를 누르면 exit_handler 함수 실행
    keyboard.on_press_key('esc', exit_handler)

    # 클릭 스레드 시작 (x, y 인자 제거)
    click_thread = threading.Thread(target=click)
    click_thread.daemon = True
    click_thread.start()

    try:
        # 메인 스레드가 종료되지 않도록 유지
        while not exit_event.is_set():
            time.sleep(0.1)
            # 주기적으로 ESC 키 상태 확인
            if keyboard.is_pressed('esc'):
                exit_handler()
    except KeyboardInterrupt:
        # Ctrl+C로 프로그램 종료 시 처리
        exit_handler()
    
    print("프로그램이 종료됩니다.")

if __name__ == "__main__":
    main()