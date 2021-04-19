import random
file = input("Please enter the name of the file: ")
with open (file, "r") as list:
    rows = list.readlines()
    for row in rows:
        splitedRow = row.split(",")
    splitedRow1 = splitedRow[1]
    user = splitedRow1[1] + splitedRow1[3] + splitedRow1[1]
    splitedRow2 = splitedRow[2]
    nam = splitedRow2[1] + splitedRow2[3] + splitedRow2[1]
    splitedRow4 = splitedRow[4]
    n = splitedRow4[1]
    number = str(random.randint(1,100))
    username = user + nam + n + number
    print (username)  