
#!/bin/bash

# Check if archive directory exists, if not create it
if [ ! -d "archive" ]; then
    mkdir archive
    echo "Created archive directory."
fi

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# Define filenames
ORIGINAL="grades.csv"
ARCHIVED="grades_${TIMESTAMP}.csv"

# Check if grades.csv exists before archiving
if [ ! -f "$ORIGINAL" ]; then
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi

# Rename and move grades.csv to archive
mv "$ORIGINAL" "archive/$ARCHIVED"
echo "Moved '$ORIGINAL' to 'archive/$ARCHIVED'."

# Create a fresh empty grades.csv
touch "$ORIGINAL"
echo "Created new empty grades.csv."

# Log the operation
echo "[$TIMESTAMP] Archived: $ORIGINAL -> archive/$ARCHIVED" >> organizer.log
echo "Logged operation to organizer.log."

