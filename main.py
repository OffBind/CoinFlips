import random

results = []
sum = 0

# 0 is tales
# 1 is heads
for i in range(1000000):
    # do this a millon times
    results.append(random.randint(0, 1))

for num in results:
    # add all of the numbers together
    sum = sum + num

# this gets the percentage in hundreths
result = sum / len(results)
# this formats the result into percentage
percentage = "{:.4%}".format(result)
print(percentage)
