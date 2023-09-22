import csv, random
autor = input()
Number5 = open('Number5', 'w')
print('№4:')
count3 = 0
with open('books (1).csv') as first_file:
    first_reader = csv.reader(first_file, delimiter = ';')
    count1 = 0
    count2 = 0
    bibl_links = [0]*20
    a = []
    for i in first_reader:
        if len(i[1])>30:
            count2 += 1
        a.append(i)
        if (a[count1][3] == autor) and (2016<=int(a[count1][6][6:10])<=2018):
            print(a[count1][1])
        count1 += 1
    for i in range(20):
        r = random.randint(1, count1)
        bibl_links[i] = f'{a[r][3]}. {a[r][1]} - {a[r][6][6:10]}'
    for i in bibl_links:
        count3 += 1
        wrnumber5 = str(count3)+' '+i
        print(wrnumber5, file = Number5)
Number5.close()
print('№2')
print(count1-1)
print('№3')
print(count2)