"""Tests for validators.py – run:  python test_validators.py   (or: pytest)"""
from datetime import date
from werkzeug.datastructures import MultiDict      # installed with Flask: same type as request.form
from validators import validate_profile

TODAY = date(2026, 11, 16)                         # fixed day, so the age tests never change

VALID = {
    "student_id": "202312345", "fullname": "Lea  Haddad", "email": "Lea.Haddad@usek.edu.lb",
    "phone": "+961 3 123 456", "birthdate": "2005-04-20", "major": "computer", "gpa": "86.5",
    "credits": "96", "graduation": "spring", "skills": ["html", "python"], "software": ["vscode"],
    "project_title": "Smart Campus Map", "description": "A web map of the campus.",
    "team_size": "3", "project_color": "#336699", "meeting_time": "14:30", "confirmation": "yes",
}


def form(**changes):
    """VALID data with some fields changed (None removes the field)."""
    data = {**VALID, **changes}
    pairs = []
    for key, value in data.items():
        if value is None:
            continue
        for v in (value if isinstance(value, list) else [value]):
            pairs.append((key, v))
    return MultiDict(pairs)


def errors_of(**changes):
    return validate_profile(form(**changes), today=TODAY)[0]


# ---------- in class ----------
def test_valid_form_has_no_error():
    errors, cleaned = validate_profile(form(), today=TODAY)
    assert errors == {}
    assert cleaned["email"] == "lea.haddad@usek.edu.lb"     # lower case
    assert cleaned["fullname"] == "Lea Haddad"              # inner spaces collapsed
    assert cleaned["gpa"] == 86.5


def test_required_fields():
    for name in ["student_id", "fullname", "email", "major", "gpa"]:
        assert name in errors_of(**{name: "   "}), name


def test_student_id():
    assert "student_id" in errors_of(student_id="hello")
    assert "student_id" in errors_of(student_id="12345")
    assert "student_id" not in errors_of(student_id=" 202312345 ")


def test_fullname():
    assert "fullname" in errors_of(fullname="<script>alert(1)</script>")
    assert "fullname" in errors_of(fullname="Al")
    assert "fullname" not in errors_of(fullname="Jean-Marc O'Neil")


def test_email():
    assert "email" in errors_of(email="not-an-email")
    assert "email" in errors_of(email="lea@gmail.com")
    assert "email" not in errors_of(email="LEA@USEK.EDU.LB")


def test_major_allow_list():
    assert "major" in errors_of(major="Hacking")


def test_gpa():
    for bad in ["999", "39.9", "abc"]:
        assert "gpa" in errors_of(gpa=bad), bad
    for good in ["40", "100", "75.25"]:
        assert "gpa" not in errors_of(gpa=good), good


# ---------- at home (groups) ----------
def test_phone():
    assert "phone" in errors_of(phone="70123456")
    assert "phone" not in errors_of(phone="")               # optional
    assert "phone" not in errors_of(phone="+96171123456")


def test_birthdate():
    assert "birthdate" in errors_of(birthdate="2030-01-01")   # future
    assert "birthdate" in errors_of(birthdate="2020-01-01")   # age 6
    assert "birthdate" in errors_of(birthdate="2005-02-30")   # not a real day
    assert "birthdate" not in errors_of(birthdate="")


def test_credits_and_team_size():
    assert validate_profile(form(), today=TODAY)[1]["credits"] == 96          # stored as int
    for bad in ["149", "-1", "12.5", "abc"]:
        assert "credits" in errors_of(credits=bad), bad
    for bad in ["0", "5", "two"]:
        assert "team_size" in errors_of(team_size=bad), bad


def test_graduation_skills_software():
    assert "graduation" in errors_of(graduation="winter")
    assert "skills" in errors_of(skills=["html", "hacking"])
    assert "software" in errors_of(software=["photoshop"])
    assert "skills" not in errors_of(skills=None)            # no checkbox ticked is allowed


def test_lengths():
    assert "project_title" in errors_of(project_title="x" * 121)
    assert "description" in errors_of(description="x" * 1001)


def test_color_and_meeting_time():
    assert "project_color" in errors_of(project_color="red")
    assert validate_profile(form(project_color=""), today=TODAY)[1]["project_color"] == "#336699"
    for bad in ["07:59", "18:01", "12:75", "noon"]:
        assert "meeting_time" in errors_of(meeting_time=bad), bad


def test_confirmation():
    assert "confirmation" in errors_of(confirmation=None)


if __name__ == "__main__":
    tests = [(n, f) for n, f in globals().items() if n.startswith("test_")]
    failed = 0
    for name, test in tests:
        try:
            test()
            print(f"PASS  {name}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {name}  {e}")
        except Exception as e:                       # a crash is also a failure
            failed += 1
            print(f"ERROR {name}  {type(e).__name__}: {e}")
    print(f"\n{len(tests) - failed} of {len(tests)} tests passed")
