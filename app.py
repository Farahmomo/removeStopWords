from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    return ' '.join([word for word in words if word not in stop_words])

def count_word_frequency(text):
    words = word_tokenize(text.lower())
    return Counter(words)

def main():
    random_paragraphs_file = "random_paragraphs.txt"

    paragraphs = read_file(random_paragraphs_file)

    processed_text = remove_stop_words(paragraphs)

    word_frequency = count_word_frequency(processed_text)

    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")


main()