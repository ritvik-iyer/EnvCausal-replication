# Library for Mandarin to English translation 
import pinyin
# Libraries for data manipulation 
import numpy as np
import pandas as pd 

def eng_translator(phrase_list):
    translation_map = {}
    for phrase in phrase_list:
        pinyin_phrase = pinyin.get(phrase, format="strip", delimiter=" ")
        pinyin_phrase = ''.join(pinyin_phrase.split(' '))
        pinyin_phrase = pinyin_phrase[0].upper() + pinyin_phrase[1:]
        translation_map[phrase] = pinyin_phrase
    return translation_map

def translate_column_to_eng(df, col):
    unique_phrases = np.unique(df[col]).tolist()
    translation_map = eng_translator(unique_phrases)
    return df[col].map(translation_map)