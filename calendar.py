import datetime
import time

class Event:
    def __init__(self, name, date, category, recurring=None):
        self.name = name
        self.date = date
        self.category = category
        self.recurring = recurring

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def delete_event(self, event_name):
        events_to_remove = [e for e in self.events if e.name == event_name]
        if events_to_remove:
            self.events = [e for e in self.events if e not in events_to_remove]
            return True
        else:
            return False

    def list_events(self, date):
        events_on_date = [e for e in self.events if e.date == date]
        return events_on_date

    def list_events_by_category(self, category):
        events_in_category = [e for e in self.events if e.category == category]
        return events_in_category

    def notify_upcoming_events(self, days_until_event=1):
        today = datetime.date.today()
        upcoming_date = today + datetime.timedelta(days=days_until_event)
        upcoming_events = [e for e in self.events if e.date == upcoming_date]
        if upcoming_events:
            print(f"Upcoming events ({upcoming_date}):")
            for event in upcoming_events:
                print(f"{event.name} ({event.category})")
        else:
            print("No upcoming events.")

def main():
    my_calendar = Calendar()
    while True:
        print("\nOptions:")
        print("1. Add Event 📅")
        print("2. Delete Event ❌")
        print("3. List Events for Date 📆")
        print("4. List Events by Category 📁")
        print("5. Notify Upcoming Events 🔔")
        print("6. Exit 🚪")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter event name: ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            category = input("Enter event category: ")
            recurring = input("Is this a recurring event? (Y/N): ").strip().lower()
            if recurring == "y":
                recurring = input("Enter the recurrence pattern (e.g., daily, weekly, monthly): ")
            else:
                recurring = None
            event = Event(name, date, category, recurring)
            my_calendar.add_event(event)
            print("Event added! 🎉")

        elif choice == "2":
            event_name = input("Enter event name to delete: ")
            if my_calendar.delete_event(event_name):
                print("Event deleted. ❌")
            else:
                print("Event not found. 🚫")

        elif choice == "3":
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            events = my_calendar.list_events(date)
            if events:
                print(f"Events for {date_str}:")
                for event in events:
                    print(f"- {event.name} ({event.category})")
            else:
                print("No events for this date. 📭")

        elif choice == "4":
            category = input("Enter category to list events: ")
            events = my_calendar.list_events_by_category(category)
            if events:
                print(f"Events in category '{category}':")
                for event in events:
                    print(f"- {event.name} ({event.date})")
            else:
                print(f"No events found in category '{category}'. 📁")

        elif choice == "5":
            my_calendar.notify_upcoming_events()
            
        elif choice == "6":
            print("Exiting the calendar. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
