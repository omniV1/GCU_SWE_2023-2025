Owen Lindsey — Portfolio Site Figma Make Prompt
COMPLETE PROMPT (copy everything below this line)
---
Design a portfolio website for Owen Lindsey, a software engineer and United States Air Force veteran. The design concept is "Field Terminal" — a military field operations interface that doubles as a personal portfolio. The aesthetic fuses two identities: earthy utilitarian (military, national parks, scouting, olive/khaki tones, rugged photography) as the structural DNA, and dark retro-tech (terminal green accents, monospace typography, neon interface elements, cyberpunk illustration energy) as the interface language. These two aesthetics must feel unified, not competing.
---
DESIGN SYSTEM
Color Palette:
Background primary: #0D0F0A (near-black with olive undertone)
Background secondary: #141810 (dark forest)
Surface/card: #1C2116 (dark military green)
Border/divider: #2E3828 (muted olive)
Terminal green (primary accent): #4AFF6B
Amber (secondary accent): #D4820A
Muted tan (tertiary): #A89070
Text primary: #E8E4D8 (warm off-white, like aged paper)
Text secondary: #7A8572 (muted sage)
Text dim: #4A5244
Typography:
Display/hero: "Big Shoulders Display" or "Bebas Neue" — wide, military stencil feel — all caps for section headers
Body/UI: "IBM Plex Mono" or "JetBrains Mono" — monospace, terminal aesthetic
Accent/labels: "Space Grotesk" — clean, slightly geometric for nav and UI labels
Never use rounded, playful, or serif fonts
Texture & Atmosphere:
Subtle noise/grain texture overlay on all backgrounds (5% opacity)
Dark landscape photography (mountains, desert, aerial) used as full-bleed section backgrounds — desaturated to 20% saturation, darkened to 15-20% brightness
Occasional grid lines (1px, 3% opacity) suggesting graph paper or targeting reticle
Status indicator dots (small circles, terminal green) used as decorative bullets and state markers
Thin horizontal rules (#2E3828) between sections
Interactive Language:
Hover states: terminal green left-border reveal + slight background lightening
Cards: flat with 1px border (#2E3828), no drop shadows — use border color changes on hover
Buttons: filled terminal green with dark text, or ghost (terminal green border + text only)
All transitions: 150ms ease — fast and crisp, not floaty
---
PAGE STRUCTURE
PAGE 1 — HOMEPAGE
Full-viewport hero section:
Background: dark mountain/aerial landscape photo (desaturated, very dark). Centered layout.
Top-left corner: small "OL" monogram in terminal green, monospace font.
Navigation bar (top): horizontal, all-caps monospace labels — PROJECTS / ABOUT / RESUME / CONTACT — right-aligned. Nav items separated by thin vertical pipes " | ". No hamburger menu on desktop.
Hero content (vertically centered, left-aligned):
```
[STATUS: ONLINE]          <- small terminal green label, monospace, above name
OWEN
LINDSEY                   <- display font, massive, stacked, cream/off-white
Software Engineer         <- smaller, Space Grotesk, muted tan color
```
Below the name, a horizontal "status readout" bar — styled like a system dashboard or military briefing card. Three or four columns separated by vertical dividers:
```
BRANCH          EDUCATION              STACK                LOCATION
USAF Veteran    B.S. Computer Sci.     Java · Python · TS   Phoenix, AZ
                Grand Canyon Univ.     React · Spring Boot
                Class of 2025
```
Below status readout: two ghost buttons side by side — [ VIEW PROJECTS ] and [ DOWNLOAD RESUME ]
Thin animated scan line at very bottom of hero (optional, subtle — a single 1px line that slowly moves down, terminal aesthetic).
---
Featured Projects Strip (below hero, ~80px padding top/bottom):
Section label: "// SELECTED WORK" in terminal green monospace, left-aligned, above a thin horizontal rule.
Three project cards in a row. Each card:
Dark surface background (#1C2116), 1px border (#2E3828)
Top-left: small tech stack tags (pill labels, #2E3828 bg, muted text)
Project title in display font
One-line description in monospace body text
Bottom row: [ VIEW CASE STUDY → ] link in terminal green
Card 1 — Airport Gate Management System
Tags: Java · Spring Boot · MySQL · Docker
Title: AIRPORT GATE MGMT SYSTEM
Description: Enterprise-grade airport operations platform with role-based access across 4 user types, full CRUD for 6 entity types, and OpenAPI documentation.
Card 2 — Multi-Agent Code Quality System
Tags: Python · ML · SonarQube · Pre-commit
Title: MULTI-AGENT CODE QUALITY
Description: Adaptive ML classifier system predicting SonarQube gate failures in real-time across 8 quality dimensions using per-gate activation function selection.
Card 3 — Aircraft Fleet Manager
Tags: React · TypeScript · Tailwind · Vite
Title: AIRCRAFT FLEET MANAGER
Description: Full-stack aviation management dashboard with real-time data visualization, Recharts analytics, and Radix UI component system.
Below the three cards: a text link "VIEW ALL PROJECTS →" right-aligned, terminal green.
---
Skills / Tech Stack Section (below projects):
Section label: "// TECHNICAL PROFILE"
Display as a grid of categories, each with a header and list of tech items. Use monospace font. Items are plain text, separated by thin dividers. No icons. No progress bars.
```
LANGUAGES          FRONTEND              BACKEND              SYSTEMS & TOOLS
Java               React + TypeScript    Spring Boot 3         Docker
C# / .NET          Angular               Node.js / Express     SonarQube
Python             Tailwind CSS          ASP.NET Core MVC      Git / GitHub
TypeScript         Radix UI              .NET Web API          OpenAPI / Swagger
JavaScript         Recharts              Spring Security       Pre-commit Hooks
C / Bash           Bootstrap             REST API Design       Maven
SQL                                      MongoDB / MySQL       OS Fundamentals
```
---
Brief About Strip (single row, 2-column layout):
Left: dark background with a portrait photo (if available) or a topographic map SVG texture.
Right: short bio block.
```
ABOUT

Software engineer, USAF veteran, and perpetual builder. I spent years working
on F-22 avionics systems before earning my B.S. in Computer Science from Grand
Canyon University. I build things that are fast, purposeful, and don't break.

My projects range from enterprise Java systems to ML-powered dev tools —
always with aviation-grade attention to detail.

[ READ MORE → ]
```
---
PAGE 2 — PROJECTS (Full List)
Section header: "// ALL PROJECTS"
Subtitle in muted monospace: "Full project index — click any entry for technical details."
Layout: Two-column grid on desktop, single column on mobile. Each card is slightly taller than homepage cards to allow more metadata.
Project cards include:
Title (display font)
Category tag: ENTERPRISE / FULL-STACK / ML-AI / SYSTEMS / ALGORITHMS
Tech stack pills
2–3 sentence description
[ EXPAND DETAILS ] toggle that reveals a collapsible section (progressive disclosure) with:
Architecture overview
Key technical decisions
Challenges solved
Link to GitHub repo
Full project list:
1. Airport Gate Management System (AGMS)
Category: ENTERPRISE
Stack: Java 17 · Spring Boot 3 · Spring Security · MySQL · Thymeleaf · Bootstrap · Docker · OpenAPI
Short: Full-stack enterprise airport operations platform built across 6+ development milestones.
Expanded: N-layer architecture (Controller → Service → Repository). Role-based access control for Admin, Gate Agent, Airline Rep, and Passenger user types. Complete CRUD across 6 entity types: gates, flights, airlines, assignments, terminals, passengers. Integrated Docker containerization, SonarQube static analysis, and OpenAPI/Swagger documentation. Built with test-driven milestones from schema design through deployment.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
2. Multi-Agent Code Quality System
Category: ML-AI
Stack: Python · NumPy · Pandas · Radon · SonarQube API · Matplotlib · Rich
Short: ML-inspired multi-agent system that predicts SonarQube quality gate failures before commit.
Expanded: Supervisor and architecture agents coordinate 8 specialized quality gate analyzers (bugs, vulnerabilities, security hotspots, reliability, maintainability, coverage, duplication, security rating). Adaptive activation function selection (Sigmoid vs ReLU) per gate to minimize false positives. Feature extraction includes cyclomatic complexity, nesting depth, SQL/command injection pattern detection, and hardcoded secret scanning. Confusion matrix validation against real SonarQube ground truth. Supports Python, Java, C#, JavaScript/TypeScript, and C/C++.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
3. Aircraft Fleet Manager
Category: FULL-STACK
Stack: React · TypeScript · Vite · Tailwind CSS · Radix UI · Recharts · Express
Short: Aviation-domain fleet management dashboard with real-time analytics and REST API backend.
Expanded: Component architecture built on Radix UI primitives with Tailwind utility styling. Recharts data visualization for fleet metrics and status reporting. Express REST API backend with structured endpoint design. Vite build toolchain for fast development cycles. Domain-specific design informed by real avionics background.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
4. Full-Stack Web Application (GameCube Store)
Category: FULL-STACK
Stack: Angular · React · Node.js · Express · MySQL · MongoDB · TypeScript
Short: Dual-frontend e-commerce application with complete REST API, ER modeling, and full technical documentation.
Expanded: Two complete frontend implementations — one in Angular, one in React — consuming the same Node.js/Express REST API. MySQL for relational data, MongoDB for NoSQL patterns. Full API documentation with Postman, ER diagrams, UML architecture diagrams, and wireframes. Demonstrates ability to work across the entire web stack.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
5. Minesweeper (Console + WinForms)
Category: ALGORITHMS
Stack: C# · .NET · WinForms
Short: Fully featured Minesweeper with flood-fill reveal, flag mechanics, timer, and high score tracking.
Expanded: Implemented in two versions — console and GUI. Core algorithm uses recursive flood-fill for zero-cell reveal cascades. Randomized mine placement with neighbor count calculation. WinForms GUI version adds visual polish and persistent high score storage. Demonstrates algorithmic thinking and GUI development in .NET.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
6. Aerospace API (Summer Practice)
Category: FULL-STACK
Stack: C# · .NET Web API · REST
Short: Aviation-themed REST API built during independent study — reinforces domain expertise and .NET API design.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
7. Spring Boot Enterprise App (CST-339)
Category: ENTERPRISE
Stack: Java 17 · Spring Boot 3 · MongoDB · Spring Security · Maven
Short: Multi-module enterprise application demonstrating microservices patterns, IoC, and both relational and NoSQL persistence.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
8. OS Fundamentals — Systems Programming
Category: SYSTEMS
Stack: C · Bash · GCC · Unix
Short: Low-level systems implementations including CPU scheduling simulators, IPC via pipes/signals, and synchronization with mutexes and semaphores.
GitHub: https://github.com/omniV1/GCU_SWE_2023-2025
---
PAGE 3 — ABOUT
Hero: Full-width dark background with faint topographic contour lines as texture. Large stencil display type: "ABOUT THE ENGINEER"
Two-column layout below:
Left column — Bio:
```
BACKGROUND

Software engineer and USAF veteran. Served as an F-22 Avionics Systems Specialist
before transitioning to civilian software engineering. B.S. in Computer Science,
Grand Canyon University, Class of 2025.

I bring operational discipline from the flight line to the codebase — I build systems
that are reliable under pressure, documented thoroughly, and designed to be handed off.

INTERESTS
Long-distance backpacking  ·  National parks  ·  Retro computing
Aviation history  ·  Open source tools  ·  Competitive programming
```
Right column — Timeline (vertical, styled like a mission log):
```
[2025]  B.S. Computer Science — Grand Canyon University
[2024]  Built Multi-Agent Code Quality System
[2024]  Built AGMS — enterprise airport operations platform
[2023]  Began GCU Software Engineering program
[20XX]  Separated from USAF — Avionics Systems Specialist
[20XX]  Enlisted — United States Air Force
        F-22 Raptor Avionics Systems
```
Scouting/skills section: A collapsible "ADDITIONAL QUALIFICATIONS" row for things like Eagle Scout, any certifications, etc.
---
PAGE 4 — CONTACT
Minimal. Dark background, centered layout.
```
// CONTACT

Let's build something.

Owen Lindsey
Software Engineer · Phoenix, AZ

[ Email ]     [ GitHub ]     [ LinkedIn ]     [ Resume PDF ]

"Available for full-time roles, contract work, and interesting problems."
```
Form (optional): Name / Email / Message / [ SEND TRANSMISSION ]
Style the send button as a terminal command — green background, monospace font: [ > SEND_MESSAGE ]
---
LAYOUT & COMPONENT NOTES FOR FIGMA MAKE
Max content width: 1200px, centered, with generous side padding (80px desktop, 24px mobile)
Spacing scale: Use multiples of 8px throughout
Cards: No border-radius or use 2px maximum — sharp corners reinforce the military/terminal feel
All section headers: Prefixed with "// " in terminal green, body text in off-white
Progressive disclosure: All project "expanded" sections start collapsed, revealed on click/tap
Mobile: Single column, nav collapses to a minimal top bar with a [ MENU ] text button (not a hamburger icon)
No stock illustration, no gradient blobs, no glassmorphism, no floating cards with heavy shadows
Photography: Used only as full-bleed background atmosphere, always heavily darkened and desaturated
---
IF FIGMA MAKE HAS A CHARACTER LIMIT — PRIORITY ORDER
Generate these pages in this order if you need to split:
Homepage (hero + project strip + skills + about strip)
Projects page (full list with expandable cards)
About page
Contact page
---
CORRECTIVE PROMPT (paste this if the first output looks too generic/SaaS)
"The design should not look like a SaaS landing page or startup website. Remove any gradient backgrounds, colorful blobs, rounded cards, or hero illustrations. The color palette must be near-black with olive undertones — not navy, not gray, not white. All typography should feel industrial or military — no rounded fonts. The terminal green (#4AFF6B) accent should be used sparingly as a highlight, not as a primary background color. The overall feel should be austere, precise, and intentional — like a field operations briefing document rendered as a website."