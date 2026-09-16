score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
elif score >= 80:
    print(f"A score of {score} earns grade: A")
elif score >= 70:
    print(f"A score of {score} earns grade: B")
elif score >= 60:
    print(f"A score of {score} earns grade: C")
elif score >= 50:
    print(f"A score of {score} earns grade: D")
else:
    print(f"A score of {score} earns grade: F")