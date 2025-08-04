#for,while,do_while

to_loop=True
i=0

while to_loop:
    if i>10:
      to_loop=False #these statement of false stops continuous adding up of the numbers brcause initially it was true
      print("i is",i)
    i=i+1

k=0
while k<10:
    print("k is",k)
    k=k+1


for i in range(2,10):
    print("for loop is",i)


for i in range(0,1000,2):#shows even numbers btn 0-1000
    print("all numbers are even",i)