"""
report.py - Displays tabular report and class performance metrics.
"""


def print_results(processed_students, summary):
    """Prints formatted table and class statistics."""
    print("\n" + "=" * 88)
    print(f"{'STUDENT PERFORMANCE REPORT':^88}")
    print("=" * 88)

    # Header
    header = f"{'Roll':<6} | {'Name':<16} | {'Sub1':<5} {'Sub2':<5} {'Sub3':<5} {'Sub4':<5} {'Sub5':<5} | {'Total':<6} | {'Avg (%)':<7} | {'Grade':<5} | {'Status':<5}"
    print(header)
    print("-" * 88)

    # Student Rows
    for s in processed_students:
        m = s["Marks"]
        m_str = f"{m[0]:<5.1f} {m[1]:<5.1f} {m[2]:<5.1f} {m[3]:<5.1f} {m[4]:<5.1f}"
        row = f"{s['Roll No']:<6} | {s['Name']:<16} | {m_str} | {s['Total']:<6.1f} | {s['Average']:<7.2f} | {s['Grade']:<5} | {s['Status']:<5}"
        print(row)

    print("=" * 88)

    # Class Summary
    print("\n--- CLASS PERFORMANCE SUMMARY STATISTICS ---")
    print(f"  * Class Average Percentage : {summary['Class Average']:.2f}%")
    print(f"  * Highest Total Marks      : {summary['Highest Total']:.1f}")
    print(f"  * Lowest Total Marks       : {summary['Lowest Total']:.1f}")
    print(
        f"  * Class Topper             : {summary['Topper']['Name']} (Roll No: {summary['Topper']['Roll No']}) - Total: {summary['Topper']['Total']:.1f}")
    print(f"  * Total Students Passed    : {summary['Passed Count']}")
    print(f"  * Total Students Failed    : {summary['Failed Count']}")
    print("-" * 50 + "\n")