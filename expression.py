# string & numeric values can operate together with *
a,b=5,6
txt="@"
print(5*txt*6)

#string & string can operate with +
a,b="2",3
txt="#"
print((a+txt)*b)

#numeric values can operate together with all arithmetic operators
a,b=5,6
c=4
print(a+b*c)

# arithmetic expression with integer and float will result in float
a,b=5,6.2
c=a+b
print(c)
print(type(c))

# result of divison operator with two integers will be float
a,b=7,2
c=a/b
print(c)
print(type(c))

# integer division with float and int will give int displayed as float
a,b=7.0,2
c=a//b
print(c)
print(type(c))

a,b=12,5
c=a//b
print(c)
print(type(c))

a,b=-12,5
c=a//b
print(c)
print(type(c))

a,b=12,-5
c=a//b
print(c)
print(type(c))

#reminder is negative when denominator is negative
a,b=-5,2
c=a%b
print(c)

a,b=5,2
c=a%b
print(c)

a,b=5,-2
c=a%b
print(c)