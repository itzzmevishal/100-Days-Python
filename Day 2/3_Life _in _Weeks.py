# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# ANSWERπππππππππ

# π¨ Don't change the code below π
age = input("What is your current age? ")
# π¨ Don't change the code above π

# Write your code below this line π

age_as_int = int(age)
year = 90-age_as_int
day = year*365
weeks = year*52
months = year*12
print(f"You have {day} days, {weeks} weeks, and {months} months left.")
