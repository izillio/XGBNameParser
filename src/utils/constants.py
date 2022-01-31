MODEL_DIR = './src/model'
WORD_ENDINGS_PATH = './src/model/endings.txt'
WORD_BEGINNINGS_PATH = './src/model/beginnings.txt'
UNIQUE_CHAR_PATH = './src/model/chars.txt'
PREFIXES_PATH = './src/model/prefixes.txt'
MODEL_PATH = './src/model/model.bin'

PARAMS_ENDING_3 = {'subsets': ['MiddleName', 'GivenName', 'Surname'],
          'ending': True,
          'window': 3,
          'thresh': 0.01}

PARAMS_ENDING_2 = {'subsets': ['MiddleName', 'GivenName', 'Surname'],
          'ending': True,
          'window': 2,
          'thresh': 0.02}

PARAMS_BEGINNING_3 = {'subsets': ['MiddleName', 'GivenName', 'Surname'],
          'ending': False,
          'window': 3,
          'thresh': 0.01}

PARAMS_BEGINNING_2 = {'subsets': ['MiddleName', 'GivenName', 'Surname'],
          'ending': False,
          'window': 2,
          'thresh': 0.02}

RE_ALL_LET = r'[a-zA-Z]+'
RE_ALL_LET_NUM = '[^A-Za-z0-9]+'
RE_NO_LET = r'[^a-zA-Z]+'
RE_ALL_CONSONANTS = r'[^aeiou]'

SUFFIXES_FIELDS = ['SuffixOther', 'SuffixGenerational', 'PrefixMarital', 'PrefixOther']
SUFFIXES_THRESH = 0.01