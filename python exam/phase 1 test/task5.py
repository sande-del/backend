# Q5 — Dictionary
# Given this dictionary: marks = {"Math": 90, "Science": 85, "English": 78}
# Add a new subject "Python" with marks 95
# Print all subjects and marks in the format: "Subject: Marks"
marks = {"Math": 90, "Science": 85, "English": 78}
marks["python"] = 95
print(marks)
for key,values in marks.items():
    print(key,":",values)