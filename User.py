import random
#def oPen (file):
#    file = input("Please enter the name of the file: ")
#    with open (file, "r", encodning="utf-8") as list:
#        return list

#def username (Förnamn, Efternamn):
#    k = oPen()
#    print 
#    rows = list.readlines()
#    for row in rows:
#        splitedRow = row.split(",")
#        username = splitedRow[1][1] + splitedrow[1] 


file = input("Please enter the name of the file: ")
with open (file, "r") as list:
    rows = list.readlines()
    for row in rows:
        splitedRow = row.split(",")
        splitedRow1 = splitedRow[1]
        splitedRow1 = str(splitedRow1)
        user = splitedRow1[1] + splitedRow1[3] + splitedRow1[1]
        splitedRow2 = splitedRow[2]
        splitedRow2 = str(splitedRow2)
        nam = splitedRow2[1] + splitedRow2[3] + splitedRow2[1]
        splitedRow4 = splitedRow[4]
        splitedRow4 = str(splitedRow4)
        n = splitedRow4[1]
        number = str(random.randint(1,100))
        username = user + nam + n + number
        print (username)  