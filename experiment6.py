# students in exams
cet = {"Tanmay", "Bob"}
jee = {"Zakir", "Bob"}
neet = {"Saad", "Eve"}
print("All students:", cet|jee|neet) #Union
print("Students in all exam:", cet & jee & neet) # intersection
print("Cet but not in jee:", cet - jee) #Difference