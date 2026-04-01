# Lab 1: Grade Evaluator & Archiver

A Python application that calculates a student's final academic standing based on a CSV file of course grades, and a Bash shell script that automates archiving of grade files.

---

## Project Files

| File | Description |
|---|---|
| `grade-evaluator.py` | Python script that validates and evaluates grades |
| `organizer.sh` | Bash script that archives grades.csv and logs the operation |
| `grades.csv` | CSV file containing course grades |

---

## How to Run the Python Application

### Requirements
- Python 3.x installed

### Steps
1. Make sure `grades.csv` is in the same folder as `grade-evaluator.py`
2. Open your terminal and navigate to the project folder:
```
   cd path/to/your/folder
```
3. Run the script:
```
   python grade-evaluator.py
```
4. When prompted, type the filename:
```
   Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

### What it does
- Validates all scores are between 0 and 100
- Validates that weights total 100 (Formative = 60, Summative = 40)
- Calculates the final grade and GPA (out of 5.0)
- Determines Pass/Fail status (requires 50% minimum in BOTH categories)
- Identifies which failed formative assignment is eligible for resubmission

---

## How to Run the Shell Script

### Requirements
- Bash shell (Linux, macOS, or Git Bash on Windows)

### Steps
1. Open your terminal and navigate to the project folder:
```
   cd path/to/your/folder
```
2. Make the script executable (first time only):
```
   chmod +x organizer.sh
```
3. Run the script:
```
   ./organizer.sh
```

### What it does
- Creates an `archive` folder if it does not exist
- Renames `grades.csv` with a timestamp (e.g., `grades_20251105-170000.csv`)
- Moves the renamed file into the `archive` folder
- Creates a new empty `grades.csv` ready for the next batch
- Logs the operation into `organizer.log`

---

## grades.csv Format

The CSV file must use tab separation with the following columns:

| Column | Description |
|---|---|
| `assignment` | Name of the assignment |
| `group` | Either `Formative` or `Summative` |
| `score` | Score between 0 and 100 |
| `weight` | Weight of the assignment |

### Example
```
assignment	group	score	weight
Quiz	Formative	85	20
Midterm Project	Summative	70	20
```

---

## GPA Formula
```
GPA = (Total Grade / 100) * 5.0
```

## Pass/Fail Rule

A student **PASSES** only if they score **50% or above in BOTH**:
- Formative assignments (weighted out of 60)
- Summative assignments (weighted out of 40)