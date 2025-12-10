<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;">
  <h1>Technology Security in Christian Organizations</h1>
  <h2>Owen Lindsey</h2>
  <h2>Professor Sluiter, Shad</h2>
  <h2>CST-407</h2>
  <h2>Grand Canyon University</h2>
</div>

# Goals: 

1. Identify and Assess Vulnerabilities in Organizational Technology Systems

Evaluate an organization's current software, hardware, and policies to identify areas that are susceptible to security breaches or operational failures.

2. Develop and Implement Disaster Preparedness Plans

Create comprehensive disaster recovery and preparedness plans, ensuring that critical data and services can be restored quickly in the event of a system failure, cyberattack, or natural disaster.

3. Promote Security Awareness and Best Practices

Explain the importance of educating staff and volunteers about security best practices, such as password management, phishing awareness, and the use of multi-factor authentication. Explain how the church adheres to ethical codes of conduct through a data usage awareness campaign.



# Our Mission

![[Pasted image 20251209115828.png]]

In this email from Pastor John Matthews, I found key focuses and will list their priority based on my understanding. 

1. Maintaining the trust of our congregation - This is an overarching goal that encapsulates the goals below and is paramount to the ministry. 

2. Financial stability - Financial fraud would be a major concern here. Review status reports and consumer reviews for software before committing. 

3. The consistency and reliability of our worship services and events along with scalability. - the goal is to be able to grow and reliably serve the congregation. 

4. operational efficiency - The ability to simplify current processes to reduce administration strain. 

5. legal and regulatory compliance - Focus on data privacy, GDPR or CCPA laws to protect the ministry from legal complications. 


<div style="page-break-after: always;"></div>

# Technology Security Audit Tables

The tables below use the Part 4 audit checklist categories for each technology in use at Grace Community Fellowship. Status legend: Good = strong practice confirmed, Adequate = acceptable but needs improvement, Urgent = gap or prior incident to address, TBD = evidence required.

## Breeze ChMS

| Audit Category | Status | Notes |
| --- | --- | --- |
| General Technology Review | Adequate | Core member/event system; verify current data map and vendor backup cadence. |
| Cloud and Hosting Security | Good | Cloud-hosted with encrypted connections and payment industry-aligned controls; database backups every 6 hours, code/media daily; confirm hosting region (see 19). |
| Authentication and Access Control | Adequate | Enforce role-based access, multi-factor authentication for admins, prompt removal of departed staff/volunteers; unique subdomain login. |
| Donation and Financial Security | Adequate | Supports online giving; if enabled, validate payment security documentation and restrict exports/application programming interface keys (see 19). |
| Communication Tools Security | N/A | Not a primary comms platform. |
| Live Streaming and Presentation Security | N/A | Not used for content delivery. |
| Software Maintenance and Updates | Adequate | Track vendor release notes, rotate application programming interface tokens, and review Tithe.ly integrations if enabled. |

**Recommendation:** Support with conditions (Moderate Risk) retain Breeze; enforce multi-factor authentication and role hygiene, confirm backup/region posture, align payment security evidence if using giving, and audit application programming interface tokens.

<div style="page-break-after: always;"></div>

## Pushpay

| Audit Category                           | Status   | Notes                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Technology Review                | Adequate | Primary giving channel; validate configuration aligns with finance policies.                                                                                                                                                                                            |
| Cloud and Hosting Security               | Adequate      | Published privacy/security policy (Jul 9, 2025); confirm encrypted connections, uptime service levels, and data residency (see 21).                                                                                                                                                                                                               |
| Authentication and Access Control        | Adequate | Require multi-factor authentication for finance admins and prohibit shared logins.                                                                                                                                                                                                              |
| Donation and Financial Security          | Adequate | Confirm payment security attestations, fraud monitoring, and encryption at rest/in transit (see 1–3, 21).                                                                                                                                                                                       |
| Vendor Security Reviews                  | Urgent   | Recent user reviews (Trustpilot Sep 2025, Jun 2024; TrustRadius 2024) and Better Business Bureau complaints (billing issues, stored cards, cancellation lock-in across 2023-2025) highlight usability, contract, and billing risk; re-evaluate vendor fit and ensure exit/contingency plan. |
| Communication Tools Security             | N/A      | Not a comms platform.                                                                                                                                                                                                                                                   |
| Live Streaming and Presentation Security | N/A      | Not applicable.                                                                                                                                                                                                                                                         |
| Software Maintenance and Updates         | Adequate | Schedule periodic reviews of integrations and webhooks after vendor updates.                                                                                                                                                                                            |

