import math

def Armstrong():
    how_many = 0
    for number in range(9,int(input("Zakres do: "))):
      number=str(number)
      sum=0
      power=len(number)
      num_tab=[]
      for n in number:
          num_tab+=[int(n)]
      for n in num_tab:
        sum+=math.pow(n,power)
      if sum==int(number):
        print(number)
        how_many+=1
    print("Znaleziono {0} liczb Armstronga".format(how_many))

Armstrong()



