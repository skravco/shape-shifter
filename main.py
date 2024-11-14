# main.py

from exercise import Exercise
from library import ExerciseLibrary
from scheduler import WorkoutScheduler
from message import EmailService
import datetime
import os

class Main:
    # Coordinates the workout program, selecting exercises and sending emails.
    def __init__(self, exercise_library, workout_scheduler, email_service):
        self.exercise_library = exercise_library
        self.workout_scheduler = workout_scheduler
        self.email_service = email_service

    def send_todays_workout(self):
        today = datetime.datetime.now().strftime("%A")
        muscle_group = self.workout_scheduler.get_muscle_group(today)

        if muscle_group == "Rest":
            print(f"No workout scheduled for {today}.")
            return # Do nothing if today is Rest

        exercise = self.exercise_library.get_exercise(muscle_group)

        if exercise is None:
            print(f"No exercise found for {muscle_group} on {today}")
            return

        # Prepare email content
        subject = f"Workout for {today}"
        message = f"Today's workout: {exercise}"
        
        # Send the email
        self.email_service.send_email(subject, message)


# ----- Mock Data and Program Execution -----

# Sample exercises
exercises = [
    Exercise("Push-ups", "Chest", 20),
    Exercise("Pull-ups", "Back", 15),
    Exercise("Squats", "Legs", 25),
    Exercise("Bicep Curls", "Arms", 15),
    Exercise("Plank", "Core", 60),
    Exercise("Lunges", "Legs", 20),
    Exercise("Dumbbell Press", "Chest", 15)
]

# Map days of the week to muscle groups
days_muscle_map = {
    "Monday": "Chest",
    "Tuesday": "Back",
    "Wednesday": "Legs",
    "Thursday": "Arms",
    "Friday": "Core",
    "Saturday": "Legs",
    "Sunday": "Rest"
}

# Email configuration
email_config = {
    'from_email': 'your_email@example.com',
    'to_email': 'recipient_email@example.com',
    'smtp_server': 'sandbox.smtp.mailtrap.io',
    'smtp_port': 2525,
    'username': os.getenv('MAILTRAP_USERNAME'),
    'password': os.getenv('MAILTRAP_PASSWORD'),
}

# Instantiate each module class
exercise_library = ExerciseLibrary(exercises)
workout_scheduler = WorkoutScheduler(days_muscle_map)
email_service = EmailService(email_config)

# Run the workout program
program = Main(exercise_library, workout_scheduler , email_service)
program.send_todays_workout()
