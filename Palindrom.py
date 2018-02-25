
def create_num_tab(number):
    num_tab = []
    for i in number:
        num_tab += [i]
    return num_tab

def split_in_two(num_tab):
  left_side=[]
  right_side=[]
  if len(num_tab)%2!=0: #kiedy liczba cyfr jest nieparzysta
    n=0
    while n<len(num_tab):
      if n<len(num_tab)//2:
        left_side+=num_tab[n]
      elif n>len(num_tab)//2:
        right_side+=num_tab[n]
      n+=1
  else: #kiedy liczba cyfr jest parzysta
    n=0
    while n<len(num_tab):
        if n<len(num_tab)/2:
            left_side+=num_tab[n]
        else:
            right_side+=num_tab[n]
        n+=1
  right_side.reverse()
  return left_side, right_side

def palindrome_check(left_side, right_side):
  is_palindrome=False
  e=0
  while e < len(left_side): #sprawdzanie, czy liczba jest palindromem
    if int(left_side[e])==int(right_side[e]):
      is_palindrome=True
    else:
      is_palindrome=False
      break
    e+=1
  return is_palindrome

def new_number(number):
  num_tab = create_num_tab(number)
  number=int(number)
  num_tab.reverse()
  number_new=number+int("".join(num_tab))
  print("\nnowa liczba: {0} + {1} = {2}".format(number, "".join(num_tab), number_new))
  number = number_new
  return number

def palindrome():
    number=input("Podaj liczbę: ")
    int_number=int(number)

    while int_number<100000000: #szukanie w zakresie do 1000000, można zmieniać
      tab=(split_in_two(create_num_tab(number)))
      if palindrome_check(tab[0],tab[1]):
          print("Liczba {0} jest palindromem".format(number))
          break
      else:
          print("liczba {0} nie jest palindromem".format(number))
          int_number=new_number(number)
          number=str(int_number)


palindrome()






