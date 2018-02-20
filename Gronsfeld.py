def coding(text, key):
    text_tab=[]
    key_tab=[]
    output_text_tab=[]
    for i in text.upper():
        text_tab+=[int(ord(i))]
    for i in str(key):
        key_tab+=[i]
    n = 1
    for i in range(len(text_tab)):
        if i<len(key_tab):
            text_tab[i]+=int(key_tab[i])
        else:
            if i % len(key_tab) == 0 and i != len(key_tab):
                n += 1
            j=i-n*len(key_tab)
            text_tab[i]+=int(key_tab[j])
    for i in text_tab:
        output_text_tab+=chr(i)
    output_text="".join(output_text_tab)
    return output_text

def encoding(text, key):
    text_tab = []
    key_tab = []
    output_text_tab = []
    for i in text.upper():
        text_tab += [int(ord(i))]
    for i in str(key):
        key_tab += [i]
    n = 1
    for i in range(len(text_tab)):
        if i < len(key_tab):
            text_tab[i] -= int(key_tab[i])
        else:
            if i % len(key_tab) == 0 and i != len(key_tab):
                n += 1
            j = i - n * len(key_tab)
            text_tab[i] -= int(key_tab[j])
    for i in text_tab:
        output_text_tab += chr(i)
    output_text = "".join(output_text_tab)
    return output_text

def gronsfeld_demonstration(text): #Funkcja pokazująca szyfrowanie i deszyfrowanie
    key=input("Wprowadź klucz: ")
    print("\nTekst po zaszyfrowaniu: \n{0}".format(coding(text,key)))
    print("\nTekst po odczycie: \n{0} ".format(encoding(coding(text,key),key)))

def import_text():
    file=open(input("Podaj nazwę pliku: "))
    try:
        text=file.read()
    finally:
        file.close()
    return text


gronsfeld_demonstration(import_text())