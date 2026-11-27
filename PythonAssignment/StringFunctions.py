username = input("enter a username :")

if(len(username)>12):
    print("username cannot be more than 12 charcter")
elif username.find(" ") != -1:
    print("there cannnot be spaces in username")
elif username.isdigit()== True:
    print("username cannot have digits")
else:
    print(f"wellcome {username}")

# 1. Base String
text = "  introvert brat  "

# 2. Common String Functions
clean_text = text.strip()       # Removes trailing/leading spaces -> "introvert brat"
loud_text = clean_text.upper()  # Converts to uppercase -> "INTROVERT BRAT"
word_list = clean_text.split()  # Splits into a list of words -> ['introvert', 'brat']

# 3. Print Results
print("Original:", text)
print("Cleaned: ", clean_text)
print("Loud:    ", loud_text)
print("Split:   ", word_list)
