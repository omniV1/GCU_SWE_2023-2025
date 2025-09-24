# CST-321 — Operating System Fundamentals

Systems programming in C and shell, exploring how operating systems schedule work, manage memory, and provide interprocess communication and filesystems.

## What’s here
- `src/`: Topic folders containing C programs, shell scripts, and experiments
- `Documentation/`: Screenshots and writeups for assignments and milestones
- `Notes/`: Topic notes and references

## Major concepts covered
- Processes and threads: lifecycle, context switching, signals
- CPU scheduling: FCFS, SJF, priority, round-robin; turnaround/response time
- Synchronization: race conditions, mutexes, semaphores, monitors
- Interprocess communication (IPC): pipes, signals, shared memory, message queues
- Memory management: paging/segmentation, page replacement, virtual memory
- Filesystems: directories, inodes, permissions, buffering, I/O
- Shell and toolchain: gcc/clang, make, bash, scripting basics

## Toolchain and prerequisites
- C compiler: gcc/clang
- Make (optional) and bash (WSL/Unix-like recommended on Windows)
- On Windows, using WSL simplifies POSIX APIs and shell tooling

## Build and run
- Simple program:
  - `gcc -Wall -O2 -o program src/topicX/program.c`
  - `./program` (on Windows cmd: `program.exe`)
- With Makefiles (where present):
  - `make` in the topic directory, then run produced binaries

## Highlights
- Scheduling experiments comparing average waiting/turnaround across algorithms
- IPC labs using pipes and signals to coordinate multiple processes
- Synchronization exercises demonstrating data races and fixes with semaphores

## Acknowledgments
- Professor Mark Reha for course materials and guidance
- pandoc for converting Markdown to Word/PDF in documentation