**Recommendation:** Replace (High Risk) begin exit planning toward Tithe.ly or Planning Center Giving based on recurring billing/refund complaints; enforce multi-factor authentication and a refund/escalation playbook until migration completes.

<div style="page-break-after: always;"></div>

## ProPresenter

| Audit Category                           | Status   | Notes                                                                                                                                                                                                                |
| ---------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Technology Review                | Adequate | Audio-visual workstation software; keep device inventory tied to services.                                                                                                                                           |
| Cloud and Hosting Security               | N/A      | Primarily on-prem software; limit network exposure.                                                                                                                                                                  |
| Authentication and Access Control        | Adequate | Uses Account Manager roles (owner/admin/member) plus network passwords for remote connections and application programming interface; ensure unique logins, seat control, and operating system permissions (see 6–8). |
| Donation and Financial Security          | N/A      | Not applicable.                                                                                                                                                                                                      |
| Communication Tools Security             | N/A      | Not applicable.                                                                                                                                                                                                      |
| Live Streaming and Presentation Security | Adequate | Control content sources, sanitize media, and keep offline fallback slides.                                                                                                                                           |
| Software Maintenance and Updates         | Adequate | Apply patches during maintenance windows; note user reports of Windows build glitches and video stutter; test updates before Sunday.                                                                                 |
| Vendor Security Reviews                  | Adequate | Mixed reliability feedback (Reddit thread, GetApp); better stability on macOS, Windows users cite bugs/performance; monitor vendor fixes.                                                                            |

**Recommendation:** Support with conditions keep ProPresenter; prioritize macOS where possible, stage/rollback Windows updates around services, pretest video playback, and enforce Account Manager roles plus network passwords for remote connections and application programming interface access.

<div style="page-break-after: always;"></div>

## BoxCast

| Audit Category | Status | Notes |
| --- | --- | --- |
| General Technology Review | Adequate | Critical for livestreams; document ingest points and endpoints. |
| Cloud and Hosting Security | Adequate | Confirm streams use encrypted delivery and restrict embed domains. |
| Authentication and Access Control | Adequate | Lock down stream keys, admin roles, and multi-factor authentication for console access. |
| Donation and Financial Security | N/A | Not applicable. |
| Communication Tools Security | N/A | Not applicable. |
| Live Streaming and Presentation Security | Adequate | Monitor for hijacking attempts; audit who can start/stop broadcasts. |
| Software Maintenance and Updates | Adequate | Track firmware/app updates on encoders/devices; note recent minor outages (Oct 20: 2h35m; Nov 2: 5m; Dec 5: 20m) (see status history). |
| Vendor Security Reviews | Adequate | Status history shows limited outages; request uptime targets/history and maintain failover. |

**Recommendation:** Support with evidence retain BoxCast only after confirming uptime targets/history; document stream-key handling and keep YouTube Live as a failover.

<div style="page-break-after: always;"></div>

## Eventbrite

