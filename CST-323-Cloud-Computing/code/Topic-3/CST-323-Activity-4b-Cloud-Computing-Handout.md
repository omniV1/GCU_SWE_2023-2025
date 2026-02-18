# Cloud Computing Handout

**Name:** Owen Lindsey

---

## Part 1. Early Advances in Cloud Computing

**Fill in the blanks as you watch/listen:**

1. In 1996, Hotmail, allowed email through a web browser.

2. VMware pioneered virtual machines in 1999.

3. In 2006, Amazon, began renting servers to customers.

---

## Part 2. Five Essential Characteristics of Cloud Computing

**Match each description to the correct term**

| Term                              | Description [Fill in the blank]                                              |
| --------------------------------- | ---------------------------------------------------------------------------- |
| On-demand self-service            | • Like a vending machine: order servers, storage, etc. without human contact |
| Resource pooling                  | • Large shared pool, library of resources                                    |
| Rapid Elasticity                  | • Expand/shrink service based on demand spikes                               |
| Broad Network Access              | • Service is available globally, on many platforms                           |
| Measured service with pay per use | • Pay-as-you-go model; like a cell phone bill                                |

<div style="page-break-after: always;"></div>

---

## Part 3. Pizza as a Service

**Fill in the chart to show who does the work**

| Task            | IaaS (Home Kitchen) | PaaS (Take & Bake)    | SaaS (Restaurant)     |
| --------------- | ------------------- | --------------------- | --------------------- |
| Buy ingredients | You provide this    | Service provides this | Service provides this |
| Assemble pizza  | You provide this    | Service provides this | Service provides this |
| Cook in oven    | You provide this    | You provide this      | Service provides this |
| Wash dishes     | You provide this    | You provide this      | Service provides this |
| Serve/Eat       | You provide this    | You provide this      | Service provides this |

**Question:** Which model has the highest cost but lowest effort? SaaS, The more responsibility taken away, the higher the cost. 


---

## Part 4. Service Categories

**Match the example to the type of service:**

- Email - SaaS
- Azure hosting a Spring Boot + MySQL app - PaaS 
- Virtual network with routers & firewalls - IaaS
- GoDaddy web hosting - IaaS



---

## Part 5. Control vs. Responsibility

**Fill in the continuum:**

- **IaaS** - You manage: OS, firewalls, antivirus, networking, and applications.
- **PaaS** - You focus on: Your application data and code; the provider manages the platform, runtime, and infrastructure.
- **SaaS** - You only: You simply use the application

---

## Part 6. Benefits & Concerns

**List one benefit and one concern for each**

| Platform | Advantage                                                | Disadvantage                                             |
| -------- | -------------------------------------------------------- | -------------------------------------------------------- |
| SaaS     | Less operational burden.                                 | Less control overall unless it is the app configuration. |
| PaaS     | Some control over app configuration, app server, and OS. | No control over load balance, networking, or antivirus.  |
| IaaS     | Tons of control over each component.                     | Tons of operational burden.                              |

<div style="page-break-after: always;"></div>

---

## Part 7. Collaborating with AI

This section involves experimenting with using Artificial Intelligence (AI) as a learning partner. The purpose is not for AI to do homework, but to **practice how to deepen your understanding of cloud computing**.

Think of AI as an on-demand tutor that can explain concepts, provide examples, and play "devil's advocate." The best way to learn with AI is to:

1. **Start with a strong question.**
2. **Dig deeper.** (e.g., "Why?", "What if?", "Tell me another example?")
3. **Compare perspectives.** (AI can show multiple sides, explain advantages/disadvantages, or opposing opinions)
4. **Look for evidence.** (Ask for case studies, company blogs, news reports)
5. **Reflect.** (Take notes on what surprised you, confirmed your assumptions, or shifted your opinions)

**Goal:** The goal is not to outsource your thinking, but to practice curiosity. By the end, you should be able to explain what you learned in your own words and connect it back to cloud computing concepts.

**Instructions:**

1. Choose two of the following prompts to begin your conversation.
2. Continue follow-up questions until you have satisfied your curiosity or learned something that you believe will be useful in your career.
3. Condense the things you learned to a short list of key findings.
4. Include the summarized findings in a Word document which you will submit in this activity deliverables.

---

### Prompt 1: Cloud Security Trade-offs

Is it safer to keep sensitive data in-house or trust major cloud providers (AWS, Azure, Google Cloud)? What are the security pros and cons? How does the answer change for healthcare vs. retail? Can you find a real-life example of a company making a good or bad cloud security decision, and what lessons were learned?

**Why ask this question:** Experts disagree. Some say cloud is safer (redundancy, security teams at cloud companies are experts), others say local control is safer.

#### AI Collaboration Summary (Prompt 1)

**AI analysis:** Security should be scaled to business scope rather than applied uniformly. Sensitive environments like hospitals or government agencies require stronger controls, but that does not necessarily mean keeping everything in-house. Many regulated organizations use cloud providers with HIPAA-compliant or FedRAMP-certified offerings, and services like Supabase offer HIPAA-compliant database and storage options when the business needs justify it.

