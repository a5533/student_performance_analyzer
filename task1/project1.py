import csv
import os
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. READ CSV DATA (PURE PYTHON)
# ---------------------------------------------------------
# Locate file dynamically in the same folder as project1.py
data = []
with open("Student_Grade_Management.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(
            {
                "Name": row["Name"],
                "Sub1": float(row["Sub1"]),
                "Sub2": float(row["Sub2"]),
                "Sub3": float(row["Sub3"]),
                "Sub4": float(row["Sub4"]),
                "Sub5": float(row["Sub5"]),
                "Total": float(row["Total"]),
                "Average": float(row["Average"]),
                "Grade": row["Grade"],
            }
        )

# Prepare lists for plotting
names = [student["Name"] for student in data]
averages = [student["Average"] for student in data]
subjects = ["Sub1", "Sub2", "Sub3", "Sub4", "Sub5"]

# ---------------------------------------------------------
# GRAPH 1: STUDENT-WISE AVERAGE MARKS
# ---------------------------------------------------------
plt.figure(figsize=(10, 5))
plt.bar(names, averages, color="#4682b4", edgecolor="black")
plt.title("1. Student-wise Average Marks Comparison")
plt.xlabel("Student Name")
plt.ylabel("Average Score (%)")
plt.xticks(rotation=30, ha="right")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, avg in enumerate(averages):
    plt.text(i, avg + 1.5, f"{avg:.1f}", ha="center", fontweight="bold")

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# GRAPH 2: SUBJECT-WISE CLASS AVERAGE MARKS
# ---------------------------------------------------------
subject_averages = []
for sub in subjects:
    sub_scores = [student[sub] for student in data]
    avg = sum(sub_scores) / len(sub_scores)
    subject_averages.append(avg)

plt.figure(figsize=(8, 5))
plt.bar(subjects, subject_averages, color="#2e8b57", edgecolor="black")
plt.title("2. Subject-wise Class Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Class Average Score")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, avg in enumerate(subject_averages):
    plt.text(i, avg + 1.5, f"{avg:.1f}", ha="center", fontweight="bold")

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# GRAPH 3: GRADE FREQUENCY DISTRIBUTION
# ---------------------------------------------------------
grade_order = ["A+", "A", "B", "C", "D", "F"]
grade_counts = {g: 0 for g in grade_order}
for student in data:
    g = student["Grade"]
    if g in grade_counts:
        grade_counts[g] += 1

counts = [grade_counts[g] for g in grade_order]

plt.figure(figsize=(8, 5))
plt.bar(grade_order, counts, color="#8a2be2", edgecolor="black")
plt.title("3. Grade Frequency Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.grid(axis="y", linestyle="--", alpha=0.5)

for i, count in enumerate(counts):
    if count > 0:
        plt.text(i, count + 0.1, str(count), ha="center", fontweight="bold")

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# GRAPH 4: STACKED BAR CHART (SUBJECT BREAKDOWN)
# ---------------------------------------------------------
plt.figure(figsize=(12, 6))
bottoms = [0.0] * len(names)
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

for idx, sub in enumerate(subjects):
    scores = [student[sub] for student in data]
    plt.bar(
        names,
        scores,
        bottom=bottoms,
        label=sub,
        color=colors[idx],
        edgecolor="white",
    )
    bottoms = [b + s for b, s in zip(bottoms, scores)]

plt.title("4. Stacked Bar Chart: Subject Breakdown per Student")
plt.xlabel("Student Name")
plt.ylabel("Total Score")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Subjects", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()