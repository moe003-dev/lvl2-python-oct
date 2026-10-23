score = float(input("Enter your score: "))

if score >= 70 and score <= 100:
    print("grade = A")
elif score >= 60 and score < 70:
    print("grade = B")
elif score >= 50 and score < 60:
    print("grade = C")
elif score >= 45 and score < 50:
    print("grade = D")
elif score >= 40 and score < 45:
    print("grade = E")
elif score >= 0 and score < 40:
    print("grade = F")
else:
    print("Invalid score. Enter a score between 0 and 100")