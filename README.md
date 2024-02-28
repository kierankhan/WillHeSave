# WillHeSave

Predicts whether a user will save a song to their spotify library using the Random Forest algorithm from Sklearn.

## How to use

Simply clone this repository, pip install requirements.txt and run the train_model.ipynb. You will be prompted for either a link to a song or a playlist depending on which of the last two cells you run.

By default the model is trained on my friend Eric's spotify data (I can't nail down his music taste!). If you want to train it for yourself, you have to do a couple things:

1. Go to the spotify developer portal and make a new project. From there you can get the client_id and client_secret keys, and replace them for the ones in train_model.ipynb.

2. Make two spotify playlists of songs you really like, and songs you don't. The larger sample size the better! Once you have these, navigate to this cell:
```
# good = create_df_from_playlist("https://open.spotify.com/playlist/6vOYm55EbfPnFpAgZynn6I?si=9070e8f011494eb0", 1)
# good2 = create_df_from_playlist("https://open.spotify.com/playlist/1bb77h4aEV7sutQ8EIvrL9?si=4ed01da7142d4f72", 1)
# bad = create_df_from_playlist("https://open.spotify.com/playlist/5Dflf6jWmbFbpgjsJV4cwI?si=36def02aab974355", 0)
# 
# df = pd.concat([good, good2, bad], ignore_index=True)
df = pd.read_csv("eric_samples.csv")
df
```
Uncomment the commented section and comment ```df = pd.read_csv("eric_samples.csv")``` and plug in the playlists for good and bad respectively.
Rerun the program and you should be good to go! The model currently has __~75%__ accuracy. 

More to come. Next I will train a deep learning model using Mel Spectrograms. Stay Tuned!
