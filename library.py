# exercise_library.py

import random
from exercise import Exercise

class ExerciseLibrary:
# Manages a collection of exercises and provides methods to fetch exercises by muscle group.
    def __init__(self, exercises):
        self.exercises = exercises

    def get_exercise(self, muscle_group):
        # Returns a random exercise for the specified muscle group.
        filtered_exercises = []
        for exercise in self.exercises:
            if exercise.muscle_group == muscle_group:
                filtered_exercises.append(exercise)
        
        if len(filtered_exercises) == 0:
            return None  # No exercise found for this muscle group
        
        return random.choice(filtered_exercises)
