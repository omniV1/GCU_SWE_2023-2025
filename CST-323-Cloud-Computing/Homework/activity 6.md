---
title: Activity 6 — Deploy to Google Cloud
course: CST-323
instructor: Professor Sluiter
author: Owen Lindsey
date: 2026-03-08
tags:
  - cloud-computing
  - google-cloud
  - spring-boot
  - mysql
  - cloud-run
  - cloud-sql
aliases:
  - Activity 6
---

<style>
@media print {
  body { font-size: 11px; line-height: 1.35; }
  h1 { font-size: 22px; margin: 0.3em 0; }
  h2 { font-size: 18px; margin: 0.3em 0; }
  h3 { font-size: 15px; margin: 0.2em 0; }
  h4 { font-size: 13px; margin: 0.2em 0; }
  p, li, td, th, blockquote { font-size: 11px; line-height: 1.35; }
  blockquote { margin: 0.3em 0; padding: 0.2em 0.6em; }
  table { font-size: 10px; margin: 0.3em 0; }
  th, td { padding: 2px 6px; }
  img { max-height: 280px; width: auto; display: block; margin: 0.3em auto; }
  pre, code { font-size: 10px; }
  pre { margin: 0.3em 0; padding: 0.3em; }
  hr { margin: 0.3em 0; }
  ul, ol { margin: 0.3em 0; padding-left: 1.4em; }
  .page-break { page-break-after: always; }
  table { page-break-inside: avoid; }
  img { page-break-inside: avoid; }
}
</style>

# Activity 6 — Deploy to Google Cloud

## Orders4U Google Cloud Deployment

---

