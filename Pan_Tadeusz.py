import collections

def import_text():
    file=open('PTadeusz.txt')
    try:
        text=file.read().lower()
        interpunction_signs=['.',',','"','!','?',':',';','-','<','>','(',')','[',']']
        for i in interpunction_signs:
            text=text.replace(i,"")
        text=text.replace("\n"," ")
        text=text.split(" ")
    finally:
        file.close()
    return text


def words_counting(text):
    words_dictionary={}
    for i in text:
        if i!="":
          if i not in words_dictionary:
              words_dictionary[i]=1
          else:
              words_dictionary[i]+=1
    most_often_words = {k: collections.OrderedDict(sorted(words_dictionary.items(), key=lambda t: t[1],reverse=True))[k] for k in list(collections.OrderedDict(sorted(words_dictionary.items(), key=lambda t: t[1],reverse=True)))[:20]}
    for key, value in most_often_words.items():
        print('Słowo: "{0}" występuje {1} razy'.format(key, value))



words_counting(import_text())
