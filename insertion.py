import random
from nltk.corpus import wordnet

def random_insertion(text, n=1):
    words = text.split()
    new_words = words.copy()
    for _ in range(n):
        add_word(new_words)
    return " ".join(new_words)

def add_word(new_words):
    synonyms = []
    counter = 0
    while len(synonyms) < 1:
        random_word = new_words[random.randint(0, len(new_words)-1)]
        synonyms = get_synonyms(random_word)
        counter += 1
        if counter >= 10:
            return
    random_synonym = synonyms[0]
    random_idx = random.randint(0, len(new_words)-1)
    new_words.insert(random_idx, random_synonym)

print(random_insertion(text, 2))
