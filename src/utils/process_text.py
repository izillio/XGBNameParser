import re
import numpy as np
from src.utils.constants import WORD_ENDINGS_PATH, WORD_BEGINNINGS_PATH, UNIQUE_CHAR_PATH, PREFIXES_PATH, \
    RE_NO_LET, RE_ALL_CONSONANTS, VALUABLE_LETTER_COMB


def open_feat_list(path):
    '''Open saved .txt file, read lines, return list'''
    with open(path, 'r') as f:
        feat_list = [x[:-1] for x in f.readlines()] #remove \n
    return feat_list

def preprocess_ending_match(text, part):
    '''Match ending of the token'''
    window = len(part)
    return str(text)[-window:] == part

def preprocess_beginning_match(text, part):
    '''Match beginning of the token'''
    window = len(part)
    return str(text)[:window] == part

def preprocess_match_vector(text, feat_list, ending=True):
    '''Create a vector of matches with features from list of features and token'''
    text_norm = text.lower()
    if ending:
        process_function = preprocess_ending_match
    else:
        process_function = preprocess_beginning_match
    features_vector = []
    for feat in feat_list:
        features_vector.append(process_function(text_norm, feat))
    return features_vector

def define_word_length(text):
    '''Count all letters in token'''
    l = len(re.sub(RE_NO_LET, '', text))
    return [l]

def find_spec_symbols(text, symb_list):
    '''Create a vector of occurrences of symbols in token'''
    features_vector = []
    for s in symb_list:
        features_vector.append(text.count(s))
    return features_vector

def vowel_ratio(token):
    '''Calculate ratio of vowels in in token'''
    tok_len = len(token)
    vow_len = len(re.sub(RE_ALL_CONSONANTS, '', token.lower()))
    return [vow_len / tok_len]

def convert_text_to_vector(text):
    '''Convert single token to vector'''
    vector = [
        *preprocess_match_vector(text, open_feat_list(WORD_ENDINGS_PATH), ending=True),
        *preprocess_match_vector(text, open_feat_list(WORD_BEGINNINGS_PATH), ending=False),
        *define_word_length(text),
        *find_spec_symbols(text, open_feat_list(UNIQUE_CHAR_PATH)),
        *preprocess_match_vector(text, open_feat_list(PREFIXES_PATH), ending=False),
        *vowel_ratio(text),
        *find_spec_symbols(text, VALUABLE_LETTER_COMB),
            ]
    return vector

def process_tokenized_name(tokens):
    '''Convert tokenized name to 3-gram vector'''
    datapoint_vector = []
    vectors = [convert_text_to_vector(tok) for tok in tokens]
    vec_length = len(vectors[0])
    empty_vec = [np.nan] * vec_length
    for i in range(len(tokens)):
        left_vector_idx = i - 1
        right_vector_idx = i + 1
        if left_vector_idx < 0:
            l_vec = empty_vec
        else:
            l_vec = vectors[left_vector_idx]
        if right_vector_idx >= len(tokens):
            r_vec = empty_vec
        else:
            r_vec = vectors[left_vector_idx]

        datapoint_vector.append([*l_vec, *vectors[i], *r_vec])
    return datapoint_vector

def make_feature_matrix(data, target):
    '''Convert dataset to 3-grams feature matrix'''
    three_gramm_dataset = []
    three_gramm_target = []
    for name_idx, name in enumerate(data):
        three_gramm_dataset += process_tokenized_name(name)
        three_gramm_target += target[name_idx]
    return np.array(three_gramm_dataset), np.array(three_gramm_target)