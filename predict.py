from tkinter import *
from tkinter import ttk
import spotipy as sp
import numpy as np
import import_ipynb
from train_model import RFM

def predict():
    song_link = song_entry.get()
    arr = create_arr_from_song(song_link)
    print(RFM.predict(arr))


def create_arr_from_song(song_link: str):
    song_URI = song_link.split("/")[-1].split("?")[0]
    row = []
    track = sp.track(song_URI)
    row.append(track["name"])
    print(row)
    row.append(song_URI)
    track_pop = row.append(track["popularity"])
    artist_uri = track["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    #Name, popularity, genre
    artist_name = row.append(track["artists"][0]["name"])
    artist_pop = row.append(artist_info["popularity"])
    artist_genres = row.append(artist_info["genres"])

    features = sp.audio_features(song_URI)[0]
    # print(features)

    row.extend(list(features.values()))
    # arr = np.array(row)
    return row


root = Tk()
root.title("Predict Song")
root.geometry('300x100')

song_label = Label(root, text="Song Link:")
song_label.pack()
song_entry = Entry(root, width=20)
song_entry.pack()

register_button = Button(root, text="Predict", command=predict)
register_button.pack()

# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
#
# feet = StringVar()
# song_entry= ttk.Entry(mainframe, width=20, textvariable=feet)
# song_entry.grid(column=2, row=1, sticky=(W, E))
#
# ttk.Button(mainframe, text="Predict", command=predict).grid(column=3, row=3, sticky=W)

root.mainloop()