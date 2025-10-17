import pyautogui
import time # time.sleep(1)
import pygetwindow as gw
# import subprocess # subprocess.run(path_steam)

# path_steam=r"C:\Program Files (x86)\Steam\steam.exe"
nome_da_janela_de_sw="BlueStacks App Player"

# pyautogui.PAUSE=1
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
window_sw_title=nome_da_janela_de_sw
window_sw = gw.getWindowsWithTitle(window_sw_title)[0]
bbox_sw = (window_sw.left, window_sw.top, window_sw.right, window_sw.bottom)
window_sw.activate()
# time.sleep(0.5); pyautogui.screenshot('C:\\Users\\CAMILA\\Documents\\Bruno\\swbot\\bluestacks_sw.png',region=bbox_sw)
icon_battle=pyautogui.locateOnScreen('C:\\Users\\CAMILA\\Documents\\Bruno\\swbot\\bluestacks_sw.png',confidence=0.8)


pyautogui.moveTo(icon_battle[0],icon_battle[1])
window_sw.activate()
pyautogui.click(button='left', clicks=1)


# pyautogui.click(button='right', clicks=3, interval=0.25)

# pyautogui.click('sw_repeat_battle.png')

# import time
# import pygetwindow as gw
# from PIL import ImageGrab

# # window_title="Summoners War (Steam)"

# def capture_window_screenshot(window_title):
#     try:
#         # Find the window by its title
#         window = gw.getWindowsWithTitle(window_title)[0]
        
#         # Activate the window (optional, but can help with some applications)
#         window.activate()
#         time.sleep(0.5)

#         # Get the window's bounding box
#         bbox = (window.left, window.top, window.right, window.bottom)

#         # Take a screenshot of the specified region
#         screenshot = ImageGrab.grab(bbox)
#         return screenshot
#     except IndexError:
#         print(f"Window with title '{window_title}' not found.")
#         return None

# # Example usage:
# # Assuming you have a program named "Notepad" open
# janela = capture_window_screenshot("Summoners War (Steam)")


# if janela:
#     janela.save("janela.png")
#     print("Screenshot salva como janela.png")