from celery import shared_task ,Celery
from datetime import datetime, timedelta
from backend.model import *
from flask import current_app as app
from backend.mail_service import send_email


@shared_task(ignore_results=False)
def add(x,y):
    return(x+y)


@shared_task(ignore_result=False)
def send_course_content_notification(course_id):
    """
    Sends an email notification to students when new content is added to a course.
    """
    with app.app_context():
        course = Course.query.get(course_id)
        if not course:
            return "Course not found."

        students = User.query.join(CourseOpted, CourseOpted.user_id == User.id)
        students = students.filter(CourseOpted.course_id == course_id).all()
        
        recipients = [student.email for student in students if student.email not in {"student@app.com", "instructor@app.com"}]

        subject = f"🎉 New Content Added to {course.course_name}!"

        content = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                    text-align: center;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                }}
                h2 {{
                    color: #333;
                }}
                p {{
                    color: #555;
                    font-size: 16px;
                }}
                .cta-button {{
                    display: inline-block;
                    padding: 12px 24px;
                    margin-top: 20px;
                    font-size: 16px;
                    color: #fff;
                    background-color: #007bff;
                    text-decoration: none;
                    border-radius: 5px;
                }}
                .footer {{
                    margin-top: 20px;
                    font-size: 12px;
                    color: #888;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>📚 New Content Available!</h2>
                <p>Hello,</p>
                <p>We have added new content to your course: <b>{course.course_name}</b>.</p>
                <p>Click the button below to explore the latest updates:</p>
                <p>View Course Page<p>
                <p>Please check the platform for details.</p>
#             <p>Best regards,<br>Course Management Team</p>
            </div>
        </body>
        </html>
        """

        send_email(subject, recipients, content)



@shared_task(ignore_result=False)
def send_assignment_notification(course_id, assignment_id):
    """
    Sends an email notification to students when a new assignment is posted.
    """
    with app.app_context():
        course = Course.query.get(course_id)
        assignment = Assignment.query.get(assignment_id)
        if not course or not assignment:
            return "Course or assignment not found."
        
        students = User.query.join(CourseOpted, CourseOpted.user_id == User.id)
        students = students.filter(CourseOpted.course_id == course_id).all()

        recipients = [student.email for student in students if student.email not in {"student@app.com", "instructor@app.com"}]

        if not recipients:
            return "No valid recipient emails found."

        subject = f"New Assignment for {course.course_name}"
        content = f"""
        <html>
        <body>
            <p>Hello,</p>
            <p>A new assignment has been posted for <b>{course.course_name}</b>.</p>
            <p><b>Questions:</b> {assignment.title}</p>
            <p><b>Deadline:</b> {assignment.due_date.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Submit before the deadline.</p>
            <p>Best regards,<br>Course Management Team</p>
        </body>
        </html>
        """

        send_email(subject, recipients, content)


@shared_task(ignore_result=False)
def send_assignment_deadline_reminder():
    """
    Sends an email reminder to students if their assignment is due today.
    """
    with app.app_context():
        now = datetime.utcnow()  
        today_start = datetime(now.year, now.month, now.day, 0, 0, 0)  # 00:00:00 UTC
        today_end = datetime(now.year, now.month, now.day, 23, 59, 59)  # 23:59:59 UTC

        print(f"Checking assignments between {today_start} and {today_end}")

        # Retrieve assignments due today (between today_start and today_end)
        assignments_due = Assignment.query.filter(
            Assignment.due_date >= today_start,
            Assignment.due_date <= today_end
        ).all()

        print(f"Now (UTC): {now}, Today's Date: {now.date()}")
        print(f"Assignments Due Count: {len(assignments_due)}")

        if not assignments_due:
            return "No assignments due today."

        for assignment in assignments_due:
            print(f"Assignment ID: {assignment.id}, Due Date: {assignment.due_date}")

            students = User.query.join(CourseOpted, CourseOpted.user_id == User.id)\
                                 .filter(CourseOpted.course_id == assignment.course_id)\
                                 .all()

            if not students:
                print(f"No students found for Assignment ID: {assignment.id}")
                continue  

            recipients = [student.email for student in students if student.email not in {"student@app.com", "instructor@app.com"}]

            print(f"Sending email to: {recipients}")

            subject = f"Reminder: Assignment Deadline for {assignment.course.course_name}"
            content = f"""
            <html>
            <body>
                <p>Hello,</p>
                <p>A new assignment has been posted for <b>{assignment.course.course_name}</b>.</p>
                <p><b>Questions:</b> {assignment.title}</p>
                <p><b>Deadline:</b> {assignment.due_date.strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p>Submit before the deadline.</p>
                <p>Best regards,<br>Course Management Team</p>
            </body>
            </html>
            """
                   
            send_email(subject, recipients, content)

        return f"Sent reminders for {len(assignments_due)} assignments due today."

