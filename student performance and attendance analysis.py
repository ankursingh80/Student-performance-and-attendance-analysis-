import json
import os

FILENAME = "student_database.json"

def load_database():
    """Loads student data from a JSON file if it exists, otherwise returns default data."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
                return {int(k): v for k, v in data.items()}
        except Exception:
            print("Error reading database file. Loading default records.")
    
   
    return {
        1: {"name": "Ankur Singh", "attendance": 97, "math": 100, "science": 100, "english": 100},
        2: {"name": "Ananya Bhati", "attendance": 92, "math": 95, "science": 91, "english": 94},
        3: {"name": "Rohit Tyagi", "attendance": 68, "math": 55, "science": 60, "english": 65},
        4: {"name": "Reema Yadav", "attendance": 74, "math": 72, "science": 78, "english": 80},
        5: {"name": "Aniket Sharma", "attendance": 99, "math": 9, "science": 2, "english": 0},
        6: {"name": "Anubhav Verma", "attendance": 99, "math": 9, "science": 2, "english": 2},
        7: {"name": "Priya Chauhan", "attendance": 88, "math": 84, "science": 89, "english": 91},
        8: {"name": "Siddharth Malhotra", "attendance": 95, "math": 98, "science": 94, "english": 88},
        9: {"name": "Kavita Bisht", "attendance": 79, "math": 68, "science": 74, "english": 82},
        10: {"name": "Varun Tomar", "attendance": 62, "math": 45, "science": 50, "english": 58},
        11: {"name": "Neha Chaudhary", "attendance": 91, "math": 87, "science": 85, "english": 90},
        12: {"name": "Harshvardhan Rawat", "attendance": 84, "math": 76, "science": 81, "english": 73},
        13: {"name": "Sneha Gupta", "attendance": 96, "math": 92, "science": 96, "english": 95},
        14: {"name": "Aryan Bansal", "attendance": 71, "math": 61, "science": 59, "english": 64},
        15: {"name": "Divya Joshi", "attendance": 89, "math": 82, "science": 88, "english": 86},
        16: {"name": "Kartikeya Pandey", "attendance": 55, "math": 38, "science": 42, "english": 49},
        17: {"name": "Meenakshi Negi", "attendance": 93, "math": 90, "science": 87, "english": 93},
        18: {"name": "Yashwardhan Solanki", "attendance": 77, "math": 66, "science": 70, "english": 68},
        19: {"name": "Pooja Thakur", "attendance": 85, "math": 79, "science": 83, "english": 85},
        20: {"name": "Rishabh Saxena", "attendance": 90, "math": 88, "science": 92, "english": 84},
    }

def save_database(db):
    """Saves the student dictionary to a JSON file."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(db, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")


student_database = load_database()

def calculate_average(marks_dict):
    return (marks_dict["math"] + marks_dict["science"] + marks_dict["english"]) / 3

def get_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 50: return "D"
    else: return "F"

def display_all_records():
    """Displays records with sorting and filtering options."""
    if not student_database:
        print("\nNo records found.")
        return

    print("\n--- View Options ---")
    print("1. View All Students")
    print("2. View Only Regular Students")
    print("3. View Only Defaulters")
    filter_choice = input("Choose filter option (1-3, default 1): ").strip()

    print("\n--- Sort Options ---")
    print("1. Sort by Roll Number")
    print("2. Sort by Name")
    print("3. Sort by Average Marks (High to Low)")
    sort_choice = input("Choose sorting option (1-3, default 1): ").strip()

    records = list(student_database.items())

  
    if filter_choice == '2':
        records = [r for r in records if r[1]["attendance"] >= 75 and calculate_average(r[1]) >= 50]
    elif filter_choice == '3':
        records = [r for r in records if r[1]["attendance"] < 75 or calculate_average(r[1]) < 50]

  
    if sort_choice == '2':
        records.sort(key=lambda x: x[1]['name'])
    elif sort_choice == '3':
        records.sort(key=lambda x: calculate_average(x[1]), reverse=True)
    else:
        records.sort(key=lambda x: x[0])

    if not records:
        print("\nNo students match this criteria.")
        return

    print("\n" + "=" * 75)
    print(f"{'Roll No':<8} {'Name':<20} {'Attendance':<12} {'Avg Marks':<10} {'Grade':<8} {'Status':<10}")
    print("=" * 75)
    
    for roll, data in records:
        avg = calculate_average(data)
        grade = get_grade(avg)
        status = "Defaulter" if data["attendance"] < 75 or avg < 50 else "Regular"
        print(f"{roll:<8} {data['name']:<20} {str(data['attendance']) + '%':<12} {avg:<10.2f} {grade:<8} {status:<10}")
    
    print("=" * 75)

