"""
calculations.py - Performs core calculations and class-wide statistics.
"""


def assign_grade_and_status(avg_mark):
    """
    Determines letter grade and pass/fail status based on average mark.
    Criteria:
        90 - 100 : A+ (Pass)
        80 - 89  : A  (Pass)
        70 - 79  : B  (Pass)
        60 - 69  : C  (Pass)
        50 - 59  : D  (Pass)
        Below 50 : F  (Fail)
    """
    if avg_mark >= 90:
        return "A+", "Pass"
    elif avg_mark >= 80:
        return "A", "Pass"
    elif avg_mark >= 70:
        return "B", "Pass"
    elif avg_mark >= 60:
        return "C", "Pass"
    elif avg_mark >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"


def process_student_records(students):
    """Calculates total, average, grade, and status for each student."""
    processed = []
    for s in students:
        total = sum(s["Marks"])
        avg = total / len(s["Marks"])
        grade, status = assign_grade_and_status(avg)

        record = {
            "Roll No": s["Roll No"],
            "Name": s["Name"],
            "Marks": s["Marks"],
            "Total": total,
            "Average": avg,
            "Grade": grade,
            "Status": status
        }
        processed.append(record)
    return processed


def compute_class_summary(processed_students):
    """Calculates overall statistics for the class."""
    totals = [s["Total"] for s in processed_students]
    averages = [s["Average"] for s in processed_students]

    class_avg = sum(averages) / len(averages)
    highest_total = max(totals)
    lowest_total = min(totals)

    topper = max(processed_students, key=lambda s: s["Total"])
    passed_count = sum(1 for s in processed_students if s["Status"] == "Pass")
    failed_count = sum(1 for s in processed_students if s["Status"] == "Fail")

    return {
        "Class Average": class_avg,
        "Highest Total": highest_total,
        "Lowest Total": lowest_total,
        "Topper": topper,
        "Passed Count": passed_count,
        "Failed Count": failed_count
    }