| Audit Category                           | Status   | Notes                                                                                                                                                                                                                       |
| ---------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Technology Review                | Adequate | Event RSVPs/ticketing; address usability gaps for older members.                                                                                                                                                            |
| Cloud and Hosting Security               | Adequate      | Review data retention and privacy settings; Eventbrite publishes a privacy policy (Jan 27, 2025) and provides organizer/consumer controls (see policy).                                                                                                                                                               |
| Authentication and Access Control        | Adequate | Use individual accounts with multi-factor authentication; avoid shared organizer logins.                                                                                                                                                            |
| Donation and Financial Security          | Adequate | If collecting paid registrations, confirm payment processor compliance and refund controls.                                                                                                                                 |
| Vendor Security Reviews                  | Urgent   | Recent complaints (Trustpilot Nov–Dec 2025; Better Business Bureau 456 complaints/172 last 12 months) cite non-refunded cancellations, locked payouts, and forced auto-renew/missed refunds require clear refund service levels and organizer screening. |
| Communication Tools Security             | Adequate | Vet outbound messaging templates and unsubscribe handling.                                                                                                                                                                  |
| Live Streaming and Presentation Security | N/A      | Not applicable.                                                                                                                                                                                                             |
| Software Maintenance and Updates         | Adequate | Periodically review integrations (calendar, email) after vendor changes.                                                                                                                                                    |

**Recommendation:** Replace (High Risk) shift registrations to Planning Center Registrations or SignUpGenius given refund/payout complaints; if retained, mandate escrowed payouts and written refund service levels.

<div style="page-break-after: always;"></div>

## Planning Center Services

| Audit Category                           | Status   | Notes                                                                                                                                                                                                 |
| ---------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General Technology Review                | Good | Volunteer scheduling backbone; ensure roster accuracy post-2023 upgrade.                                                                                                                              |
| Cloud and Hosting Security               | Good      | Cloud-hosted with published privacy/security notice (Nov 14, 2025); confirm data segregation for ministries (see 9–12).                                                                                                                                      |
| Authentication and Access Control        | Adequate | Enforce least privilege for schedulers vs volunteers; require multi-factor authentication for admins.                                                                                                                         |
| Donation and Financial Security          | N/A      | Not applicable.                                                                                                                                                                                       |
| Communication Tools Security             | Adequate | Review reminder/notification settings to avoid oversharing contact data.                                                                                                                              |
| Live Streaming and Presentation Security | N/A      | Not applicable.                                                                                                                                                                                       |
| Software Maintenance and Updates         | Adequate | Monitor vendor updates that impact mobile apps and calendar sync.                                                                                                                                     |
| Vendor Security Reviews                  | Good | Positive user feedback on reliability/scheduling (Reddit, SoftwareAdvice 4.7/5, G2 2025) and Better Business Bureau shows zero complaints; occasional Sunday load issues noted; confirm uptime service levels and support paths (see 9–12). |

**Recommendation:** Support continue Planning Center Services as the volunteer backbone; validate uptime service levels, add Sunday performance monitoring, and keep multi-factor authentication/least-privilege enforced.

<div style="page-break-after: always;"></div>

## Subsplash

| Audit Category | Status | Notes |
| --- | --- | --- |
| General Technology Review | Adequate | Hosts website/app; central hub for sermons and giving links. |
| Cloud and Hosting Security | Good | Certificate renewal was automated after 2022 outage; verify content delivery network and web application firewall protections to keep posture strong. |
| Authentication and Access Control | Good | Limit content management system editors, enable multi-factor authentication if available, and audit application programming interface keys. |
| Donation and Financial Security | N/A | Payments routed elsewhere; ensure only vetted giving links are embedded. |
| Communication Tools Security | Adequate | Review push notification permissions and privacy disclosures. |
| Live Streaming and Presentation Security | Adequate | Validate embedded streams and file permissions before publishing. |
| Software Maintenance and Updates | Adequate | Track platform updates that affect mobile app builds and plugins. |
| Vendor Security Reviews | Adequate | Mixed feedback: positive all-in-one reviews vs Trustpilot complaints about upselling, delays, cancellations; Better Business Bureau shows 4 complaints in 3 years; require clear service levels, refund terms, and support response targets (see 13–16). |

**Recommendation:** Support with conditions retain Subsplash; verify web application firewall and content delivery network protections, require clear contract/support/refund terms given mixed reviews, and audit editor/API access quarterly.

