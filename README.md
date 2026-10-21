# GIN446 Group 05 project — CampusConnect

Group 05 web programming project built incrementally during class.

## Team and purpose
- **Members and GitHub usernames:** Gebran (GebranGebran), Joe Atallah (web446)
- **Repository owner:** Gebran · **Deployment owner:** Gebran
- **Project theme and target users:** CampusConnect, a directory of campus services (study spaces, engineering workshops, student support, career and internship guidance) for USEK students
- **Repository URL:** https://github.com/GebranGebran/gin446-group-05
- **Render URL:** https://gin446-group-05.onrender.com/

## Project structure
```
README.md            project introduction (this file)
AI_LOG.md            AI development log (Grid lab)
.gitignore
public/              everything Render publishes
  index.html         CampusConnect homepage (Flexbox milestone)
  css/styles.css     homepage stylesheet
  lab-grid/          AI-assisted CSS Grid lab (index.html, style.css)
```

## Local preview
Open `public/index.html`, or use VS Code Live Server on that file.
Optional with Python installed: `python -m http.server 5500 --directory public`
Then visit http://localhost:5500. The Grid lab is at `/lab-grid/`.

## Render configuration
Static Site connected to this GitHub repository.
Branch: `main`. Root Directory: blank.
Build Command: `echo "No build required"`
Publish Directory: `public`
Automatic deploys on commits to `main`. No Start Command. No environment variables.

## Milestone 01 checklist
- [x] Correct group name and actual project content
- [x] Header and navigation use Flexbox
- [x] Hero uses wrapping and meaningful flex bases
- [x] At least three cards with different text lengths (four, including a long-title card)
- [x] Equal card heights within each line and bottom-aligned links
- [ ] Tested at 375, 768, and 1280 CSS pixels, with no horizontal overflow
- [ ] Keyboard focus visible and links reach real section targets
- [ ] Each member contributes at least one merged commit
- [ ] A merged change appears at the same Render URL

## Test log
| Check | Result and correction |
|---|---|
| 375px viewport and no horizontal scrolling | TODO |
| 768px viewport and readable wrapping | TODO |
| 1280px viewport and aligned card links | TODO |
| 200% zoom and readable content | TODO |
| Tab navigation and visible focus | TODO |
| All navigation and card targets work | TODO |
| Merged visible change appears on Render | TODO |

## Progress log
| Session | Work completed | Member contributions | Evidence |
|---|---|---|---|
| 01 | Repository and Render Static Site created; first homepage version deployed ("Version 02") | Gebran: created the repository, uploaded the starter, connected Render | Commits 97ea753–c14e565, live URL |
| 04 (Grid lab) | Manual 3-column grid, responsive 3/2/1 columns, AI_LOG.md | Gebran: grid lab and first two AI interactions | Commits d97fa63–f15ca2c |
| 01 (Flexbox milestone) | Site moved to `public/`; Flexbox TODO 1–8; real content, team section, long-title fourth card ("Version 03"); lab-grid stray CSS removed; AI_LOG completed | Joe: branch `feature/flexbox-homepage`, pull request reviewed and merged by Gebran | Commits 73486eb–d55e00c, PR link: TODO |

## Next milestones
Grid and media queries; JavaScript filtering; HTTP API; Flask CRUD; database;
validation and access control; final tests and demonstration.
