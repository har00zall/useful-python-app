import speech_recognition as sr
import cv2 as opencv
import pytesseract
import pyautogui
import keyboard
import pyttsx3

class MainLoop:

    def __init__(self):
        pass

    @staticmethod
    def move_my_mouse():
        

        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img = opencv.imread("Try.png")
        img = opencv.cvtColor(img, opencv.COLOR_BGR2RGB)

        while True:
            if keyboard.is_pressed('space'):
                screenshot = pyautogui.screenshot()
                screenshot.save("Try.png")
            
            if keyboard.is_pressed('enter'):
                text = pytesseract.image_to_string(img)
                pyautogui.write(text)

            if keyboard.is_pressed('ctrl+s'):
                text = pytesseract.image_to_string(img)
                engine = pyttsx3.init()
                engine.say(text=text)
                engine.runAndWait()

            if keyboard.is_pressed('escape'):
                exit(-1)


if __name__ == "__main__":
    main = MainLoop()
    main.move_my_mouse()
