# workout_scheduler.py

class WorkoutScheduler:
    # Manages the workout schedule, mapping days of the week to muscle groups.
    def __init__(self, days_muscle_map):
        self.days_muscle_map = days_muscle_map

    def get_muscle_group(self, day):
        # Returns the muscle group scheduled for the specified day.
        return self.days_muscle_map.get(day)
