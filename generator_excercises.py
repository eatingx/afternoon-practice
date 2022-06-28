#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
def primes_gen():
    n=2
    while True:
        test=True
        for x in range(2, int(n/2)+1):
            if n % x ==0:
                test=False
                break
        if test:
          yield n
        n+=1

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')
# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.
def unique_letters(str):
    letters=[]
    for item in str:
        if item not in letters:
            letters.append(item)
    return letters

for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o