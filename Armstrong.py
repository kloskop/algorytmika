import math

def Armstrong():

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
    print("\nKoniec obliczeń")

Armstrong()



