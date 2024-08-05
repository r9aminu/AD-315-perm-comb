import math

def perm_comb(n, r):
    permutations = math.factorial(n) // math.factorial(n - r)
    combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    return permutations, combinations


# n!/(n-r)!
# n!/r!(n-r)!

n = int(input("number of items: "))
r = int(input("chosen items: "))

if n < 0 or r < 0:
    print("input cannot be less than 0.")
elif r > n:
    print("n must be greater than r.")
else:
    permutations, combinations = perm_comb(n, r)
    print(f"P({n}, {r}) = {permutations}")
    print(f"C({n}, {r}) = {combinations}")

