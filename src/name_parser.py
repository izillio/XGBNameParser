import numpy as np
import xgboost as xgb

from src.utils.constants import WORD_ENDINGS_PATH, WORD_BEGINNINGS_PATH, UNIQUE_CHAR_PATH, PREFIXES_PATH, MODEL_PATH
from src.utils.process_text import open_feat_list, process_tokenized_name


class NameParser:
    def __init__(self):
        self.endings_list = open_feat_list(WORD_ENDINGS_PATH)
        self.beginnings_list = open_feat_list(WORD_BEGINNINGS_PATH)
        self.chars_list = open_feat_list(UNIQUE_CHAR_PATH)
        self.prefixes = open_feat_list(PREFIXES_PATH)
        self.classifier = self.load_model()
        self.classes = self.classifier.classes_

    def load_model(self):
        '''Load pre-trainde XGB model'''
        xgb_model = xgb.XGBClassifier()
        xgb_model.load_model(MODEL_PATH)
        return xgb_model

    def preprocess(self, tokens):
        '''Convert tokens to feature vectors'''
        feature_matrix = np.array(process_tokenized_name(tokens))
        return feature_matrix

    def predict_tokens(self, tokens):
        '''Predict tags for tokens'''
        pred_vector = self.classifier.predict(self.preprocess(tokens))
        prediction = list(zip(pred_vector, tokens))
        return prediction

    def tokenize(self, string):
        '''Most primitive tokenizer'''
        tokens = string.split(' ')
        return tokens

    def tag(self, string):
        '''Tag parts of name in string'''
        tokens = self.tokenize(string)
        prediction = self.predict_tokens(tokens)
        return prediction



