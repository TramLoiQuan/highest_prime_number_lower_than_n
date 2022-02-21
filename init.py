"""
This file is to use the sieve of Eratosthenes to generate all prime numbers less than N
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
import numpy as np
import pickle
import argparse
###

def sieve_of_eratosthenes(nmax: int) -> np.ndarray:
	"""
	Generate all prime numbers less than nmax
	"""
	np01 = np.ones(nmax,dtype=np.int8)
	np01[0],np01[1]=0,0
	sqrt_n = int(np.sqrt(nmax))
	for i in range(2,sqrt_n+1):
		if np01[i]==1:
			j = i*i
			while j<nmax:
				np01[j] = 0
				j+=i
	###
	return np.where(np01==1)[0]
###

if __name__ == "__main__":
	##
	prime_100_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	prime_100_seive = sieve_of_eratosthenes(100)
	assert np.all(prime_100_seive==prime_100_test), "incorrectly generate all prime numbers less than 100"
	##
	parser = argparse.ArgumentParser()
	parser.add_argument("-nmax", type=int, required=True)
	args = parser.parse_args()
	nmax=args.nmax
	np02 = sieve_of_eratosthenes(nmax)
	d01 = {"nmax":nmax, "np02":np02}
	with open("prime_numbers_less_than_n.pickle", "wb") as picklefile:
		pickle.dump(d01, picklefile, protocol=4)
    ##
	