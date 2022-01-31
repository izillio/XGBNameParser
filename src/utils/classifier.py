import xgboost as xgb

from src.utils.constants import MODEL_PATH


def train_and_save_model(X, y):
    clf = xgb.XGBClassifier(objective='multi:softprob')
    clf.fit(X, y)
    clf.save_model(MODEL_PATH)