import numpy as np
import csv

#Prime number is a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
#due to random occurrence prime numbers, there is no formula for generating prime numbers.
#the best method to find prime numbers is to sieve out non prime numbers, i am using the same method.
#this programe will sieve out the composite numbers and create a list of prime numbers, then out it into a .csv file.

target = 100 #total range of our search for prime numbers
prime = np.array([]) # empty numpy array to store prime numbers

#this function will check composite numbers. ie if its is divisible by any prime numbers then it will reture False
def primecheck(x,primeList):    #X is the number to be checked and primeList is the list of prime numbers available.
    for j in primeList:
        if j<=np.sqrt(x): #np.sqrt(x) is used because at least one factor of a number is less then its squre root, it will reduce the area of search
            if x%j == 0: # x%j will output remainder of x/j. if its zero, then x is not prime. 
                return False
        else: 
            break # use prime number from primeList that are less than squre root of x else break. it will be use less to go above that

#mainloop
for i in range(2,target+1): #useing 1 for starting number will complicate things. target + 1 to include target in the search
    if primecheck(i,prime) != False: #if a number is prime primecheck() will outpute nothing so if it is nothing
        prime = np.append(prime, i) # append the number in prime Array.

# Output the list into .csv
#str(target) means total range of search
#str(len(prime)) means total number primes found
with open('prime_'+str(target)+'_('+str(len(prime))+').csv', 'w', newline='') as csvfile:
    primewriter = csv.writer(csvfile, delimiter=',')
    primewriter.writerow(prime)
print(str(target))
print(str(len(prime)))
