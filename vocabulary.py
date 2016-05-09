# coding: utf-8
import nltk
nltk.download('punkt')

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize


with open(r'.\2000_frequent_words.txt') as f:
    # Easy words that should be excluded when analyzing
    # Convert them to lowercase just in case
    easy_words = [word.lower() for word in f.read().split()]

assert easy_words[:2] ==['the', 'i']

def get_base(word):
    """ Returns the base of a word.
        Most logic is handled by `wordnet.morphy` but
        there were some exceptions that I would like to modify,
        such as 'was' -> 'wa'."""
    exceptions = ['was', 'has', 'does', 'less']
    if word in exceptions:
        return word

    base = wordnet.morphy(word)
    if base is None:
        # If no base is found, just use that word
        base = word
    return base

assert get_base('hellos') == 'hello' and get_base('was') == 'was'


def import_vocabularies(s):
    """ returns a set of valid words from a string.
    Valid words are defined by a combination of alphabets and '-'(hyphen) """
    valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'

    # Get all tokens from string and convert them to lowercase
    tokens = [token.lower() for token in word_tokenize(s)]
    def is_word(token):
        """ Checks if a given token is a valid word or not """
        return all(character in valid_characters for character in token)

    vocabularies = set()
    for token in tokens:
        if not is_word(token):
            # Not a word, probably special character or something.
            continue

        # Get the base of word
        word = get_base(token)
        vocabularies.add(word)
    return vocabularies

assert import_vocabularies('Hello, worlds!') == {'hello', 'world'}


def get_definitions(vocabularies):
    """ Return a dictionary of vocabularies and their definitions """
    definitions = dict()
    for vocab in vocabularies:
        synonyms = wordnet.synsets(vocab)
        if not synonyms:
            # If there is no definition
            definition = 'No definition found.'
        else:
            # Fetch the first definition
            definition = synonyms[0].definition()
        definitions[vocab] = definition
    return definitions

assert get_definitions(['hello', 'world']) == \
        {'world': 'everything that exists anywhere',
         'hello': 'an expression of greeting'}


def analyze_hard_vocabulary(s):
    """ Returns dictionary of hard vocabularies and its definitions """
    vocabularies = import_vocabularies(s)
    hard_vocabularies = {vocab for vocab in vocabularies if vocab not in easy_words}
    return get_definitions(hard_vocabularies)

assert analyze_hard_vocabulary('Hello, horrifying world!') == \
    {'horrify': 'fill with apprehension or alarm; cause to be unpleasantly surprised'}