|                |                                                                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Author**     | Owen Lindsey                                                                                                                         |
| **Course**     | CST-323 Cloud Computing                                                                                                              |
| **Instructor** | Professor Sluiter                                                                                                                    |
| **Date**       | 08 March 2026                                                                                                                        |
| **Links**      | Application URLs<br><br>- **Production:** [Orders App](https://orderapp-930760042677.us-south1.run.app/users/login)<br>             |

---

## Table of Contents

- [Section 1: Google Cloud Project Setup](#section-1-google-cloud-project-setup)
- [Section 2: Cloud SQL MySQL Database Setup](#section-2-cloud-sql-mysql-database-setup)
- [Section 3: Spring Boot & Deployment Configuration](#section-3-spring-boot--deployment-configuration)
- [Section 4: Cloud Run Deployment](#section-4-cloud-run-deployment)
- [Section 5: Testing and Verification](#section-5-testing-and-verification)
- [Section 6: AI Exploration Summary](#section-6-ai-exploration-summary)
- [Section 7: Reflection](#section-7-reflection)

---

<div style="page-break-after: always;"></div>

## Section 1: Google Cloud Project Setup

### 1.1 Project & Account Configuration

A Google Cloud account was configured using the $300 free trial credit. A new project named `CST323-SpringBoot` was created as the container for all cloud resources used in this activity. Cloud SQL and Cloud Run were provisioned inside this project.

**Verification Checklist:**
- [x] Google Cloud account active with $300 free trial
- [x] Project `CST323-SpringBoot` created
- [x] Billing account linked and free trial confirmed
- [x] Region selected: **us-south1** (Cloud Run) / **us-west1** (Cloud SQL)
- [x] Cloud SQL Admin API enabled
- [x] Cloud Run API enabled
- [x] Cloud Build API enabled

**Google Cloud vs. Other Providers:**

| Concept            | Google Cloud      | AWS                     | Azure                         |
| ------------------ | ----------------- | ----------------------- | ----------------------------- |
| Managed MySQL      | Cloud SQL         | Amazon RDS              | Azure Database for MySQL      |
| Containerized PaaS | Cloud Run         | Elastic Beanstalk       | Azure App Service             |
| CI/CD Build        | Cloud Build       | CodeBuild               | Azure DevOps Pipelines        |
| Container Registry | Artifact Registry | Amazon ECR              | Azure Container Registry      |
| Resource Grouping  | Project           | EB Application + Env    | Resource Group                |
| Environment Vars   | Cloud Run `--set-env-vars` | EB Environment Properties | App Service Application Settings |

---

<div style="page-break-after: always;"></div>

## Section 2: Cloud SQL MySQL Database Setup

### 2.1 Cloud SQL Instances Dashboard

> **Caption:** The Google Cloud SQL instances dashboard showing the `ordersdb` Cloud SQL instance with status "Running." The instance is a MySQL 8.0 Sandbox edition hosted in the us-west1 region on a shared-core machine type with HDD storage — the most cost-effective configuration for a student project. This managed database instance serves as the backend for the Orders4U Spring Boot application and replaces the local MAMP/MySQL server used during earlier development.

![[Pasted image 20260303213405.png]]

**Cloud SQL Instance Overview:**

| Setting         | Value        |
| --------------- | ------------ |
| Instance ID     | ordersdb     |
| Status          | Running      |
| Database Engine | MySQL 8.0    |
| Edition         | Sandbox      |
| Region          | us-west1     |
| Machine Type    | Shared-core  |
| Storage Type    | HDD          |

---

<div style="page-break-after: always;"></div>

### 2.2 Instance Connection Information

> **Caption:** The Overview tab of the Cloud SQL instance displaying the connection name, public IP address, and connection summary panel. The connection name — formatted as `<project-id>:<region>:<instance-name>` — is the identifier used in the Cloud SQL Socket Factory JDBC URL so that Cloud Run can locate and tunnel into the database without needing a direct public IP. The public IP address is separately used by MySQL Workbench on the developer's machine to import the schema and seed data.

![[Pasted image 20260303213522.png]]

**Connectivity Configuration:**

| Setting              | Value                                                             |
| -------------------- | ----------------------------------------------------------------- |
| Connection Name      | `cst323-springboot:us-west1:<instance-name>`                      |
| Public IP            | Listed in console (used by MySQL Workbench)                       |
| Port                 | 3306                                                              |
| Authorized Networks  | Developer's current IP added for local Workbench access           |
| Private IP           | Not enabled (simplified for class use)                            |

> **Note:** The authorized network IP must be updated whenever the development machine moves to a new network (home, classroom, café), since each network assigns a different public IP to the laptop.

---

<div style="page-break-after: always;"></div>

### 2.3 Database Schema — ordersdb

> **Caption:** The Cloud SQL Databases tab showing the `ordersdb` schema successfully created within the Cloud SQL instance. The database uses the `utf8mb4` character set, which is the MySQL 8.0 default and provides full Unicode support for all modern characters. The ORDERS and USERS tables from the local development database were imported into this schema via MySQL Workbench after the authorized network rule was added to allow the laptop's IP.

![[Pasted image 20260303213152.png]]

**Database Configuration:**

| Property      | Value          |
| ------------- | -------------- |
| Database Name | ordersdb       |
| Character Set | utf8mb4        |
| Tables        | ORDERS, USERS  |

**Why utf8mb4?**
- Full Unicode support for all modern language characters and emoji (older `utf8` misses some 4-byte characters)
- Industry standard and the default in MySQL 8.0 and all modern frameworks including Spring Boot and Hibernate
- Prevents data corruption when saving multilingual or special-character data

**Verification Checklist:**
- [x] Cloud SQL instance created and status is "Running"
- [x] `ordersdb` database created with `utf8mb4` encoding
- [x] Public IP authorized for developer machine Workbench access
- [x] MySQL Workbench connection test passed (SSL: Require)
- [x] ORDERS and USERS data imported from local MySQL instance

---

<div style="page-break-after: always;"></div>

## Section 3: Spring Boot & Deployment Configuration

### 3.1 Key Dependencies (pom.xml)

Two critical dependencies were added to connect the Spring Boot application to Cloud SQL. The Cloud SQL Socket Factory replaces direct public-IP connections with an authenticated internal tunnel, which is required because Cloud Run containers run in a managed sandbox with no direct external network access.

| Dependency                                                        | Purpose                                                                        |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `com.mysql:mysql-connector-j:8.3.0`                              | MySQL 8.x JDBC driver compatible with the Cloud SQL connector                  |
| `com.google.cloud.sql:mysql-socket-factory-connector-j-8:1.13.1` | Authenticates and routes connections through Google's internal Cloud SQL API   |
| `spring-boot-starter-web`                                         | Web application framework and embedded Tomcat                                  |
| `spring-boot-starter-data-jpa`                                    | JPA/Hibernate ORM for database access                                          |
| `spring-boot-starter-thymeleaf`                                   | Server-side HTML templating engine                                             |

> **Why the Cloud SQL Socket Factory is required:** If you omit `mysql-socket-factory-connector-j-8`, Spring Boot falls back to the standard MySQL driver, which tries to connect to a public IP like `jdbc:mysql://34.x.x.x:3306/ordersdb`. Cloud Run cannot reach that IP — it returns `Communications link failure` or `Connection refused` because it has no direct external network path to the database. The Socket Factory instead authenticates via the Cloud Run service account and tunnels the connection through Google's private network.

---

### 3.2 Deployment Configuration (Dockerfile + Cloud Build)

Rather than App Engine's `app.yaml`, this project was containerized and deployed to **Cloud Run** via **Cloud Build**. A `Dockerfile` in the project root packages the Spring Boot JAR into a container image. Cloud Build compiles and pushes the image to Artifact Registry; Cloud Run serves the container over HTTPS.

**Environment Variables (injected at Cloud Run deploy time):**

| Variable                          | Purpose                                                      |
| --------------------------------- | ------------------------------------------------------------ |
| `SPRING_DATASOURCE_URL`           | JDBC URL using the Cloud SQL Socket Factory                  |
| `SPRING_DATASOURCE_USERNAME`      | MySQL username                                               |
| `SPRING_DATASOURCE_PASSWORD`      | MySQL password (sensitive — not stored in source code)       |
| `SPRING_JPA_HIBERNATE_DDL_AUTO`   | `update` — creates/updates tables on application startup     |
| `SPRING_JPA_DATABASE_PLATFORM`    | `org.hibernate.dialect.MySQLDialect`                         |

**application.properties (environment variable placeholders):**

```properties
server.port=${PORT}
spring.datasource.url=${SPRING_DATASOURCE_URL}
spring.datasource.username=${SPRING_DATASOURCE_USERNAME}
spring.datasource.password=${SPRING_DATASOURCE_PASSWORD}
spring.jpa.hibernate.ddl-auto=${SPRING_JPA_HIBERNATE_DDL_AUTO}
spring.jpa.database-platform=${SPRING_JPA_DATABASE_PLATFORM}
```

**Cloud SQL Socket Factory JDBC URL format:**

```
jdbc:mysql://google/ordersdb
  ?socketFactory=com.google.cloud.sql.mysql.SocketFactory
  &cloudSqlInstance=cst323-springboot:us-west1:<instance-name>
  &ipTypes=PUBLIC
  &sslMode=DISABLED
  &serverTimezone=UTC
```

> **Note:** `sslMode=DISABLED` is safe here because the Socket Factory handles encryption internally through Google's private network. If connecting to a public IP directly, `sslMode=REQUIRED` or `VERIFY_IDENTITY` would be necessary.

---

<div style="page-break-after: always;"></div>

## Section 4: Cloud Run Deployment

### 4.1 Cloud Run Service Dashboard

> **Caption:** The Google Cloud Run service dashboard showing the `orderapp` service deployed and running with a healthy status. The service is hosted in the `us-south1` region and receives HTTPS traffic at the public URL `https://orderapp-930760042677.us-south1.run.app`. Cloud Run automatically manages container scaling, HTTPS routing, and TLS certificate provisioning — no virtual machine or server configuration is required. The service scales to zero instances when idle, eliminating compute costs during periods of inactivity.

![[Pasted image 20260303213836.png]]

**Cloud Run Service Summary:**

| Setting         | Value                                                       |
| --------------- | ----------------------------------------------------------- |
| Service Name    | orderapp                                                    |
| Status          | Serving (OK)                                                |
| Region          | us-south1                                                   |
| URL             | `https://orderapp-930760042677.us-south1.run.app`           |
| Deployment      | Cloud Build + Container Image via Artifact Registry         |
| Scaling         | Automatic (min 0, max 2 instances)                          |
| Authentication  | Allow unauthenticated requests (public web app)             |

**Verification Checklist:**
- [x] Cloud Build compiled the project and pushed the container image to Artifact Registry
- [x] Cloud Run service deployed from the container image without errors
- [x] Service URL is publicly accessible over HTTPS
- [x] Cloud SQL connection established via Socket Factory on startup
- [x] Spring Boot application started successfully (confirmed in Cloud Logging)

---

<div style="page-break-after: always;"></div>

## Section 5: Testing and Verification

### 5.1 Login Page

> **Caption:** The Orders4U login page served from the Cloud Run URL (`orderapp-930760042677.us-south1.run.app/users/login`). The Spring Security login form prompts for Username and Password. This confirms the containerized Spring Boot application is running on Cloud Run, the HTTPS endpoint is active, and the Spring Security filter chain is responding correctly — unauthenticated requests are intercepted and redirected to this login page before any protected route is accessible.

![[Pasted image 20260303213932.png]]

---

<div style="page-break-after: always;"></div>

### 5.2 All Orders — Database Read

> **Caption:** The Orders4U inventory dashboard after a successful login, showing all orders loaded from the Cloud SQL MySQL database. Each order appears as a product card with its name, price, and quantity. The data is retrieved by the Spring Boot `OrdersController` via a JPA `findAll()` call routed through the Cloud SQL Socket Factory to the `ordersdb` instance in us-west1. This confirms the full application stack — Cloud Run container → Socket Factory → Cloud SQL — is operating correctly.

![[Pasted image 20260303214034.png]]

**Verification:**
- [x] All orders rendered from Cloud SQL `ordersdb.ORDERS` table
- [x] Product names, prices, and quantities loaded correctly
- [x] Cloud SQL Socket Factory connection active (no connection errors in logs)

---

<div style="page-break-after: always;"></div>

### 5.3 Order Detail View — Single Record Read

> **Caption:** The order detail view for a specific order showing the Order Number, Product Name, Price, and Quantity alongside Edit, Delete, and Back action buttons. This demonstrates a READ operation on a single record: the `OrdersController` calls JPA's `findById()` with the order's primary key, and the result is rendered by the Thymeleaf view template. The page is served from the Cloud Run container connected to the Cloud SQL instance.

![[Pasted image 20260303214117.png]]

---

<div style="page-break-after: always;"></div>

### 5.4 Delete Order — Database Delete

> **Caption (Confirmation):** The delete action for the "Liquid Luck" order (order number c-777, $8,000). The user clicked the Delete button on the order detail page, triggering a client-side confirmation dialog before the HTTP DELETE request is sent to the Spring Boot controller and the row is removed from the Cloud SQL `ordersdb.ORDERS` table.

![[Pasted image 20260303214226.png]]

<div style="page-break-after: always;"></div>

> **Caption (Result):** The inventory page after "Liquid Luck" has been successfully deleted. The order no longer appears among the product cards, confirming the DELETE operation was committed to the Cloud SQL database and the subsequent `findAll()` query correctly excludes the removed record.

![[Pasted image 20260303214312.png]]

**Verification:**
- [x] Delete confirmation fires before committing the database operation
- [x] Order removed from Cloud SQL `ordersdb.ORDERS` table
- [x] Inventory page refreshes and omits the deleted order

---

<div style="page-break-after: always;"></div>

### 5.5 Edit Order — Database Update

> **Caption (Before):** The order detail view displaying an order's current values before editing. The Order Number is visible alongside the Product Name, Price, and Quantity. Clicking the Edit button navigates to the update form, which is pre-populated with these values fetched from the Cloud SQL database via a JPA `findById()` call.

![[Pasted image 20260303214415.png]]

<div style="page-break-after: always;"></div>

> **Caption (After):** The order detail view after a successful UPDATE operation. The Order Number has been changed to a new value, confirming that the Spring Boot service layer called the JPA `save()` method and the updated record was committed to the Cloud SQL `ordersdb.ORDERS` table. The detail page re-fetches the order by ID after the update to display the current persisted state.

![[Pasted image 20260303214516.png]]

**Verification:**
- [x] Edit form pre-populated with current Cloud SQL values
- [x] Updated Order Number committed to Cloud SQL
- [x] Detail view reflects the changed value after save

---

<div style="page-break-after: always;"></div>

### 5.6 Create Order — Database Insert

> **Caption:** The "Add Order" form on the live Cloud Run deployment. The form collects Order Number, Product Name, Price, and Quantity. Submitting the form sends a POST request to the Spring Boot `OrdersController`, which calls the JPA `save()` method on a new `Orders` entity and inserts a new row into the Cloud SQL `ordersdb.ORDERS` table.

![[Pasted image 20260303214704.png]]

<div style="page-break-after: always;"></div>

> **Caption:** The inventory dashboard after the new order has been successfully created and saved to Cloud SQL. The newly added order now appears among the existing product cards, confirming the INSERT operation was committed to the database and the subsequent `findAll()` READ query returned the new record in the response.

![[Pasted image 20260303214739.png]]

**Verification:**
- [x] Create form accepts all required order fields
- [x] New order inserted into Cloud SQL `ordersdb.ORDERS` table via JPA `save()`
- [x] Inventory dashboard displays the newly created order on refresh

---

<div style="page-break-after: always;"></div>

### 5.7 Full CRUD Verification Summary

| Operation | Action                          | Result | Evidence                                         |
| --------- | ------------------------------- | ------ | ------------------------------------------------ |
| CREATE    | Add new order via form          | Pass   | New order appears in inventory dashboard         |
| READ      | View all orders (inventory)     | Pass   | All orders loaded from Cloud SQL `ordersdb`      |
| READ      | View single order detail        | Pass   | Individual record rendered by `findById()`       |
| UPDATE    | Edit order number               | Pass   | Updated value persisted to Cloud SQL             |
| DELETE    | Delete "Liquid Luck" (c-777)    | Pass   | Order removed from database and inventory        |

---

<div style="page-break-after: always;"></div>

## Section 6: AI Exploration Summary

### Chosen AI Prompt

**Prompt — Security Hardening & Secret Management**

> "Analyze my `app.yaml` and `application.properties` files to see if secrets and SSL are configured securely. Provide: a checklist to move passwords and secrets out of code into Google Secret Manager; JDBC URL examples for `sslMode=REQUIRED`, `VERIFY_CA`, `VERIFY_IDENTITY` and when to use each; steps to restrict Cloud SQL to App Engine/Cloud Run connections using the Cloud SQL Socket Factory; and a 10-item verification list with gcloud commands or console paths to confirm secure deployment."

---

### Key Findings

#### Moving Secrets Out of Configuration Files

Storing the database password in `app.yaml` or as plain Cloud Run environment variables is acceptable for classroom projects but creates risk if the configuration file is ever committed to version control. Google Secret Manager provides a production-grade alternative with an audit trail.

Migration steps the AI provided:

1. **Create a secret:** `gcloud secrets create db-password --data-file=./password.txt`
2. **Grant the Cloud Run service account access:** `gcloud secrets add-iam-policy-binding db-password --member="serviceAccount:<PROJECT_NUMBER>-compute@developer.gserviceaccount.com" --role="roles/secretmanager.secretAccessor"`
3. **Reference it at deploy time:** `gcloud run deploy orderapp --set-secrets=SPRING_DATASOURCE_PASSWORD=db-password:latest`

The application code and `application.properties` `${SPRING_DATASOURCE_PASSWORD}` placeholder require no changes — Cloud Run injects the secret as an environment variable at runtime.

---

#### SSL Mode Options for MySQL Connections

| `sslMode` Value   | Description                                               | When to Use                                                  |
| ----------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| `DISABLED`        | No SSL enforced by the JDBC driver                        | With Cloud SQL Socket Factory only — the connector handles internal encryption |
| `REQUIRED`        | SSL required; server certificate not validated            | Basic encryption without certificate management overhead     |
| `VERIFY_CA`       | SSL + validate the server's certificate authority         | Connecting from outside Google's network with a known CA     |
| `VERIFY_IDENTITY` | SSL + validate CA + validate hostname in certificate      | Production; highest security, prevents man-in-the-middle attacks |

> `sslMode=DISABLED` is safe in this project because the Cloud SQL Socket Factory routes the connection through Google's private network via an authenticated API call — the transport is already encrypted at the network layer. For a direct public-IP connection, `sslMode=VERIFY_IDENTITY` would be required.

---

<div style="page-break-after: always;"></div>

#### 10-Item Security Verification Checklist

| # | Check                                                      | Command / Console Path                                                         |
| - | ---------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1 | Database password not committed to Git                     | `git log --all -p -- app.yaml` (should show no plain-text passwords)          |
| 2 | Cloud Run service account has `cloudsql.client` role       | `gcloud projects get-iam-policy <PROJECT_ID>`                                  |
| 3 | Cloud SQL Socket Factory dependency present in pom.xml     | Verify `mysql-socket-factory-connector-j-8` in `pom.xml`                      |
| 4 | JDBC URL uses Socket Factory, not public IP                | Confirm URL starts with `jdbc:mysql://google/` and includes `socketFactory=...` |
| 5 | Cloud SQL authorized networks limited to developer IPs     | Cloud Console → Cloud SQL → Connections → Authorized Networks                  |
| 6 | Cloud Run service accessible over HTTPS only               | Cloud Console → Cloud Run → Service → Security tab                             |
| 7 | Cloud Run min instances = 0 (no idle cost)                 | Cloud Console → Cloud Run → Service → Edit & Deploy → Capacity                 |
| 8 | Cloud SQL Admin API enabled                                | `gcloud services list --enabled \| grep sqladmin`                              |
| 9 | Logs show successful Spring Boot startup (no DB errors)    | `gcloud run services logs tail orderapp --region=us-south1`                    |
| 10| Service URL returns HTTP 200 at login endpoint             | `curl -I https://orderapp-930760042677.us-south1.run.app/users/login`          |

---

### What I Learned

1. **The Cloud SQL Socket Factory is the correct database connection method for Cloud Run and App Engine** — It handles authentication via the service account and encryption internally, making `sslMode=DISABLED` in the JDBC URL safe. Using a direct public IP URL fails silently because the container sandbox cannot reach it.

2. **Google Secret Manager is a drop-in upgrade from plain environment variables** — Cloud Run injects the secret as an environment variable at runtime; the `${...}` placeholder pattern in `application.properties` works identically regardless of whether the value comes from `--set-env-vars` or `--set-secrets`.

3. **`VERIFY_IDENTITY` is the gold standard for direct MySQL connections** — It validates both the certificate authority and that the hostname in the certificate matches the server, preventing man-in-the-middle attacks. This is the right setting for any non-Socket-Factory connection in production.

4. **The `cloudsql.client` IAM role is a required prerequisite** — Without it, the Socket Factory cannot authenticate and all database connections fail with permission errors, regardless of whether the JDBC URL is syntactically correct.

---

<div style="page-break-after: always;"></div>

## Section 7: Reflection

### Deployment Challenges Encountered

**Challenge 1: Cloud SQL Connector vs. Direct Public IP**

The initial `application.properties` used a standard public-IP JDBC URL (`jdbc:mysql://34.x.x.x:3306/ordersdb`). After deploying to Cloud Run, every request returned a `Communications link failure` because the container sandbox cannot open an outbound TCP connection to an external MySQL IP.

**Solution:** Updated the JDBC URL to use the Cloud SQL Socket Factory format (`jdbc:mysql://google/ordersdb?socketFactory=com.google.cloud.sql.mysql.SocketFactory&cloudSqlInstance=<PROJECT>:<REGION>:<INSTANCE>`) and added the `mysql-socket-factory-connector-j-8` Maven dependency. This replaced the failing direct connection with an authenticated tunnel through Google's private Cloud SQL API.

---

**Challenge 2: Cloud Build Dockerfile Configuration**

The initial Cloud Build trigger failed because the `Dockerfile` was named `dockerfile` (lowercase), which Docker does not recognize on case-sensitive Linux filesystems. The Maven wrapper (`mvnw`) also lacked execute permissions, causing the build step to fail with `Permission denied`.

**Solution:** Renamed the file to `Dockerfile` (capital D, the Docker convention) and added a `chmod +x mvnw` command to the Cloud Build steps to mark the Maven wrapper as executable before the build runs. Both fixes were committed together and the subsequent Cloud Build trigger succeeded.

---

**Challenge 3: Cloud Run vs. App Engine Deployment Model**

The assignment guide describes deploying to App Engine using `app.yaml`. This project used Cloud Run instead — a container-based approach where environment variables are passed at deploy time via `gcloud run deploy --set-env-vars` rather than declared in a YAML file. The Spring Boot application itself required no code changes, but the deployment workflow and troubleshooting steps differed from the guide.

**Solution:** Translated each `app.yaml` `env_variables` entry into a `--set-env-vars` flag for the `gcloud run deploy` command. The `application.properties` `${...}` placeholder pattern works identically in both deployment models because Spring Boot reads from the OS environment regardless of how the variables were injected.

---

<div style="page-break-after: always;"></div>

### Google Cloud vs. AWS — Comparative Experience

Deploying Orders4U to Google Cloud after the AWS Elastic Beanstalk deployment in Activity 5 provided a direct comparison between two major cloud platforms using the same Spring Boot + MySQL application.

The database setup steps were structurally identical: provision a managed MySQL instance, set credentials, authorize the developer's IP, import the schema via MySQL Workbench. Cloud SQL and Amazon RDS differ mainly in their access control models — Cloud SQL uses an authorized networks whitelist at the instance level, while RDS uses VPC security group rules. Cloud SQL's approach is simpler for a solo developer; RDS security groups integrate more naturally into complex multi-resource architectures.

The deployment mechanism differed more substantially. Elastic Beanstalk accepted a plain JAR file and handled containerization internally, requiring no Docker knowledge. Cloud Run required an explicit `Dockerfile` and a Cloud Build pipeline — more setup upfront, but the container model is more portable and makes the runtime environment explicit. Both platforms inject environment variables that Spring Boot reads via `${...}` placeholders, so application code was unchanged between deployments.

**Service Equivalency Table:**

| Concept               | Google Cloud                                  | AWS                              |
| --------------------- | --------------------------------------------- | -------------------------------- |
| Managed MySQL         | Cloud SQL (MySQL 8.0, Sandbox)                | Amazon RDS (MySQL 8.4, t4g.micro)|
| PaaS Compute          | Cloud Run (containerized, serverless)         | Elastic Beanstalk (JAR, Corretto)|
| CI/CD Build           | Cloud Build + Artifact Registry               | Console upload or EB CLI         |
| Environment Variables | `gcloud run deploy --set-env-vars`            | EB Environment Properties        |
| Log Inspection        | `gcloud run services logs tail`               | CloudWatch Logs                  |
| DB Connectivity       | Cloud SQL Socket Factory (internal tunnel)    | RDS security group + SSL         |
| Free Tier             | $300 credit (90 days) + Always Free products  | 12-month Free Tier               |

---

### Key Terminology Learned

| Term                      | Definition                                                                                    |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| Cloud SQL                 | Google's managed relational database service supporting MySQL, PostgreSQL, and SQL Server      |
| Cloud Run                 | Google's serverless container platform; scales to zero and manages HTTPS routing automatically |
| Cloud Build               | Google's CI/CD pipeline; compiles source and pushes container images to Artifact Registry     |
| Artifact Registry         | Google's container image repository; stores Docker images built by Cloud Build                |
| Cloud SQL Socket Factory  | Java library that routes Cloud SQL connections through Google's private API instead of a public IP |
| Socket Factory JDBC URL   | `jdbc:mysql://google/<DB>?socketFactory=com.google.cloud.sql.mysql.SocketFactory&cloudSqlInstance=<PROJECT>:<REGION>:<INSTANCE>` |
| Service Account           | Google Cloud identity used by Cloud Run to authenticate with other GCP services (Cloud SQL, Secret Manager) |
| `cloudsql.client` role    | IAM permission required for App Engine or Cloud Run to connect to a Cloud SQL instance        |
| Secret Manager            | Google's managed secrets store; injects credentials as environment variables at runtime        |
| `utf8mb4`                 | MySQL character set with full Unicode support; default in MySQL 8.0                            |

---

### How I Will Approach My Next Cloud Deployment

Having now deployed Orders4U to Azure (Activity 3), AWS (Activity 5), and Google Cloud (Activity 6), three consistent lessons stand out that will shape every future cloud deployment.

First, configure the platform-specific database connector before writing a single line of application code. Every deployment failed initially because the default JDBC driver tried to reach the database over a direct public IP, which PaaS sandboxes block. Cloud SQL requires the Socket Factory; RDS requires the security group and SSL. Getting this right at project initialization eliminates the most common class of deployment failures.

Second, use containerization intentionally. Cloud Run required a `Dockerfile`, which felt like extra work compared to Elastic Beanstalk's JAR upload — but the explicit container definition turned out to be a better debugging artifact. When the build failed, the `Dockerfile` made the root cause obvious. PaaS abstractions that hide the container are convenient until something goes wrong.

Third, keep secrets out of source control from the very first commit. Both AWS and Google Cloud make it straightforward to inject credentials as environment variables at deploy time — there is no reason to put a password anywhere near Git. Secret Manager and EB Environment Properties are both easier to update than rotating exposed credentials after an accidental commit.

---

<div style="page-break-after: always;"></div>

## Appendix: Quick Reference

### Google Cloud Resources Created

| Resource           | Name / Identifier                                          | Type                    | Region    |
| ------------------ | ---------------------------------------------------------- | ----------------------- | --------- |
| Cloud SQL Instance | ordersdb                                                   | MySQL 8.0 Sandbox       | us-west1  |
| Database Schema    | ordersdb                                                   | MySQL Schema            | —         |
| Cloud Run Service  | orderapp                                                   | Cloud Run (Container)   | us-south1 |
| Cloud Build        | Trigger on push                                            | CI/CD Pipeline          | —         |

### Useful Commands

```bash
# Authenticate and initialize
gcloud init
gcloud auth login

# Set the active project
gcloud config set project cst323-springboot

# List all projects
gcloud projects list

# Build the JAR (skip tests for speed)
mvn clean package -DskipTests

# Verify the JAR was created
ls target/*.jar

# Deploy to Cloud Run manually
gcloud run deploy orderapp \
  --image gcr.io/<PROJECT_ID>/orderapp \
  --region us-south1 \
  --platform managed \
  --allow-unauthenticated

# Grant App Engine service account Storage Admin (if using App Engine)
gcloud projects add-iam-policy-binding cst323-springboot \
  --member="serviceAccount:cst323-springboot@appspot.gserviceaccount.com" \
  --role="roles/storage.admin"

# View live Cloud Run logs
gcloud run services logs tail orderapp --region=us-south1

# Read recent logs
gcloud run services logs read orderapp --region=us-south1

# List all Cloud Run services
gcloud run services list
```

### Application URL

- **Production:** https://orderapp-930760042677.us-south1.run.app

### Database Connection

- **Cloud SQL Instance:** `cst323-springboot:us-west1:<instance-name>`
- **Port:** 3306
- **Database:** ordersdb
- **Connection Method:** Cloud SQL Socket Factory (authenticated internal tunnel via service account)
- **MySQL Workbench:** Public IP with SSL = Require + authorized network rule for developer IP

---
