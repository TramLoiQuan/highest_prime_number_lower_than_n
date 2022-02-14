# Description
* This code is used to find the highest prime number lower than a given number `n`.  
* Initially, we generate all prime numbers less than `nmax`, then save this list and `nmax` into pickle file for late use.  
* Whenever we run the query, the list will be loaded to search for the prime number.  
* If the input `n <= nmax`, we use binary search on the list to find the highest prime.  
* If the input `n > nmax`, we will find all prime number from `nmax+1` to `n`, return the last prime number, update the list and `nmax`, then overwrite the pickle file.
# Usage
1. Initial the list of prime numbers less than `nmax` (e.g. 100) 
    ```bash
    python init.py -nmax 100
    ```
2. Find the highest prime number lower than `n` (e.g. 1000)
    ```bash
    python main.py -n 1000
    ```
3. We can add some testcases in the file `test.py` to see if it works
    ```bash
    python test.py
    ```
