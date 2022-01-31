from src.name_parser import NameParser
from src.utils.options import args

if __name__ == "__main__":
    parser = NameParser()
    print(f'INPUT: {args.name}')
    print(f'OUTPUT: {parser.tag(args.name)}')
