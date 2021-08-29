import csv

with open("SOCR-HeightWeight.csv",newline = '')as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#find mean 
n = len(new_data)
a = 0 
for x in new_data:
    a+=x

mean = a/n

print("mean/average for height is : ",mean)

    

