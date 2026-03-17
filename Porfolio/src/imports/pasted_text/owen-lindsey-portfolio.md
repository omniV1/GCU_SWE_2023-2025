Design a personal portfolio website for Owen Lindsey — a senior Computer Science student, Air Force veteran, and aspiring defense-tech software engineer. The site needs to serve double duty: it's a professional portfolio for recruiters and hiring managers, and a personal brand expression that communicates who Owen is beyond the resume.
Design Language: "Field Terminal"
The aesthetic is a hybrid of two worlds: utilitarian military/outdoors and dark retro-tech. Think of a field operations terminal built into a ranger station — rugged, functional, but running sophisticated software underneath. This is NOT generic dark-mode developer portfolio. It should feel like it was designed by someone who has worked on fighter jets AND writes code.
Color palette:

Primary background: Deep olive drab (#1a1f16) transitioning to near-black (#0d0f0b)
Secondary surface: Warm khaki/sand (#c2b280) used sparingly for cards, callouts, and section dividers
Accent 1: Terminal green (#39ff14) — used for interactive elements, links, status indicators, and highlights
Accent 2: Muted amber (#d4a017) — used for secondary emphasis, tags, and warm highlights
Text primary: Off-white (#e8e4d9) with a warm, parchment-like tone
Text secondary: Desaturated sage (#8a9178)
Error/alert: Burnt orange (#cc5500)

Typography:

Display/headings: A heavy, industrial condensed typeface — think Druk Wide, Dharma Gothic, or Anton Extended. All-caps. Tightly tracked. This is the personality of the site.
Body text: A clean monospace font like JetBrains Mono, IBM Plex Mono, or Space Mono — reinforcing the technical identity without sacrificing readability.
Accent text: A humanist sans-serif like DM Sans or Instrument Sans for UI labels, navigation, and metadata — the warm counterpoint.

Texture and atmosphere:

Subtle topographic map line pattern as a background texture (very low opacity, 3-5%) in hero sections
Noise/grain overlay across dark surfaces (film grain feel, not digital noise)
Thin ruled lines and grid marks as decorative structure — like a surveyor's field notebook
Photography (landscapes, nature, outdoor shots) used as large atmospheric bleeds behind sections, desaturated and blended into the dark palette


Page Structure
1. HOME / LANDING PAGE
Hero section:

Large display type: "OWEN LINDSEY" spanning the full width
Subtitle in monospace: "Full-Stack Dev · Systems Thinker · Veteran"
Brief 2-line positioning statement: "Air Force avionics technician turned software engineer. I build things that work under pressure."
Two CTA buttons styled as terminal commands: > View Projects and > Download Resume
Background: A subtle, darkened landscape photograph (mountains or open terrain) with the topographic line texture overlaid

Quick-scan section (below the fold):

Three columns or a horizontal strip with key facts, styled like a status readout or data dashboard:

"4 years USAF · F-22 Avionics"
"B.S. Computer Science · May 2026"
"Full-Stack · Cloud · ML/AI"


Each fact has a small icon or status dot in terminal green

Featured Projects section:

2-3 project cards in a grid
Each card shows: project name (large display type), one-line description, tech stack tags (small pills in amber), and a thumbnail or screenshot
Cards are visually scannable — a recruiter can absorb the essentials in seconds
Hover state reveals a brief expanded description (2-3 sentences)
Click navigates to full project detail page

Footer:

Minimal. Links to GitHub, LinkedIn, email
Small text: location (Colorado Springs, CO), and a short sign-off


2. PROJECTS PAGE
Layout: Grid of project cards (2 columns on desktop, 1 on mobile)
Each project card contains:

Project name in display type
Role tag (e.g., "Project Lead", "Solo Dev", "Contributor")
One-line summary
Tech stack as small tags/pills
Status indicator: a colored dot — green for live/complete, amber for in-progress, grey for archived
Thumbnail screenshot or mockup

Project Detail Page (when a project is clicked):

Full-width hero with project name and a large screenshot or mockup
Section 1 — Overview: 3-4 sentences. What is it, who is it for, what problem does it solve. This is the recruiter-friendly summary.
Section 2 — Technical Deep Dive (expandable/collapsible): Architecture decisions, tech stack rationale, challenges encountered, code patterns used. This is for the hiring manager or engineer who wants depth. Use expandable accordion sections so it doesn't overwhelm at first glance.
Section 3 — Outcome/Impact: Metrics, screenshots of the live product, links to repo or live demo
Sidebar or sticky nav for jumping between sections on long detail pages


3. ABOUT PAGE

Left column: A portrait photo or stylized personal image, with a desaturated treatment that matches the site palette
Right column: Personal narrative — not a resume rehash, but the story. Military service, transition to tech, what drives the work. Written in first person, conversational but confident.
Below: An interests/influences section styled as a visual grid or mood board — books, games, manga, philosophy references. This is the personality layer. Small image tiles with labels, arranged in a loose masonry grid. Not critical information but shows depth.
A "Currently" strip at the bottom: what Owen is reading, playing, building, or learning right now — styled like a live status feed


4. RESUME PAGE

Clean, structured layout that mirrors a traditional resume but is designed for web
Sections: Experience, Education, Skills, Certifications
Each entry is scannable: bold title, organization, date range, 2-3 bullet points
A prominent "Download PDF" button at the top styled as a terminal command
Skills displayed as a grid of tags grouped by category (Languages, Frameworks, Tools, Platforms)


5. CONTACT PAGE

Simple and direct
A short message: "I'm relocating to Colorado Springs in mid-2026 and actively looking for software engineering roles in defense tech. Let's talk."
Contact form with fields: Name, Email, Message
Direct links: Email, LinkedIn, GitHub
Styled consistently — form inputs should feel like terminal input fields with the monospace font and a blinking cursor effect


6. BLOG PAGE (optional/secondary)

Simple list layout with post titles, dates, and 1-line previews
Tags for categorization (Tech, Thoughts, Projects)
Clean reading experience on individual posts — generous line height, readable column width


Interaction & Motion

Page transitions: subtle fade or slide, nothing flashy
Scroll-triggered fade-in for content sections (staggered, not simultaneous)
Hover states on project cards: slight lift/shadow + reveal of expanded text
The terminal green accent should pulse subtly on active/focused elements
Navigation: fixed top bar with the site name on the left and nav links on the right, collapsing to a hamburger on mobile
The nav bar should feel like a command bar — monospace font, tight spacing, terminal-style separators (pipes or slashes)

Responsive Design

Desktop: full multi-column layouts, large typography, atmospheric photography
Tablet: condensed grid, photography scales down
Mobile: single column, photography becomes more subtle, typography stays bold but scales appropriately
The site should feel intentional at every breakpoint, not like a desktop site that was squeezed

Overall Tone
This site should feel like it was built by someone with precision, depth, and range. It's not a template. It's not a "creative coder" portfolio with gratuitous WebGL. It's a site that communicates: this person has real-world experience, technical skill, and a point of view. The design should be confident without being loud — the kind of thing where a recruiter thinks "this person clearly knows what they're doing" and an engineer thinks "this person has taste."