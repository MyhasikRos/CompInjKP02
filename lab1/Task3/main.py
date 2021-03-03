array = [-1, 5, 0, -10, -5, 4, 0, -17, 18, -24]
maxNegative = float('-inf')
multipliedNegatives = 1
consoleOut = ""
for element in reversed(array):
    if element < 0:
        if element > maxNegative:
            maxNegative = element
        multipliedNegatives *= element
    if element != 0:
        consoleOut += str(element) + ' '
print(consoleOut)
if maxNegative != float('-inf'):
    print("Max negative: %d" % maxNegative)
    print("Multiplied negative numbers: %d" % multipliedNegatives)
else:
    print("No negative values in array")