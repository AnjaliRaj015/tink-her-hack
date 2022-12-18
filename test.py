import csv
rows = []
with open("test2.csv", 'r', encoding='utf-8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
       if (row[0] == "12/12/22") :
        print(row[0],",",row[2],":",row[3])
     
 for row in csvreader:
       if (row[3]).find(".pdf") == -1 :
        print("")
       else:
        print(row[0],",",row[2],":",row[3])

for row in csvreader:
       if (row[0] == "12/12/22" or row[0] == "16/12/22"):
        print(row[0],",",row[2],":",row[3])              