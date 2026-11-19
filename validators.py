"""Server-side validation of the Engineering Student Profile form (GIN446 – Chapter 9 lab).

validate_profile(form) receives request.form and returns (errors, cleaned):
  errors  – dict  {field_name: "message"}   (empty dict = the form is valid)
  cleaned – dict  {field_name: clean value} (stripped, converted, normalised)
"""
import re
from datetime import date, datetime

# ---------- 1. Patterns (regular expressions) ----------
STUDENT_ID_RE = re.compile(r"^\d{9}$")                          # exactly 9 digits
NAME_RE = re.compile(r"^[A-Za-zÀ-ÿ' -]{3,60}$")                 # letters, space, ' and -
EMAIL_RE = re.compile(r"^[a-z0-9._%+-]+@usek\.edu\.lb$")         # university e-mail only
PHONE_RE = re.compile(r"^\+961 ?\d{1,2} ?\d{3} ?\d{3}$")         # +961 3 123 456 / +96171123456
COLOR_RE = re.compile(r"^#[0-9a-fA-F]{6}$")                      # #336699
TIME_RE = re.compile(r"^\d{2}:\d{2}$")                           # 14:30

# ---------- 2. Allow-lists ----------
MAJORS = {"computer", "communication", "electrical", "mechanical", "civil", "chemical"}
GRADUATION_TERMS = {"spring", "summer", "fall"}
SKILLS = {"html", "css", "javascript", "python", "git"}
SOFTWARE = {"vscode", "github", "figma", "matlab", "autocad"}

REQUIRED = ["student_id", "fullname", "email", "major", "gpa", "credits",
            "graduation", "project_title", "team_size", "confirmation"]

MAX_TITLE = 120
MAX_DESCRIPTION = 1000


# ---------- 3. Helpers ----------
def to_number(text):
    """'85.5' -> 85.5 ; 'abc' or '' -> None"""
    try:
        return float(text)
    except (TypeError, ValueError):
        return None


def to_int(text):
    """'12' -> 12 ; '12.5', 'abc' or '' -> None"""
    try:
        return int(text)
    except (TypeError, ValueError):
        return None


def parse_date(text):
    """'2004-05-17' -> date(2004, 5, 17) ; anything else -> None"""
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def age_on(birth, today):
    """Age in full years on the given day."""
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


# ---------- 4. The validator ----------
def validate_profile(form, today=None):
    today = today or date.today()
    errors, cleaned = {}, {}

    def text(name):
        return (form.get(name) or "").strip()

    # 4.1 required fields
    for name in REQUIRED:
        if not text(name):
            errors[name] = "This field is required."

    # 4.2 student ID  (done for you as an example)
    student_id = text("student_id")
    if student_id and not STUDENT_ID_RE.match(student_id):
        errors["student_id"] = "Student ID must be exactly 9 digits."
    cleaned["student_id"] = student_id

    # ===== IN CLASS (Task 4) =====
    # 4.3 full name: collapse the inner spaces ("Lea  Haddad" -> "Lea Haddad"), then format check
    fullname = " ".join(text("fullname").split())
    if fullname and not NAME_RE.match(fullname):
        errors["fullname"] = "Name: 3 to 60 letters, spaces, ' or - only."
    cleaned["fullname"] = fullname

    # 4.4 e-mail: normalise to lower case, then format check (university domain only)
    email = text("email").lower()
    if email and not EMAIL_RE.match(email):
        errors["email"] = "Use your university e-mail (…@usek.edu.lb)."
    cleaned["email"] = email

    # 4.7 major: allow-list – only the values we offer in the <select> are accepted
    major = text("major")
    if major and major not in MAJORS:
        errors["major"] = "Choose a major from the list."
    cleaned["major"] = major

    # 4.8 GPA: convert to a number (None if not a number), then range check 40..100
    gpa_text = text("gpa")
    gpa = to_number(gpa_text)
    if gpa_text and (gpa is None or not 40 <= gpa <= 100):
        errors["gpa"] = "GPA must be a number between 40 and 100."
    cleaned["gpa"] = gpa if gpa is not None else gpa_text   # float when valid, raw text to refill otherwise

    # ===== AT HOME (groups) – see the lab guide, Part B =====
    # TODO 4.5  phone (optional)        PHONE_RE
    # TODO 4.6  birthdate (optional)    parse_date(), not in the future, age_on() between 15 and 100
    # TODO 4.9  credits                 to_int(), 0 to 148
    # TODO 4.10 graduation              in GRADUATION_TERMS
    # TODO 4.11 skills / software       form.getlist(name); every value in SKILLS / SOFTWARE
    # TODO 4.12 project_title <= MAX_TITLE characters, description <= MAX_DESCRIPTION
    # TODO 4.13 team_size               to_int(), 1 to 4
    # TODO 4.14 project_color           default "#336699", COLOR_RE, store in lower case
    # TODO 4.15 meeting_time (optional) TIME_RE, minutes < 60, between "08:00" and "18:00"
    # TODO 4.16 confirmation            cleaned["confirmation"] = (text("confirmation") == "yes")

    # keep the raw text of any field not cleaned above, so the form can be refilled
    for name in form:
        if name not in cleaned:
            cleaned[name] = form.getlist(name) if name in ("skills", "software") else text(name)

    return errors, cleaned
