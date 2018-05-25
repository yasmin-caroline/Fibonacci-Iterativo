import time

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a  

for i in range(30):
  ini = time.time()
  for x in range(1000):
    fibonacci(x)
  fim = time.time()
  print (fim-ini)

print ("\n Fim do algoritmo iterativo com 1000 elementos. \n")

for i in range(30):
  ini = time.time()
  for x in range(5000):
    fibonacci(x)
  fim = time.time()
  print (fim-ini)

print ("\n Fim do algoritmo iterativo com 5000 elementos. \n")

for i in range(30):
  ini = time.time()
  for x in range(10000):
    fibonacci(x)
  fim = time.time()
  print (fim-ini)

print ("\n Fim do algoritmo iterativo com 10000 elementos.")