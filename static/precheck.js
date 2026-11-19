// Optional comfort: check a few fields in the browser BEFORE sending.
// The rules MIRROR validators.py (same regex, same limits, same messages),
// but the server still checks everything – this file can be switched off by anyone.
const RULES = {
  student_id: { test: (v) => /^\d{9}$/.test(v), msg: "Student ID must be exactly 9 digits." },
  email: {
    test: (v) => /^[a-z0-9._%+-]+@usek\.edu\.lb$/.test(v.toLowerCase()),
    msg: "Use your university e-mail (…@usek.edu.lb).",
  },
  phone: {   // optional: empty is fine
    test: (v) => v === "" || /^\+961 ?\d{1,2} ?\d{3} ?\d{3}$/.test(v),
    msg: "Phone must be a Lebanese number, e.g. +961 3 123 456.",
  },
  gpa: {
    test: (v) => v !== "" && !isNaN(Number(v)) && Number(v) >= 40 && Number(v) <= 100,
    msg: "GPA must be a number between 40 and 100.",
  },
  team_size: {
    test: (v) => /^[+-]?\d+$/.test(v) && Number(v) >= 1 && Number(v) <= 4,   // like int() in Python
    msg: "Team size must be 1, 2, 3 or 4.",
  },
};

const form = document.querySelector("form.profile");

function showError(input, message) {
  const label = input.closest("label");
  let span = label.querySelector(".error");
  if (!span) { span = document.createElement("span"); span.className = "error"; label.append(span); }
  span.textContent = message;
  label.classList.toggle("invalid", message !== "");
  if (message === "") span.remove();
}

function check(name) {
  const input = form.elements[name];
  const ok = RULES[name].test(input.value.trim());
  showError(input, ok ? "" : RULES[name].msg);
  return ok;
}

form.noValidate = true;   // this script replaces the browser bubbles with the SAME messages as the server
const serverOnly = new URLSearchParams(location.search).has("nocheck");   // ?nocheck=1 tests the server alone

form.addEventListener("submit", (event) => {
  if (serverOnly) return;
  let firstBad = null;
  for (const name of Object.keys(RULES)) {
    if (!check(name) && !firstBad) firstBad = form.elements[name];
  }
  if (firstBad) { event.preventDefault(); firstBad.focus(); }   // stay on the page, nothing is sent
});

// Bonus B+3 – live check: once a field has been left (blur), re-check it on every keystroke
if (!serverOnly) {
  for (const name of Object.keys(RULES)) {
    const input = form.elements[name];
    input.addEventListener("blur", () => { input.dataset.touched = "1"; check(name); });
    input.addEventListener("input", () => { if (input.dataset.touched) check(name); });
  }
}

// Bonus B+2 – ask the server too (POST /api/validate), without leaving the page
const askBtn = document.querySelector("#ask-server");
if (askBtn) {
  askBtn.addEventListener("click", async () => {
    const out = document.querySelector("#api-result");
    try {
      const response = await fetch("/api/validate", { method: "POST", body: new FormData(form) });
      const errors = await response.json();
      const count = Object.keys(errors).length;
      out.textContent = response.ok ? "Server says: everything is valid (200)."
                                    : `Server says: ${count} problem(s) (${response.status}).`;
      out.className = response.ok ? "ok" : "error";
    } catch (error) {
      out.textContent = "Network error: " + error.message;
    }
  });
}
