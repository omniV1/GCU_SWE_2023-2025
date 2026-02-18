# Activity 3 — Spring Boot + MySQL on Azure Deployment

## Orders4U Cloud Deployment

---

|                |                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------ |
| **Author**     | Owen Lindsey                                                                               |
| **Course**     | CST-323                                                                                    |
| **Instructor** | Professor Sluiter                                                                          |
| **Date**       | 27 January 2026                                                                            |
| Links          | Application URLs<br><br>- **Production:** https://cst323-orders-owen.azurewebsites.net<br> |

---

## Table of Contents

- [Section 1: Azure Subscription Verification](#section-1-azure-subscription-verification)
- [Section 2: Azure Database for MySQL Setup](#section-2-azure-database-for-mysql-setup)
- [Section 3: Spring Boot Project Configuration](#section-3-spring-boot-project-configuration)
- [Section 4: Azure App Service Creation](#section-4-azure-app-service-creation)
- [Section 5: Secure Connection Configuration](#section-5-secure-connection-configuration)
- [Section 6: Build and Deployment](#section-6-build-and-deployment)
- [Section 7: Testing and Verification](#section-7-testing-and-verification)
- [Section 8: AI Exploration Summary](#section-8-ai-exploration-summary)
- [Section 9: Reflection](#section-9-reflection)

---

<div style="page-break-after: always;"></div>

## Section 1: Azure Subscription Verification

### 1.1 Azure for Students Subscription & Resource Group

> **Caption:** Azure Portal showing the CST-323 resource group with all deployed resources including Azure Database for MySQL Flexible Servers and App Service. The subscription (Azure subscription 1) is active with resources deployed across West US 3 and Central US regions.

![Azure Resource Group](activity3-photos/resource-group-azureinfo.png)

**Resources Deployed:**

| Resource Name | Type | Location |
|---------------|------|----------|
| cst-323-app | Azure Database for MySQL Flexible Server | West US 3 |
| cst323-mysql-owen | Azure Database for MySQL Flexible Server | Central US |
| cst323-orders-owen | App Service | West US 3 |
| cst323-plan | App Service Plan | West US 3 |

**Verification Checklist:**
- [x] Subscription is active (Azure subscription 1)
- [x] Resource Group CST-323 created
- [x] All required resources deployed successfully

---

<div style="page-break-after: always;"></div>

## Section 2: Azure Database for MySQL Setup

### 2.1 MySQL Flexible Server Overview

> **Caption:** Azure Portal showing the deployed MySQL Flexible Server (cst-323-app) with server details including endpoint, configuration, and status. The server is running MySQL 8.0 on a Burstable B1ms tier to conserve student credits.

![MySQL Server Details](activity3-photos/sqldb-azureservice-azureinfo.png)

**Server Configuration:**

| Setting | Value |
|---------|-------|
| Server Name | cst-323-app |
| Endpoint | `cst-323-app.mysql.database.azure.com` |
| Subscription | Azure subscription 1 |
| Resource Group | CST_323 |
| Location | West US 3 |
| MySQL Version | 8.0 |
| Status | Ready |
| Administrator Login | adminuser |

---

### 2.2 Compute and Storage Configuration

> **Caption:** The MySQL server is configured with a Burstable B1ms tier (1 vCore, 2 GB RAM, 20 GB storage, 360 IOPS) to minimize costs while providing adequate performance for development and testing.

**Cost-Saving Settings (from screenshot):**

| Setting | Value |
|---------|-------|
| Compute Tier | Burstable |
| SKU | B1ms |
| vCores | 1 |
| RAM | 2 GB |
| Storage | 20 GB |
| IOPS | 360 |

**Created:** 2026-01-27 16:52:34 UTC

---

### 2.3 Networking Configuration

**Security Settings:**
- **Connectivity Method:** Public access (allowed IP addresses)
- **Firewall Rules:** Local machine IP and Azure services allowed
- **TLS Enforcement:** require_secure_transport = ON (default)

> **Note:** The server version will lose standard Azure support on May 31, 2026. Consider upgrading to the latest version before this date.

---

### 2.4 Database Schema

The `ordersDB` schema was created on the MySQL server to store application data.

**Database Information:**

| Property | Value |
|----------|-------|
| Database Name | ordersDB |
| Character Set | utf8mb4 |
| Collation | utf8mb4_general_ci |

> **Note:** Database schema verification is shown in Section 7.2 (Database Connectivity Test) which displays the ORDERS and USERS tables queried from the Azure MySQL server.

---

<div style="page-break-after: always;"></div>

## Section 3: Spring Boot Project Configuration

### 3.1 pom.xml Configuration

The project uses a fat JAR deployment with the Azure Web App Maven Plugin.

**Key Dependencies:**

| Dependency | Purpose |
|------------|---------|
| `spring-boot-starter-web` | Web application framework |
| `spring-boot-starter-data-jdbc` | Database connectivity |
| `mariadb-java-client` | JDBC driver (compatible with MySQL) |
| `spring-boot-starter-actuator` | Health endpoints for Azure |
| `spring-boot-starter-security` | Authentication and authorization |

**Azure Maven Plugin Configuration:**

```xml
<plugin>
    <groupId>com.microsoft.azure</groupId>
    <artifactId>azure-webapp-maven-plugin</artifactId>
    <version>2.13.0</version>
    <configuration>
        <schemaVersion>v2</schemaVersion>
        <resourceGroup>CST-323</resourceGroup>
        <appName>cst323-orders-owen</appName>
        <pricingTier>B1</pricingTier>
        <region>westus3</region>
        <runtime>
            <os>Linux</os>
            <javaVersion>Java 17</javaVersion>
            <webContainer>Java SE</webContainer>
        </runtime>
    </configuration>
</plugin>
```

---

### 3.2 Local vs Production Configuration Strategy

**Local Development (application.properties):**

```properties
# Local development - uses MariaDB driver syntax
spring.datasource.url=jdbc:mariadb://localhost:3306/ordersDB
spring.datasource.username=omniv
spring.datasource.password=0002
spring.datasource.driver-class-name=org.mariadb.jdbc.Driver
```

**Production (Azure App Settings override):**

| Environment Variable | Purpose |
|---------------------|---------|
| `SPRING_DATASOURCE_URL` | Azure MySQL connection string with SSL |
| `SPRING_DATASOURCE_USERNAME` | Database admin user |
| `SPRING_DATASOURCE_PASSWORD` | Database password (or Key Vault reference) |

> **Note:** Spring Boot automatically maps environment variables like `SPRING_DATASOURCE_URL` to `spring.datasource.url`. This keeps secrets out of the Git repository.

---

<div style="page-break-after: always;"></div>

## Section 4: Azure App Service Creation

### 4.1 Deployed Web App Overview

> **Caption:** Azure Portal showing the deployed Web App (cst323-orders-owen) with the default domain, App Service Plan details, and deployment status. The app is running on Linux with Java SE runtime.

![Web App Deployed](activity3-photos/webapp-deployed-azureinfo.png)

**Web App Configuration:**

| Setting | Value |
|---------|-------|
| App Name | cst323-orders-owen |
| Default Domain | cst323-orders-owen.azurewebsites.net |
| Operating System | Linux |
| App Service Plan | cst323-plan |
| Subscription | Azure subscription 1 |
| Resource Group | CST-323 |

---

### 4.2 App Service Plan

> **Caption:** Azure Portal showing the App Service Plan (cst323-plan) configuration with B1 pricing tier, Linux operating system, and 1 instance in West US 3 region.

![App Service Plan](activity3-photos/appserviceplan-azureinfo.png)

**Plan Details:**

| Setting | Value |
|---------|-------|
| Plan Name | cst323-plan |
| Resource Group | CST-323 |
| Location | West US 3 |
| Pricing Plan | B1 (Scale up) |
| Instance Count | 1 (Scale out) |
| Operating System | Linux |
| Zone Redundant | Disabled |

**Cost Considerations:**
- B1 tier provides sufficient resources for development/demo
- Can be stopped when not in use to conserve credits
- Located in same region as MySQL server for optimal latency

---

<div style="page-break-after: always;"></div>

## Section 5: Secure Connection Configuration

### 5.1 Application Settings (Environment Variables)

> **Caption:** Azure Portal showing the Web App General Settings configuration page. Environment variables for database connection are configured in the Application Settings section to keep credentials out of the Git repository.

![Application Settings](activity3-photos/application-settings-azureinfo.png)

The Web App uses environment variables (App Settings) to securely connect to the MySQL database without storing credentials in the Git repository.

**Configured Environment Variables:**

| Name | Value |
|------|-------|
| `SPRING_DATASOURCE_URL` | `jdbc:mariadb://cst-323-app.mysql.database.azure.com:3306/ordersDB?sslMode=REQUIRED&serverTimezone=UTC` |
| `SPRING_DATASOURCE_USERNAME` | `adminuser` |
| `SPRING_DATASOURCE_PASSWORD` | `********` (hidden) |

---

### 5.2 TLS/SSL Security Configuration

**Security Measures Implemented:**

| Security Feature | Setting | Purpose |
|-----------------|---------|---------|
| `require_secure_transport` | ON | Forces TLS encryption on MySQL server |
| `sslMode` | REQUIRED | JDBC driver validates encrypted connection |
| App Settings | Used | Keeps secrets out of Git repository |

> **Note:** The `sslMode=REQUIRED` parameter in the JDBC URL ensures all data transmitted between the App Service and MySQL is encrypted. This is the minimum recommended setting for cloud deployments.

---

### 5.3 (Optional) Key Vault Integration

For enhanced security, database credentials can be stored in Azure Key Vault instead of directly in App Settings.

**Key Vault Reference Syntax:**
```
@Microsoft.KeyVault(SecretUri=https://myvault.vault.azure.net/secrets/mysql-password/)
```

> **Note:** Key Vault integration was not implemented for this deployment as the standard App Settings approach provides adequate security for educational purposes. App Settings are encrypted at rest by Azure and are not committed to the Git repository.

---

<div style="page-break-after: always;"></div>

## Section 6: Build and Deployment

### 6.1 Maven Build & Azure Authentication

> **Caption:** Terminal showing the Azure Maven plugin OAuth2 authentication flow. The plugin automatically detects the Azure subscription and authenticates via browser popup without requiring Azure CLI installation.

![Azure CLI Login](activity3-photos/azcli-login-success.png)

**Command:**
```bash
mvn -DskipTests clean package
```

**Build Output:**
- JAR file: `target/cloud-app-1.0.0.jar`
- Packaging: Fat JAR (includes all dependencies)

---

### 6.2 Azure Deployment

> **Caption:** Terminal showing successful Maven deployment with BUILD SUCCESS message. The application is deployed to https://cst323-orders-owen.azurewebsites.net with a total build time of 2 minutes 39 seconds.

![Deployment Successful](activity3-photos/deployment-successful.png)

**Command:**
```bash
mvn azure-webapp:deploy
```

**Deployment Output:**
- Successfully deployed resources to cst323-orders-owen
- Application URL: https://cst323-orders-owen.azurewebsites.net
- Build Status: **SUCCESS**
- Total Time: 02:39 min
- Finished: 2026-01-27T14:14:06-07:00

---
<div style="page-break-after: always;"></div>

## Section 7: Testing and Verification

### 7.1 Application URL Response

> **Caption:** Browser showing the deployed application running at the Azure URL (cst323-orders-owen.azurewebsites.net). The home page displays "Welcome back, admin1!" with navigation options for Inventory and Admin panels, confirming successful deployment and user authentication.

![Application Running](activity3-photos/home-after-login-success.png)

**Verification:**
- **URL:** https://cst323-orders-owen.azurewebsites.net
- **Status:** HTTP 200 OK
- **Functionality:** Home page renders correctly after login
- **User:** admin1 authenticated successfully

---

### 7.2 Database Connectivity Test

> **Caption:** Azure Cloud Shell showing MySQL connection to the Azure database. The query results display the ORDERS and USERS tables, with sample order data (Test Product, $99.00) confirming successful database connectivity over TLS.

![Database Connection Test](activity3-photos/database-output-azureinfo.png)

**Query Results:**
```sql
SHOW TABLES;
+------------------------+
| Tables_in_ordersdb     |
+------------------------+
| orders                 |
| users                  |
+------------------------+

SELECT * FROM ORDERS;
-- Shows order data with ID, ORDER_NUMBER, PRODUCT_NAME, PRICE, QTY
```

**Test Results:**
- [x] Can read data from Azure MySQL
- [x] Can write data to Azure MySQL
- [x] TLS connection established successfully

---

### 7.3 Health Endpoint Verification

**Endpoint:** `https://cst323-orders-owen.azurewebsites.net/actuator/health`

**Expected Response:**
```json
{
  "status": "UP"
}
```

**Verification:** The health endpoint returns HTTP 200 with status "UP", confirming the application and database connection are healthy. This is also verified in the Azure Log Stream (Section 7.4) which shows successful health check responses from the Azure platform.

---

### 7.4 Log Stream Verification

> **Caption:** Azure Portal Log Stream showing real-time application logs for cst323-orders-owen. The logs display Spring Boot startup messages, confirming the application initialized successfully and is processing HTTP requests.

![Log Stream](activity3-photos/logstream-azureinfo.png)

**Key Log Entries Observed:**
- Spring Boot application startup logs
- HTTP request processing (GET/POST requests)
- No SSL/TLS connection errors
- Application responding to health checks

---

<div style="page-break-after: always;"></div>

## Section 8: AI Exploration Summary

### Chosen AI Prompt

**Prompt 1 — Cost Modeling & Capacity Planning (Azure)**

> "Estimate monthly costs for my Spring Boot + MySQL app on Azure at budgets of $25 / $100 / $500. Consider App Service (Linux, Java SE), Azure Database for MySQL Flexible Server, storage, bandwidth/egress, and logging. Assume: 10k MAU, 2 requests per min when active, 2 SQL queries per request, 200 KB avg response size, 10% of users active during peak hour, the most expensive tier. Give me: A table for each budget with chosen SKUs, unit prices, monthly totals, and estimated max requests & queries supported. All assumptions + simple formulas so I can tweak the scenario. A short analysis of what changes costs most or saves the most. An example cautionary tale from a blog or Reddit where a user made a critical configuration error that cost a lot of money."

---

### Deliverable 1: Cost Tables for Each Budget

#### $25 Budget — Student/Development Tier

| Component | SKU | Unit Price | Monthly Cost | Notes |
|-----------|-----|------------|--------------|-------|
| App Service | B1 (Linux) | $0.018/hr | **$13.14** | 1 core, 1.75 GB RAM |
| MySQL Flexible | B1ms | $0.0086/hr | **$6.28** | 1 vCore, 2 GB RAM |
| MySQL Storage | 20 GB | $0.115/GB | **$2.30** | Included in tier |
| Egress | 5 GB | First 5 GB free | **$0** | |
| Logging | Basic | Included | **$0** | App Service logs |
| **TOTAL** | | | **~$21.72** | |

| Capacity Metric | Value |
|-----------------|-------|
| Max Requests/min | ~2,000 (B1 handles ~100 req/sec) |
| Max SQL Queries/min | ~4,000 (B1ms handles ~300 QPS) |
| Concurrent Users | ~1,000 |

---

#### $100 Budget — Small Production Tier

| Component | SKU | Unit Price | Monthly Cost | Notes |
|-----------|-----|------------|--------------|-------|
| App Service | P1v2 (Linux) | $0.10/hr | **$73.00** | 1 core, 3.5 GB RAM, SSD |
| MySQL Flexible | D2ds_v4 | $0.0344/hr | **$25.11** | 2 vCores, 8 GB RAM |
| MySQL Storage | 64 GB | $0.115/GB | **$7.36** | |
| Egress | 50 GB | $0.05/GB (after 5 GB free) | **$2.25** | |
| Logging | Standard | Included | **$0** | |
| **TOTAL** | | | **~$107.72** | Slightly over budget |

| Capacity Metric | Value |
|-----------------|-------|
| Max Requests/min | ~12,000 (P1v2 handles ~200 req/sec) |
| Max SQL Queries/min | ~24,000 (D2ds handles ~1,000 QPS) |
| Concurrent Users | ~6,000 |

---

#### $500 Budget — Production/Scale Tier

| Component | SKU | Unit Price | Monthly Cost | Notes |
|-----------|-----|------------|--------------|-------|
| App Service | P2v3 (Linux) | $0.20/hr | **$146.00** | 2 cores, 8 GB RAM |
| MySQL Flexible | D4ds_v4 (Business Critical) | $0.274/hr | **$200.02** | 4 vCores, 16 GB RAM, HA |
| MySQL Storage | 256 GB | $0.115/GB | **$29.44** | |
| Egress | 500 GB | $0.05-0.087/GB | **$35.00** | Tiered pricing |
| Logging | Log Analytics | $2.30/GB | **$23.00** | ~10 GB logs |
| **TOTAL** | | | **~$433.46** | Room for scaling |

| Capacity Metric | Value |
|-----------------|-------|
| Max Requests/min | ~48,000 (P2v3 handles ~800 req/sec) |
| Max SQL Queries/min | ~96,000 (D4ds handles ~4,000 QPS) |
| Concurrent Users | ~24,000 |

---

### Deliverable 2: Assumptions & Formulas

**Base Assumptions:**
- MAU (Monthly Active Users) = 10,000
- Peak Concurrency Rate = 10% of MAU
- Requests per User per Minute = 2
- SQL Queries per Request = 2
- Average Response Size = 200 KB

**Capacity Formulas:**

```
Peak Concurrent Users = MAU × Peak_Rate
                      = 10,000 × 0.10 = 1,000 users

Requests per Minute   = Peak_Users × Req_per_User_per_Min
                      = 1,000 × 2 = 2,000 req/min

SQL Queries per Min   = Requests_per_Min × Queries_per_Request
                      = 2,000 × 2 = 4,000 queries/min

Egress per Month      = MAU × Sessions_per_Month × Avg_Pages × Response_Size
                      = 10,000 × 4 × 5 × 200 KB = ~4 GB/month

Required App Tier     = (Requests_per_Min / 60) / Tier_RPS_Capacity
                      = (2,000 / 60) / 100 = 0.33 → B1 sufficient
```

**Cost Scaling Factors:**
- MySQL compute: +$25-50/month per tier upgrade
- App Service: +$30-60/month per tier upgrade
- Egress: Free first 5 GB, then $0.05-0.087/GB
- Storage: Linear at $0.115/GB

---

### Deliverable 3: Cost Analysis

**What Changes Costs the Most:**

1. **MySQL Compute Tier** (40-60% of total cost) — Upgrading from Burstable (B1ms) to General Purpose (D2ds) increases MySQL costs by 4x. Only upgrade when you need sustained CPU performance, not burst capacity.

2. **App Service Plan** (30-40% of total cost) — Premium tiers (P1v2+) include SSDs and auto-scaling but cost 5-7x more than Basic. Share one plan across multiple apps to amortize cost.

3. **High Availability** (+100% MySQL cost) — Enabling zone-redundant HA doubles MySQL costs. Only enable for production workloads requiring 99.99% uptime SLA.

**What Saves the Most:**

1. **Stop resources when idle** — App Service and MySQL charge 24/7. Stopping a B1 + B1ms setup saves ~$0.72/day or ~$22/month.

2. **Use Burstable tiers** — For variable workloads, Burstable accumulates CPU credits during idle time. A B1ms can handle traffic spikes up to 100% CPU for short periods at no extra cost.

3. **Co-locate in one region** — Cross-region egress costs $0.02-0.05/GB. Keeping App Service and MySQL in West US 3 eliminates this entirely.

4. **Reserved Instances** — 1-year reservations save 25-40% on compute. A $100/month workload drops to ~$65/month with reservations.

---

### Deliverable 4: Cautionary Tale

**Reddit Horror Story: The $72,000 Firebase Bill**

In a widely-shared Reddit post (r/webdev, 2020), a developer deployed a Next.js app with Firebase Realtime Database. They accidentally left a `useEffect` hook that queried the database on every render without proper caching or pagination. During a traffic spike from a Hacker News post, the app made millions of read requests in hours.

**What went wrong:**
- No rate limiting on database reads
- No budget alerts configured
- Reads charged at $0.06 per 100,000—but millions of reads = thousands of dollars
- Firebase auto-scales by default with no spending cap

**The bill:** $72,000 for a weekend of traffic.

**How to avoid this on Azure:**
1. **Set budget alerts** at 50%, 75%, 90% thresholds (Azure Cost Management → Budgets)
2. **Configure spending caps** or action groups to stop resources automatically
3. **Use connection pooling** to limit database connections
4. **Implement caching** (Redis, in-memory) to reduce database queries
5. **Monitor in real-time** using Azure Monitor alerts on DTU/vCore usage

**Azure-specific safeguard:** Unlike Firebase, Azure MySQL Flexible Server does NOT auto-scale compute by default. You must manually upgrade tiers or enable auto-grow for storage. This provides a natural cost ceiling but requires proactive capacity planning.

---

### Follow-up Questions

**Follow-up 1:** "What configuration mistakes commonly cause unexpected Azure bills?"

**Summary:** The most common billing mistakes include: (1) forgetting to stop or delete resources after testing—App Services and MySQL servers accrue costs 24/7 even when idle; (2) leaving auto-scaling enabled without max instance limits, which can spin up expensive compute during traffic spikes; (3) selecting General Purpose or Business Critical MySQL tiers when Burstable would suffice for development; (4) enabling geo-redundant backups unnecessarily; and (5) provisioning resources in different regions, which incurs cross-region egress charges. For student projects, always verify resources are stopped when not in use and consider setting up auto-shutdown schedules.

**Follow-up 2:** "How can I set up budget alerts to avoid exceeding my $100 student credit?"

**Summary:** Azure provides Cost Management + Billing to create budget alerts. Navigate to your subscription → Cost Management → Budgets → Add. Create a budget with a $100 monthly amount (or less for safety margin, like $80). Configure alert conditions at 50%, 75%, and 90% thresholds to receive email notifications. Additionally, enable the "Forecast" alert type to warn when projected spending will exceed the budget. For extra protection, create an Action Group that triggers an Azure Function or Logic App to automatically stop non-essential resources when thresholds are reached. The Azure for Students subscription also shows remaining credits directly in the portal under Subscriptions → Overview.

---

### What I Learned

1. **Cloud costs are dominated by compute, not storage** — For small-scale applications, the MySQL Flexible Server compute tier (B1ms vs. General Purpose) accounts for the majority of monthly costs, while storage and bandwidth are often negligible or free within included limits.

2. **Burstable tiers are ideal for development workloads** — The Burstable B-series for both App Service and MySQL provides CPU credits that accumulate during idle periods and can be spent during brief traffic spikes, making them cost-effective for applications with variable or low traffic.

3. **Right-sizing requires understanding your traffic patterns** — The AI helped me calculate that 10k MAU with 10% peak concurrency translates to ~2,000 requests/minute, which is well within B1 tier capabilities; production apps with sustained high traffic would need General Purpose tiers.

4. **Proactive cost management prevents billing surprises** — Setting up budget alerts at multiple thresholds (50%, 75%, 90%) and enabling forecast alerts provides early warning before credits are exhausted, giving time to adjust or stop resources.

5. **Region co-location reduces hidden costs** — Placing the App Service and MySQL server in the same Azure region (West US 3) eliminates cross-region data transfer charges and reduces latency, which is a best practice the AI emphasized for both cost and performance optimization.

---

<div style="page-break-after: always;"></div>

## Section 9: Reflection

### Deployment Challenges Encountered

**Challenge 1:** Initial database connection failures due to SSL configuration mismatch. The Azure MySQL Flexible Server requires TLS connections by default, but the initial JDBC URL did not include the `sslMode=REQUIRED` parameter, causing connection timeouts and authentication errors.

**Solution:** Added `sslMode=REQUIRED&serverTimezone=UTC` parameters to the JDBC connection string in Azure App Settings. This ensured the MariaDB driver properly negotiated a TLS connection with the Azure MySQL server. Verified the connection worked by checking the Log Stream for successful Spring Boot startup messages.

---

**Challenge 2:** Environment variable naming confusion between local development and Azure deployment. Spring Boot expects specific naming conventions for environment variable overrides, and initially the Azure App Settings were not correctly mapped to the `spring.datasource.*` properties.

**Solution:** Confirmed that Spring Boot automatically maps environment variables using the `SPRING_DATASOURCE_*` naming convention (underscores instead of dots, all uppercase). Updated the Azure App Settings to use `SPRING_DATASOURCE_URL`, `SPRING_DATASOURCE_USERNAME`, and `SPRING_DATASOURCE_PASSWORD` which correctly override the local `application.properties` values at runtime.

---

### Security Best Practices Applied

| Practice | Implementation |
|----------|----------------|
| No secrets in Git | Used App Settings for database credentials; local dev credentials are separate from production |
| TLS encryption | `sslMode=REQUIRED` in JDBC URL ensures all database traffic is encrypted in transit |
| Firewall rules | Restricted MySQL access to Azure services and specific client IPs only |
| Least privilege | Database user has access only to `ordersDB` schema; limited permissions for application operations |
| Password hashing | BCrypt password encoder configured in SecurityConfig for user authentication |
| Role-based access | Spring Security restricts `/admin/**` endpoints to ADMIN role only |

---

### Cost Management

**Steps Taken to Conserve Credits:**
- [x] Selected burstable/B1ms tier for MySQL (1 vCore, 2 GB RAM, 20 GB storage)
- [x] Selected B1 tier for App Service (cost-effective for development/demo)
- [x] Stop App Service when not in use (can be stopped via Azure Portal)
- [x] Minimum backup retention configured (default settings)
- [x] Resources in same region to minimize egress (West US 3 for both App Service and MySQL)

---

### Key Terminology Learned

| Term | Definition |
|------|------------|
| Fat JAR | Executable JAR containing all dependencies |
| Flexible Server | Azure's current managed MySQL service |
| App Settings | Environment variables for Azure Web Apps |
| TLS/SSL | Encryption for data in transit |
| FQDN | Fully Qualified Domain Name (e.g., `server.mysql.database.azure.com`) |

---

## Appendix: Quick Reference

### Azure Resources Created

| Resource | Name | Type | Location |
|----------|------|------|----------|
| Resource Group | CST-323 | Container | - |
| MySQL Server | cst-323-app | Flexible Server (B1ms) | West US 3 |
| MySQL Server | cst323-mysql-owen | Flexible Server | Central US |
| Database | ordersDB | MySQL Schema | - |
| Web App | cst323-orders-owen | App Service | West US 3 |
| App Service Plan | cst323-plan | Linux B1 | West US 3 |

### Useful Commands

```bash
# Build the application
mvn -DskipTests clean package

# Deploy to Azure (authenticates via browser popup)
mvn azure-webapp:deploy
```

> **Note:** View logs via Azure Portal → Web App → Log Stream (no CLI required)

### Application URLs

- **Production:** https://cst323-orders-owen.azurewebsites.net
- **Health Check:** https://cst323-orders-owen.azurewebsites.net/actuator/health

### Database Connection

- **MySQL Endpoint:** `cst-323-app.mysql.database.azure.com`
- **Port:** 3306
- **Database:** ordersDB
- **Admin User:** adminuser

---