<div style="page-break-after: always;"></div>

## Aplos

| Audit Category | Status | Notes |
| --- | --- | --- |
| General Technology Review | Adequate | Finance backbone; aligns with accounting processes adopted in 2019. |
| Cloud and Hosting Security | Adequate | Published privacy/security notice (Sep 24, 2025); US-hosted; confirm data residency details and security measures for financial data (see 19). |
| Authentication and Access Control | Adequate | Enforce multi-factor authentication, unique logins, and segregation of duties for approvals. |
| Donation and Financial Security | Adequate | Verify payment security and independent attestation reports, audit trails, and encryption coverage. |
| Communication Tools Security | N/A | Not applicable. |
| Live Streaming and Presentation Security | N/A | Not applicable. |
| Software Maintenance and Updates | Adequate | Schedule reviews after major releases; validate export integrations. |

**Recommendation:** Support retain Aplos contingent on current payment security evidence, enforced multi-factor authentication and segregation of duties, and periodic audit of exports/integrations.

<div style="page-break-after: always;"></div>

## Flocknote

| Audit Category | Status | Notes |
| --- | --- | --- |
| General Technology Review | Adequate | Primary email/text platform; prior breach exposed member emails. |
| Cloud and Hosting Security | Adequate | Published privacy/security policy (Feb 14, 2023); request current data retention details. |
| Authentication and Access Control | Urgent | Past shared logins led to 2021 breach; verify multi-factor authentication and strong password policy now enforced for all admins. |
| Donation and Financial Security | N/A | Not applicable. |
| Communication Tools Security | Adequate | Ensure opt-outs honored, phishing awareness for senders, and incident response plan tested. |
| Live Streaming and Presentation Security | N/A | Not applicable. |
| Software Maintenance and Updates | Adequate | Monitor vendor updates that affect contact lists or API access. |
| Vendor Security Reviews | Adequate | Strong user satisfaction (Trustpilot 4.7/5, Capterra 4.7/5) but past breach and shared logins raise risk; keep multi-factor authentication and admin hygiene enforced (see 17–18). |

**Recommendation:** Support with remediation (Elevated Risk) continue Flocknote only after multi-factor authentication and unique admins are enforced and roles reviewed; otherwise migrate to a secured alternative (i.e., Mailchimp or Church Community Builder).

<div style="page-break-after: always;"></div>

# Report summary 

The tables above are how I graded the ministry's current technologies. Several platforms are sound with routine controls; a few need targeted remediation; two should be replaced because of sustained vendor and billing risks. A simplification path can also reduce vendor sprawl.

**Key vulnerabilities**: Pushpay and Eventbrite have sustained billing/refund and contract complaints; Flocknote had a prior breach tied to shared logins; ProPresenter can be unstable on Windows builds if updates are not staged; BoxCast has had brief outages; Breeze, Flocknote, and ProPresenter all depend on enforcing strong authentication and role hygiene to avoid repeat incidents (see sources 1–21).

Planning Center Services and Subsplash have solid hosting and access controls. BoxCast is workable given short outages; keep it only after confirming uptime history and with a livestream backup. Aplos is fine when strong authentication and role separation are enforced. Manage these with periodic access reviews, backup/restore checks, and application programming interface key rotation.

Breeze is serviceable with clear cloud/backup setup; confirm region/backup details and keep strong authentication and roles in order. ProPresenter is stable if updates are staged and macOS prioritized; Windows builds require pretesting. Flocknote stays viable only after strong authentication and unique admin accounts are enforced; otherwise move to a secured communications tool. Pushpay and Eventbrite show sustained billing/refund and contract complaints; replace them (i.e., Planning Center Giving; Planning Center Registrations) while keeping strong authentication and a refund/escalation playbook until cutover completes. Align service levels, privacy commitments, and refund terms for any temporary Eventbrite use.

