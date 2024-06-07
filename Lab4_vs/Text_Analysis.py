import re
import zipfile
import pickle

def isdeclarative(sentence):
    return sentence.endswith('.')

def isinterrogative(sentence):
    return sentence.endswith('?')

def isimperative(sentence):
    return sentence.endswith('!')

def analyze_text(filename):
    with open(filename, 'r') as file:
        text = file.read()

    sentences = re.split(r'[.!?]', text)
    num_sentences = len(sentences)

    num_narrative = len([s for s in sentences if isdeclarative(s)])
    num_interrogative = len([s for s in sentences if isinterrogative(s)])
    num_imperative = len([s for s in sentences if isimperative(s)])

    avg_sentence_length = sum(len(s) for s in sentences) / num_sentences

    words = re.findall(r'\b\w+\b', text)
    avg_word_length = sum(len(w) for w in words) / len(words)

    smileys = re.findall(r'[:;]-*[()\[\]]+', text)
    num_smileys = len(smileys)

    sentences_with_apostrophe = [s for s in sentences if "'" in s]

    text = re.sub(r'\b\d{2}:\d{2}(:\d{2})?\b', '(TBD)', text)

    words_ending_vowel = len([w for w in words if w[-1] in 'aeiou'])

    word_lengths = [len(w) for w in words]
    avg_word_length_rounded = round(sum(word_lengths) / len(words))
    words_avg_length = [w for w in words if len(w) == avg_word_length_rounded]

    every_fifth_word = words[::5]

    result = {
        'num_sentences': num_sentences,
        'num_narrative': num_narrative,
        'num_interrogative': num_interrogative,
        'num_imperative': num_imperative,
        'avg_sentence_length': avg_sentence_length,
        'avg_word_length': avg_word_length,
        'num_smileys': num_smileys,
        'sentences_with_apostrophe': sentences_with_apostrophe,
        'text': text,
        'words_ending_vowel': words_ending_vowel,
        'words_avg_length': words_avg_length,
        'every_fifth_word': every_fifth_word,
    }

    with open('result.pkl', 'wb') as file:
        pickle.dump(result, file)

    with zipfile.ZipFile('result.zip', 'w') as zipf:
        zipf.write('result.pkl')

    return result
