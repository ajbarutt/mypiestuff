

try:
	from functools import lru_cache
except:
	from backports.functools_lru_cache import lru_cache

@lru_cache()
cache = [0,1]

def fib(n):
	if n==0:return 0
	if n==1:return 1
	return fib(n-1) + fib(n-2)

def fibc(n):

	assert(isinstance(n,int))
	assert(n>0)

	if len(cache) >= n+1: return cache[n]
	result = fibc(n-1) + fibc(n-2)
	cache.append(result)
	return cache[n]

print fib(55)