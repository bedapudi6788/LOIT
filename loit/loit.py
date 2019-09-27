import os
import bz2
import json
import logging
import pydload
from progressbar import progressbar

urls = {
    'telugu': {
        'data': 'https://github.com/bedapudi6788/LOIT/releases/download/v1/lit-t.json.bz2',
        'cbow': 'https://github.com/bedapudi6788/LOIT/releases/download/v1/telugu_cbow_100d.bin',
        'skipgram': 'https://github.com/bedapudi6788/LOIT/releases/download/v1/telugu_skipgram_100d.bin'
    },
    'hindi': {
        'data': 'https://github.com/bedapudi6788/LOIT/releases/download/v1/lit-t.json.bz2',
        'cbow': 'https://github.com/bedapudi6788/LOIT/releases/download/v1/hindi_cbow_100d.bin',
        'skipgram': 'https://github.com/bedapudi6788/LOIT/releases/download/v1/hindi_skipgram_100d.bin'
    }
}


def download(lang_name, to_download):
    if lang_name not in urls:
        logging.error(lang_name + ' is not supported yet.')
        exit()
    
    if to_download not in urls[lang_name]:
        logging.error(lang_name + ' : ' + to_download + ' is not supported yet.')
        exit()
    
    home = os.path.expanduser("~")
    lang_path = os.path.join(home, '.LOIT_' + lang_name)
    to_download_path = os.path.join(lang_path, to_download)
    url = urls[lang_name][to_download]

    if not os.path.exists(lang_path):
        os.mkdir(lang_path)
    
    logging.info('Downloading ' + lang_name + ' : ' + to_download)
    pydload.dload(url=url, save_to_path=to_download_path, max_time=None)
    
    return True

def read_data(lang_name):
    home = os.path.expanduser("~")
    lang_path = os.path.join(home, '.LOIT_' + lang_name)
    to_download_path = os.path.join(lang_path, 'data')
    
    if not os.path.exists(to_download_path):
        logging.warning(to_download_path + ' does not exist. Downloading it.')
        download(lang_name, 'data')
    
    opened_file = bz2.BZ2File(to_download_path, "r")
    
    for line in opened_file:
        line = json.loads(line.strip())
        yield line

def load_vectors(lang_name, type):
    try:
        import fasttext
    except Exception as ex:
        logging.exception(str(ex))
        print('Run pip install git+https://github.com/facebookresearch/fastText to install fasttext')
        exit()

    home = os.path.expanduser("~")
    lang_path = os.path.join(home, '.LOIT_' + lang_name)
    to_download_path = os.path.join(lang_path, type)

    if not os.path.exists(to_download_path):
        logging.warning(to_download_path + ' does not exist. Downloading it.')
        download(lang_name, type)
    
    model = fasttext.load_model(to_download_path)
    
    return model