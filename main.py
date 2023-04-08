# das weg


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import tkinter as tk
from tkinter import ttk
import serial

# root = tk.Tk()


def button_clicked():
    print('Button clicked')

    def StringUmw(data):
        data = data.decode("utf-8")  # Löscht das b'...'   /r/n wird durch [0:-2] gelöscht
        data = data[0:-2]
        return data

    ser = serial.Serial('/dev/ttyUSB0', 9600)  # Start serial communication
    data = '#'
    while data != '###':
        data = ser.readline()  # Wait for line from Arduino and read it
        # print("Received: '{}'".format(data))  # Print the line to the console
        # data = data.decode("utf-8") # Löscht das b'...'   /r/n wird durch [0:-2] gelöscht
        # data = data[0:-2]
        data = StringUmw(data)
        print(data)  # Print the line to the console [2:-3]
        if data == 'POS':
            ZangePos = StringUmw(ser.readline())
            UArmPos = StringUmw(ser.readline())
            OArmPos = StringUmw(ser.readline())
            DrehPos = int(StringUmw(ser.readline()))  # Jetzt is es ein int
            DrehPos = DrehPos + 0
            print(DrehPos)


    message2 = tk.Label(root, text="Hellommmmmmmmmmm")
    message2.pack()



root = tk.Tk()
root.title('Roboter HMI')
root.geometry('600x400+50+50') # x y +abstand von oben links


# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()
message2 = tk.Label(root, text="Hello, World!ddddd")
message2.pack()

button = ttk.Button(root, text='Warten auf Daten', command=button_clicked)
button.pack()


# keep the window displaying
root.mainloop()
