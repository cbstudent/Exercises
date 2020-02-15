def getNthFib(n):
    # Write your code here.
	prev = {}
    return _getNthFib(n, prev)

def _getNthFib(n, prev):
	if n == 1:
		return 0
	if n == 2:
		return 1
	if n in prev:
		return prev[n]
	fib = _getNthFib(n-2, prev) + _getNthFib(n-1, prev)
	prev[n] = fib
	return fib
