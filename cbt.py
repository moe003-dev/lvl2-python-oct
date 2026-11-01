score = 0


print ("""
    What is the capital city of Nigeria?
    A. Lagos
    B. Abuja
    C. Kano
    D. Port Harcourt
""")
answer = input("Answer: ").strip().upper()
if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is B")
    

print ("""
    Which of the following is a function of the CPU in a computer?
    A. Storing files permanently
    B. Displaying images on the screen
    C. Processing instructions
    D. Connecting to the internet
""")
answer = input("Answer: ").strip().upper()
if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is C")


print ("""
    Which of these is an example of an input device?
    A. Monitor
    B. Printer
    C. Speaker
    D. Keyboard
""")
answer = input("Answer: ").strip().upper()
if answer == "D":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is D")


print ("""
    What is the chemical symbol for water?
    A. H2O
    B. CO2
    C. O2
    D. NaCl
""")
answer = input("Answer: ").strip().upper()
if answer == "A":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is A")


print ("""
    5. Which of the following is a function of the CPU in a computer?
    A. Storing files permanently
    B. Displaying images on the screen
    C. Processing instructions
    D. Connecting to the internet
""")
answer = input("Answer: ").strip().upper()
if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. The correct answer is C")


print(f"\n you scored: {score}/5 \n")


# .strip("characters") method is used to remove any leading and trailing whitespace characters from the string. It does not remove whitespace characters that are in the middle of the string.

# .title() method is used to convert the first character of each word in the string to uppercase and the rest of the characters to lowercase. It is often used to format strings in a title case format.

#  .replace("old", "new") method is used to replace all occurrences of a specified substring (old) with another substring (new) in the string. It returns a new string with the replacements made, leaving the original string unchanged.

# .split("separator") method is used to split a string into a list of substrings based on a specified separator. If no separator is provided, it splits the string at whitespace characters by default. The resulting list contains the individual substrings.

# .slice[start:end] method is used to extract a portion of a string by specifying the starting and ending indices. It returns a new string that includes the characters from the starting index up to, but not including, the ending index. If the starting index is omitted, it defaults to 0, and if the ending index is omitted, it defaults to the length of the string.

# .join(iterable) method is used to concatenate the elements of an iterable (such as a list or tuple) into a single string, with a specified separator between each element. The separator is the string on which the .join() method is called.

# .index("substring") method is used to find the index of the first occurrence of a specified substring within a string. It returns the index of the substring if found, and raises a ValueError if the substring is not found.


# print("How are you doing\r today?")
# print(r"https://9jarocks.net/videodownload/dashing-youth-season-1-chinese-drama-id296469.html")