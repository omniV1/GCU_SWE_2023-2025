import { useState } from "react";
import { ChevronDown, ExternalLink } from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { FadeIn } from "./FadeIn";
import { HudCard } from "./HudCard";

interface Project {
  id: string;
  title: string;
  category: string;
  tags: string[];
  short: string;
  expanded: string;
  github: string;
  liveUrl?: string;
}

const allProjects: Project[] = [
  {
    id: "lunara",
    title: "LUNARA CARE",
    category: "FULL-STACK",
    tags: ["React 18", "TypeScript", "Vite", "Tailwind CSS", "Node.js", "Express", "MongoDB", "Mongoose", "Socket.IO", "JWT", "Passport.js", "Zod", "React Hook Form", "Axios", "Docker", "SonarQube", "Swagger/OpenAPI", "Jest", "Supertest"],
    short: "Production-deployed care coordination platform connecting doulas and new mothers. Built as senior capstone and shipped to real users at lunaracare.org.",
    expanded: "Provider dashboard surfaces active clients, upcoming appointments, and flagged check-ins at a glance. Providers manage client accounts, schedule appointments via an integrated calendar, exchange real-time messages, publish educational blog posts and resource articles, review uploaded documents with structured feedback, and build individualized care plans with milestone tracking.\n\nClient onboarding uses a multi-step intake wizard capturing personal, birth, feeding, support-network, and health information. Clients record daily check-ins with a 1\u201310 mood rating and 10 physical symptom self-assessments (fatigue, sleep quality, appetite, anxiety, pain). Clients upload documents, browse resources, track care plan milestones, book appointments, and message their provider via Socket.IO-powered real-time chat.\n\nBackend exposes 19 route modules and 70+ API endpoints. 20+ Mongoose models. JWT + Passport.js authentication with TOTP multi-factor auth. MongoDB GridFS for file storage. Security stack: Helmet, CORS, bcrypt (12 salt rounds), rate limiting, express-validator. Email via Nodemailer, push notifications via Web Push.\n\nQuality: 375 automated tests across unit, component, service, and integration layers. 81.9% code coverage. All SonarQube quality gates rated A. Deployed via Vercel (frontend) and Render (backend).",
    github: "https://github.com/omniV1/AQC",
    liveUrl: "https://www.lunaracare.org",
  },
  {
    id: "agms",
    title: "AIRPORT GATE MGMT SYSTEM",
    category: "ENTERPRISE",
    tags: ["Java 17", "Spring Boot 3", "Spring Security", "Spring Data REST", "MySQL", "Thymeleaf", "JUnit 5", "Mockito", "SonarQube", "OpenAPI 3.0", "JaCoCo"],
    short: "Full-stack enterprise airport operations platform built across 6+ development milestones with Spring Boot Actuator monitoring and Cloud SQL deployment support.",
    expanded: "N-layer architecture (Controller \u2192 Service \u2192 Repository) with Spring Data REST and HATEOAS. Role-based access control for Admin, Gate Agent, Airline Rep, and Passenger user types. Complete CRUD across 6 entity types: gates, flights, airlines, assignments, terminals, passengers.\n\nJUnit 5 + Mockito test suite with JaCoCo code coverage reporting. SonarQube static analysis integration. SpringDoc OpenAPI 3.0 documentation with Swagger UI. Bean validation across all form inputs. Spring Boot Actuator for runtime monitoring.\n\nCloud Run deployment with Cloud SQL connector. Javadoc generation for full API documentation.",
    github: "https://github.com/omniV1/GCU_SWE_2023-2025/tree/main/CST-339-Java3/workspaceCST-339/src/Milestone/agms",
  },
  {
    id: "multi-agent",
    title: "MULTI-AGENT CODE QUALITY",
    category: "ML-AI",
    tags: ["Python", "NumPy", "Pandas", "Radon", "SonarQube API", "Matplotlib", "Rich", "Git Hooks"],
    short: "Deep learning-inspired multi-agent system that predicts SonarQube quality gate failures before commit. Installs as a Git pre-commit hook for real-time analysis.",
    expanded: "Supervisor and architecture agents coordinate 8 specialized quality gate analyzers: Bug Gate (complexity, nesting depth), Vulnerability Gate (SQL injection, eval, XSS), Security Hotspot Gate (crypto, file ops, network), Reliability Gate (error handling), Security Gate (vulnerability severity), Maintainability Gate (code smells, function length), Coverage Gate (test coverage), and Duplication Gate (copy-paste detection).\n\nAdaptive activation function selection (Sigmoid vs ReLU) per gate to minimize false positives with specificity-optimized training. Feature extraction includes cyclomatic complexity via Radon, nesting depth analysis, SQL/command injection pattern detection, and hardcoded secret scanning.\n\nConfusion matrix validation against real SonarQube ground truth. Supports Python, Java, C#, JavaScript/TypeScript, and C/C++. Installs as a Git pre-commit hook via `install_hook.py` for real-time pre-commit analysis. Includes batch analysis mode for scanning entire codebases across multiple languages.",
    github: "https://github.com/omniV1/GCU_SWE_2023-2025/tree/main/agent-quality-system",
  },
  {
    id: "cinescope",
    title: "CINESCOPE",
    category: "FULL-STACK",
    tags: ["C#", "ASP.NET Core", "Blazor WASM", ".NET 9", "MongoDB", "MudBlazor", "Claude API", "Azure", "JWT"],
    short: "Movie review platform with AI-powered recommendations, multi-layered content moderation, and admin dashboard. Served as primary developer, owning architecture, API design, and all core feature implementation.",
    expanded: "5-tier architecture: Blazor WebAssembly SPA \u2192 ASP.NET Core API \u2192 Service layer \u2192 MongoDB repositories \u2192 database. 9 controllers, 9 services, and 9 DTO types.\n\nAI movie recommendations via Anthropic Claude API using Model Context Protocol (MCP) with process lifecycle management and health monitoring. Content moderation uses multi-layered filtering: banned word matching, character substitution normalization (1\u2192i, 4\u2192a, $\u2192s), spacing removal, repeated character collapse, and phrase-level detection with severity scoring.\n\nJWT authentication with BCrypt hashing, account lockout after 3 failed attempts, and token refresh. Role-based access control (Admin/User). Admin dashboard for user management, content moderation, and banned word administration.\n\nDeployed to Azure with GitHub Actions CI/CD. Azure Key Vault for secrets management. reCAPTCHA bot protection. 2-week Agile sprints with Jira tracking and peer-reviewed pull requests.",
    github: "https://github.com/omniV1/CineScope",
  },
  {
    id: "fleet-manager",
    title: "AIRCRAFT FLEET MANAGER",
    category: "FULL-STACK",
    tags: ["React 18", "TypeScript", "Redux Toolkit", "Material UI", "Tailwind CSS", "C#", "ASP.NET Core", ".NET 8", "Entity Framework Core", "MySQL"],
    short: "Aviation maintenance tracking system with React frontend, ASP.NET Core REST API, and Entity Framework persistence. Domain-specific design informed by real F-22 maintenance background.",
    expanded: "React 18 frontend with Redux Toolkit state management, Material UI components, Formik/Yup form validation, and Axios API integration. Full CRUD component suite for aircraft listing, details, creation, editing, and deletion.\n\nASP.NET Core .NET 8 backend with Entity Framework Core migrations and MySQL database. Custom error handling middleware and status code configuration. RESTful endpoints for aircraft CRUD operations.\n\nPostman API documentation. Responsive UI with both Material UI and Tailwind CSS styling. SASS preprocessing for custom styles.",
    github: "https://github.com/omniV1/GCU_SWE_2023-2025/tree/main/CST-391-Web_dev/src/Milestone",
  },
  {
    id: "os-fundamentals",
    title: "OS FUNDAMENTALS",
    category: "SYSTEMS",
    tags: ["C", "Bash", "GCC", "Make", "Unix"],
    short: "Low-level systems programming: CPU scheduling simulators (FCFS, SJF, priority, round-robin), IPC via pipes/signals/shared memory, and synchronization with mutexes and semaphores.",
    expanded: "Scheduling experiments comparing FCFS, SJF, priority, and round-robin algorithms with performance analysis. IPC labs using pipes and signals for process coordination, shared memory, and message queues.\n\nSynchronization exercises demonstrating data races, mutex locks, and semaphore-based solutions. Memory management implementations covering paging, segmentation, and page replacement algorithms.\n\nFilesystem work with directories, inodes, permissions, and I/O buffering. Built with gcc/clang and Make build system on Unix environments.",
    github: "https://github.com/omniV1/GCU_SWE_2023-2025/tree/main/CST-321-Operating-system-fundamentals",
  },
];

