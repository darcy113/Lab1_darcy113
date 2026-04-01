import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })

        if not assignments:
            print("Error: The CSV file is empty. No grades to process.")
            sys.exit(1)

        return assignments

    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    # a) Check if all scores are between 0 and 100
    print("\n>> Grade Validation:")
    all_scores_valid = True
    for a in data:
        if not (0 <= a['score'] <= 100):
            print(f"   Invalid score for '{a['assignment']}': {a['score']} (must be 0-100)")
            all_scores_valid = False
    if all_scores_valid:
        print("   All scores are valid (0-100).")

    # b) Validate total weights (Total=100, Summative=40, Formative=60)
    print("\n>> Weight Validation:")
    total_weight = sum(a['weight'] for a in data)
    formative_weight = sum(a['weight'] for a in data if a['group'] == 'Formative')
    summative_weight = sum(a['weight'] for a in data if a['group'] == 'Summative')

    print(f"   Total Weight:      {total_weight} (expected 100)")
    print(f"   Formative Weight:  {formative_weight} (expected 60)")
    print(f"   Summative Weight:  {summative_weight} (expected 40)")

    if total_weight != 100 or formative_weight != 60 or summative_weight != 40:
        print("   ERROR: Weights do not meet the required distribution. Exiting.")
        sys.exit(1)
    else:
        print("   All weights are valid.")

    # c) Calculate Final Grade and GPA
    print("\n>> Grade Calculation:")
    formative_assignments = [a for a in data if a['group'] == 'Formative']
    summative_assignments = [a for a in data if a['group'] == 'Summative']

    # Weighted score for each group
    formative_score = sum((a['score'] * a['weight']) for a in formative_assignments)
    summative_score = sum((a['score'] * a['weight']) for a in summative_assignments)

    # Percentage in each group (out of their total group weight)
    formative_percentage = formative_score / formative_weight
    summative_percentage = summative_score / summative_weight

    # Overall final grade
    total_grade = (formative_score + summative_score) / 100
    gpa = (total_grade / 100) * 5.0

    print(f"   Formative Score:   {formative_percentage:.2f}%")
    print(f"   Summative Score:   {summative_percentage:.2f}%")
    print(f"   Final Grade:       {total_grade:.2f}%")
    print(f"   GPA:               {gpa:.2f} / 5.0")

    # d) Determine Pass/Fail (must score >= 50% in BOTH categories)
    print("\n>> Pass/Fail Status:")
    formative_passed = formative_percentage >= 50
    summative_passed = summative_percentage >= 50

    print(f"   Formative: {'PASSED' if formative_passed else 'FAILED'} ({formative_percentage:.2f}%)")
    print(f"   Summative: {'PASSED' if summative_passed else 'FAILED'} ({summative_percentage:.2f}%)")

    # e) Check for failed formative assignments and find highest weight for resubmission
    failed_formative = [a for a in formative_assignments if a['score'] < 50]

    resubmission_candidates = []
    if failed_formative:
        highest_weight = max(a['weight'] for a in failed_formative)
        resubmission_candidates = [a for a in failed_formative if a['weight'] == highest_weight]

    # f) Print final decision
    print("\n" + "=" * 50)
    if formative_passed and summative_passed:
        print("   FINAL STATUS: PASSED")
    else:
        print("   FINAL STATUS: FAILED")
        if not formative_passed:
            print("   Reason: Formative score is below 50%")
        if not summative_passed:
            print("   Reason: Summative score is below 50%")

    if resubmission_candidates:
        print("\n>> Resubmission Eligible Assignment(s):")
        for a in resubmission_candidates:
            print(f"   - {a['assignment']} (Score: {a['score']}%, Weight: {a['weight']})")
    else:
        print("\n>> No resubmission needed.")

    print("=" * 50)


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2. Process the features
    evaluate_grades(course_data)