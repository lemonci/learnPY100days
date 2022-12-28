import time
import tkinter
import tkinter.messagebox
from threading import Thread

def main():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('Reminder', 'Download finishes!')
            # Enable download button
            button1.config(state=tkinter.NORMAL)

    def download():
        # Disable download button
        button1.config(state=tkinter.DISABLED)
        # Set the thread to daemon with the daemon parameter (execution is not retained if the main program exits)
        # Processing time-consuming download tasks in threads
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('About', 'Author: Luo Hao(v1.0)')

    top = tkinter.Tk()
    top.title('Single thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='About', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()