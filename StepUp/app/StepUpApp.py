
class StepUpApp:
    def __init__(self):
        self.step_count = 0
        self.daily_goal = 0

    def set_goal(self):
        try:
            self.daily_goal = int(input("Enter your daily step goal: "))
            print(f"Daily goal set to {self.daily_goal} steps.")
        except ValueError:
            print("Please enter a valid number for the daily goal.")

    def add_steps(self, steps):
        self.step_count += steps
        print(f"Added {steps} steps. Total steps: {self.step_count}")

    def check_progress(self):
        if self.daily_goal == 0:
            print("Please set a daily goal first.")
            return

        print(f"Steps today: {self.step_count} / {self.daily_goal}")
        if self.step_count >= self.daily_goal:
            print("Congratulations! You've reached your goal!")
        else:
            print("Keep going! You're almost there!")

    def reset_day(self):
        print("Resetting step count for a new day...")
        self.step_count = 0
        print("Step count reset.")

    def main_menu(self):
        while True:
            print("\n--- StepUp App ---")
            print("1. Set Daily Step Goal")
            print("2. Add Steps")
            print("3. Check Progress")
            print("4. Reset Day")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                self.set_goal()
            elif choice == '2':
                try:
                    steps = int(input("Enter steps to add: "))
                    self.add_steps(steps)
                except ValueError:
                    print("Please enter a valid number of steps.")
            elif choice == '3':
                self.check_progress()
            elif choice == '4':
                self.reset_day()
            elif choice == '5':
                print("Exiting StepUp. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the StepUp app
if __name__ == "__main__":
    app = StepUpApp()
    app.main_menu()
