from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# Mock Database (In-Memory Dictionary)
certificates_db = {
    "CERT101": {
        "student_name": "Alok Kumar",
        "course": "Computer Science & Engineering",
        "issue_date": "2026-05-15",
        "status": "Valid",
        "grade": "A+"
    },
    "CERT102": {
        "student_name": "Kamlesh Kumar",
        "course": "Data Structures & Algorithms",
        "issue_date": "2026-04-10",
        "status": "Valid",
        "grade": "A"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    cert_id = request.form.get('cert_id', '').strip().upper()
    cert_data = certificates_db.get(cert_id)
    return render_template('verify.html', cert_id=cert_id, cert_data=cert_data)

if __name__ == '__main__':
    app.run(debug=True)
  
