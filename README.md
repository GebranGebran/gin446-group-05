# GIN446 – Chapter 9 lab – Server-side validation

```
python -m venv .venv
.venv\Scripts\activate            (Windows)      source .venv/bin/activate   (macOS / Linux)
pip install -r requirements.txt
flask --app app run --debug       -> http://127.0.0.1:5000/
python test_validators.py         -> runs the tests
```

| URL | What it is |
|---|---|
| /profile | old form, posts to /submit-profile (no server check) |
| /static/bypass.html | JavaScript page that posts invalid data with fetch() |
| /profile-validated | new form, checked by validators.py |
| /profile-validated?nocheck=1 | same form without the browser checks (tests the server alone) |

Deploy on Render: build command `pip install -r requirements.txt`, start command `gunicorn app:app`.
