import os
import shutil

from src.utils.classifier import train_and_save_model
from src.utils.constants import MODEL_DIR
from src.utils.features_generation import extract_features
from src.utils.make_dataset import get_XMLtree, exctract_corpus, extract_dataset
from src.utils.process_text import make_feature_matrix


def make_directory():
    '''Make directory for model'''
    if os.path.isdir(MODEL_DIR):
        shutil.rmtree(MODEL_DIR)
    os.makedirs(MODEL_DIR, exist_ok=True)

def train_model(data_path):
    '''Train model for name parsing'''
    make_directory()
    tree = get_XMLtree(data_path)
    # Extract valuable features from the current dataset
    extract_features(*exctract_corpus(tree))
    # Create tokenized dataset
    dataset, target = extract_dataset(tree)
    # Convert tokenized dataset to vectors
    train_and_save_model(*make_feature_matrix(dataset, target))
    print('Model saved')


if __name__ == "__main__":
    data_path = './data/person_labeled.xml'
    train_model(data_path)