Consolidate people, volunteers, registrations, and giving into Planning Center; drop Breeze, Pushpay, and Eventbrite to remove overlap. Pick one communications tool (Flocknote with enforced strong authentication and unique admins, or a simple email/SMS tool) to avoid duplication. Keep ProPresenter for slides. Choose BoxCast with a YouTube Live failover, or go YouTube only if simpler streaming is acceptable. Keep Subsplash only if the app/media hub is essential; otherwise a simple website plus Planning Center links and YouTube embeds may suffice. This reduces logins, duplicate payment processors, and redundant event tools.


<div style="page-break-after: always;"></div>

# References

1. Trustpilot: Pushpay user reviews (Sep 2025, Jun 2024) - https://www.trustpilot.com/review/pushpay.com  
2. TrustRadius: Pushpay reviews (Anthony Miller Jun 2024; Stephen Crawford Apr 2022; Kendra Zondervan Feb 2020) - https://www.trustradius.com/products/pushpay/reviews  
3. BBB: Pushpay USA Inc. complaints (2023-2025) - https://www.bbb.org/us/wa/redmond/profile/payment-processing-services/pushpay-usa-inc-1296-1000060647/complaints?page=1  
4. Trustpilot: Eventbrite user reviews (Nov-Dec 2025) - https://www.trustpilot.com/review/www.eventbrite.com  
5. BBB: Eventbrite, Inc. complaints (456 in last 3 years; 172 in last 12 months) - https://www.bbb.org/us/ca/san-francisco/profile/online-event-registration/eventbrite-inc-1116-76754/complaints  
6. Reddit: r/ProPresenter Windows stability thread (community feedback on bugs vs macOS performance) - https://www.reddit.com/r/ProPresenter/  
7. GetApp: ProPresenter ratings and feature reviews (overall 4.6/5; text editing, multi-screen) - https://www.getapp.com/it-management-software/a/propresenter/reviews/  
8. SoftwareAdvice: ProPresenter user reviews and ratings - https://www.softwareadvice.com/church-presentation/propresenter-profile/  
9. Reddit: r/churchtech Planning Center thread (volunteer scheduling and suite adoption feedback) - https://www.reddit.com/r/churchtech/comments/1d4ef2z/how_good_is_planning_center/  
10. SoftwareAdvice: Planning Center reviews (overall 4.7/5; ease-of-use 4.4, support 4.6) - https://www.softwareadvice.com/accounting/planning-center-profile/reviews/  
11. G2: Planning Center reviews (2025 volunteer scheduling/usability feedback) - https://www.g2.com/sellers/planning-center#reviews  
12. BBB: The Planning Center profile (0 complaints) - https://www.bbb.org/us/il/moline/profile/financial-planning-consultants/the-planning-center-0664-32016246  
13. Capterra: Subsplash reviews (overall 4.5/5; ease 4.4, support 4.4) - https://www.capterra.com/p/177932/Subsplash/reviews/  
14. SoftwareAdvice: Subsplash reviews and ratings - https://www.softwareadvice.com/nonprofit/subsplash-profile/reviews/  
15. Trustpilot: Subsplash user reviews (2025 mix of positive and critical) - https://www.trustpilot.com/review/subsplash.com  
16. BBB: Subsplash complaints (4 in last 3 years; 1 in last 12 months) - https://www.bbb.org/us/wa/mountlake-terrace/profile/computer-software-developers/subsplash-1296-1000057519/complaints  
17. Trustpilot: Flocknote user reviews (4.7/5) - https://www.trustpilot.com/review/flocknote.com  
18. Capterra: Flocknote reviews (4.7/5; ease 4.4, support 4.8) - https://www.capterra.com/p/149433/Flocknote/reviews/  
19. Aplos: Privacy policy and security notice (Sep 24, 2025) - https://www.aplos.com/privacy  
20. Flocknote: Privacy and Security Policy (Feb 14, 2023) - https://flocknote.com/privacy/  
21. Pushpay: Privacy Policy (Jul 9, 2025) - https://pushpay.com/legal-center/privacy/  
