import csv, random
autor = input('Ведите фамилию и имя автора: ')
Number_5 = open('Number_5', 'w')
print('№4:')
number_write = 0
with open('books (1).csv') as first_file:
    book_records = csv.reader(first_file, delimiter = ';')
    number_book = 0
    big_name_book = 0
    bibl_links = [0]*20
    list_book = []
    for book in book_records:
        if len(book[1]) > 30:
            big_name_book += 1
        list_book.append(book)
        str_book = list_book[number_book]
        list_autor = str_book[3]
        date = str_book[6]
        date_years = date[6:10]
        name_book = str_book[1]
        if (list_autor == autor) and (2016 <= int(date_years) <= 2018):
            print(name_book)
        number_book += 1
    for book in range(20):
        random_number = random.randint(1, number_book)
        random_book = list_book[random_number]
        author = random_book[3]
        title = random_book[1]
        date = random_book[6]
        date_years = date[6:10]
        bibl_links[book] = f'{author}. {title} - {date_years}'
    for book in bibl_links:
        number_write += 1
        wrnumber5 = str(number_write) + ' ' + book
        print(wrnumber5, file = Number_5)
Number_5.close()
print(f'№2: {number_book-1}')
print(f'№3: {big_name_book}')