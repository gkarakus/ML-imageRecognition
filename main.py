import requests

x = requests.get('https://finance.yahoo.com/')
print(x.status_code)

print(x.text)

liste = x.text.split("<")


f = open("c:/Python/pdene.txt", "w")
for y in liste:
#  print(y)
  f.write(y + '\n')
f.close()


"""
# Opening file
file1 = open('c:/Python/pdene.txt', 'w')
count = 0
 
# Using for loop
print("Using for loop")
for line in file1:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
 
# Closing files
file1.close()

"""
