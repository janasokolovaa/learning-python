# Understanding strings

# giving an existing variable a new value - annual rainfall example
january_rainfall = 5.5
february_rainfall = 6.0
march_rainfall = 3.2

annual_rainfall = january_rainfall + february_rainfall + march_rainfall
print(annual_rainfall)

april_rainfall = 1.2
may_rainfall = 2.0
june_rainfall = 6.8

annual_rainfall += april_rainfall + may_rainfall + june_rainfall
print(annual_rainfall)

# giving an existing variable a new value - shopping example
t_shirt = 15
sweater = 25
jeans = 40

total_cost = t_shirt + sweater + jeans
# discount of 15% given
total_cost *= 0.85
print(total_cost)

# strings to integers
number1 = "645"
number2 = "34890"

string_addition = number1 + number2
integer_addition = int(number1) + int(number2)
print(integer_addition)

# strings to floats
string_num = "98.78"
print(float(string_num) * 89)


# upper case, lower case, length
practice = "Hello, my name is Jana"
print(practice)
print(len(practice))
print(practice .upper())
print(practice .lower())

# adding variables to strings
name = "Jana"
age = "22"
action = "learning python"
print("Hi everyone, my name is %s, I am %s, and I am currently %s!" %(name, age, action))
