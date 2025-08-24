def pick_attendees(class_file, attendee_file):
    try:
        with open(class_file, "r") as f:
            students = f.readlines()

        attendees = []
        for line in students:
            name, grade = line.strip().split(",")
            if grade.upper() == "A":
                attendees.append(name)

        with open(attendee_file, "w") as f:
            for student in attendees:
                f.write(student + "\n")

        print(f"✅ Attendees list written to {attendee_file}")

    except FileNotFoundError:
        print(f"❌ Error: {class_file} not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


def read_user_file():
    filename = input("Enter the class list filename: ")
    try:
        with open(filename, "r") as f:
            print("\n--- Class List ---")
            print(f.read())
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    read_user_file()
    pick_attendees("class_list.txt", "function_attendees.txt")

