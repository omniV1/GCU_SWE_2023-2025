/**
 * Portfolio site voice: plain, specific, recruiter-scannable in ~30 seconds.
 */

export const recruiterLinks = [
  { label: "Resume (PDF)", href: "/Owen_Lindsey_Resume.pdf", download: true },
  { label: "LinkedIn", href: "https://www.linkedin.com/in/owen-lindsey-5b323a23b/" },
  { label: "Email", href: "mailto:owen.lindsey98@outlook.com" },
  { label: "GitHub", href: "https://github.com/omniV1" },
] as const

export const siteCopy = {
  brand: {
    logo: "Owen Lindsey",
    footer: "© 2026 Owen Lindsey · Full-stack software engineer · Phoenix, AZ",
  },

  nav: {
    projects: "Projects",
    about: "About",
    resume: "Resume",
    contact: "Contact",
    menuOpen: "Close",
    menuClosed: "Menu",
    resumeCta: "Resume ↓",
  },

  home: {
    heroRole: "Full-Stack Software Engineer",
    heroTagline:
      "I ship full-stack apps end to end—React and TypeScript on the front, .NET or Node on the back—with four live demos you can click through below.",
    heroSub:
      "GCU '26 (B.S. Software Development, ML/AI minor). Five years on F-22 maintenance before I wrote code for a living.",
    typewriter: [
      "React · TypeScript · .NET · Node.js",
      "4 live apps in production",
      "Open to full-time · Phoenix or remote",
    ],
    readout: [
      { label: "Status", value: "Open to work\nFull-time preferred" },
      { label: "Education", value: "B.S. Software Dev\nML/AI minor · GCU '26" },
      { label: "Stack", value: "React · TypeScript\n.NET · Node.js · Python" },
      { label: "Location", value: "Phoenix, AZ\nRemote OK" },
    ],
    ctaProjects: "View projects",
    ctaContact: "Contact",
    ctaResume: "Download resume",
    metrics: [
      { value: "2026", label: "Graduated", sub: "GCU · Software Dev + ML/AI" },
      { value: "4", label: "Live apps", sub: "Lunara, Iron Palace, Turnover Log, NLP Sentiment" },
    ],
    recruiter: {
      eyebrow: "Recruiter snapshot",
      bullets: [
        "Targeting junior / entry-level full-stack roles (and teams that value ops or maintenance backgrounds).",
        "Strongest proof: Lunara Care—live capstone with 375 automated tests and 82% line coverage.",
        "Stack match: React, TypeScript, ASP.NET Core, Node.js, MongoDB, PostgreSQL, JWT, CI/CD.",
        "Secret clearance held during USAF service; not currently active.",
      ],
    },
    workSection: "Selected work (live demos)",
    workViewAll: "All projects + coursework",
    techSection: "Technical skills",
    aboutTitle: "Background",
    aboutPoints: [
      "Lunara Care is my capstone—live at lunaracare.org with a full case study at lunara-profile.design.",
      "Iron Palace and Turnover Log are shipped apps; NLP Sentiment is a deployed PyTorch + Streamlit demo.",
      "I spent five years on F-22s at Edwards before GCU. I still think in handoffs, checklists, and who uses the tool next.",
    ],
    aboutMore: "Full bio",
    aboutContact: "Email me",
    ctaTitle: "Looking for a wingman?",
    ctaBody: "Full-time or contract. Phoenix-based, open to remote. Reply by email or LinkedIn—I read everything.",
    ctaBottomContact: "Contact",
    ctaBottomResume: "Resume (PDF)",
  },

  featuredProjects: [
    {
      id: "lunara",
      tags: ["React", "TypeScript", "Node.js", "MongoDB"],
      title: "Lunara Care",
      description:
        "Capstone in production at lunaracare.org. Provider/client platform with scheduling, real-time chat, and care plans. 375 tests, 82% coverage.",
      liveUrl: "https://www.lunaracare.org",
      caseStudyUrl: "https://www.lunara-profile.design/",
      screenshot: "/screenshots/LunaraHome.png",
    },
    {
      id: "turnover-log",
      tags: ["React", "ASP.NET Core 8", "PostgreSQL"],
      title: "Turnover Log",
      description:
        "Shift handoff app from my maintenance background. React + ASP.NET Core 8, JWT auth, supervisor inbox, GitHub Actions CI.",
      liveUrl: "https://turnover-log.vercel.app",
      screenshot: "/screenshots/TurnoverTechHome.png",
    },
    {
      id: "iron-palace",
      tags: ["React", "Vite", "Docker"],
      title: "Iron Palace Podcast",
      description:
        "Client podcast site at ironpalace.live. YouTube RSS at build time, in-app player, admin panel, Dockerized static deploy.",
      liveUrl: "https://ironpalace.live",
      screenshot: "/screenshots/IronPalacePodcastHome.png",
    },
    {
      id: "nlp-sentiment",
      tags: ["Python", "PyTorch", "Streamlit"],
      title: "Movie Sentiment Analyzer",
      description:
        "PyTorch classifier with separated train/serve layers. Live Streamlit demo with translation-comparison tab for cross-lingual drift.",
      liveUrl: "https://nlp-moviereview.streamlit.app/",
      screenshot: "/screenshots/MovieReviewSentimentAnalyzer.png",
    },
  ] as const,

  projectsPage: {
    eyebrow: "Projects",
    title: "Work samples",
    intro:
      "Start with the four live apps on the home page. Everything else is coursework, client work, or tools I built to learn. Each live badge links to something you can click.",
    statLearningEyebrow: "Statistical learning · AIT-110",
    statLearningIntro:
      "Notebook work with walkthrough videos—useful if you're evaluating ML fundamentals, not just framework tutorials.",
    expand: "Technical detail",
    collapse: "Less detail",
    viewGithub: "Code on GitHub",
    liveBadge: "Live demo",
  },

  about: {
    eyebrow: "About",
    title: "Owen Lindsey",
    backgroundTitle: "Summary",
    paragraphs: [
      "Full-stack software engineer (GCU, Apr 2026). I build from database to UI and leave code testable and documented. Best reference: Lunara Care at lunaracare.org—375 automated tests, SonarQube A ratings, production deploy on Vercel + Render.",
      "ML/AI minor with hands-on work: survival analysis, SVMs, and a PyTorch sentiment model I trained and deployed to Streamlit (linked from this site).",
      "USAF veteran—five years on F-22 maintenance at Edwards AFB, crew chief work with USAF, Lockheed, and Boeing. Secret clearance during service; inactive since separation. Turnover Log came directly from shift-handoff pain on the flight line.",
    ],
    interestsTitle: "Off the clock",
    timelineTitle: "Timeline",
    qualificationsTitle: "Also worth knowing",
  },

  resume: {
    eyebrow: "Resume",
    title: "Junior SDE resume (PDF)",
    body: "One-page, ATS-friendly PDF tuned for junior software engineer and entry-level full-stack roles. Matches the live demos and metrics on this site.",
    targetLine: "Targeting junior SDE · full-stack · backend-leaning · Phoenix, AZ & remote",
    highlightsTitle: "What's on the PDF",
    highlights: [
      "One page, ATS-friendly PDF aligned with this portfolio",
      "Four live apps: Lunara Care, Turnover Log, Iron Palace, NLP Sentiment",
      "Lunara capstone: 375 tests, 82% coverage, production at lunaracare.org",
      "Stack: React, TypeScript, Node.js, ASP.NET Core, PostgreSQL, MongoDB, JWT, CI/CD",
      "USAF veteran (F-22 maintenance); clearance inactive since separation",
    ],
    download: "Download PDF",
    viewInBrowser: "Open in browser",
  },

  contact: {
    eyebrow: "Contact",
    title: "Get in touch",
    role: "Full-Stack Software Engineer · Open to work · Phoenix, AZ",
    seekingTitle: "Open to",
    seeking: [
      "Junior / entry-level full-stack roles",
      "Backend or frontend-heavy teams",
      "Remote or Phoenix-area hybrid",
      "Defense, aerospace, or ops-adjacent software",
    ],
    note: "Email is fastest: owen.lindsey98@outlook.com. Include the role title and stack if you have one—I reply to every serious inquiry.",
    formName: "Name",
    formEmail: "Email",
    formMessage: "Message",
    formPlaceholder: "Role, team, or project—whatever you have",
    formSubmit: "Send message",
    formSent: "Thanks—message received.",
  },
} as const

/** Humanized Turnover Log entry, merged in ProjectsPage */
export const turnoverLogProject = {
  short:
    "Maintenance shift handoff: asset ID, priority, supervisor inbox without SMTP. React on Vercel, ASP.NET Core 8 API on Render, PostgreSQL, JWT, xUnit + GitHub Actions.",
  expanded: `Built after F-22 crew-chief work at Edwards. The problem is the handoff between shifts—not another generic task board.

Technicians log open items by tail number or asset ID. Supervisors get in-app alerts when something opens or closes. Email is optional; the app runs fine without SMTP.

Stack: React 18 + TypeScript + Vite on Vercel, ASP.NET Core 8 + EF Core on Render with PostgreSQL, JWT auth. xUnit integration tests in GitHub Actions on every push.`,
} as const
