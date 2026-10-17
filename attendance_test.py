
# AttendX Attendance Test
# Sample test case for a student attendance application

def test_attendance_marking():
    student_id = "STU001"
    attendance_status = "Present"

    # Check that student ID and status are provided
    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("PASS: Student ID and attendance status are valid")


test_attendance_marking()
