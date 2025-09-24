# GCU SWE Portfolio (2023–2025)

This is a master repository of coursework, projects, and milestones completed during my Software Engineering program. It aggregates multiple course repos, self‑study work, and capstone/milestone projects across C#, Java, Python, JavaScript/TypeScript, operating systems, databases, and security.

Use the directory index below to navigate by course. Each section lists what the folder contains, technologies used, and notable assignments or milestones. Where available, links point to per‑course READMEs for deeper details.

## Directory Index (by course)

- **AIT-104-Data-mining-machine-learning**: Intro ML and data analysis with Python/pandas.
  - Contents: Jupyter notebooks (linear modeling), weekly learning notes, CSV datasets (`AAPL.csv`, `PLTR.csv`).
  - Highlights: Linear modeling notebooks and curated study notes.

- **CST-150-C#1**: C# I fundamentals with WinForms.
  - Contents: `Milestone_Fall2023` WinForms app with forms (`frmIntro`, `frmCurrentInventory`) and supporting classes.
  - Highlights: Inventory management milestone (WinForms).

- **CST-180-Python**: Python basics and assignments.
  - Contents: Class notes (md/pdf), homework (e.g., `PopulationSimulation`), templates for document generation.

- **CST-201-algorithims-data-structures**: Algorithms and data structures in C#.
  - Contents: Topics 1–5 source trees, documentation per topic, and notes.
  - Highlights: String matching, searching/sorting topics, and applied exercises.

- **CST-239-Java2**: Java II OOP and application development.
  - Contents: Activities and multi‑part milestone work; documentation and presentations.
  - Highlights: Later milestones (6–7) with larger application builds.

- **CST-250-C#2**: C# II with OOP, recursion, file I/O, and GUI basics.
  - Contents:
    - Activities: `AnimalClasses` (inheritance/interfaces), `ChessBoardConsoleApp` and `ChessBoardGuiApp` (WinForms), `TextFileDataAccessDemo` (file I/O), `Activity3_Recursion` (CountToOne, Factorial, GCD, Knight’s Tour).
    - Milestone: Minesweeper (console and WinForms GUI) with flood fill, flags, and high scores.
  - Highlights: Minesweeper GUI milestone; chessboard movement logic; recursion exercises.

- **CST-321-Operating-system-fundamentals**: OS concepts and systems programming in C.
  - Contents: `src` C projects and shell scripts; extensive documentation and notes.
  - Read more: `CST-321-Operating-system-fundamentals/README.md`.

- **CST-326-Written-Verbal-Communication-SWE**: Professional communication for SWE.
  - Contents: `CineScopeProduction` (.NET/razor project) and course PDFs.

- **CST-339-Java3**: Enterprise Java (Spring, Maven, MongoDB, Security, Microservices).
  - Contents: Large `workspaceCST-339` with labs and milestone; documentation by topic.
  - Read more: `CST-339-Java3/README.md`.

- **CST-345-Database-Design**: Relational/NoSQL database design and applications.
  - Contents: SQL exercises, Windows/.NET database apps, MongoDB apps, milestone docs.
  - Highlights: MongoMusicApp, Cst‑345 Milestone 2 and 4.

- **CST-350-C#3**: ASP.NET Core MVC, authentication, sessions, and web development in C#.
  - Contents: Topic folders, documentation, and `CST-350-Milestone` web app.
  - Read more: `CST-350-C#3/Readme.md`.

- **CST-391-Web_dev**: JavaScript/TypeScript full‑stack (Node/Express, Angular).
  - Contents: `src` for activities and milestone; `docs` for screenshots/design.
  - Read more: `CST-391-Web_dev/readme.md`.

- **CST-407-Application-Security-Foundations**: AppSec foundations and secure coding.
  - Contents: Assignments, Java coding exercises, security docs and images.
  - Read more: `CST-407-Application-Security-Foundations/README.md`.

- **SummerPractice**: Self‑directed practice and side projects across C#, Java, TS.
  - Contents: `AerospaceAPI`, language‑specific practice folders, and notes.
  - Read more: `SummerPractice/README.md`.

## Notable milestones and brief descriptions

- **CST‑250 Minesweeper (GUI and Console)**: Complete Minesweeper with dynamic bomb placement, neighbor counting, flood‑fill reveal, flagging, timer, and high‑score persistence. Key files: `CST-250-C#2/Code/Milestone/src/MinesweeperGui/MinesweeperGui`.
- **CST‑350 Web App Milestone**: ASP.NET Core application demonstrating MVC patterns, routing, authentication, and session‑driven flows. See `CST-350-C#3/CST-350-Milestone` and course README.
- **CST‑391 Milestone 3 (REST API + Frontends)**: GameCube store REST API with Angular and React frontends, Postman documentation, ER/UML diagrams, and wireframes. See `CST-391-Web_dev/src/Milestone` and course README.
- **CST‑339 Enterprise Topics**: Spring Boot, MVC, Data JDBC/MongoDB, Security, and Microservices culminating in enterprise app modules. See `CST-339-Java3/README.md`.
- **CST‑345 Database Milestones**: Schema design, SQL CRUD, and MongoDB application builds with documentation. See `CST-345-Database-Design`.

## How to navigate and run examples

- Open per‑course solutions/projects in their native tools:
  - C#/.NET: Visual Studio or `dotnet` CLI. Open `.sln` or `.csproj` and run.
  - Java: Open in IntelliJ/Eclipse; use Maven/Gradle where applicable.
  - Node/Angular: `npm install` then `npm start`/`ng serve` from the `src` folder.
  - Python: Open notebooks in Jupyter or VS Code; ensure dependencies installed.
- Each course folder with a README provides deeper setup and run instructions.

## Conventions used in this repo

- Per‑course folders contain `src`/`Code`, `docs`/`Documentation`, and `Notes` where available.
- Screenshots and artifacts live under `docs`/`Documentation` or `screenshots`.
- Multiple .NET solutions are organized per activity/milestone for isolation.

## Organization status and next steps

Some earlier courses are less structured (inconsistent naming, zips, mixed `Readme.md` vs `README.md`). A proposed reorganization plan with concrete steps is in `REPO_ORGANIZATION_PLAN.md`. We will review that plan prior to any structural changes.

## License

See `LICENSE` at the repository root.
