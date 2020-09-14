import csv

def thing2():
    pass
def thing1():
    with open('_books_youngadult.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        print('[')
        for line in csv_reader:
            count = 0
            for data in line:
                line[count] = data.replace("'","*")
                count+=1
            print(line,',')
        print(']')

thing1()