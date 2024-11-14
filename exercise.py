# exercise.py

class Exercise:
# Represents a single exercise with a name, muscle group, and number of repetitions.
    def __init__(self, name, muscle_group, repeats):
        self.name = name
        self.muscle_group = muscle_group
        self.repeats = repeats

    def __str__(self):
        # Returns a readable string representation of the exercise.
        return f"{self.name} - {self.repeats} reps"
