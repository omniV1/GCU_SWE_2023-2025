# Summer Practice

A personal workspace for continued technical study and deliberate practice across the languages and frameworks I work with most often. Originally started during university breaks, it has since become an ongoing portfolio of post-graduation skill development, exploratory builds, and algorithmic problem solving.

## Overview

The repository is organized by language and project type. Each subdirectory is self-contained and reflects a different area of focus, ranging from full-stack application work to language fundamentals and data structures and algorithms practice.

## Contents

| Directory | Description |
| --- | --- |
| `AerospaceAPI/` | Full-stack aviation-themed project. ASP.NET Core Web API (`AircraftMaintenanceAPI/`) with EF Core, DTOs, middleware, and Swagger documentation, paired with a React + TypeScript + Tailwind frontend (`aircraft-maintenance-frontend/`). |
| `C#/` | Console applications and exercises focused on .NET fundamentals, LINQ, and object-oriented design. |
| `Java/` | OOP exercises and small applications covering core language features, collections, and design patterns. |
| `TypeScript/` | Type-safe JavaScript practice including utility types, generics, and small client-side applications. |
| `python/` | Algorithm and data structures practice, including LeetCode-style problems and short experiments. |

## Focus Areas

- **API design and development** — RESTful endpoints, request/response modeling, validation, status code semantics, and API documentation.
- **Full-stack integration** — connecting a typed frontend to a strongly-typed backend with realistic data flows.
- **Language fluency** — maintaining working proficiency across C#, Java, TypeScript, and Python.
- **Algorithms and problem solving** — consistent practice on classic problems to keep interview readiness and analytical thinking sharp.
- **Tooling and workflow** — package managers, build systems, IDE/debugger configuration, and version control hygiene.

## Running the Projects

### AerospaceAPI (backend)

```bash
cd SummerPractice/AerospaceAPI/AircraftMaintenanceAPI
dotnet restore
dotnet ef database update
dotnet run
```

Open Visual Studio and press F5 for the integrated debugger experience.

### AerospaceAPI (frontend)

```bash
cd SummerPractice/AerospaceAPI/aircraft-maintenance-frontend
npm install
npm start
```

### C# console projects

```bash
cd SummerPractice/C#/<Week>
dotnet run
```

### Java exercises

```bash
cd SummerPractice/Java/<week>
javac *.java
java <MainClass>
```

Or import the folder into IntelliJ IDEA or Eclipse.

### TypeScript exercises

```bash
cd SummerPractice/TypeScript/<week>
npm install
npx tsc && node dist/index.js
```

### Python practice

```bash
cd SummerPractice/python
python <script>.py
```

## Purpose

This repository exists to keep my fundamentals sharp, explore patterns across ecosystems, and document my continued growth as an engineer beyond formal coursework. The work here is intentionally varied — small enough to iterate quickly, but representative of the kinds of problems and architectures I care about professionally.