def search_student():
    """Searches student by Roll Number or Name."""
    print("\n--- Search Student ---")
    query = input("Enter Roll Number or Student Name to search: ").strip()
    
    found = []
    if query.isdigit():
        roll = int(query)
        if roll in student_database:
            found.append((roll, student_database[roll]))
    else:
        for roll, data in student_database.items():
            if query.lower() in data['name'].lower():
                found.append((roll, data))
                
    if not found:
        print(f"No student found matching '{query}'.")
        return

    for roll, data in found:
        avg = calculate_average(data)
        grade = get_grade(avg)
        status = "Defaulter" if data["attendance"] < 75 or avg < 50 else "Regular"
        
        print("\n" + "-" * 40)
        print(f"STUDENT REPORT CARD (Roll No: {roll})")
        print("-" * 40)
        print(f"Name       : {data['name']}")
        print(f"Attendance : {data['attendance']}%")
        print(f"Math Marks : {data['math']}")
        print(f"Science    : {data['science']}")
        print(f"English    : {data['english']}")
        print(f"Average    : {avg:.2f}")
        print(f"Grade      : {grade}")
        print(f"Status     : {status}")
        print("-" * 40)

def add_student():
    """Adds a new student with safe validation."""
    print("\n--- Add New Student Record ---")
    try:
        roll = int(input("Enter new Roll Number: "))
        if roll in student_database:
            print("Error: This Roll Number already exists!")
            return
            
        name = input("Enter Student Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return

        while True:
            try:
                attendance = int(input("Enter Attendance Percentage (0-100): "))
                if 0 <= attendance <= 100: break
                print("Attendance must be between 0 and 100.")
            except ValueError: print("Please enter a valid integer.")

        while True:
            try:
                math = float(input("Enter Math Marks (0-100): "))
                science = float(input("Enter Science Marks (0-100): "))
                english = float(input("Enter English Marks (0-100): "))
                if all(0 <= m <= 100 for m in [math, science, english]): break
                print("Marks must be between 0 and 100.")
            except ValueError: print("Please enter valid numbers.")
        
        student_database[roll] = {"name": name, "attendance": attendance, "math": math, "science": science, "english": english}
        save_database(student_database)
        print(f"Success! Student '{name}' added and saved.")
    except ValueError:
        print("Invalid input! Operation cancelled.")

def class_summary():
    """Shows advanced analytics including Leaderboard and Subject Toppers."""
    print("\n--- Advanced Class Analytics & Summary ---")
    if not student_database:
        print("No student records available.")
        return
        
    total_students = len(student_database)
    defaulters = sum(1 for d in student_database.values() if d["attendance"] < 75 or calculate_average(d) < 50)
    
    total_math = sum(d["math"] for d in student_database.values())
    total_sci = sum(d["science"] for d in student_database.values())
    total_eng = sum(d["english"] for d in student_database.values())
    
    math_topper = max(student_database.values(), key=lambda x: x['math'])
    sci_topper = max(student_database.values(), key=lambda x: x['science'])
    eng_topper = max(student_database.values(), key=lambda x: x['english'])

    sorted_students = sorted(student_database.items(), key=lambda x: calculate_average(x[1]), reverse=True)

    print(f"Total Students       : {total_students}")
    print(f"Regular Students     : {total_students - defaulters}")
    print(f"Defaulters           : {defaulters}")
    print("-" * 45)
    print(f"Class Average (Math)    : {total_math / total_students:.2f}")
    print(f"Class Average (Science) : {total_sci / total_students:.2f}")
    print(f"Class Average (English) : {total_eng / total_students:.2f}")
    print("-" * 45)
    print("🏆 Top 3 Leaderboard:")
    for i, (r, data) in enumerate(sorted_students[:3], 1):
        print(f"  {i}. {data['name']} (Avg: {calculate_average(data):.2f})")
    print("-" * 45)
    print(f"⭐ Math Topper    : {math_topper['name']} ({math_topper['math']} marks)")
    print(f"⭐ Science Topper : {sci_topper['name']} ({sci_topper['science']} marks)")
    print(f"⭐ English Topper : {eng_topper['name']} ({eng_topper['english']} marks)")

def edit_student():
    """Edits an existing student's data."""
    print("\n--- Edit Student Record ---")
    try:
        roll = int(input("Enter Roll Number to edit: "))
        if roll not in student_database:
            print(f"Error: Roll Number {roll} does not exist!")
            return
            
        student = student_database[roll]
        print(f"Editing record for: {student['name']} (Press Enter to keep old value)")
        
        new_name = input(f"New name [{student['name']}]: ").strip()
        if new_name: student["name"] = new_name
            
        att = input(f"New attendance [{student['attendance']}%]: ").strip()
        if att: student["attendance"] = int(att)
            
        m = input(f"New math marks [{student['math']}]: ").strip()
        if m: student["math"] = float(m)
            
        s = input(f"New science marks [{student['science']}]: ").strip()
        if s: student["science"] = float(s)
            
        e = input(f"New english marks [{student['english']}]: ").strip()
        if e: student["english"] = float(e)
            
        save_database(student_database)
        print(f"\nSuccess! Record updated.")
    except ValueError:
        print("Invalid input!")

def delete_student():
    """Deletes a student record."""
    print("\n--- Delete Student Record ---")
    try:
        roll = int(input("Enter Roll Number to delete: "))
        if roll in student_database:
            confirm = input(f"Delete {student_database[roll]['name']}? (y/n): ").strip().lower()
            if confirm == 'y':
                name = student_database.pop(roll)['name']
                save_database(student_database)
                print(f"Student '{name}' deleted successfully.")
            else: print("Cancelled.")
        else: print("Roll Number not found.")
    except ValueError: print("Invalid input!")

def export_full_report():
    """Exports all student records into a text file report card."""
    filename = "class_report_card.txt"
    try:
        with open(filename, "w") as f:
            f.write("=" * 75 + "\n")
            f.write("                    CLASS PERFORMANCE REPORT CARD\n")
            f.write("=" * 75 + "\n")
            f.write(f"{'Roll No':<8} {'Name':<20} {'Attendance':<12} {'Avg Marks':<10} {'Grade':<8} {'Status':<10}\n")
            f.write("-" * 75 + "\n")
            
            for roll, data in sorted(student_database.items()):
                avg = calculate_average(data)
                grade = get_grade(avg)
                status = "Defaulter" if data["attendance"] < 75 or avg < 50 else "Regular"
                f.write(f"{roll:<8} {data['name']:<20} {str(data['attendance']) + '%':<12} {avg:<10.2f} {grade:<8} {status:<10}\n")
                
            f.write("=" * 75 + "\n")
        print(f"\nSuccess! Full class report exported as '{filename}'.")
    except Exception as e:
        print(f"Error exporting file: {e}")

def export_single_report():
    """Exports a single student's complete details and marks into a text file."""
    print("\n--- Export Single Student Report Card ---")
    try:
        roll = int(input("Enter Roll Number of the student: "))
        if roll not in student_database:
            print(f"Error: Roll Number {roll} does not exist!")
            return
            
        student = student_database[roll]
        avg = calculate_average(student)
        grade = get_grade(avg)
        status = "Defaulter" if student["attendance"] < 75 or avg < 50 else "Regular"
        
        safe_name = "".join(c for c in student['name'] if c.isalnum() or c.isspace()).strip().replace(" ", "_")
        filename = f"report_card_roll_{roll}_{safe_name}.txt"
        
        with open(filename, "w") as f:
            f.write("=" * 45 + "\n")
            f.write(f"        INDIVIDUAL STUDENT REPORT CARD\n")
            f.write("=" * 45 + "\n")
            f.write(f"Roll Number : {roll}\n")
            f.write(f"Name        : {student['name']}\n")
            f.write(f"Attendance  : {student['attendance']}%\n")
            f.write("-" * 45 + "\n")
            f.write(f"Math Marks  : {student['math']}\n")
            f.write(f"Science     : {student['science']}\n")
            f.write(f"English     : {student['english']}\n")
            f.write("-" * 45 + "\n")
            f.write(f"Average     : {avg:.2f}\n")
            f.write(f"Grade       : {grade}\n")
            f.write(f"Status      : {status}\n")
            f.write("=" * 45 + "\n")
            
        print(f"\nSuccess! Report card saved as '{filename}' in your folder.")
    except ValueError:
        print("Invalid input! Please enter a valid numeric Roll Number.")

def main():
    while True:
        print("\n==============================================")
        print("   ADVANCED STUDENT MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. View All Records (with Filters & Sorting)")
        print("2. Search Student (Roll No or Name)")
        print("3. Add New Student Record")
        print("4. View Class Analytics & Leaderboard")
        print("5. Edit Student Record")
        print("6. Delete Student Record")
        print("7. Export Full Class Report (.txt)")
        print("8. Export Single Student Report Card (.txt)")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()

        if choice == '1': display_all_records()
        elif choice == '2': search_student()
        elif choice == '3': add_student()
        elif choice == '4': class_summary()
        elif choice == '5': edit_student()
        elif choice == '6': delete_student()
        elif choice == '7': export_full_report()
        elif choice == '8': export_single_report()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-9.")

if __name__ == "__main__":
    main()
