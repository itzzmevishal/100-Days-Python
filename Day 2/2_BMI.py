# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g.
# If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Calculate the BMI(Body Mass Index) of the Body

# ANSWERπππππππ

# π¨ Don't change the code below π
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# π¨ Don't change the code above π

# Write your code below this line π
BMI = (int(weight) / float(height)**2)
print(int(BMI))
