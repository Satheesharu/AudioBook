import PyPDF2
import pyttsx3
from tkinter import *
from tkinter import ttk   #progressbar
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.tix import * #Ballon text
from gtts import gTTS
from playsound import playsound
import os
import eyed3 # find mp3 File length
import pygame #music player
import time
############ Initialized window ####################

def mainFunction(hidePopUp=0):

    root = Tk()
    root.iconbitmap('C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/icon.ico')
    root.geometry("800x500")
    root.resizable(0, 0)
    root.title('Audio Book')

    # create tooltip
    tip = Balloon(root)

    # Designate Height and Width of our app
    app_width = 800
    app_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2 ) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    # define background image
    img = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/f1.png")

    # crete canvas
    mycanvas = Canvas(root, width=800, height=500)
    mycanvas.pack(fill="both", expand=True)

    # Set image
    mycanvas.create_image(0, 0, image=img, anchor="nw")



    def mainExit():

        root.destroy()


    if(hidePopUp == 0):
        messagebox.showinfo("PopUp Message", "Please... Make sure your Laptop is Connected To Internet!!!")



    #Text to speech Function
    def frame1():
        root = Tk()
        root.iconbitmap('C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/icon.ico')
        root.geometry('800x500')
        root.resizable(0, 0)
        root.title('Speech Convertion')


        # Designate Height and Width of our app
        app_width = 800
        app_height = 500

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # create tooltip
        tip = Balloon(root)

        # define image
        img = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/k.png")


        # crete canvas
        mycanvas= Canvas(root, width=800, height=500)
        mycanvas.pack()

        #Set image
        mycanvas.create_image(0,0, image=img, anchor="nw")

        # label
        mycanvas.create_text(150,30, text="Text - To - Speech",font=("Segoe UI",25,'bold'),fill="white")
        mycanvas.create_text(105,73, text="Enter Text Here",font=("Segoe Print",17,'bold'))

        ##text variable
        Msg = StringVar()


        #Create Entry Field
        entry_field = Entry(root,textvariable =Msg, width ='30',bd=2,font=5)

        entry_window = mycanvas.create_window(20,90,anchor="nw",window=entry_field)


        ###################define function#############################   #


        def Text_to_speech():
            if len(entry_field.get()) == 0:
                btnf1.config(image=btnimg1)
                messagebox.showerror("Warning","Please Enter Some Text")

            else:

                Message = entry_field.get()
                speech = gTTS(text=Message)
                speech.save('D.mp3')
                playsound('D.mp3')
                os.remove('D.mp3')



        def Exit():
            root.destroy()
            mainFunction(hidePopUp=1)

        def Reset():
            Msg.set("")

        def returncolor():
            btnf1.config(image=btnimg1)

        def playButton():
            btnf1.config(image=btnimg4)
            btnf1.after(100, lambda: [Text_to_speech(), returncolor()])


        btnimg1 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/play.png")
        btnimg2 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/back.png")
        btnimg3 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/reset.png")
        btnimg4 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/playing.png")

        #frame1 Buttons
        btnf1 = Button(root, image=btnimg1 , font = 'arial 15 bold',cursor="hand2", command =playButton,
                       width =50,height=50,activebackground='skyblue')
        btnf1.place(x=25, y=130)

        btnf2 = Button(root,image=btnimg2,font = 'arial 15 bold' ,cursor="hand2",bg='white',
                       command = Exit,width =50,height=50,activebackground='skyblue')
        btnf2.place(x=100,y=130)

        btnf3 = Button(root, image=btnimg3, font='arial 15 bold',cursor="hand2",
                       command = Reset,width =50,height=50,activebackground='skyblue')
        btnf3.place(x=175 , y =130)

        # bind tooltip with button1
        tip.bind_widget(btnf1, balloonmsg="Play")
        # bind tooltip with button2
        tip.bind_widget(btnf2, balloonmsg="Click to Go Back")
        # bind tooltip with button3
        tip.bind_widget(btnf3, balloonmsg="Reset")


        root.mainloop()


    #Pdf to Audio Function
    def frame2():


        root = Tk()
        root.iconbitmap('C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/icon.ico')
        root.geometry('800x500')
        root.resizable(0, 0)
        root.title('Audio Convertion')
        pygame.mixer.init()

        # create tooltip
        tip = Balloon(root)

        # Designate Height and Width of our app
        app_width = 800
        app_height = 500

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # define image
        img = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/f2.png")

        # crete canvas
        mycanvas = Canvas(root, width=800, height=500)
        mycanvas.pack(fill="both", expand=True)

        # Set image
        mycanvas.create_image(0, 0, image=img, anchor="nw")

        # label
        mycanvas.create_text(150, 30, text="PDF - To - Audio", font=("Segoe UI", 25,'bold'),fill="white")
        mycanvas.create_text(100,85, text="Select Folder",font=("Segoe Print",18,'bold'))
        mycanvas.create_text(140,340, text="Music Player",font=("Century Gothic",28,'bold'),fill="sienna4")
                                                            #Century Gothic Segoe Print Segoe UI"

        # Create progressbar window
        def progress():

            t = Toplevel()
            t.iconbitmap('C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/icon.ico')
            t.geometry('400x100')
            t.resizable(0, 0)
            t.title("progressbar")

            # Designate Height and Width of our app
            app_width = 400
            app_height = 100

            screen_width = t.winfo_screenwidth()
            screen_height = t.winfo_screenheight()

            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)

            t.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            label = Label(t, text="Loading...", font="arial 15 bold").pack()

            my_progress = ttk.Progressbar(t, orient=HORIZONTAL, length=300, mode='determinate')
            my_progress.pack(pady=10)

            label1 = Label(t, text="")
            label1.pack()


            for i in range(6):
                label1.config(text=my_progress['value'])
                my_progress['value'] += 20
                t.update_idletasks()
                time.sleep(1)

            t.destroy()


        def play():
            global loaded
            pygame.mixer.music.unload()
            pbtn1.config(image=btnimg3)
            book = askopenfilename()
            pdfReader = PyPDF2.PdfFileReader(book)
            speaker = pyttsx3.init()
            rate = speaker.getProperty('rate')
            print("speechrate :", rate)
            speaker.setProperty('rate', 150)
            voices = speaker.getProperty('voices')
            # changing index, changes voices, 0 for male
            # changing index, changes voices, 1 for female
            speaker.setProperty('voice', voices[1].id)
            pages = pdfReader.numPages
            print("number of pages :",pages)
            messagebox.showinfo("PopUp Message","Please wait...It takes some time to load! Untill don't click any button")

            for num in range(0, pages):


                page = pdfReader.getPage(num)
                text = page.extractText()
                speech = gTTS(text=text)
                speech.save('D1.mp3')

            progress()

            messagebox.showinfo("PopUp Message", "Conversion Completed!!!")
            loaded=TRUE



        global played
        global loaded
        loaded = FALSE
        played = FALSE
        def start(is_played):
            global played
            global loaded
            played = is_played

            if loaded==FALSE:

                messagebox.showerror("Alert","Please Import PDF file")

            else:
                pygame.mixer.music.load("D1.mp3")
                pygame.mixer.music.play(loops=0)
                played = TRUE


        def stop():
            global played
            pygame.mixer.music.stop()
            pbtn1.config(image=btnimg3)
            pbtn3.config(image=btnimg5)
            played=FALSE



        # Pause/Resume function
        global paused
        paused = FALSE

        def resume(is_paused):

            global paused
            paused = is_paused

            if (paused):
                #unpause player
                pygame.mixer.music.unpause()
                paused = FALSE
                pbtn3.config(image=btnimg5)

                if(played==TRUE):
                     pbtn1.config(image=btnimg4)


            elif played:
                pygame.mixer.music.pause()
                paused = TRUE
                pbtn3.config(image=btnimg6)
                pbtn1.config(image=btnimg8)



        def set_vol(val):
            volume = int(val) / 100
            pygame.mixer.music.set_volume(volume)

        global v
        v = FALSE
        def volume(is_v):
            global v
            v = is_v
            if v:
                # volume mute
                scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol, bg="red", fg="white")
                scale.set(0)
                pygame.mixer.music.set_volume(0)
                scale.place(x=310, y=255)
                scale.config(state=DISABLED)
                # changing image
                pbtn4.config(image=btnimg10)
                v=FALSE




            else:
                scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol, bg="red", fg="white")
                scale.set(50)
                pygame.mixer.music.set_volume(0.7)
                scale.place(x=310, y=255)
                pbtn4.config(image=btnimg9)
                v=TRUE



        # startbutton image changing
        def returncolor():
            pbtn1.config(image=btnimg3)

        def playButton():
            # audio = ("D1.mp3")
            # print(audio.info.length)
            global loaded
            if loaded==FALSE:
                pbtn1.config(image=btnimg3)
                pbtn1.after(100,start(played))


            else:

                duration = eyed3.load('D1.mp3').info.time_secs
                t=int(duration*1000)
                print("millisec:",t)
                pbtn1.config(image=btnimg4)
                pbtn1.after(100,start(played))
                pbtn1.after(t,returncolor)

        def Exit():
            pygame.mixer.music.unload()
            root.destroy()
            mainFunction(hidePopUp=1)


        # define button image
        btnimg1 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/select.png")
        btnimg2 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/back.png")
        btnimg3 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/power-button.png")
        btnimg4 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/playing.png")
        btnimg5 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/pause.png")
        btnimg6 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/play1.png")
        btnimg7 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/stop.png")
        btnimg8 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/notplaying.png")
        btnimg9 = PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/volume1.png")
        btnimg10= PhotoImage(file="C:/Users/satheesh/PycharmProjects/pythonProject/venv/images/mute.png")

            


        #frame2 buttons
        btnf1 = Button(root, image =btnimg1 , font = 'arial 15 bold',cursor="hand2",bg='white', command=lambda :play(),
                       width =50,height=50,activebackground='#8EA7AE')
        btnf1.place(x=30, y=120)

        btnf2 = Button(root,image=btnimg2,font = 'arial 15 bold',cursor="hand2",bg='white',command =lambda: Exit(),
                       width =50,height=50,activebackground='#8EA7AE')
        btnf2.place(x=100,y=120)



        pbtn1=Button(root,image=btnimg3,command=lambda :[playButton()],font='arial 15 bold',cursor="hand2",width =50,height=50)
        pbtn1.place(x=30,y=250)
        pbtn2=Button(root,image=btnimg7,command=stop,font='arial 15 bold',cursor="hand2",width =50,height=50)
        pbtn2.place(x=100,y=250)
        pbtn3=Button(root,image=btnimg5,command=lambda :[resume(paused)],font='arial 15 bold',cursor="hand2",width =50,height=50)
        pbtn3.place(x=170,y=250)
        pbtn4=Button(root,image=btnimg9,command=lambda :[volume(v)],font='arial 15 bold',cursor="hand2",width =50,height=50)
        pbtn4.place(x=240,y=250)




        # bind tooltip with button1
        tip.bind_widget(btnf1, balloonmsg="Select the PDF File")
        # bind tooltip with button2
        tip.bind_widget(btnf2, balloonmsg="Click to Go Back")
        # bind tooltip with button1
        tip.bind_widget(pbtn1, balloonmsg="Start Playing")
        # bind tooltip with button1
        tip.bind_widget(pbtn2, balloonmsg="Stop")
        # bind tooltip with button1
        tip.bind_widget(pbtn3, balloonmsg="Pause/Resume")
        # bind tooltip with button1
        tip.bind_widget(pbtn4, balloonmsg="Adjust Volume / Mute")

        root.mainloop()


    def change(e):

        e.widget['bg'] = 'goldenrod2'
        e.widget['fg'] = 'OrangeRed1'



    def change_back(e):

        e.widget['bg'] = 'goldenrod1'
        e.widget['fg'] = 'white'
        mybtn3['bg']='orangered1'
        mybtn3['fg']='black'



    #mainFunction buttons
    # button1
    mybtn1 = Button(root, text="Text To Speech", font = ("Century Gothic", 18, "bold"),cursor="hand2",width=15,height=2,bg='goldenrod1',
                    fg='white',activebackground='peach puff',command=lambda: [mainExit(), frame1()])
    mybtn1.place(x=80, y=200)

    # hover mouse effect
    mybtn1.bind("<Enter>", change)
    mybtn1.bind("<Leave>", change_back)


    # button2
    mybtn2 = Button(root, text="Pdf To Audio", font = ("Century Gothic", 18, "bold"),cursor="hand2",width=15,height=2,bg='goldenrod1',
                    fg='white',activebackground='peach puff',command=lambda: [mainExit(), frame2()])
    mybtn2.place(x=500, y=200)

    # hover mouse effect
    mybtn2.bind("<Enter>", change)
    mybtn2.bind("<Leave>", change_back)

    # button3
    mybtn3 = Button(root, text='E X I T', font=("arial", 15, "bold"),cursor="hand2",width=6,height=1,
                    command=mainExit, bg='orangered1',activebackground='peach puff')
    mybtn3.place(x=360, y=320)

    # hover mouse effect
    mybtn3.bind("<Enter>", change)
    mybtn3.bind("<Leave>", change_back)


    # bind tooltip with button1
    tip.bind_widget(mybtn1, balloonmsg="Hi User !, click to enter the Speech Convertion")
    # bind tooltip with button2
    tip.bind_widget(mybtn2, balloonmsg="Hi User !, click to enter the Audio Convertion")
    # bind tooltip with button3
    tip.bind_widget(mybtn3, balloonmsg="Bye !, click to Exit")


    # infinite loop to run program
    root.mainloop()

# calling the Main function
mainFunction()