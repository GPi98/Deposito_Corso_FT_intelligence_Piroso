def fibonacci(n):       #funzione presa dalle slide
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

print("inserire un numero, mostrerò la sequenza di fibonacci")
n = int(input())

for numero in fibonacci(n): 
    print(numero, end=" ")