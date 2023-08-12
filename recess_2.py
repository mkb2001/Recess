#EXERCISE 1
#Write a programm to ask students about their mental health
#Ask them to rate their from 1 to 10 their mental health 

print("Welcome to the Student Mental Health Survey!")

student_name = input("Please enter your name: ")

print(f"Hello, {student_name}! Let's begin the survey.")

survey_responses = {
    "Name": student_name,
    "Mental Health": "",
    "Rating": 0
}

mental_health = input("How would you describe your current mental health? (e.g., sad, anxious): ")
rating = int(input("On a scale of 1 to 10, with 1 being very poor and 10 being excellent, how would you rate your mental health? "))

survey_responses["Mental Health"] = mental_health
survey_responses["Rating"] = rating

print("Thank you for participating in the survey! Here are your responses:")

for key, value in survey_responses.items():
    print(f"{key}: {value}")
