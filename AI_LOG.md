# AI Development Log

Group 05 — GIN446 Web Programming. Each entry says which member used AI.
All AI output was reviewed, tested in the browser, and accepted, modified or rejected by the member named.

---

## Interaction 1 (Gebran)

Task:
Build the project homepage for the Grid lab: header, Flexbox navigation, six cards in a 3-column CSS Grid with gap, footer, and basic readable styling.

AI tool:
Claude (Anthropic), in the Claude chat app.

My prompt:
TODO-GEBRAN: paste the exact prompt you used.

AI recommendation:
Use display: flex on nav; display: grid on .cards with grid-template-columns: repeat(3, 1fr) and gap instead of margins; add padding, borders and colors on .card for readability.

My decision:
ACCEPT

Why:
TODO-GEBRAN: technical reason.

Verification:
TODO-GEBRAN: how you tested it (e.g. Live Server, six cards visible in three equal columns).

What I learned:
TODO-GEBRAN: 2–4 sentences in your own words.

---

## Interaction 2 (Gebran)

Task:
Make the card grid responsive: 3 columns on desktop, 2 on tablet, 1 on mobile, with no horizontal scrolling.

AI tool:
Claude (Anthropic), in the Claude chat app.

My prompt:
TODO-GEBRAN: paste the exact prompt you used.

AI recommendation:
Add two media queries: at max-width 1023px set grid-template-columns: repeat(2, 1fr), and at max-width 599px set it to 1fr; let the nav wrap on small screens. Later, I also asked for better page styling and Claude gave a fuller stylesheet with the same breakpoints.

My decision:
ACCEPT

Why:
TODO-GEBRAN: technical reason.

Verification:
TODO-GEBRAN: how you tested it (e.g. DevTools at about 1440, 768 and 375 px).

What I learned:
TODO-GEBRAN: 2–4 sentences in your own words.

---

## Interaction 3 (Joe) — Homework 9.2: AI debugging challenge

Task:
Explain why `grid-template-columns: 300px 300px 300px; gap: 30px; width: 100%;` overflows on a 375 px screen, and choose a correction I understand.

AI tool:
Claude (Anthropic), Claude app.

My prompt:
"Here is my prediction for this CSS on a 375px screen: when we say 375px is for the phone width so the template will be compatible with the phone. Explain why horizontal overflow may occur, and suggest possible corrections with an explanation for each. Do not rewrite my whole stylesheet."

AI recommendation:
My prediction was wrong. The columns are fixed: 3 × 300 px + 2 × 30 px = 960 px, so on a 375 px screen about 585 px overflows and the page scrolls sideways; `width: 100%` only sizes the container, not its fixed columns. Suggested corrections: (1) flexible `repeat(3, 1fr)` columns with media queries for 2 and 1 columns; (2) `repeat(auto-fit, minmax(250px, 1fr))` without media queries; (3) smaller fixed columns (not recommended).

My decision:
ACCEPT correction 1.

Why:
It uses flexible columns and media queries. `1fr` means "one share of the free space", so the columns divide whatever width exists instead of demanding 300 px each, and it gives exactly the required 3/2/1 columns. Correction 3 is rejected because fixed pixel columns still cannot adapt.

Verification:
In DevTools at 375 px on `lab-grid/index.html`, the `@media (max-width: 599px)` rule applies `grid-template-columns: 1fr`: one card per row and no horizontal scrollbar. Also checked 768 px (2 columns) and desktop (3 columns).

What I learned:
I learned that I should always pay attention to details and think what the end user might use as a device and what screen type is using (phone, desktop, etc.), because the front end of any website is necessary for the user to feel free while using it; it should be simple and user friendly on any device.
: My prediction was wrong because I didn’t add up the fixed widths: 3 × 300px + 2 × 30px = 960px, which is much wider than a 375px phone, so the cards overflow and the page scrolls sideways.

---

## Interaction 4 (Joe) — Homework 9.3: Flexbox or Grid?

Task:
Decide Flexbox or Grid for three scenarios, then compare with an AI recommendation.

AI tool:
Claude (Anthropic), Claude app.

My prompt:
"for navigation menu my choice is grid because users when they are navigating a menu they don't need to scroll to see the search they need they see them in blocks in many dimensions. 12 card product gallery is better in flexbox, becuase the users will be scrolling so it is easy to see product after product. login is better with flexbox, they are in order under each other." (Sent after the AI was asked to give its recommendation for each scenario.)

AI recommendation:

| Scenario | My choice first | AI recommendation | Final decision + reason |
|---|---|---|---|
| Navigation menu | Grid | Flexbox: a menu is one row of links (one dimension); flex sizes each link to its text and wraps | ACCEPT: my first thought was Flexbox; after imagining the layout, a single row of links is one-dimensional, which is what Flexbox is for. Our homepage uses `.nav-list { display: flex; }`. |
| 12-card product gallery | Flexbox | Grid: rows and columns (two dimensions) line up and share row heights; flex rows are independent | ACCEPT (changed from my first choice): the course recommends Grid for card collections, and I saw why on our Flexbox homepage: at 768 px the wrapped card stretched across a whole row, while the Grid lab kept every card in equal, aligned columns. |
| Login form | Flexbox | Flexbox column is fine for stacked fields; Grid if labels sit beside inputs | ACCEPT: the fields are stacked one under another, so `flex-direction: column` with `gap` is enough. |

