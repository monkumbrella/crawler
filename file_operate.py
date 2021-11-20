#open("1.txt","w")

'''f = open("1.txt","w")

for n in range(3):
	f.write("this is line %d\r\n" %(n))
f.close()

f=open("1.txt", "a+")

for n in range(2):
     f.write("appended line %d\r\n" % (n))'''


'''f = open("1.txt", "r")

if f.mode == 'r':
	content =f.read()

print(content)
f.close()   '''


with open('readme.txt', 'w') as f:
    f.write('Create a new text file!')
