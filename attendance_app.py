from flask import Flask, render_template, request, jsonify
import pandas as pd
from datetime import datetime
import os

app = Flask(__name__)

# Path to your attendance spreadsheet
ATTENDANCE_FILE = 'attendance.xlsx'

@app.route('/')
def index():
    """Display the attendance form"""
    return render_template('attendance_form.html')

@app.route('/record', methods=['POST'])
def record_attendance():
    """Record attendance when form is submitted"""
    try:
        # Get student information from form
        student_id = request.form.get('student_id')
        student_name = request.form.get('student_name')
        
        if not student_id or not student_name:
            return jsonify({'status': 'error', 'message': 'Please provide both ID and name'})
        
        # Get current date and time
        scan_date = datetime.now().strftime("%Y-%m-%d")
        scan_time = datetime.now().strftime("%H:%M:%S")
        scan_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create new attendance record
        new_record = {
            'Student_ID': student_id,
            'Student_Name': student_name,
            'Date': scan_date,
            'Time': scan_time,
            'DateTime': scan_datetime
        }
        
        # Check if spreadsheet exists
        if os.path.exists(ATTENDANCE_FILE):
            df = pd.read_excel(ATTENDANCE_FILE)
            df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        else:
            df = pd.DataFrame([new_record])
        
        # Save to Excel
        df.to_excel(ATTENDANCE_FILE, index=False)
        
        return jsonify({
            'status': 'success', 
            'message': f'Attendance recorded for {student_name} at {scan_time}'
        })
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)