My decision:
See the table above (ACCEPT / ACCEPT / ACCEPT).

Why:
See the "Final decision + reason" column.

Verification:
Compared with our own code: the homepage navigation (`.nav-list`) uses Flexbox, and the six-card lab area uses Grid. On the Flexbox homepage at 768 px, the wrapped third card stretched across the whole second row, while the Grid lab kept equal columns.

What I learned:
I learned that Flexbox is better when items are in one row, like a menu, and Grid is better when items must line up in rows and columns, like a card gallery.

---

## Interaction 5 (Joe) — Homework 9.4: AI bad-advice critique

Task:
Explain why positioning cards with `margin-left: 10px / 320px / 630px` can look correct on one screen but is a poor responsive solution, and compare with the AI's answer.

AI tool:
Claude (Anthropic), Claude app.

My prompt:
"it is good for laptop but for a phone device a 630 px is bad becuase the phone is 375px, based on the x px that i gave it"

AI recommendation:
My reasoning is correct. Additional reasons: `.card3` starts 255 px past the right edge of a 375 px phone, causing horizontal overflow; the margins only work at the one width they were measured for and break with a different width, font size or zoom; a fourth card needs another hand-calculated margin. Fix: let the container place the items with `display: grid; grid-template-columns: repeat(3, 1fr); gap` (or flex-wrap with gap).

My decision:
ACCEPT

Why:
Fixed pixel offsets are calculated for one screen size, so they cannot adapt. A grid or flex container lets the browser compute the positions at every width, and `gap` replaces the individual margins.

Verification:
Our Grid lab uses `repeat(3, 1fr)` with `gap` and media queries; checked at 375, 768 and desktop widths with no horizontal scrolling.

What I learned:
I learned that fixed margins like 630px only work on desktop screen size, and on a 375px phone the card goes off the screen. It also breaks when I add a card. A better way is to use display: grid with gap, so the browser places the cards at every width.

---

## Interaction 6 (Joe) — Flexbox homepage (Milestone 01), CSS TODO 1–8

Task:
Complete the Flexbox layout of the homepage (header, navigation, hero, cards, footer) and move the site into `public/` as required by the GitHub-Render guide.

AI tool:
Claude (Anthropic), Claude app.

My prompt:
"Now help do step by step like newly student starting this project. I would appriciate your help and your explanation of every step why we doing it and in general if we need to do it in other porjects."

AI recommendation:
Restructure the repository into `public/` with `git mv` and add the starter `.gitignore`; then for each TODO, explain the property and give a fill-in-the-blank rule to complete (e.g. flex is applied to the parent and affects only its direct children; `flex: 2 1 28rem` = grow, shrink, basis; `margin-top: auto` pins the card link to the bottom). The AI reviewed each rule and found two `display`/`flex-wrap` values and the footer selector still left blank.

My decision:
MODIFY

Why:
I wrote the rules myself from the templates. For TODO 2 I used `margin-left: auto` instead of the suggested `margin-inline-start: auto`; both push the navigation to the right in a left-to-right page.

Verification:
Live Server at 1280 px: header in one row, hero in two regions, four cards of equal height with buttons aligned at the bottom. At 375 px: header items and cards wrap, no horizontal scrolling. Checked the committed file on GitHub.

What I learned:
The rule I remember best is margin-left: auto on the nav.Before I added it, the menu was right next to the logo; after, the menu and button moved to the right, because the auto margin takes all the free space. I also learned that flex only affects the direct children of the container, which is why the links needed their own flex container on .nav-list.

---

## Interaction 7 (Joe) — Content and lab-sheet explanations

Task:
Replace the sample content (services, team, version label), add a fourth card with a long title (challenge), and draft the explanations for Tasks 1–3 of the Flexbox lab.

AI tool:
Claude (Anthropic), Claude app.

My prompt:
"please write you this paragraph as I am writing it." and, for the content, "default ok" (accepting the proposed theme, services, fourth card, team text and "Version 03" label).

AI recommendation:
A complete `public/index.html` keeping all existing classes and ids, with USEK-specific descriptions of different lengths, a "Career and internship guidance for engineering students" card linked to a new `#career-details` section, and a team list with GitHub usernames. Draft paragraphs explaining why two flex containers are needed, flex-basis and wrapping, and why equal height does not apply across wrapped rows.

My decision:
MODIFY

Why:
I checked the content matches our group, kept the structure so the existing CSS still applies, and filled in the wrap width I measured myself in the Task 2 paragraph.

Verification:
Tested at 375, 768 and 1280 px: no horizontal scrolling; four equal-height cards on desktop, 2 + 2 at 768 px, one per row at 375 px; every navigation and card link reaches an existing section.

What I learned:
When I replaced the page text, I learned that I had to keep the same classes and ids in the HTML, because the CSS and the links depend on those names and not on the text. I also learned that the homepage file must be named exactly index.html, otherwise the server will not show it.
