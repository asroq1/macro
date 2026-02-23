import pyautogui
import time
import re
import os

def get_current_mouse_position():
    """현재 마우스 위치를 반환합니다."""
    x, y = pyautogui.position()
    return x, y

def update_macro_file(x, y, file_path='/Users/devicii/Desktop/macro/macro.py'):
    """macro.py 파일의 x, y 좌표 값을 업데이트합니다."""
    if not os.path.exists(file_path):
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return False
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    # x, y 값을 찾아 업데이트
    updated_content = re.sub(r'x=\d+', f'x={x}', content)
    updated_content = re.sub(r'y=\d+', f'y={y}', updated_content)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)
    
    print(f"macro.py 파일이 업데이트되었습니다. 새로운 좌표: x={x}, y={y}")
    return True

def main():
    print("3초 후에 현재 마우스 위치를 감지합니다. 원하는 위치에 마우스를 놓으세요...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    x, y = get_current_mouse_position()
    print(f"감지된 마우스 위치: x={x}, y={y}")
    
    if update_macro_file(x, y):
        print("macro.py 파일이 성공적으로 업데이트되었습니다.")
    else:
        print("macro.py 파일 업데이트에 실패했습니다.")

if __name__ == "__main__":
    main()