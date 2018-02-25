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
  print("Liczby pierwsze w zakresie do {0}\n".format(n))
  print_counter=0
  line=""
  for i in primes:

      if print_counter<20:
          print(i, sep=' ', end=' ', flush=True)
      else:
          print(i)
          print_counter=0
      print_counter += 1
  print("\nZnaleziono {0} liczb pierwszych".format(len(primes)))





eratostenes()