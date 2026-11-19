// Bypass test: send invalid data directly to the server (Chapter 8: fetch, async/await)
const JUNK = {
  student_id: "hello",
  fullname: "<b>Hacker</b>",
  email: "not-an-email",
  major: "Hacking",
  gpa: "999",
  credits: "-5",
  graduation: "winter",
  skills: ["html", "lock-picking"],
  project_title: "x".repeat(150),
  team_size: "40",
  project_color: "red",
  meeting_time: "03:00",
  confirmation: "yes",
};

function buildFormData(data) {
  const fd = new FormData();
  for (const [key, value] of Object.entries(data)) {
    if (Array.isArray(value)) value.forEach((v) => fd.append(key, v));   // same name several times = checkboxes
    else fd.append(key, value);
  }
  return fd;
}

async function send(url) {
  const status = document.querySelector("#status");
  status.textContent = "sending…";
  try {
    const response = await fetch(url, { method: "POST", body: buildFormData(JUNK) });
    status.textContent = `${response.status} ${response.statusText || ""} – ${url}`;
    status.className = "status s" + response.status;
    document.querySelector("#page").srcdoc = await response.text();   // show the HTML the server returned
  } catch (error) {
    status.textContent = "Network error: " + error.message + " (is Flask running?)";
  }
}

document.querySelector("#sent").textContent = JSON.stringify(JUNK, null, 2);
document.querySelector("#old").addEventListener("click", () => send("/submit-profile"));
document.querySelector("#new").addEventListener("click", () => send("/profile-validated"));
