import os
import time
import pyautogui
from convert import convert_text_to_exel, remove_text_file

def export_data() -> bool: 
    pyautogui.press("win")
    pyautogui.write("notepad")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("ctrl", "v")
    # pyautogui.press("enter")
    time.sleep(2)
    # pyautogui.hotkey("alt", "f")
    # pyautogui.press("enter")
    # pyautogui.press("down", presses=2) # ADJUST FOR ANAGO'S LAYOUT
    # pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "shift", "s")  
    time.sleep(2) 
    pyautogui.hotkey("alt", "d")
    pyautogui.write(r"C:\Users\Javy\Documents")
    pyautogui.press("enter")
    pyautogui.press("tab", presses=6)
    pyautogui.write("Anago_Knife_Scores")
    pyautogui.press("tab", presses=4)
    pyautogui.press("enter")
    time.sleep(2)
        
    
def remove_file_if_exists() -> str:
    if os.path.exists(r"C:\Users\Javy\Documents\Anago_Knife_Scores.xlsx"):
        os.remove(r"C:\Users\Javy\Documents\Anago_Knife_Scores.xlsx")
        print("File has been removed")
        return True
    print("File does not exist")
    return False

def check_if_file_exists() -> str:
    if os.path.exists(r"C:\Users\Javy\Documents\Anago_Knife_Scores.txt"):
        return True
    return False

def main() -> None:
    remove_file_if_exists()
    export_data()
    if check_if_file_exists():
        convert_text_to_exel()
        time.sleep(.5)
        remove_text_file()
        
        
        
    
     
# Ctrl + S: Often used to open the 'Save As' dialog, which might allow you to choose the save location for your file.
# Alt + Underlined letter: In Windows applications, pressing Alt plus the underlined letter in a menu option often opens that menu or selects that option.
# Tab and Shift + Tab: Moves focus between different controls within a window. You can use these to navigate to the "Save exported data to:" field if it's selectable.
# F4 or Alt + Down Arrow: When a path field is selected, these shortcuts sometimes open the drop-down list or browse function associated with that field.

if __name__ == '__main__':
    main()

