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

# download fasttext cbow vectors and read them 
loit.load_vectors('hindi', 'cbow')

# download fasttext skipgram vectors and read them
loit.load_vectors('hindi', 'skipgram')

# read the jsons from data
#returns iterator that yields jsons
it = loit.read_data('telugu')

for tweet_json in it:
    print(tweet_json['tweet'])
    input()
```

# ToDO
1. Train a DeepMoji type of model on this data.
