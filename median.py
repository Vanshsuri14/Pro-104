import csv

with open("SOCR-HeightWeight.csv",newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#fine median
new_data.sort()

n = len(new_data)


if(n%2 == 0):
    firstNumber = new_data[n//2]
    secondNumber = new_data[n//2-1]
    median = (firstNumber+secondNumber)/2
else:
    median = new_data[n//2]

print("median is :",median)