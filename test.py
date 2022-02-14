import pickle
import numpy as np
#
from main import *
##

if __name__ == "__main__":
	prime_100_test = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
	assert binary_search(prime_100_test, 0, len(prime_100_test)-1, 84) == 83, "test binary_search fail"
	assert is_prime(prime_100_test,70) == False, "test is_prime fail"
	assert find_the_highest_prime_lower_than_n(1011) == 1009, "fail to find the highest prime lower than 1011"