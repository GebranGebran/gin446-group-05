# AI Development Log

## Interaction 1

Task:
Build the project homepage: header, Flexbox navigation, six cards in a 3-column CSS Grid with gap, footer, and basic readable styling.

AI tool:
Claude (Anthropic), in the Claude chat app.

AI recommendation:
Use display: flex on nav; display: grid on .cards with grid-template-columns: repeat(3, 1fr) and gap instead of margins; add padding, borders and colors on .card for readability.

My decision:
ACCEPT

## Interaction 2

Task:
Make the card grid responsive: 3 columns on desktop, 2 on tablet, 1 on mobile, with no horizontal scrolling.

AI tool:
Claude (Anthropic), in the Claude chat app.

AI recommendation:
Add two media queries: at max-width 1023px set grid-template-columns: repeat(2, 1fr), and at max-width 599px set it to 1fr; let the nav wrap on small screens. Later, I also asked for better page styling and Claude gave a fuller stylesheet with the same breakpoints.

My decision:
ACCEPT