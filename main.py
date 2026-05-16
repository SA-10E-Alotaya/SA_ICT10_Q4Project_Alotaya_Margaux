import os
from flask import Flask, send_from_directory, Response

app = Flask(__name__, static_folder=None)
BASE_DIR = os.path.dirname(__file__)

# ===== ATTENDANCE PYSCRIPT =====
ATTENDANCE_SCRIPT = """from pyscript import document, display
import numpy as np

# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
days = []
absences = []


def displaying(e):
    day = document.getElementById('dayOfTheWeek').value
    absence = int(document.getElementById('absences').value)

    # Save data
    days.append(day)
    absences.append(absence)

    # Convert to NumPy array
    converted_absences = np.array(absences)

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    # Display plot
    plt.show()
"""

# ===== CLASSMATES PYSCRIPT =====
CLASSMATES_SCRIPT = """# SW2 4th Quarter
from pyscript import document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

classmate_list = [
    Classmate("Margaux", "Emerald", "Art"),
    Classmate("Alwit", "Emerald", "Science"),
    Classmate("Shean", "Emerald", "English"),
    Classmate("Benjamin", "Emerald", "History"),
    Classmate("Kaitlin", "Emerald", "Art"),
    Classmate("Samuel", "Emerald", "Computer Programming"),
    Classmate("CJ", "Emerald", "Science"),
    Classmate("Matt", "Emerald", "English"),
    Classmate("Rochel", "Emerald", "History"),
    Classmate("Toni", "Emerald", "Art"),
    Classmate("Travis", "Emerald", "Computer Programming"),
    Classmate("Joshua", "Emerald", "Science"),
    Classmate("Reese", "Emerald", "English"),
    Classmate("Alyza", "Emerald", "History"),
    Classmate("Zaia", "Emerald", "Art"),
    Classmate("Janinna", "Emerald", "Computer Programming"),
    Classmate("Leona", "Emerald", "Science"),
    Classmate("Aion", "Emerald", "English"),
    Classmate("Cen", "Emerald", "History"),
    Classmate("Kushdeep", "Emerald", "Art"),
    Classmate("Ekam", "Emerald", "Computer Programming"),
    Classmate("Eris", "Emerald", "Science"),
    Classmate("Hanna", "Emerald", "English"),
    Classmate("Lesvie", "Emerald", "History"),
    Classmate("Sophia", "Emerald", "Art"),
    Classmate("Simrat", "Emerald", "Computer Programming"),
    Classmate("Lucillind", "Emerald", "Science"),
    Classmate("Opdesh", "Emerald", "English"),
    Classmate("Wilwen", "Emerald", "History"),
    Classmate("Lewis", "Emerald", "Art"),
    Classmate("Padme", "Emerald", "Art"),
]

name_input = document.getElementById("name-input")
section_input = document.getElementById("section-input")
subject_input = document.getElementById("subject-input")
message = document.getElementById("message")
list_container = document.getElementById("classmate-list")
list_wrapper = document.getElementById("classmate-list-wrapper")
show_button = document.getElementById("show-button")


def render_list(event=None):
    list_container.innerHTML = ''
    if not classmate_list:
        list_container.innerHTML = '<p class="text-muted">No classmates added yet.</p>'
        return

    for student in classmate_list:
        list_container.innerHTML += f'<p class="mb-2">{student.introduce()}</p>'


def toggle_list(event=None):
    if list_wrapper.style.display == 'none' or list_wrapper.style.display == '':
        render_list()
        list_wrapper.style.display = 'block'
        show_button.innerText = 'Hide List'
    else:
        list_wrapper.style.display = 'none'
        show_button.innerText = 'Show List'


def add_classmate(event=None):
    name = str(name_input.value).strip()
    section = str(section_input.value).strip()
    subject = str(subject_input.value).strip()

    if not name or not section or not subject:
        message.innerHTML = '<span class="text-danger">Please fill in all fields before adding.</span>'
        return

    classmate_list.append(Classmate(name, section, subject))
    name_input.value = ''
    section_input.value = ''
    subject_input.value = ''
    message.innerHTML = '<span class="text-success">Classmate added successfully!</span>'

    if list_wrapper.style.display != 'none' and list_wrapper.style.display != '':
        render_list()

render_list()
"""

# ===== FLASK ROUTES =====
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/attendance')
@app.route('/attendance/')
@app.route('/attendance.html')
def attendance():
    return send_from_directory(BASE_DIR, 'attendance.html')

@app.route('/api/attendance-script')
def attendance_script():
    return Response(ATTENDANCE_SCRIPT, mimetype='text/plain')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/classmates')
@app.route('/classmates/')
@app.route('/Classmates.html')
def classmates():
    return send_from_directory(BASE_DIR, 'Classmates.html')

@app.route('/api/classmates-script')
def classmates_script():
    return Response(CLASSMATES_SCRIPT, mimetype='text/plain')

@app.route('/index.html')
def index_html():
    return send_from_directory(BASE_DIR, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
