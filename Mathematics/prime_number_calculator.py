###
# Find all prime number up tp n
max = int(input("Find prime up to n? : "))
prime_list_up_to = []

for x in range(2, max + 1): # For loop to check each number
    is_prime = True
    index = 0
    root = int(x ** 0.5) + 1

    while index < len(prime_list_up_to) and prime_list_up_to[index] <= root:
        if x % prime_list_up_to[index] == 0:
            is_prime = False
            break
        index += 1

    if is_prime:
        prime_list_up_to.append(x)

print(prime_list_up_to)


###
# Find all prime number up to n
count = int(input("Find n of primes"))
prime_list_to_n = []
y = 2

while len(prime_list_up_to) < count:
    is_prime = True
    index = 0
    root = int(y ** 0.5) + 1

    while index < len(prime_list_to_n) and prime_list_to_n[index] <= root:
        if y % prime_list_to_n[index] == 0:
            is_prime = False
            break

            index += 1

        if is_prime:
            prime_list_to_n.append(y)

        y += 1

print(prime_list_to_n)
