import csv

#status = 'Hola mi nombre es Hernan'
#x = status.split()
#list(x)

#print(x)

outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', '30'])
outputWriter.writerow(['test1', 'test2', '20'])
#outputWriter.writerow(x)
outputFile.close()

listData = open('output.csv', 'r') 
data = csv.reader(listData)

count = 0
total = 0

for item in data:
    for row in item:
        if row.isnumeric():
            count += 1
            total += int(row)
print(f'Count is: {count}')
print(f'total is: {total}')
print(f'Average is: {total} / {count}:', total / count)
