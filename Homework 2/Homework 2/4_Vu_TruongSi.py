import sys
import csv
if __name__ == "__main__":
    arglist = []
    for argument in sys.argv:
        arglist.append(argument)

    openFile = arglist[1]
    outFile = arglist[2]
    res = []

    with open(openFile, 'r', encoding = "utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            res.append(row)

    trans = []
    for i in range(len(res[0])):
        temp = []
        for j in range(len(res)):
            temp.append(res[j][i])
        trans.append(temp)
        
    with open(outFile, "w", encoding = "utf-8-sig") as file:
        for row in trans:
            file.writelines(",".join(row) + "\n")
else:
    print("Please run this program from the command line")
