import numpy as np
import argparse
import pickle
##
__all__ = ["is_prime","binary_search","find_the_highest_prime_lower_than_n"]
##

def is_prime(np02:np.ndarray, tn01:int)->bool:
	"""
	Check if tn01 is prime: tn01 is not divisible to any prime number from 2 to sqrt(tn01)

	Args:
		np02: np.ndarray of all prime numbers loaded from file, this is used to extract prime numbers from 2 to sqrt(tn01)
		tn01: the number is needed to check
	Returns:
		True if tn01 is prime, otherwise False
	"""
	tn02 = int(np.sqrt(tn01))
	tnp02 = np02[np02<=tn02]
	tnp03 = tn01%tnp02
	return False if np.any(tnp03==0) else True
##

def binary_search(np02:np.ndarray, left:int, right:int, n:int)->int:
	"""
	Args:
		np02: np.ndarray of all prime numbers loaded from pickle file
		left: left index of the array
		right: right index of the array
	Returns:
		The highest prime number less than n
	"""
	if (left <= right):
		mid = int((left + right) / 2)
		if ((mid == 0) or (mid == len(np02) - 1)):
			return np02[mid]
		elif ((np02[mid] <= n) and (np02[mid + 1] > n)):
			return np02[mid]
		elif (n < np02[mid]):
			return binary_search(np02, left, mid - 1, n)
		else:
			return binary_search(np02, mid + 1, right, n)
##

def find_the_highest_prime_lower_than_n(n:int)->int:
	"""
	Load the pickle file.
	If n > nmax, find all prime numbers in [nmax+1, n], update nmax, update np02, then overwrite the pickle file
	Else: just use binary search to find the highest prime number lower than n
	"""
	with open("prime_numbers_less_than_n.pickle", "rb") as picklefile:
		d01 = pickle.load(picklefile)
	##
	nmax=d01["nmax"]
	np02=d01["np02"]
	##
	if n>nmax:
		for tn01 in range(nmax+1, n+1):
			if is_prime(np02, tn01):
				np02 = np.append(np02, tn01)
		##
		return np02[-1]
		d01["nmax"]=n
		d01["np02"]=np02
		with open("prime_numbers_less_than_n.pickle", "wb") as picklefile:
			pickle.dump(d01, picklefile, protocol=4)
	###
	else:
		return binary_search(np02, 0, len(np02)-1, n)
##

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", type=int, required=True)
	args = parser.parse_args()
	n=args.n
	##
	print(find_the_highest_prime_lower_than_n(n))

##
