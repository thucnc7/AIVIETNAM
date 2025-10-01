import re
with open("/home/nexy/Code/AIVIETNAM/Week2/input.txt",'r') as f :
    sentences = f.readlines()

# print(sentences)

def strip_punct(sentence:str) -> str:
    sentence = sentence.lower()
    return re.sub(r'[^\w\s]',' ',sentence,flags= re.UNICODE).strip()
    
def process_Sentence(sentence:str ):
    sentence.lower()
    sentence = strip_punct(sentence)
    words = sentence.split()
    return words

dictionary = set()

def main() :
    for sentence in sentences :
        dictionary.update(process_Sentence(sentence))
    dic = {w:i for i,w in enumerate(dictionary)}
    print(dic)

from xulistring import XLiString as xl

    xl.

main()
