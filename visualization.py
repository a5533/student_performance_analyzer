"""
visualization.py - Generates Matplotlib graphs for performance analysis.
"""

import matplotlib
matplotlib.use('TkAgg')  # Forces interactive window pop-up
import matplotlib.pyplot as plt

def generate_visualizations(processed_students, summary):
    """Generates 5 required visual charts using Matplotlib."""

    names = [s["Name"] for s in processed_students]
    totals = [s["Total"] for s in processed_students]
    averages = [s["Average"] for s in processed_students]
    grades = [s["Grade"] for s in processed_students]
    class_avg = summary["Class Average"]

    # Setup subplots figure layout
    fig = plt.figure(figsize=(16, 10))
    plt.suptitle("Student Performance Analytical Dashboard", fontsize=16, fontweight="bold")

    # 1. Bar Chart: Student Name vs Total Marks
    ax1 = plt.subplot(2, 3, 1)
    ax1.bar(names, totals, color="skyblue", edgecolor="black")
    ax1.set_title("Total Marks per Student", fontweight="bold")
    ax1.set_ylabel("Total Marks")
    plt.xticks(rotation=45, ha="right")

    # 2. Pie Chart: Grade Distribution
    ax2 = plt.subplot(2, 3, 2)
    grade_counts = {}
    for g in grades:
        grade_counts[g] = grade_counts.get(g, 0) + 1

    ax2.pie(
        grade_counts.values(),
        labels=grade_counts.keys(),
        autopct="%1.1f%%",
        startangle=140,
        colors=["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c1f0","#ffb3e6"]
    )
    ax2.set_title("Grade Distribution", fontweight="bold")

    # 3. Line Chart: Student Average Scores vs Class Average
    ax3 = plt.subplot(2, 3, 4)
    ax3.plot(names, averages, marker='o', color='blue', linewidth=2, label="Student Avg")
    ax3.axhline(y=class_avg, color='r', linestyle='--', label=f"Class Avg ({class_avg:.1f}%)")
    ax3.set_title("Student Averages vs Class Average", fontweight="bold")
    ax3.set_ylabel("Average Score (%)")
    ax3.legend(loc="lower right")
    plt.xticks(rotation=45, ha="right")

    # 4. Histogram: Distribution of Total Marks
    ax4 = plt.subplot(2, 3, 5)
    ax4.hist(totals, bins=5, color="lightgreen", edgecolor="black")
    ax4.set_title("Distribution of Total Marks", fontweight="bold")
    ax4.set_xlabel("Total Marks Range")
    ax4.set_ylabel("Number of Students")

    # 5. Box Plot: Subject-wise Score Spread & Outliers
    ax5 = plt.subplot(2, 3, 3)
    subject_marks = [[] for _ in range(5)]
    for s in processed_students:
        for sub_idx in range(5):
            subject_marks[sub_idx].append(s["Marks"][sub_idx])

    ax5.boxplot(subject_marks, labels=[f"Sub {i+1}" for i in range(5)], patch_artist=True)
    ax5.set_title("Subject-wise Score Spread", fontweight="bold")
    ax5.set_ylabel("Marks (0-100)")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show(block=True)