# main.py
from tracker import Tracker

def main():
    tracker = Tracker()

    while True:
        print("\nWelcome to One Dollar Habit Tracker 💰")
        print("1. Add a new habit")
        print("2. Mark a habit as done today")
        print("3. View all habits")
        print("4. Show total earnings")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter habit name: ")
            tracker.add_habit(name)
            print(f"✅ Habit '{name}' added!")

        elif choice == '2':
            name = input("Which habit did you complete today? ")
            result = tracker.complete_habit(name)
            if result is True:
                print("🎉 Good job! You earned $1 today!")
            elif result is False:
                print("⚠️ You already marked this habit as done today.")
            else:
                print("❌ Habit not found.")

        elif choice == '3':
            print("\n📋 Your Habits:")
            for habit in tracker.get_habits():
                last = habit.last_completed if habit.last_completed else "Never"
                print(f"- {habit.name}: {habit.streak}-day streak (Last done: {last})")

        elif choice == '4':
            print(f"\n💵 Total Earnings: ${tracker.get_earnings()}")

        elif choice == '5':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
