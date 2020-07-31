import os
import pathlib

import nltk
import requests

nltk.download('punkt')

from bs4 import BeautifulSoup

BASE_DIR = pathlib.Path.cwd()
DIRECTORY_TRAIN = BASE_DIR.joinpath('data_ru', 'protechn_corpus_eval', 'train')
DIRECTORY_DEV = BASE_DIR.joinpath('data_ru', 'protechn_corpus_eval', 'dev')
DIRECTORY_TEST = BASE_DIR.joinpath('data_ru', 'protechn_corpus_eval', 'test')
DIRECTORY_MARKUP = BASE_DIR.joinpath('data_ru', 'protechn_corpus_eval', 'markup')
DIRECTORY_PREDICT = BASE_DIR.joinpath('data_ru', 'protechn_corpus_eval', 'predict')
ARTICLE = 7
TECHNIQUES = [
    "No", "Remark", "Praise", "Insult", "Bug", "Defect", "Question", "Wish"
]
HUMAN_READABLE_TECHNIQUES = [
    "No", "Remark", "Praise", "Insult", "Bug", "Defect", "Question", "Wish"
]


from flask_app.routes import get_existent_ids, get_list, write_existent_dict


def create_labels_file():
    for f in DIRECTORY_TRAIN.glob('*.txt'):
        DIRECTORY_TRAIN.joinpath('.'.join([f.name.split('.')[0], 'labels', 'tsv'])).touch()


def to_sentences(directories, directory):
    ids = get_existent_ids(directories=directories)
    for id_ in ids:
        overwrite_one_article(id_, directory=directory)


def overwrite_one_article(id_, directory=DIRECTORY_TRAIN):
    lst = get_list(id_)
    symbols = []
    techniques = []
    with open(directory.joinpath(f'article{id_}.txt'), 'r+', encoding='utf-8') as f:
        text = f.read()
        sent_text = '\n'.join(nltk.sent_tokenize(text))  # , language="russian"
        i = 0
        j = 0
        while i < len(text) and j < len(sent_text):
            if text[i] == sent_text[j]:
                symbols.append(text[i])
                techniques.append(lst[i])
                i += 1
                j += 1
            else:
                if sent_text[j] == '\n':
                    symbols.append(sent_text[j])
                    techniques.append(lst[i])
                    j += 1
                while i < len(text) and j < len(sent_text) and text[i] != sent_text[j]:
                    i += 1
        f.seek(0)
        f.write(''.join(symbols))
        f.truncate()
    assert len(symbols) == len(techniques)
    write_existent_dict(id_, techniques)


def main():
    # extract_putins_interviews()
    # create_labels_file()
    # overwrite_one_article(83173104362)
    to_sentences(directories=(DIRECTORY_MARKUP,), directory=DIRECTORY_MARKUP)


if __name__ == '__main__':
    main()
