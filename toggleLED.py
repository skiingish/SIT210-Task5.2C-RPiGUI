# Toggle the selected LED when radio button is pressed 

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### Hardware
redLed=LED(18) #gpio 18
greenLed=LED(23) #gpio 23
blueLed=LED(24) #gpio 24

redLed.on() # start with red led on

### Define GUI elements ###
win = Tk()
win.title("LED Toggler") # title
#win.geometry("200x200") # window size 
myFont = tkinter.font.Font(family = 'Helvetica', size = 16, weight = "bold") # font 
rad = IntVar() #used to the radio var

### Functions

def checkRadio(): #checks which radio button was selected
    selectedLED = rad.get()
    toggleLED(selectedLED) # call toggleLED passing the LED to be turned on
def toggleLED(ledToggled):
    cleanUpLEDs() #toggle all LEDs off before turning on selected
    if ledToggled == 0:
        print("RED")
        redLed.on()
    elif ledToggled == 1:
        print("GREEN")
        greenLed.on()
    else:
        print("BLUE")
        blueLed.on()
def cleanUpLEDs(): #used to off all LEDs 
    redLed.off()
    greenLed.off()
    blueLed.off()
def close():
    RPi.GPIO.cleanup()
    win.destroy()

### Widgets below  

## Radio Buttons for the different LEDs and exit button

# RED
R1 = Radiobutton(win, text="Red",variable=rad,value=0, command = checkRadio, height = 1, width = 8)
R1.grid(row=1, column=1, pady=2)
# GREEN
R2 = Radiobutton(win, text="Green",variable=rad,value=1, command = checkRadio, height = 1, width = 8)
R2.grid(row=2, column=1, pady=2)
# BLUE
R3 = Radiobutton(win, text="Blue",variable=rad,value=2, command = checkRadio, height = 1, width = 8)
R3.grid(row=3, column=1, pady=2)
#EXIT BUTTON
exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=10)
exitButton.grid(row=4, column=1, padx=40, pady=10)


win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO as window closes 
win.mainloop() # Loops forever
 