#################################################################
##########  Generation of table using comprehension ###############
########

num=int(input("Please enter number to generate table: "))

table=[num*i for i in range(1,10)]

print(table)