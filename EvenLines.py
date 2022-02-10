file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()
file.close()

file = open("filename.txt", "w")
file.write(outfile)
file.close()



# with open("filename.txt","w")  as file:    #this opens file1 in write mode but will close it after the write statement.
#     outfile = ""
#     for line in range(1, 10):
#         if line % 2 == 0:
#            outfile += file.readline()
#         else:
#            file.readline()

# file = open("filename.txt", "w")
# file.write(outfile)
# file.close()          