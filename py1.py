#print("3 " +  6)

delimiter = '.'
delimiter2 = 3
print(delimiter*2*3)
#print(delimiter * "2")
print("--------\n")
print(delimiter2 * "2")

print("--------\n")

x = 'Thank'
y = 'You'
#print('Thank'+'you')
#print('Thank','you')

#print((x+y)*5) 
#print(x,y, "nice to see you")
#print(x,y + "nice to see you")

### error on "+" 
#print(x + 2 + "nice to see you")

#print(x * 2 + "nice to see you")
#print((x,y)*1) #This one..

#print separate digits from 2 digits input number 

#n = int(input("please input two digits number: "))

#print(n)

# first solution using // and mod
#x1 = n//10    # the same as int(n/10)
#print("the first integer :" + str(x1))
#x2 =  n%10
#print("the second integer: "+ str(x2))
#print(5%3)

#"abcdedf"

# second solution uses string indices 

#s = str(n)  # "3456"  [ "3", "5"]
#print(s)
#print(s[0:1])
#print(s[1:2])
#print(s[0:8])
#print(s[1:3])

#"35abc"

# place holder example
cost = 10.253
print("the cost is %8.2f value" % cost) 
print("the cost is "  + "%8f" % cost + " value") 
print("the cost is %-8.2f value" % cost) 

a = 'apple'
print("the fruit is %8s" % a) 

one = "Team"
two = "Wins"
print ("%15s || %12s " %(one , two) )
print ("%-15s || %-12s " %(one , two) )

print ("%15s || %12s " %("Bruins", "6") )
print ("%15s || %12s " %("Vikings", "2") )

print (one + " || %12s" %two)

#https://www.w3schools.com/python/python_conditions.asp
print(12>2)
print(5> 36)
print(20-10 == 10)
print(20-10 != 8)  # != the same as <>


a = 333
b = 200
if b > a:
  print("b is greater than a")
  print("this is true statement")
else:
  print("b is not greater than a ")
  print("this is false statement")

a ="cherry"

if a == "pearl":
    print("this is pearl")
elif a=="cherry":
    print("this is cherry")
elif a=="orange":
  print("this is orange")
#else:
#  print("this is apple")
  
a=10
b=5 
c= 12

if a>b and a> c:
   print("AND all greater than")
else:
   print("AND one is less than")


if a>b or a> c:
   print("OR all greater than")
else:
   print("OR one is less than")