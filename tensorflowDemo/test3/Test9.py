# coding:utf-8
import requests
import io
from zipfile import ZipFile

if __name__ == '__main__':
    sentence_url = "http://www.manythings.org/anki/deu-eng.zip"
    r = requests.get(sentence_url)
    z = ZipFile(io.BytesIO(r.content))
    file = z.read('deu.txt')
    eng_ger_data = file.decode()
    eng_ger_data = eng_ger_data.encode('ascii', errors='ignore')
    eng_ger_data = eng_ger_data.decode().split('\n')
    eng_ger_data = [x.split('\t') for x in eng_ger_data if len(x) >= 1]
    [english_sentence, german_sentence] = [list(x) for x in zip(*eng_ger_data)]
    print(len(english_sentence))
    print(len(german_sentence))
    print(eng_ger_data[9])
    print(eng_ger_data[10])
    print(german_sentence)


