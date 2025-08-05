# part 1:  Arthmetic operators

a = 15
b = 4

print("Addition: a + b = " , a + b)
print("Subtraction: a - b =" , a - b)
print("multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponentiation: a ** b =", a ** b)

# Part 2:  Arthematic Assignment operators

x = 10
print("initial value of x:", x)

x += 5
print("After x =+ 5:",x)

x *= 2
print("After x *= 2:",x)

x -= 4
print("After x -= 4:",x)

x /= 2
print("After x /= 2:",x)

# Part 3:  Comparison Opperators

a = 7
b = 10 

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b )
print("a < b:", a < b )
print("a >= b:", a >=b )
print("a <= b:", a <= b)

# Part 4:  Logical Opperators

x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

#Part 5:  Mambership Opperators

institude = "Saylani Mass IT"

print("'s' in institude:" ,"s" in institude)
print("'Saylani' in institude: ","Saylani" in institude)
print("'Saylani' not in institude: ", "Saylani" not in institude)

# Part 6:  Identity Opperators

a = 5
b = 5
c = 1000

print("a is b:", a is b)
print("a is c:", a is c)
print("c is not b:", c is not b )

# BONUS CHELLANGE

name = "Talha"
password ="Axiom123"
i_name = input("Enter your name: ")
i_password = input("Enter your password: ")
check = ({name == i_name} and {password == i_password})
print(check)



