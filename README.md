# Student Performance Analyzer

A lightweight Python application designed to ingest, process, analyze, and visualize academic performance data for students across multiple subjects. Built to adhere to minimal dependency requirements, the application handles all data parsing, aggregation, and mathematical computations using native Python data structures and standard libraries (`csv`, `os`), relying externally only on `matplotlib` for graphical visualization.

---

## Key Features

* **Zero Heavy Data Dependencies:** Operates without Pandas or NumPy, utilizing native Python dictionaries, list comprehensions, and built-in functions (`sum()`, `len()`, `enumerate()`).
* **Robust File Path Management:** Employs dynamic relative pathing via `os.path` to ensure seamless execution across different operating systems and IDEs (such as PyCharm or VS Code).
* **Automated Data Ingestion:** Parses CSV files into structured dictionary representations with runtime type conversion for mathematical calculations.
* **Comprehensive Visualizations:** Generates four distinct analytical bar charts to assess individual and cohort academic metrics.

---

## Dataset Schema

The application expects input data formatted as a CSV file (`Student_Grade_Management.csv`) with the following column structure:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `Roll No` | Integer | Unique identifier for each student |
| `Name` | String | Full name of the student |
| `Sub1` – `Sub5` | Float/Int | Numerical scores across 5 individual subjects (0–100) |
| `Total` | Float/Int | Cumulative score across all 5 subjects (Max: 500) |
| `Average` | Float | Percentage/mean score across all 5 subjects |
| `Grade` | String | Categorical grade assignment (`A+`, `A`, `B`, `C`, `D`, `F`) |

---

## Repository Structure

```text
student_performance_analyzer/
│
├── task1/
│   ├── Student_Grade_Management.csv   # Source dataset
│   └── project1.py                     # Main execution script
│
└── README.md                          # Project documentation

```

---

## Visualizations Generated

The script processes the CSV dataset and renders four analytical bar charts:

1. **Student-Wise Average Marks Comparison (Vertical Bar Chart)**
* **Metrics:** Student Names vs. Individual Average Scores (%)
* **Purpose:** Highlights top performers and identifies students needing academic support.


2. **Subject-Wise Class Average Marks (Bar Chart)**
* **Metrics:** Subjects (`Sub1`–`Sub5`) vs. Class Mean Score
* **Purpose:** Evaluates overall class performance and subject difficulty levels.


3. **Grade Frequency Distribution (Distribution Bar Chart)**
* **Metrics:** Grade Categories (`A+`, `A`, `B`, `C`, `D`, `F`) vs. Student Count
* **Purpose:** Visualizes cohort score spread and class performance density.


4. **Subject Breakdown per Student (Stacked Bar Chart)**
* **Metrics:** Student Names vs. Total Cumulative Marks (Segmented by Subject)
* **Purpose:** Illustrates how individual subject scores contribute to a student's total academic score.



---

## Installation & Setup

### Prerequisites

* **Python 3.8+** installed on your system.
* **Matplotlib** installed for rendering plots.

### Environment Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/student-performance-analyzer.git
cd student-performance-analyzer

```


2. **Install required dependencies:**
```bash
pip install matplotlib

```



---

## How to Run

Navigate to the directory containing `project1.py` and run the script via terminal or IDE:

```bash
cd task1
python project1.py

```

*If using PyCharm or VS Code, open `project1.py` directly and click **Run**.*

---

## Code Architecture

The script follows a modular execution flow:

```text
[ CSV File Ingestion ] ──> [ Dict Parsing & Casting ] ──> [ Pure Python Aggregations ] ──> [ Matplotlib Rendering ]

```

1. **Data Loading:** `csv.DictReader` loads records into a list of dictionaries (`data`). Numeric fields are converted to `float` values inline.
2. **Data Aggregation:**
* Student averages extracted via list comprehensions: `[s["Average"] for s in data]`.
* Subject averages calculated dynamically: `sum(sub_scores) / len(sub_scores)`.
* Grade frequency counted using standard dictionary mapping.


3. **Visualization:** Each chart figure is built, formatted with data value labels using `plt.text()`, styled with custom color palettes and grid lines, and rendered via `plt.show()`.

---

Would you like me to add a section explaining how to customize the grade boundaries or expand the code to export the generated charts directly as PNG files?
