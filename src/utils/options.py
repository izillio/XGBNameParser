import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', default='Dr. Jack Ali Reisenfeld-Rozumovsky II Jr.',
                    help='String with name to parse')
args = parser.parse_args()