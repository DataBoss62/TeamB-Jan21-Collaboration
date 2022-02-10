'''
Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
Reads and displays the names of the 1st and 4th team in the file.
Create a new Python file which does the following:

Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
Print out the edited file line by line.
'''


with open("teams.txt", "w") as file1:
  for line in range(5):
      var1 = input("Enter a team name:") + "\n"
      file1.write(var1)

with open("teams.txt","r") as file1:
      list1 = file1.readlines()

# for team in list1:
#     if list1.index(team) == 0 or list1.index == 3:
#          print(team)
         
with open("teams.txt", "w") as file1:
      for team in list1:
          if list1.index(team) == 0:
              file1.write("This is a new line\n")
          else:
              file1.write(team)
            
                



print(list1) 
print(list1[0]) 
print(list1[3])    
       