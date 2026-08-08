"""
main.py - Entry point for Student Performance Analyzer.
"""

from data_entry import get_sample_data, collect_interactive_data
from calculations import process_student_records, compute_class_summary
from report import print_results
from visualization import generate_visualizations


def main():
    print("==================================================")
    print("   WELCOME TO STUDENT PERFORMANCE ANALYZER")
    print("==================================================")
    print("1. Load Default Sample Data (10 Students)")
    print("2. Enter Data Manually")

    choice = input("\nSelect an option (1 or 2): ").strip()

    if choice == "2":
        raw_data = collect_interactive_data(num_students=10, num_subjects=5)
    else:
        print("\n--> Loading default dataset for 10 students...")
        raw_data = get_sample_data()

    # 1. Perform Calculations
    processed_students = process_student_records(raw_data)
    summary = compute_class_summary(processed_students)

    # 2. Display Tabular Report & Statistics
    print_results(processed_students, summary)

    # 3. Generate Matplotlib Charts
    generate_visualizations(processed_students, summary)


if __name__ == "__main__":
    main()