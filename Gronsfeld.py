import sys

def coding_encoding(text, key, switch):
    text_tab=[]
    key_tab=[]
    output_text_tab=[]
    if switch == "c":
       modyfier = 1
    elif switch == "d":
       modyfier = -1
    else:
       sys.exit("Wprowadzono błędną wartość wybory kodowania/dekodowania")
    for i in text.upper():
        text_tab+=[int(ord(i))]
    for i in str(key):
        key_tab+=[i]
    n = 1
    for i in range(len(text_tab)):
        if i<len(key_tab):
            text_tab[i]+=int(key_tab[i])*modyfier
        else:
            if i % len(key_tab) == 0 and i != len(key_tab):
                n += 1
            j=i-n*len(key_tab)
            text_tab[i]+=int(key_tab[j])*modyfier
    for i in text_tab:
        output_text_tab+=chr(i)
    output_text="".join(output_text_tab)
    return output_text

def gronsfeld_demonstration(): #Funkcja demonstrująca szyfrowanie i deszyfrowanie
    key=input("Wprowadź klucz: ")
    text=import_text()
    print("\nTekst po zaszyfrowaniu: \n{0}".format(coding_encoding(text,key,"c")))
    print("\nTekst po odczycie: \n{0} ".format(coding_encoding(coding_encoding(text,key,"c"),key,"d")))

def import_text():
    file=open(input("Podaj nazwę pliku: "))
    try:
        text=file.read()
    finally:
        file.close()
    return text

def gronsfeld(): #Funkcja umożliwiająca szyfrowanie/deszyfrowanie
    switch = input('Dla kodowania wpisz "c", dla dekodowania "d": ')
    text = import_text()
    key=input("Wprowadź klucz: ")
    if switch == "c":
        print("Tekst po zakodowaniu:\n")
    else:
        print("Tekst po dekodowaniu:\n")
    print(coding_encoding(text,key,switch))

gronsfeld_demonstration()
#gronsfeld()