# Event Calendar for 2025

events = {}

def add_event():
    date = input("Enter event date (format: YYYY-MM-DD): ")
    if not date.startswith("2025"):
        print("You can only add events for 2025!")
        return
    event = input("Enter event description: ")
    events[date] = event
    print("✅ Event added successfully!")

def edit_event():
    date = input("Enter event date to edit (format: YYYY-MM-DD): ")
    if date in events:
        event = input("Enter new event description: ")
        events[date] = event
        print("✏️ Event updated successfully!")
    else:
        print("❌ No event found on that date.")

def delete_event():
    date = input("Enter event date to delete (format: YYYY-MM-DD): ")
    if date in events:
        del events[date]
        print("🗑️ Event deleted successfully!")
    else:
        print("❌ No event found on that date.")

def show_events():
    if not events:
        print("📭 No events to show.")
    else:
        print("\n📅 Events in 2025:")
        for date, event in sorted(events.items()):
            print(f"{date} : {event}")
    print()

def menu():
    while True:
        print("\n--- Event Calendar 2025 ---")
        print("1. Add Event")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. Show Events")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_event()
        elif choice == '2':
            edit_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            show_events()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the menu
menu()
