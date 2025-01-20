from tkinter import *
import json
import pandas as pd
from random import *
from tkinter import messagebox
color1 = "#38a3a5"
color2 = "#57cc99"
color3 = "#80ed99"
font1 = ("ariel", 40, "italic")
font2 = ("ariel", 40, "bold")
font3 = ("ariel", 30, "bold")
#opening csv
data = pd.read_csv("data/data.csv")
word_dict = data.to_dict(orient="records")

#get words
current_language = 2
current_card = choice(word_dict)
def toggle_face():
    global current_language
    current_language +=1
    next_word()
def choice_word():
    global current_card
    current_card = choice(word_dict)
    next_word()
def next_word():
    global current_language, current_card
    keys = ["ENGLISH", "TURKISH"]
    amountOfWord = len(current_card[keys[current_language % 2]])
    if amountOfWord <= 5:
        wordLabel.place(x=280 - amountOfWord * 12, y=330)
    elif amountOfWord > 9:
        wordLabel.place(x=280 - amountOfWord * 15, y=330)
    else:
        wordLabel.place(x=280 - amountOfWord * 14, y=330)
    wordLabel.config(text=current_card[keys[current_language % 2]].lower())
    currentLangLabel.config(text=keys[current_language % 2])
def query():
    query_keys = queryBox.get().lower()
    for i in word_dict:
        if i["TURKISH"] ==  query_keys or i["ENGLISH"] == query_keys:
            messagebox.showinfo(title="found", message=f"{i['TURKISH']} --> {i['ENGLISH']}")

# UI  Setup
root = Tk()
root.title("FLASCARDs")
root.config(bg=color1)
root.minsize(width=600, height=600)
canvas = Canvas(root, width=600, height=600, bg=color1)
canvas.place(x=0, y=0)
bg_image = PhotoImage(file="data/assets/bg.png")
canvas.create_image(300, 300, image=bg_image)
#labels
currentLangLabel = Label(text=" ", highlightthickness=0, font=font1, bg="#ed7065")
currentLangLabel.place(x=180, y=180)
wordLabel = Label(text=" ", highlightthickness=0, font=font2, bg="#e7695d")
#buttons
nextBut = Button(text="⏭", highlightthickness=0, font=font3, bg="#619fa3", command=choice_word)
prevoiusBut = Button(text="🔍", highlightthickness=0, font=font3, bg="#65a6aa", command=query)
cahngeFaceBut = Button(text="🔄", highlightthickness=0, font=font3,bg="#e2675a", command=toggle_face)
nextBut.place(x=420, y=500)
prevoiusBut.place(x=120, y=500)
cahngeFaceBut.place(x=270, y=500)
queryBox = Entry(highlightthickness=0, bg="#619fa3")
queryBox.place(x=250, y=90)
next_word()
root.mainloop()