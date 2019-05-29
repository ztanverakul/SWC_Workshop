# Author: Zach Tan
# Date: 05/29/2019
# Description: First Python Script Workshop
# Collaborators: tsk tsk

import numpy as np
from math import pi, sqrt, cos
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

def sumOfAllPrimes():
	return sum(PRIMES)

if __name__ == "__main__":
	x = sumOfAllPrimes()
	print(x)
