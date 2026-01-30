# Code Quality Analysis Report

**Generated:** 2026-01-29T19:12:13.249790
**Directory:** `/run/media/omniv/T7/GCU_SWE_2023-2025`

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Files Analyzed | 1545 |
| Overall Pass Rate | 77.8% |
| Bug Gate Pass Rate | 80.6% |
| Vulnerability Gate Pass Rate | 90.1% |

## 🔴 Critical Security Findings

### SQL Injection

- **Severity:** CRITICAL
- **Files Affected:** 63
- **CWE:** CWE-89
- **OWASP:** A03:2021 Injection
- **Description:** User input directly concatenated into SQL queries
- **Recommendation:** Use parameterized queries or prepared statements
- **Example Fix:** `cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))`

**Affected Files:**
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/highlightr-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-banners/main.js` (2 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-book-search-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-media-db-plugin/main.js` (4 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-style-settings/main.js` (3 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/scribe/main.js` (6 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/templater-obsidian/main.js` (8 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/obsidian-style-settings/main.js` (3 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/scribe/main.js` (6 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/highlightr-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/obsidian-banners/main.js` (2 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/obsidian-book-search-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/obsidian-media-db-plugin/main.js` (4 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/obsidian-style-settings/main.js` (3 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/scribe/main.js` (6 occurrences)
- *... and 48 more files*

### Eval/Exec Usage

- **Severity:** CRITICAL
- **Files Affected:** 101
- **CWE:** CWE-95
- **OWASP:** A03:2021 Injection
- **Description:** Dynamic code execution that can run arbitrary code
- **Recommendation:** Use ast.literal_eval() for data parsing, or refactor to avoid dynamic execution
- **Example Fix:** `Use ast.literal_eval(data) instead of eval(data)`

**Affected Files:**
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/highlightr-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/noteson-publish/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-banners/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-book-search-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-media-db-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-style-settings/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/scribe/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/templater-obsidian/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/voice/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/noteson-publish/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/obsidian-style-settings/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/scribe/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/voice/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/code/Topic-1/AIT-204-Topic1-main/data_generators.py` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-204-Deep-Learning/code/topic-1/ANN/ANN/backend/model_pytorch.py` (1 occurrences)
- *... and 86 more files*

### Command Injection

- **Severity:** CRITICAL
- **Files Affected:** 85
- **CWE:** CWE-78
- **OWASP:** A03:2021 Injection
- **Description:** Shell commands executed with user-controlled input
- **Recommendation:** Use subprocess with shell=False and pass args as list
- **Example Fix:** `subprocess.run(['ls', '-la', directory], shell=False)`

**Affected Files:**
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/highlightr-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/noteson-publish/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-banners/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-book-search-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-media-db-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/obsidian-style-settings/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/scribe/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/.obsidian/plugins/templater-obsidian/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/noteson-publish/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/obsidian-style-settings/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/AIT-104-Data-mining-machine-learning/Python_pandas_machine_learning/.obsidian/plugins/scribe/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/highlightr-plugin/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/noteson-publish/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/obsidian-banners/main.js` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-180-Python/.obsidian/plugins/obsidian-book-search-plugin/main.js` (1 occurrences)
- *... and 70 more files*

### Buffer Overflow Risk

- **Severity:** CRITICAL
- **Files Affected:** 4
- **CWE:** CWE-120
- **OWASP:** A06:2021 Vuln Components
- **Description:** Use of unsafe C functions like strcpy, gets, sprintf
- **Recommendation:** Use safe alternatives: strncpy, fgets, snprintf
- **Example Fix:** `strncpy(dest, src, sizeof(dest) - 1)`

**Affected Files:**
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-321-Operating-system-fundamentals/src/Topic4/src/activity4.c` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-321-Operating-system-fundamentals/src/Topic4/src/mmu.c` (2 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-321-Operating-system-fundamentals/src/Topic6/c_programs/activity4.c` (1 occurrences)
- `/run/media/omniv/T7/GCU_SWE_2023-2025/CST-321-Operating-system-fundamentals/src/Topic6/c_programs/mmu.c` (2 occurrences)

## 🟠 High Severity Findings

### XSS Risk

- **Files Affected:** 43
- **CWE:** CWE-79
- **Recommendation:** Sanitize input or use safe DOM methods like textContent

### Prototype Pollution

- **Files Affected:** 37
- **CWE:** CWE-1321
- **Recommendation:** Validate object keys and use Object.create(null) for maps

### Hardcoded Secrets

- **Files Affected:** 28
- **CWE:** CWE-798
- **Recommendation:** Use environment variables or a secrets manager

### Path Traversal

- **Files Affected:** 1
- **CWE:** CWE-22
- **Recommendation:** Validate paths and use os.path.realpath to resolve

### Pickle Deserialization

- **Files Affected:** 4
- **CWE:** CWE-502
- **Recommendation:** Use JSON or implement custom serialization for untrusted data

## 🟡 Code Quality Issues

### High Cyclomatic Complexity

- **Files Affected:** 79
- **Threshold:** 15
- **Impact:** Hard to test, maintain, and understand. Increases bug probability.
- **Recommendation:** Break down into smaller functions, use early returns, extract complex conditions

### Deep Nesting

- **Files Affected:** 246
- **Threshold:** 4
- **Impact:** Reduces readability, makes code flow hard to follow.
- **Recommendation:** Use guard clauses, extract methods, or flatten logic with early returns

## Language Breakdown

| Language | Total | Passed | Failed | Pass Rate |
|----------|-------|--------|--------|-----------|
| Python | 460 | 395 | 65 | 85.9% |
| Java | 337 | 290 | 47 | 86.1% |
| Csharp | 291 | 191 | 100 | 65.6% |
| Javascript | 220 | 114 | 106 | 51.8% |
| Typescript | 198 | 177 | 21 | 89.4% |
| C | 38 | 34 | 4 | 89.5% |
| Cpp | 1 | 1 | 0 | 100.0% |
