# 🎓 Student Performance and Attendance Analysis

A Python-based Student Management System designed to manage student records, track attendance, analyze academic performance, and generate detailed student report cards.

This project helps organize student information and provides useful insights into overall class performance through automated calculations, filtering, sorting, and analytics.

## 🚀 Features

- **View Student Records:** Display all student records with filtering and sorting options.
- **Attendance Tracking:** Monitor student attendance percentages.
- **Student Search:** Search students using their roll number or name.
- **Add Student:** Add new student records with input validation.
- **Edit Student:** Update existing student information and academic marks.
- **Delete Student:** Remove student records from the database.
- **Grade Calculation:** Automatically calculate average marks and assign grades.
- **Class Analytics:** Display class averages, regular students, and defaulters.
- **Leaderboard:** Identify the top 3 performing students.
- **Subject Toppers:** Find the highest-scoring students in Mathematics, Science, and English.
- **Report Generation:** Export complete class reports and individual student report cards as `.txt` files.
- **Data Persistence:** Store student records in a JSON file so that data remains available between program executions.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Storage:** JSON
- **Python Libraries:** 
  - `json`
  - `os`

## 📊 Grading System

| Average Marks | Grade |
|---|---|
| 90 – 100 | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| Below 50 | F |

## 📌 Student Status Criteria

A student is classified as:

- **Regular:** Attendance is at least 75% AND average marks are at least 50.
- **Defaulter:** Attendance is below 75% OR average marks are below 50.

## 📂 Project Structure

```text
Student-performance-and-attendance-analysis/
│
├── main.py
├── student_database.json
├── class_report_card.txt
└── README.md
```

*Note: The generated report files and JSON database are created when the program runs. Your actual filenames may differ.*

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ankursingh80/Student-performance-and-attendance-analysis-.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-performance-and-attendance-analysis-
```

### 3. Run the Python Program

```bash
python3 main.py
```

## 💻 Main Menu

The project provides the following menu-driven operations:

1. View All Records (Filters & Sorting)
2. Search Student (Roll Number or Name)
3. Add New Student Record
4. View Class Analytics & Leaderboard
5. Edit Student Record
6. Delete Student Record
7. Export Full Class Report
8. Export Single Student Report Card
9. Exit

## 🎯 Learning Outcomes

Through this project, I explored and practiced:

- Python functions and modular programming.
- Dictionaries and data structures.
- File handling and JSON data storage.
- Conditional statements and loops.
- Exception handling and input validation.
- Sorting and filtering techniques.
- Data analysis and statistical calculations.
- Building a menu-driven application.

## 👨‍💻 Author

Ankur Singh

B.Tech – Computer Science and Engineering

GitHub: [@ankursingh80](https://github.com/ankursingh80)

---

⭐ If you find this project useful, consider giving the repository a star!
