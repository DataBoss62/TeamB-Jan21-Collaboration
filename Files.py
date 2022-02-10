# file1 = open("example.txt", "w")
# file1.write("Hello")
# file1.close

file1 = open("example.txt", "r")
var1 = file1.read()
var2 = file1.readline()
file1.seek(0)     # puts cursor back to beginning of first line
var3 = file1.readline()

file1.close

list1 = [var1]
print(list1)

# file1 = open("example.txt", "w")
# for line in list1:
#     file1.write(line)

# file1.write("\n")
# file1.close


outfile = ""
with open("example.txt","w")  as file1:    #this opens file1 in write mode but will close it after the write statement.
     file1.write(outfile)
