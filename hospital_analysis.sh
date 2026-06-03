#!/bin/bash

# hospital_analysis.sh
# Member 5 - Clinical Analyst: process_vitals()
# Member 6 - Facility Auditor: water_audit() (to be added by Member 6)

process_vitals() {
    echo "============================================"
    echo "   KNH Clinical Vitals Analysis"
    echo "   Running at: $(date)"
    echo "============================================"

    HEART_RATE_LOG="active_logs/heart_rate.log"
    TEMPERATURE_LOG="active_logs/temperature.log"
    OUTPUT_FILE="reports/critical_alerts.txt"

    # Check reports directory exists
    if [ ! -d "reports" ]; then
        echo "[ERROR] reports/ directory not found. Run hospital_admin.sh first."
        return 1
    fi

    # Check log files exist
    if [ ! -f "$HEART_RATE_LOG" ] && [ ! -f "$TEMPERATURE_LOG" ]; then
        echo "[ERROR] No log files found in active_logs/. Is the engine running?"
        return 1
    fi

    # Create fresh output file with header
    {
        echo "============================================"
        echo " KNH CRITICAL ALERTS REPORT"
        echo " Generated: $(date)"
        echo "============================================"
        echo ""
    } > "$OUTPUT_FILE"

    # Scan Heart Rate log
    echo "[INFO] Scanning Heart Rate log for CRITICAL events..."
    if [ -f "$HEART_RATE_LOG" ]; then
        HR_COUNT=$(grep -c "CRITICAL" "$HEART_RATE_LOG" 2>/dev/null || echo 0)
        echo "[INFO] Found $HR_COUNT CRITICAL heart rate record(s)."
        {
            echo "--- HEART RATE CRITICAL ALERTS ---"
            grep "CRITICAL" "$HEART_RATE_LOG" | \
                awk -F',' '{printf "Timestamp: %-25s | Device: %-20s | Value: %s\n", $1, $2, $3}'
            echo ""
        } >> "$OUTPUT_FILE"
    else
        echo "[WARNING] Heart rate log not found."
    fi

    # Scan Temperature log
    echo "[INFO] Scanning Temperature log for CRITICAL events..."
    if [ -f "$TEMPERATURE_LOG" ]; then
        TEMP_COUNT=$(grep -c "CRITICAL" "$TEMPERATURE_LOG" 2>/dev/null || echo 0)
        echo "[INFO] Found $TEMP_COUNT CRITICAL temperature record(s)."
        {
            echo "--- TEMPERATURE CRITICAL ALERTS ---"
            grep "CRITICAL" "$TEMPERATURE_LOG" | \
                awk -F',' '{printf "Timestamp: %-25s | Device: %-20s | Value: %s\n", $1, $2, $3}'
            echo ""
        } >> "$OUTPUT_FILE"
    else
        echo "[WARNING] Temperature log not found."
    fi

    # Footer
    {
        echo "============================================"
        echo " SUMMARY: Critical alerts saved to $OUTPUT_FILE"
        echo "============================================"
    } >> "$OUTPUT_FILE"

    echo ""
    echo "[SUCCESS] Critical alerts saved to $OUTPUT_FILE"
    echo "============================================"
}

# Call the function
process_vitals
