/**
 * Portfolio site voice: plain, specific, written like Owen talks.
 * Keep the HUD look; soften the words.
 */

export const siteCopy = {
  brand: {
    logo: "Owen Lindsey",
    footer: "© 2026 Owen Lindsey · Thanks for stopping by.",
  },

  nav: {
    projects: "Projects",
    about: "About",
    resume: "Resume",
    contact: "Contact",
    menuOpen: "Close",
    menuClosed: "Menu",
  },

  home: {
    heroTagline: "Full-stack developer with live apps in production, from client work to side projects.",
    heroSub:
      "GCU grad (B.S. Software Development, ML/AI minor). Before code: five years on F-22 maintenance at Edwards AFB.",
    typewriter: [
      "Full-stack software engineer",
      "React · TypeScript · .NET · Node.js",
      "USAF veteran · F-22 maintenance",
    ],
    readout: [
      { label: "Focus", value: "Full-stack product\nengineering" },
      { label: "Education", value: "B.S. Software Dev\nML/AI minor · GCU\nAug 2023 - Apr 2026" },
      { label: "Stack", value: "React · TypeScript\n.NET · Node.js" },
      { label: "Based in", value: "Phoenix, AZ\nOpen to remote" },
    ],
    ctaProjects: "See my work",
    ctaContact: "Get in touch",
    ctaResume: "Download resume",
    metrics: [
      { value: "2026", label: "Graduated", sub: "GCU · Apr 2026 · Software Dev + ML/AI" },
      { value: "4", label: "Live apps", sub: "Lunara, Iron Palace, Turnover Log + ML demos" },
      { value: "5 yr", label: "USAF", sub: "F-22 maintenance · Edwards AFB" },
      { value: "375", label: "Lunara tests", sub: "81.9% coverage in production" },
    ],
    workSection: "Work I'm proud of",
    workViewAll: "All projects",
    techSection: "What I work with",
    aboutTitle: "A little more context",
    aboutPoints: [
      {
        lead: "Production beats prototypes.",
        body: "Lunara Care is live at lunaracare.org with real doula-client users. Iron Palace, Turnover Log, and ML demos are deployed too. Links are on the projects page.",
      },
      {
        lead: "ML/AI minor, not just buzzwords.",
        body: "Survival analysis, SVMs, and a PyTorch sentiment app I trained and deployed myself, with numbers I can explain in an interview.",
      },
      {
        lead: "Maintenance background still shows up.",
        body: "Turnover Log came from shift handoffs on the flight line. I care about tools crews will actually use.",
      },
    ],
    aboutMore: "About me",
    aboutContact: "Say hello",
    ctaTitle: "Looking for a teammate?",
    ctaBody: "Open to full-time, contract, or remote roles. Based in Phoenix, AZ.",
    ctaBottomContact: "Contact me",
    ctaBottomResume: "Resume (PDF)",
  },

  featuredProjects: [
    {
      id: "lunara",
      tags: ["React", "TypeScript", "Node.js", "MongoDB"],
      title: "Lunara Care",
      description:
        "Postpartum care platform I led end to end: scheduling, chat, care plans. Live with real users at lunaracare.org.",
      liveUrl: "https://www.lunaracare.org",
    },
    {
      id: "turnover-log",
      tags: ["React", "ASP.NET Core 8", "PostgreSQL"],
      title: "Turnover Log",
      description:
        "Shift handoff board I built after F-22 maintenance work. Technicians log open items; supervisors see updates without setting up email.",
      liveUrl: "https://turnover-log.vercel.app",
    },
    {
      id: "iron-palace",
      tags: ["React", "Vite", "Docker"],
      title: "Iron Palace Podcast",
      description:
        "Podcast site for a client. Pulls YouTube RSS at build time so new episodes show up after a redeploy.",
      liveUrl: "https://ironpalace.live",
    },
  ] as const,

  projectsPage: {
    eyebrow: "Projects",
    title: "Things I've built",
    intro:
      "Coursework, client work, and projects I built and deployed on my own. Click a card for more detail, or open the live site when you see the badge.",
    statLearningEyebrow: "Statistical learning · AIT-110",
    statLearningIntro:
      "Three notebooks I'm especially proud of. Each has a walkthrough video if you want to hear my thinking out loud.",
    expand: "More detail",
    collapse: "Less detail",
    viewGithub: "Code on GitHub",
    liveBadge: "Live",
  },

  about: {
    eyebrow: "About",
    title: "Hi, I'm Owen",
    backgroundTitle: "Background",
    paragraphs: [
      "I'm a software engineer who graduated from Grand Canyon University in April 2026 (B.S. Software Development, Machine Learning & AI minor, Aug 2023 - Apr 2026). I like owning a feature from the database to the UI and leaving it in a state the next person can maintain.",
      "My ML minor wasn't a checkbox: survival analysis, SVMs, ensembles, and a PyTorch sentiment model I trained, evaluated, and deployed to Streamlit with real metrics I can walk through.",
      "Before GCU I spent five years in the Air Force on F-22 maintenance at Edwards AFB, including crew chief work with USAF, Lockheed, and Boeing teams. That's where Turnover Log started. I previously held a Secret clearance through honorable separation.",
    ],
    interestsTitle: "Off the clock",
    timelineTitle: "Timeline",
    qualificationsTitle: "Also worth knowing",
  },

  resume: {
    eyebrow: "Resume",
    title: "Download resume",
    body: "PDF resume available for download. For the most current information, see the projects and about pages.",
    download: "Download PDF",
    viewInBrowser: "View in browser",
  },

  contact: {
    eyebrow: "Contact",
    title: "Say hello",
    role: "Software engineer · Phoenix, AZ",
    seekingTitle: "What I'm looking for",
    seeking: [
      "Full-time software roles",
      "Contract or freelance projects",
      "Remote or Phoenix-area on-site",
      "Full-stack, backend, defense, or operations-software teams",
    ],
    note: "I read every message. If you're hiring or have a project in mind, tell me a bit about the team and timeline.",
    formName: "Name",
    formEmail: "Email",
    formMessage: "Message",
    formPlaceholder: "What are you working on?",
    formSubmit: "Send message",
    formSent: "Thanks, message received.",
  },
} as const

/** Humanized Turnover Log entry, merged in ProjectsPage */
export const turnoverLogProject = {
  short:
    "Shift handoff tool from my maintenance days: tail numbers, priority, and a supervisor inbox that works without SMTP. React on Vercel, .NET API on Render.",
  expanded: `I built Turnover Log after crew-chief work on the F-22. The problem is the handoff between shifts, not another generic task board.

Technicians log open items by asset or tail number. Supervisors get in-app alerts when something opens or closes. Email is optional; production runs fine without an SMTP server.

Stack: React 18 + TypeScript + Vite on Vercel, ASP.NET Core 8 + EF Core on Render with PostgreSQL, JWT auth. xUnit integration tests run in GitHub Actions on every push. The board starts empty, with no fake seed data.`,
} as const