The MongoBleed vulnerability (CVE-2025-14847) challenged a common assumption that NoSQL databases like MongoDB are inherently safer than SQL because they avoid SQL injection. MongoBleed is a zlib decompression flaw that allows unauthenticated memory reads—a different attack surface entirely. NoSQL avoids query-language exploits but remains exposed to implementation bugs, misconfiguration, and exposed instances. The Ubisoft incident showed that even a trusted cloud database can be exploited in the wild, with attackers manipulating in-game currency and cosmetics. The takeaway is that no technology is inherently secure; defense in depth and timely patching matter regardless of database model.

*Reference: [eSentire - Severe MongoDB Vulnerability CVE-2025-14847 Exploited in the Wild](https://www.esentire.com/security-advisories/severe-mongodb-vulnerability-cve-2025-14847-exploited-in-the-wild)*

**My reflection:** There are tiers to security. Each business should only apply as much security as required by its scope. I expected hospitals, government agencies, or similar data-sensitive environments to use the most secure services possible, maybe in-house, though that comes with a heavy security team burden and operational costs that smaller businesses don't need. Supabase, for example, offers HIPAA-compliant database and document storage when business needs justify it. I was in the same camp as the experts before MongoBleed: I assumed MongoDB was safer than SQL because SQL has a whole dictionary of exploits to work through, while NoSQL's non-relational nature avoids that. MongoBleed showed that I was wrong.

---

### Prompt 2: Cost vs. Flexibility in the Cloud

Do cloud services save money in the long run, or do they just shift costs? How do small startups vs. large enterprises choose cloud services differently? Can you find a real-life example of a company's financial results after switching from self-hosted to cloud?

**Why ask this question:** Cloud advocates claim cost efficiency; critics argue it's more expensive over time. There are nuanced trade-offs.

---

### Prompt 3: SaaS vs. PaaS vs. IaaS for Startups

If you were starting a new tech company, which model (SaaS, PaaS, or IaaS) would you choose first and why? How might the answer change if the company grows rapidly or operates in a highly regulated industry? Can you find an example blog or story about a startup's choice?

**Why ask this question:** No single correct answer. The variety of solutions exists because of varied customer needs.

<div style="page-break-after: always;"></div>

#### AI Collaboration Summary (Prompt 3)

**AI analysis:** The choice between SaaS, PaaS, and IaaS depends on business needs, timeline, and team capacity. There is no single correct answer; the only wrong choice is one that does not align with those needs. For a startup building a custom app with no server admin, PaaS and managed services (e.g., Render, Vercel, MongoDB Atlas) let the team focus on the product instead of infrastructure. The trade-offs are made consciously—sometimes you build something handmade from the ground up, sometimes you start with a platform and iterate.

**My reflection:** I'm working with a startup in the West Valley for my senior project. I'm building their website from the ground up, so I had to evaluate these options. At one point I considered building my own in-home server to serve the web app and self-contain the data. I knew I could do it, but time was not on my side and I needed an MVP in a few months. Speed and scalability became more important than strong and terse. I switched to a cloud-based approach using Render, Vercel, and MongoDB to keep everything cloud-based and globally servable. These trade-offs are consciously made as business needs change, sometimes you architect something handmade from the ground up, sometimes you start with a frame and go from there. There is no wrong answer; the only time there is, is if it does not align with the business needs. 

---

### Prompt 4: Balance of Cloud Computing

Do companies use multi-cloud (AWS + Azure + Google Cloud) or consolidate on one provider? Can you find a link to a case study where a company faced this decision?

**Why ask this question:** Learning from others can teach us best practices to improve reliability, costs or features.

---

### Reflection: 

I understood these concepts loosely before, I understood SaaS because that's 90% of what we encounter today. Most software is served to us and we pay a monthly usage fee for instead of building our own personal email CDN. However, I still sometimes mistake things like Vercel for SaaS cause you pay for it monthly, its actually a PaaS because you can configure app servers, operating system information, and define app configuration. Companies exist due to these infrastructures and these models support in various ways. As the handout suggests, the more you let go of control the more you have to be willing to get served whatever comes out of the kitchen. There may be a michilen star chef in there or a up and coming cook, regardless buisnesses have to ask themselves if theyd rather have a live in chef or accept what comes out of the kitchen.

<div style="page-break-after: always;"></div>

## Part 8. Apply It (Case Study)

**Circle which model(s) you would recommend and explain why:**

1. **A startup dev team building a new app with no server admin.**
   - SaaS | <mark style="background: #BBFABBA6;">PaaS</mark> | IaaS
   - Because without a server admin, a dev team should focus on using something like Vercel, which handles the responsibilities a server admin would take on—deployments, SSL certificates, CDN distribution, auto-scaling, and server maintenance—so the team can focus on writing application code instead of infrastructure.

2. **A university that wants to provide student email & file sharing.**
   - <mark style="background: #BBFABBA6;">SaaS </mark>| PaaS | IaaS
   - Because Gmail, Outlook, and other services provide all the necessary security requirements themselves and are trusted globally by a large margin. 

3. **A bank that needs full control over its security & networking.**
   - SaaS | PaaS | <mark style="background: #BBFABBA6;">IaaS</mark>
   - Because this will give them full control over their security and networking requirements. 

