import file_path_adder
from PIL.ImageGrab import grab
import mouse
from pyautogui import scroll
from numpy import array
from keyboard import wait, is_pressed
from pyautogui import position
from cv2 import imshow, waitKey, imwrite, cvtColor, COLOR_BGR2RGB, destroyAllWindows
from time import sleep
from os import listdir,remove
from easygui import msgbox
from pyttsx3 import speak

path = r"D:\R\saved screenshot images\\"

print("Deleted Files : ")
for i in listdir(path):
   sp = path+i
   print(sp)
   remove(sp)

num = 0
speak("waiting for alt..")
wait("alt")

speak("waiting for 1st position..")
mouse.wait()
x1, y1 = position()
speak("successfully captured...")
sleep(1)

speak("waiting for 2nt position..")
mouse.wait()
x2, y2 = position()
speak("successfully captured...")
sleep(1)

print(x1, y1, x2, y2)

speak("press shift to stop the loop")
while not is_pressed("shift"):
    sleep(1)
    num += 1
    try:
        img = grab(bbox=(x1, y1, x2, y2))
        img_array = cvtColor(array(img), COLOR_BGR2RGB)
    except SystemError as e:
        print(e)
        msgbox(title="Screen Shot", msg="Image Not Saved")
        break
    scroll(2*(y1-y2)-3)
    imshow("screen shot", img_array)
    fname = path + f"{num}.jpg"
    speak(num)
    imwrite(fname, img_array)
    waitKey(1)

speak("stopped..")
destroyAllWindows()
