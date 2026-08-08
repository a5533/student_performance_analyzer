"""
data_entry.py - Handles collection and validation of student data.
"""


def get_sample_data():
    """Returns a sample dataset of 10 students across 5 subjects."""
    return [
        {"Roll No": 101, "Name": "Aarav Sharma", "Marks": [85, 78, 92, 88, 90]},
        {"Roll No": 102, "Name": "Ananya Roy", "Marks": [62, 70, 68, 75, 65]},
        {"Roll No": 103, "Name": "Rohan Patel", "Marks": [95, 91, 89, 94, 96]},
        {"Roll No": 104, "Name": "Priya Singh", "Marks": [45, 52, 48, 50, 55]},
        {"Roll No": 105, "Name": "Vikram Verma", "Marks": [78, 82, 80, 79, 85]},
        {"Roll No": 106, "Name": "Neha Gupta", "Marks": [35, 40, 38, 42, 30]},
        {"Roll No": 107, "Name": "Karan Kumar", "Marks": [88, 84, 86, 90, 89]},
        {"Roll No": 108, "Name": "Sanya Malhotra", "Marks": [58, 64, 60, 62, 66]},
        {"Roll No": 109, "Name": "Rahul Mehta", "Marks": [72, 75, 70, 74, 78]},
        {"Roll No": 110, "Name": "Diya Joshi", "Marks": [91, 88, 94, 92, 95]},
    ]


def collect_interactive_data(num_students=10, num_subjects=5):
    """Interactively prompts the user to input student data with validation."""
    students = []
    print(f"\n--- Enter Data for {num_students} Students ---")

    for i in range(1, num_students + 1):
        print(f"\nStudent {i} of {num_students}:")

        while True:
            try:
                roll_no = int(input("  Roll Number: ").strip())
                break
            except ValueError:
                print("  [Error] Roll number must be an integer.")

        name = input("  Student Name: ").strip()
        while not name:
            name = input("  [Error] Name cannot be empty. Re-enter Name: ").strip()

        marks = []
        for sub in range(1, num_subjects + 1):
            while True:
                try:
                    mark = float(input(f"  Marks for Subject {sub} (0-100): ").strip())
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("  [Error] Marks must be between 0 and 100.")
                except ValueError:
                    print("  [Error] Please enter a valid numeric value.")

        students.append({
            "Roll No": roll_no,
            "Name": name,
            "Marks": marks
        })

    return students