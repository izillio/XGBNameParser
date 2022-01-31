from src.utils.constants import PARAMS_ENDING_3, PARAMS_ENDING_2, PARAMS_BEGINNING_3, PARAMS_BEGINNING_2, \
    WORD_ENDINGS_PATH, WORD_BEGINNINGS_PATH, RE_ALL_LET, UNIQUE_CHAR_PATH, RE_NO_LET, PREFIXES_PATH, SUFFIXES_FIELDS, \
    SUFFIXES_THRESH


def get_most_popular_parts_from_field(df, target, subset, window, ending=True, thresh=0.01):
    '''Exctract most frequent beginnigs/endings from selected class.
       subset - name of column (name of class)
       window - length of window
       threshold - filter by TF'''
    subset_normalized = df[target == subset].str.lower()
    if ending:
        def process(x, window):
            return str(x)[-window:]
    else:
        def process(x, window):
            return str(x)[:window]
    word_fragments = subset_normalized.map(lambda x: process(x, window))
    freq = word_fragments.value_counts(normalize=True)
    return freq[freq > thresh].index.tolist()

def get_most_popular_parts_subsets(df, target, subsets, ending=True, window=2, thresh=0.02):
    '''Exctract most frequent beginnigs/endings from group of classes.
       subsets - list of classes to process
       window - length of window
       threshold - filter by TF'''
    word_pieces = []
    for subset in subsets:
        word_pieces += get_most_popular_parts_from_field(df,
                                                         target,
                                                         subset,
                                                         window=window,
                                                         ending=ending,
                                                         thresh=thresh)
    return word_pieces

def save_most_popular_endings(df, target):
    '''Make a list of most popular word endings and save it as .txt.
       The file further will be used for token vectorization.'''
    endings = get_most_popular_parts_subsets(df, target, **PARAMS_ENDING_3)
    endings += get_most_popular_parts_subsets(df, target, **PARAMS_ENDING_2)
    endings = [f'{x}\n' for x in set(endings)]
    with open(WORD_ENDINGS_PATH, 'w') as f:
        f.writelines(endings)

def save_most_popular_beginnings(df, target):
    '''Make a list of most popular word beginnings and save it as .txt.
       The file further will be used for token vectorization.'''
    beginnings = get_most_popular_parts_subsets(df, target, **PARAMS_BEGINNING_3)
    beginnings += get_most_popular_parts_subsets(df, target, **PARAMS_BEGINNING_2)
    beginnings = [f'{x}\n' for x in set(beginnings)]
    with open(WORD_BEGINNINGS_PATH, 'w') as f:
        f.writelines(beginnings)

def save_spec_symbols(df):
    '''Make a list of most symbols and save it as .txt.
       The file further will be used for token vectorization.'''
    norm = df.str.replace(RE_ALL_LET, '', regex=True)
    tf = norm.value_counts()
    all_non_alph_symb = tf[tf>1].index.tolist()
    unique_char = []
    for string in all_non_alph_symb:
        for char in string:
            unique_char.append(char)
    unique_char = [f'{ch}\n' for ch in list(set(unique_char))]
    with open(UNIQUE_CHAR_PATH, 'w') as f:
        f.writelines(unique_char)

def extract_suffixes_from_subset(df, thresh=SUFFIXES_THRESH):
    '''Make a list of most suffixes and prefixes (Mr, Ms, M.D., II, etc.)'''
    norm = df.str.replace(RE_NO_LET, '', regex=True)
    tf = norm.value_counts(normalize=True)
    pref_list = tf[tf > thresh].index.tolist()
    return pref_list

def save_most_common_prefixes(df, target):
    '''Make a list of most suffixes and prefixes (Mr, Ms, M.D., II, etc.) and save it as .txt.
       The file further will be used for token vectorization.'''
    norm = df.str.lower()
    pref_list = []
    for subset in SUFFIXES_FIELDS:
        pref_list += extract_suffixes_from_subset(norm[target==subset])
    pref_list = [f'{ch}\n' for ch in list(set(pref_list))]
    with open(PREFIXES_PATH, 'w') as f:
        f.writelines(pref_list)

def extract_features(df, target):
    '''Extract all features such as word parts, symbols, prefixes, etc.'''
    save_most_popular_endings(df, target)
    save_most_popular_beginnings(df, target)
    save_spec_symbols(df)
    save_most_common_prefixes(df, target)

