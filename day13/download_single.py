import time
import tkinter
import tkinter.messagebox

def download():
    # Simulate the downloading task needs 10 secs
    time.sleep(10)
    tkinter.messagebox.showinfo('Reminder', 'The download finishes!')

def show_about():
    tkinter.messagebox.showinfo('About', 'Author: Luo Hao(v1.0)')

def main():
    top = tkinter.Tk()
    top.title('Single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='About', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()