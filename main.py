import random
import sys

results = []
sum = 0

if sys.argv[0] == None:
    numberOfFlips = int(input('Flip it this many times: '))
else:
    numberOfFlips = int(sys.argv[0])

# 0 is tales and 1 is heads
for i in range(numberOfFlips):
    results.append(random.randint(0, 1))

for num in results:
    # add all of the numbers together
    sum = sum + num

# this gets the percentage in hundreds
result = sum / len(results)
# this formats the result into percentage
percentage = "{:.4%}".format(result)
print(percentage)
