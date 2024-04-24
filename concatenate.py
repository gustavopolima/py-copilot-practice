#1st question
#prompt: help me concatenate some data

user1_name = input("Enter name for user 1: ")
user1_age = input("Enter age for user 1: ")
user1_email = input("Enter email for user 1: ")

user2_name = input("Enter name for user 2: ")
user2_age = input("Enter age for user 2: ")
user2_email = input("Enter email for user 2: ")


concatenateddata = "(" + user1_name + "," + user1_age + "," + user1_email + ")" + ";" + "(" + user2_name + "," + user2_age + "," + user2_email + ")"

print("The concatenated data is :", concatenateddata)