# Oracle Cloud Infrastructure Deployment — Adapted to Render

**Laboratory Completion Report (Instructor-Approved Substitution)**  
**GCU Cloud-App (Spring Boot + MySQL) — Render Web Service**

| Field | Value |
| --- | --- |
| **Date completed** | *YYYY-MM-DD* |
| **Course** | CST-323 Cloud Computing |
| **Instructor** | Professor Sluiter |
| **Author** | Owen Lindsey |
| **Substitution note** | OCI account unavailable per instructor; this report maps the OCI Container Instances + MDS workflow to **Render** (PaaS) while preserving learning goals where applicable. |
| **Application** | `code/topic-2/cloud-app` (Orders4U, `com.gcu:cloud-app:1.0.0`) |
| **Java / Spring Boot** | Eclipse Temurin 17 / Spring Boot 3.2.0 |
| **Container** | Docker image (see project `dockerfile` / `Dockerfile.local`) |
| **Live URL** | *`https://<your-service>.onrender.com`* |

---

## Contents

1. [Introduction and mapping (OCI → Render)](#1-introduction-and-mapping-oci--render)  
2. [How this differs from the CI/CD lab (SQL on Render)](#2-how-this-differs-from-the-cicd-lab-sql-on-render)  
3. [Platform comparison: OCI IaaS vs Render PaaS](#3-platform-comparison-oci-iaas-vs-render-paas)  
4. [Environment setup](#4-environment-setup)  
5. [Networking and security (conceptual vs OCI VCN)](#5-networking-and-security-conceptual-vs-oci-vcn)  
6. [MySQL database (managed or existing cloud MySQL)](#6-mysql-database-managed-or-existing-cloud-mysql)  
7. [Container image for the Orders app](#7-container-image-for-the-orders-app)  
8. [Render Web Service deployment](#8-render-web-service-deployment)  
9. [Verification and CRUD walkthrough](#9-verification-and-crud-walkthrough)  
10. [Troubleshooting](#10-troubleshooting)  
11. [AI collaboration](#11-ai-collaboration)  
12. [Conclusion and relation to the next assignment](#12-conclusion-and-relation-to-the-next-assignment)  

---

## 1 Introduction and mapping (OCI → Render)

This report documents deployment of the same Spring Boot + MySQL **Orders** application used in earlier CST-323 activities. The official curriculum activity targets **Oracle Cloud Infrastructure (OCI)**: manual **VCN**, subnets, security lists, **MySQL Database Service (MDS)**, **Oracle Container Registry (OCIR)**, and **Container Instances**. Because an OCI tenancy was not available, **Render** is used as the compute/runtime platform instead.

**What stays the same pedagogically**

- Containerized Spring Boot application.  
- External configuration via environment variables (`SPRING_DATASOURCE_*`, `PORT`).  
- Managed or cloud-hosted MySQL with JDBC.  
- Verification through browser, logs, and database behavior (CRUD).

**What changes when substituting Render**

| OCI concept | Render analogue |
| --- | --- |
| VCN, subnets, route tables, security lists | Render-managed network; HTTPS and routing handled by the platform |
| Internet gateway / public IP on compute | Public `https://*.onrender.com` URL |
| OCIR + `docker push` | Same image can be built locally **or** pushed to **GHCR** (see CI/CD lab) and referenced by URL |
| Container Instances | **Web Service** from **Existing Image** |
| MDS in private subnet + bastion / SSH tunnel | **MySQL hosted elsewhere** (see Section 6) — Render’s first-party database product is **PostgreSQL**, not MySQL |

---

## 2 How this differs from the CI/CD lab (SQL on Render)

The **Automated CI/CD Pipeline** lesson uses a small **Comments** sample application with an **in-memory** data store. The Render instructions for that lab explicitly state that **no database** and **no `SPRING_DATASOURCE_*` environment variables** are required for versions v0–v4. The pipeline is: **Git push → GitHub Actions → GHCR → Render (pull image)**.

The **Orders (cloud-app)** activity is **not** the same shape:

- It **requires MySQL** for login, orders, and Spring Security’s `UserDetailsService`.  
- You **must** set `SPRING_DATASOURCE_URL`, `SPRING_DATASOURCE_USERNAME`, and `SPRING_DATASOURCE_PASSWORD` on Render (and use a JDBC URL appropriate for **network reachability** from Render’s infrastructure).  
- The **Comments** CI/CD lab does **not** answer “where does MySQL live?” for Orders; Section 6 below does.

**Practical sequencing**

- You may deploy Orders to Render **before** the CI/CD lab (manual image build and registry of your choice), or **reuse** the GHCR image from the CI/CD lab as the Render **Existing Image** URL — the SQL requirement is independent of *how* the image is built.

---

## 3 Platform comparison: OCI IaaS vs Render PaaS

| Topic | OCI (original activity) | Render (this substitution) |
| --- | --- | --- |
| Deployment style | IaaS-first: design network, then compute/containers | PaaS: define service, image, env vars |
| MySQL | Oracle MDS, often private IP + bastion | Bring your own MySQL-compatible host (or reuse GCP/AWS/Azure MySQL from prior activities if still available) |
| Container registry | OCIR | GHCR, Docker Hub, or other registry Render can pull from |
| Ingress (port 8080) | Security lists / NSGs | Platform proxy; set `PORT` if required (Spring Boot already uses `${PORT:8080}`) |
| TLS | Configure or terminate yourself | HTTPS on `*.onrender.com` |

---

## 4 Environment setup

### 4.1 Local tools

**Listing 1 — Versions to record in this report**

```text
java --version
mvn -v
docker version
```

**Screenshot 1 —** Local toolchain. Terminal output showing Java 17, Maven, and Docker available for building and testing the container image.

### 4.2 Render account

Sign up at [https://render.com](https://render.com) (e.g. with GitHub). No OCI CLI or VCN wizard is required for this substitution.

---

## 5 Networking and security (conceptual vs OCI VCN)

On OCI, you would create a **VCN** (e.g. `10.0.0.0/16`), **public** and **private** subnets, an **internet gateway**, **route rules** (`0.0.0.0/0` → IGW), and **ingress** rules for TCP **8080** (application) and **3306** (database, scoped to the app subnet).

On **Render**, you do not configure a customer VCN. Instead, document the **logical** security model in your own words for the rubric:

- **Application:** reachable at the public Render URL; Spring Boot listens on the port provided by Render (`PORT`).  
- **Database:** should **not** be exposed to the whole internet with open `0.0.0.0/0` on 3306 in production; for a class project, if you use a cloud MySQL with authorized networks or a managed firewall, describe which IPs or networks you allowed and why.

**Screenshot 2 —** Render service dashboard. Web Service in **Live** state showing the service name and public URL.

---

## 6 MySQL database (managed or existing cloud MySQL)

Render’s native managed database in the CI/CD lab materials is **PostgreSQL**. The **cloud-app** project is wired for **MySQL** (`mysql-connector-j`, MySQL dialect in properties). For this activity, pick **one** of these approaches (confirm with your instructor if unsure):

**Option A — Reuse prior cloud MySQL (recommended if still running)**  
If you still have **Google Cloud SQL**, **AWS RDS**, or **Azure Database for MySQL** from Activities 3–6:

- Use the **public** connectivity method your provider documents (authorized networks / security groups).  
- Add Render’s outbound IPs or use a tunnel/VPN only if your instructor requires stricter isolation.  
- Set JDBC URL to a **standard** MySQL URL, **not** the Google Socket Factory URL, when the app runs on Render:

**Listing 2 — Example JDBC URL shape (replace host, db name, and SSL parameters per provider)**

```text
jdbc:mysql://<mysql-host>:3306/ordersdb?useSSL=true&serverTimezone=UTC
```

Remove or avoid relying on `socketFactory=com.google.cloud.sql.mysql.SocketFactory` on Render unless you are still running on GCP with the correct sidecar/setup.

**Option B — Separate MySQL host (student-friendly providers)**  
Provision MySQL from a provider that offers a **public hostname** and **TLS** or IP allowlisting; create schema `ordersdb` and tables consistent with your app (or let `ddl-auto` match your instructor’s expectations).

**Option C — Switching to Render PostgreSQL**  
Would require **code and dependency changes** (PostgreSQL driver, dialect, possible schema tweaks). Only use if explicitly approved; it is **not** a drop-in substitute for the OCI MySQL activity.

**Screenshot 3 —** MySQL / cloud database console. Evidence of instance running, database `ordersdb`, and connectivity settings (host, port, authorized networks) relevant to Render.

**Screenshot 4 —** Schema / tables. `USERS` and `ORDERS` (or equivalent) present — matches Spring Data JDBC entities in `cloud-app`.

---

## 7 Container image for the Orders app

### 7.1 Build context

Project root: `CST-323-Cloud-Computing/code/topic-2/cloud-app`.

**Listing 3 — Local build and Docker build (from project root)**

```bash
./mvnw clean package -DskipTests
docker build -f dockerfile -t orders-app:latest .
```

Alternatively, use `Dockerfile.local` after Maven produces `target/cloud-app-1.0.0.jar` (see file comments in repo).

### 7.2 Image registry

- **OCI activity:** `docker tag` / `docker push` to **OCIR**.  
- **This report:** Push to **GHCR** (aligns with CI/CD lab) or another registry Render accepts; make the package **public** or configure registry credentials in Render if private.

**Listing 4 — Example tag and push to GHCR (replace owner and image name)**

```bash
docker tag orders-app:latest ghcr.io/<github-username>/<image-name>:v1
docker push ghcr.io/<github-username>/<image-name>:v1
```

**Screenshot 5 —** Registry. GHCR package page or `docker push` success output showing image tag available for pull.

---

## 8 Render Web Service deployment

1. Render Dashboard → **New** → **Web Service**.  
2. Source: **Existing Image** (not “Build from repo” unless you choose that path).  
3. **Image URL:** e.g. `ghcr.io/<owner>/<image>:v1`.  
4. Instance type: **Free** (expect cold starts).  
5. **Environment variables** (minimum):

| Variable | Purpose |
| --- | --- |
| `SPRING_DATASOURCE_URL` | Full JDBC URL to MySQL (Section 6) |
| `SPRING_DATASOURCE_USERNAME` | Database user |
| `SPRING_DATASOURCE_PASSWORD` | Database password (use Render **Secret** type if available) |
| `SERVER_PORT` or rely on Render | Spring Boot uses `server.port=${PORT:8080}` — ensure compatibility with Render’s `PORT` |

6. Health check: optional path such as `/actuator/health` if exposed and secured appropriately.

**Screenshot 6 —** Render environment variables. Redact passwords in the PDF; show variable *names* and non-secret values only.

**Screenshot 7 —** Deploy logs. Spring Boot started; no Hikari / communications link failure.

---

## 9 Verification and CRUD walkthrough

Complete at least: login, list orders, view one order, create, edit, delete — mirroring the Docker lab report’s CRUD narrative but against the **deployed** URL.

**Screenshot 8 —** Login page at `https://<service>.onrender.com/users/login`.

**Screenshot 9 —** Orders list after authentication (data from cloud MySQL).

**Screenshot 10 —** One create or update operation with caption describing the persisted change.

---

## 10 Troubleshooting

| Symptom | Likely cause | What to verify |
| --- | --- | --- |
| `Communications link failure` / Hikari pool fails | DB unreachable from Render | Hostname, port, firewall / authorized networks, SSL params |
| `Access denied for user` | Wrong credentials | Env vars on Render match database user |
| App sleeps / first request slow | Free tier spin-down | Normal; note in report |
| Wrong JDBC driver path for cloud | Google Socket Factory URL on non-GCP | Use standard `jdbc:mysql://...` for cross-cloud MySQL |

---

## 11 AI collaboration

### 11.1 Prompt explored

*Choose one from the OCI activity (e.g. private subnet + bastion vs public DB security/cost trade-offs; or Container Instances vs OKE; or cross-cloud comparison). Paste your prompt here.*

### 11.2 Summary (150–200 words, your own words)

*Write your summary here after your conversation.*

---

## 12 Conclusion and relation to the next assignment

**What you accomplished (OCI rubric alignment in plain terms)**

- Compared **IaaS-style** (OCI: VCN, MDS, container on customer network) with **PaaS-style** (Render: managed routing, no VCN homework).  
- Deployed a **Dockerized** Spring Boot app with **environment-driven** datasource configuration.  
- Connected to **MySQL** using JDBC and verified behavior in the browser.

**Relation to the CI/CD lab**

- The next lesson automates **build → GHCR → deploy** with GitHub Actions and optional **Render deploy hook**.  
- The Comments app does **not** use SQL initially; the **Orders** app does — when you add the pipeline, you still keep Section 6’s MySQL hosting decision and only change *how* the image reaches Render.

---

*Completed: [date] — CST-323 Cloud Computing*
