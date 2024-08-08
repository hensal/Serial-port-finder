import os
import sys
import serial
import serial.tools.list_ports
try:
    import tkinter as tk
except ImportError:
    import tkinter as tkc

try:
    from tkinter import ttk
except ImportError:
    import tkinter.ttk as ttk


def serial_ports():
    """Lists serial port names on Ubuntu"""
    result = []
    for port_info in serial.tools.list_ports.comports():
        port = port_info.device
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("400x200")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Serial Port Finder")
        top.configure(relief="raised")
        top.configure(background="#b6b1b1")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.button = ttk.Button(top)
        self.button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.button.configure(text='Find Serial Ports', command=self.find_ports)

        self.label = ttk.Label(top)
        self.label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.label.configure(text='Available Ports will be shown here.')

    def find_ports(self):
        ports = serial_ports()
        if ports:
            self.label.configure(text='\n'.join(ports))
        else:
            self.label.configure(text='No serial ports found.')


if __name__ == '__main__':
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()
