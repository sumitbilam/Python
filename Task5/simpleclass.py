class ExerciseSession:
    def __init__(self, name = "", intensity="", length = 0):
        self.name = name
        self.intensity = intensity
        self.duration = length
    
    def get_exercise(self):
        return self.name
    
    def get_intensity(self):
        return self.intensity
    
    def get_duration(self):
        return self.duration
    
    def set_exercise(self, excercise):
        self.name = excercise
    
    def set_intensity(self, intensity):
        self.intensity = intensity
        
    def set_duration(self, duration):
        self.duration = duration
    
    def calories_burned(self):
        if self.get_intensity() == "Low":
            return 4*self.duration
        elif self.get_intensity() == "Moderate":
            return 8*self.duration
        else:
            return 12*self.duration

new_exercise = ExerciseSession("Running", "Low", 60)
print("Calories burned when intensity was low = ",new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print("Calories burned when intensity was moderate = ",new_exercise.calories_burned())



