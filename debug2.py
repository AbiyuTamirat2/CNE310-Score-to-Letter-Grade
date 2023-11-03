grade = int(input('Enter a number between 0 - 100.\n'))

def score_to_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 87:
        return "B+"
    elif grade >= 80:
        return "B"
    elif grade >= 77:
        return "C+"
    elif grade >= 70:
        return "C"
    elif grade >= 67:
        return "D+"
    elif grade >= 60:
        return "D"
    else:
        return "F"

letter_grade = score_to_letter_grade(grade)

print(f"Grade of {grade} should be {letter_grade}")