const categoryColors: Record<string, string> = {
  ENTERPRISE: "text-accent",
  "ML-AI": "text-primary",
  "FULL-STACK": "text-secondary",
  SYSTEMS: "text-muted-foreground",
};

function ProjectCard({ project, index }: { project: Project; index: number }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <HudCard label={`N${String(index + 1).padStart(2, "0")}`}>
      <div className="p-5 md:p-6">
        {/* Category + Live badge */}
        <div className="flex items-center gap-3 mb-2">
          <span
            className={`tracking-widest ${categoryColors[project.category] || "text-muted-foreground"}`}
            style={{
              fontSize: "0.55rem",
              fontFamily: "'Space Grotesk', sans-serif",
              letterSpacing: "0.15em",
            }}
          >
            {project.category}
          </span>
          {project.liveUrl && (
            <span
              className="tracking-widest text-accent"
              style={{
                fontSize: "0.55rem",
                fontFamily: "'Space Grotesk', sans-serif",
                letterSpacing: "0.15em",
                textShadow: "0 0 6px rgba(255,45,107,0.4)",
              }}
            >
              :: LIVE
            </span>
          )}
        </div>

        {/* Title */}
        <h3
          className="text-foreground mt-2 mb-3"
          style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: "1.5rem", letterSpacing: "0.04em" }}
        >
          {project.title}
        </h3>

        {/* Tags */}
        <div className="flex flex-wrap gap-1.5 mb-4">
          {project.tags.map((tag) => (
            <span
              key={tag}
              className="px-2 py-0.5 bg-primary/5 text-primary/60 border border-primary/10"
              style={{ fontSize: "0.58rem", fontFamily: "'IBM Plex Mono', monospace" }}
            >
              {tag}
            </span>
          ))}
        </div>

        {/* Short description */}
        <p className="text-foreground/60 mb-4" style={{ fontSize: "0.78rem", lineHeight: 1.7 }}>
          {project.short}
        </p>

        {/* Live URL */}
        {project.liveUrl && (
          <a
            href={project.liveUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 mb-3 text-accent hover:underline"
            style={{
              fontSize: "0.68rem",
              fontFamily: "'IBM Plex Mono', monospace",
              textShadow: "0 0 6px rgba(255,45,107,0.3)",
            }}
          >
            <ExternalLink size={12} />
            LIVE :: lunaracare.org
          </a>
        )}

        {/* Expand toggle */}
        {project.expanded && (
          <button
            onClick={() => setExpanded(!expanded)}
            className="flex items-center gap-1.5 text-primary/70 hover:text-primary transition-colors duration-150"
            style={{ fontSize: "0.68rem", fontFamily: "'IBM Plex Mono', monospace" }}
          >
            [ {expanded ? "COLLAPSE" : "EXPAND DETAILS"} ]
            <ChevronDown
              size={12}
              className={`transition-transform duration-150 ${expanded ? "rotate-180" : ""}`}
            />
          </button>
        )}

        {/* Expanded content */}
        <AnimatePresence>
          {expanded && project.expanded && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: "auto", opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.15, ease: "easeOut" }}
              className="overflow-hidden"
            >
              <div className="mt-4 pt-4 border-t border-border">
                <p className="text-foreground/50 mb-4 whitespace-pre-line" style={{ fontSize: "0.75rem", lineHeight: 1.8 }}>
                  {project.expanded}
                </p>
                <a
                  href={project.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 text-primary/70 hover:text-primary transition-colors duration-150"
                  style={{ fontSize: "0.68rem", fontFamily: "'IBM Plex Mono', monospace" }}
                >
                  <ExternalLink size={12} />
                  VIEW ON GITHUB
                </a>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* GitHub link for non-expandable */}
        {!project.expanded && (
          <a
            href={project.github}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 text-primary/70 hover:text-primary transition-colors duration-150"
            style={{ fontSize: "0.68rem", fontFamily: "'IBM Plex Mono', monospace" }}
          >
            <ExternalLink size={12} />
            VIEW ON GITHUB
          </a>
        )}
      </div>
    </HudCard>
  );
}

export function ProjectsPage() {
  return (
    <div className="py-24 px-6 md:px-20">
      <div className="max-w-[1200px] mx-auto">
        <FadeIn>
          <div className="mb-4">
            <span
              className="text-primary"
              style={{
                fontFamily: "'IBM Plex Mono', monospace",
                fontSize: "0.75rem",
                textShadow: "0 0 8px rgba(0,255,212,0.4)",
              }}
            >
              // ALL PROJECTS
            </span>
          </div>
          <h1
            className="mb-3"
            style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: "clamp(2.5rem, 6vw, 4rem)", letterSpacing: "0.04em", color: "#D4DEE8" }}
          >
            PROJECT INDEX
          </h1>
          <p className="text-muted-foreground mb-12" style={{ fontSize: "0.78rem", lineHeight: 1.7 }}>
            Full project index — click any entry for technical details.
          </p>
        </FadeIn>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {allProjects.map((project, i) => (
            <FadeIn key={project.id} delay={i * 0.06}>
              <ProjectCard project={project} index={i} />
            </FadeIn>
          ))}
        </div>
      </div>
    </div>
  );
}
