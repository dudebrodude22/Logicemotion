class LogicEmotion:
    def __init__(self, initial_value=5.0, tolerance=0.001):
        """Initialize with a starting value for emotion and logic."""
        self.emotion = initial_value
        self.logic = initial_value
        self.tolerance = tolerance  # How close values need to be to stop

    def balance(self, input_value, max_steps=100):
        """Blend logic and emotion until they stabilize."""
        current_value = input_value
        for step in range(max_steps):
            # Logic adjusts based on emotion
            if abs(current_value - self.emotion) > self.tolerance:
                self.emotion = (current_value + self.emotion) / 2
                current_value = self.emotion
            # Emotion adjusts based on logic
            elif abs(current_value - self.logic) > self.tolerance:
                self.logic = (current_value + self.logic) / 2
                current_value = self.logic
            # If both are close enough, we're done
            elif abs(self.emotion - self.logic) <= self.tolerance:
                break
        return (self.emotion + self.logic) / 2  # Final balanced state

# Let’s try it out!
model = LogicEmotion(initial_value=5.0)
print(f"Starting with 5.0: {model.balance(5.0)}")
print(f"Starting with 6.0: {model.balance(6.0)}")
