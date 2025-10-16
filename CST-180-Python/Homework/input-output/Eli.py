print("do you like cake")

# Get input from user
answer_input = input()

# Convert string to boolean
if answer_input.lower() == "true":
    Answer = True
elif answer_input.lower() == "false":
    Answer = False
else:
    print("Invalid input! Please enter 'true' or 'false'")
    Answer = None

# Check the boolean value
if Answer == True:
    print("Eli Likes cake!")
else:
    print("Eli does not like cake.")
