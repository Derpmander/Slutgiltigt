def oPen ():
    file = input("Please enter the name of the file: ")
    with open (file, "r", encodning="utf-8") as list:
        return list

def username (Förnamn, Efternamn):
    rows = list.readlines()
    for row in rows:
        splitedRow = row.split(",")
        username = splitedRow[1][1] + splitedrow[1] 


file = input("Please enter the name of the file: ")
with open (file, "r") as list:
    rows = list.readlines()
    for row in rows:
        splitedRow = row.split(",")
        username = splitedRow[1][1] + splitedRow[2] + splitedRow[4] 
    print (username)  