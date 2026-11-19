// Optional comfort: check a few fields in the browser BEFORE sending.
// The rules MIRROR validators.py, but the server still checks everything.
const RULES = {
  student_id: { test: (v) => /^\d{9}$/.test(v), msg: "Student ID must be exactly 9 digits." },
  // TODO (at home, Part B): add email, phone, gpa and team_size with the SAME rules
  // and messages as validators.py (JavaScript regex syntax is almost identical).
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

form.noValidate = true;   // this script replaces the browser bubbles with the SAME messages as the server
const serverOnly = new URLSearchParams(location.search).has("nocheck");   // ?nocheck=1 tests the server alone

form.addEventListener("submit", (event) => {
  if (serverOnly) return;
  let firstBad = null;
  for (const [name, rule] of Object.entries(RULES)) {
    const input = form.elements[name];
    const ok = rule.test(input.value.trim());
    showError(input, ok ? "" : rule.msg);
    if (!ok && !firstBad) firstBad = input;
  }
  if (firstBad) { event.preventDefault(); firstBad.focus(); }   // stay on the page
});
