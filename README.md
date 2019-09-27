# LOIT - Lot Of Indic Tweets

# Installation
```
pip install loit
```


# Usage
```
import loit

# download data
# hindi and telugu are available as of now
loit.download('hindi', 'data')

# download fasttext cbow vectors bin
loit.download('hindi', 'cbow')


# download fasttext skipgram vectors bin
loit.download('hindi', 'skipgram')

# read the jsons from data
#returns iterator that yields jsons
it = loit.read_data('telugu')

for tweet_json in it:
    print(tweet_json)['tweet']
    input()
```
