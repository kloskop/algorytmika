import math

def eratostenes():
  num_tab=[]
  n=int(input("Podaj zakres: "))
  for i in range(2,n+1):
      num_tab+=[i]

  to_remove = []
  primes = []
  number = min(num_tab)
  while number<math.sqrt(n):
      for j in range(0,len(num_tab)):
        if num_tab[j]%number==0:
          to_remove+=[num_tab[j]]
      for i in range(0,len(to_remove)):
          num_tab.remove(to_remove[i])
          if to_remove[i]==number:
              primes+=[to_remove[i]]
      number = min(num_tab)
      to_remove=[]
  primes+=num_tab
  print("Liczby pierwsze w danym zakresie\n {0}".format(primes))
  print("Liczb pierwszych w tym zakresie jest {0}".format(len(primes)))




eratostenes()