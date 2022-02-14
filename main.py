import numpy as np
import argparse
import pickle
##
__all__ = ["is_prime","binary_search","find_the_highest_prime_lower_than_n"]
##

def is_prime(l01, tn01):
	"""
	check if tn01 is prime: tn01 is not divisible to any prime number from 2 to sqrt(tn01)
	l01: list of all prime numbers loaded from file, this is used to extract prime numbers from 2 to sqrt(tn01)
	"""
	tn02 = int(np.sqrt(tn01))
	tnp02 = l01[l01<=tn02]
	tnp03 = tn01%tnp02
	return False if np.any(tnp03==0) else True
##

def binary_search(l01, left, right, n):
	"""
	This function uses binary search to find the highest prime number less than n.
	l01: list of all prime numbers loaded from pickle file
	"""
	if (left <= right):
		mid = int((left + right) / 2)
		if ((mid == 0) or (mid == len(l01) - 1)):
			return l01[mid]
		elif ((l01[mid] <= n) and (l01[mid + 1] > n)):
			return l01[mid]
		elif (n < l01[mid]):
			return binary_search(l01, left, mid - 1, n)
		else:
			return binary_search(l01, mid + 1, right, n)
##

def find_the_highest_prime_lower_than_n(n):
	with open("prime_numbers_less_than_n.pickle", "rb") as picklefile:
		d01 = pickle.load(picklefile)
	##
	nmax=d01["nmax"]
	l01=d01["l01"]
	"""
	if the input greater than nmax, we need to check wether there is any prime number in [nmax+1, n]
		if there is, we update nmax, and add those prime number to l01, then overwrite the pickle file
	else: just use binary search to find the highest prime number lower than the input
	"""
	if n>nmax:
		for tn01 in range(nmax+1, n+1):
			if is_prime(l01, tn01):
				l01 = np.append(l01, tn01)
		##
		return l01[-1]
		d01["nmax"]=n
		d01["l01"]=l01
		with open("prime_numbers_less_than_n.pickle", "wb") as picklefile:
			pickle.dump(d01, picklefile, protocol=4)
	###
	else:
		return binary_search(l01, 0, len(l01)-1, n)
##

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", type=int, required=True)
	args = parser.parse_args()
	n=args.n
	##
	print(find_the_highest_prime_lower_than_n(n))

##
