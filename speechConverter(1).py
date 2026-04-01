import tkinter as tk
from tkinter import ttk
import pyttsx3


root=tk.Tk()
root.geometry("400x300")
root.title("text to speech converter")

def action():
    sentence=txt.get("1.0","end-1c",)
    engine.setProperty('rate',tmp.get())
    engine.setProperty('volume',vol.get())
    
    sel_voice=vc.get()
    voices=engine.getProperty('voices')
    if(sel_voice=='Male'):
        engine.setProperty('voice',voices[0].id)
    elif(sel_voice=='Female'):
        engine.setProperty('voice',voices[1].id)
    
    engine.say(sentence)
    engine.runAndWait()
    
engine=pyttsx3.init()
lb1=tk.Label (root, text="Enter text: ", font=('calibri', 15))
lb1.place(x=15, y=20)

txt=tk.Text(root,width=30,height=6)
txt.place(x=115,y=20)

lb2=tk.Label(root,text="volume",font=("calibri",15))
lb2.place(x=200,y=150)

volm=tk.DoubleVar( value=1.0)
vol=tk.Scale(root,from_=0,to=1,resolution=0.1,orient="horizontal",variable=volm)
vol.place(x=180,y=180)

lb3=tk.Label(root,text="Tempo",font=("calibri",15))
lb3.place(x=300,y=150)

tmp=tk.IntVar( value=150)
tempo=tk.Scale(root,from_=1,to=300,orient="horizontal",variable=tmp)
tempo.place(x=300,y=180)

lb4=tk.Label(root,text="select voice",font=("calibri",15))
lb4.place(x=40,y=150)


vc=ttk.Combobox(root,values=['Male','Female'])
vc.set('Male')
vc.place(x=30,y=200)

btn=ttk.Button(root,text="Convert", command=action)
btn.place(x=200,y=250)

root.mainloop()