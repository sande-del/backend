# 1. Create a file "students.txt"
# 2. Write names of 3 students, each on a new line
# 3. Read the file and print each name separately (loop through lines)
# 4. Append 2 more student names
# 5. Read the file again and print all names
with open("students.txt",'w') as f:
    f.write("ram\n")
    f.write("sita\n")
    f.write("laxman\n")
with open("students.txt","r") as f:
 for line in f:
    print(line.strip())

with open("students.txt","a") as f:
   f.write("hari")
with open("students.txt","r") as f:
 for line in f:
    print(line.strip())
