from struct import pack
from tkinter import *
import requests
root = Tk()

options = { 'uk','de','en','fr','es'}
options_sec = { 'uk','de','en','fr','es'}
  
clicked = StringVar()
clicked.set('Input_lenguage')

clicked_sec = StringVar()
clicked_sec.set('Translation_language')

drop = OptionMenu( root , clicked , *options )
drop.pack()
drop = OptionMenu( root , clicked_sec , *options_sec )
drop.pack()

label = Label( root , text = " " )
label.pack()

Fr_lab = Label(text="Please print id:")
Fr_fra = Frame()
Fr_lab.pack()
Fr_fra.pack()

entry_id = Entry(master=Fr_fra)

entry_id.grid(row=1, column=1)
First_fr = Frame()
def send_id():
    enter_text = entry_id.get()
    language_fr = clicked.get()
    language_sec = clicked_sec.get()
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
    "q": "{}".format(enter_text),
    "source": "{}".format(language_fr),
    "target": "{}".format(language_sec)
    }   
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "f0eda7c17amsha10f3c793fdf668p1ba57fjsn4b46df9be184",
    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    json = response.json()
    translation = json["data"]["translations"]["translatedText"]
    finish_data.config(text="Translation: {}".format(translation))

    print(translation)
    
finish_data = Label()
finish_data.pack()

def input_data():

  Last_but = Frame()
  Last_but.pack()
  button = Button(text="Show", master=Last_but,  command=send_id)
  button.pack()

  mainloop()

input_data()