"""GIN446 – Chapter 9 lab: server-side validation of the Engineering Student Profile.

Run (inside the activated .venv):   flask --app app run --debug
Then open http://127.0.0.1:5000/
"""
from flask import Flask, render_template, request
from validators import validate_profile

app = Flask(__name__)

# labels shown in the form; the keys are the values the server accepts (see validators.py)
CHOICES = {
    "majors": {"computer": "Computer", "communication": "Communication", "electrical": "Electrical",
               "mechanical": "Mechanical", "civil": "Civil", "chemical": "Chemical"},
    "terms": {"spring": "Spring", "summer": "Summer", "fall": "Fall"},
    "skills": {"html": "HTML", "css": "CSS", "javascript": "JavaScript", "python": "Python", "git": "Git"},
    "software": {"vscode": "VS Code", "github": "GitHub", "figma": "Figma", "matlab": "MATLAB", "autocad": "AutoCAD"},
}


@app.route("/")
def home():
    weekly_work = [
        {"week": 4, "title": "Engineering Student Profile (HTML form)", "done": True},
        {"week": 7, "title": "Live Quiz with fetch()", "done": True},
        {"week": 8, "title": "Server-side validation (this lab)", "done": False},
    ]
    return render_template("index.html", weekly_work=weekly_work)


# ---------- the OLD version: no validation at all ----------
@app.route("/profile")
def profile_form():
    return render_template("profile-form.html", **CHOICES)


@app.route("/submit-profile", methods=["POST"])
def submit_profile():
    data = request.form.to_dict()
    data["skills"] = request.form.getlist("skills")
    data["software"] = request.form.getlist("software")
    return render_template("profile.html", data=data, validated=False)


# ---------- the NEW version: validated on the server ----------
@app.route("/profile-validated", methods=["GET", "POST"])
def profile_validated():
    if request.method == "GET":
        return render_template("profile-form-validated.html", errors={}, values={}, **CHOICES)

    # Task 3: validate on the server – the browser checks can always be skipped
    # 1. validate_profile() returns a tuple -> unpack it into two dicts
    errors, cleaned = validate_profile(request.form)

    # 2. at least one error (a non-empty dict is truthy): send back the SAME form,
    #    with the messages and the cleaned values, and the status code 400 Bad Request
    if errors:
        return render_template("profile-form-validated.html",
                               errors=errors, values=cleaned, **CHOICES), 400

    # 3. no error: show the profile with the "validated" badge (200 OK)
    return render_template("profile.html", data=cleaned, validated=True)

if __name__ == "__main__":
    app.run(debug=True)
