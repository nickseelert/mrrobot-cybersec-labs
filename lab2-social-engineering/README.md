# Lab 2: Social Engineering & OSINT

## Mr. Robot Reference
In Season 1, Episode 5, Elliot infiltrates Steel Mountain by creating a fake Wikipedia page and using social engineering tactics. This lab recreates those techniques, teaching you OSINT gathering and social engineering.

## Learning Objectives

By completing this lab, you will:
- Conduct Open Source Intelligence (OSINT) gathering
- Create convincing phishing campaigns
- Understand pretexting and social engineering psychology
- Build fake online personas
- Analyze metadata and digital footprints
- Recognize and defend against social engineering attacks

## Lab Scenario

You've been hired to test Steel Mountain Data Security's human security measures. Your mission is to gather intelligence about employees and attempt to gain physical or digital access through social engineering techniques.

## Prerequisites

- Completed Lab 1
- Basic understanding of web technologies
- Docker and Docker Compose installed

## Lab Architecture

The lab consists of:
- **Company Website**: Steel Mountain's corporate site with employee directory
- **Social Media Simulator**: Fake social profiles and posts
- **Email Server**: For phishing campaigns
- **OSINT Tools Container**: Automated reconnaissance tools
- **Target Employee Simulator**: Responds to social engineering attempts

## Getting Started

1. Start the lab environment:
   ```bash
   docker-compose up -d
   ```

2. Access the tools container:
   ```bash
   docker exec -it osint-tools /bin/bash
   ```

3. Browse the company website:
   ```
   http://localhost:8082
   ```

## Tasks

### Task 1: OSINT Reconnaissance (20 points)
Gather information about Steel Mountain and its employees using only public sources.

**Tools**: Google dorking, social media search, metadata extraction
**Deliverable**: Dossier on 3 key employees with personal details

### Task 2: Create Fake Personas (20 points)
Build believable online identities for social engineering.

**Tools**: Fake name generator, AI profile pictures, social media
**Deliverable**: Two complete fake profiles with backstories

### Task 3: Spear Phishing Campaign (25 points)
Craft targeted phishing emails based on OSINT findings.

**Tools**: Email templates, domain spoofing techniques
**Deliverable**: Three unique phishing emails with different approaches

### Task 4: Pretexting Scenarios (25 points)
Develop and execute pretexting calls/chats.

**Tools**: VoIP simulator, chat platforms
**Deliverable**: Recorded interactions and success analysis

### Task 5: Physical Security Assessment (10 points)
Plan a physical infiltration based on gathered intelligence.

**Tools**: Building layouts, security assessment
**Deliverable**: Infiltration plan with contingencies

## Hints

<details>
<summary>Hint 1: Employee Research</summary>

Check the company directory, but also look for:
- Personal blogs or websites
- Conference speaker profiles  
- GitHub/LinkedIn profiles
- Local news mentions
</details>

<details>
<summary>Hint 2: Metadata Analysis</summary>

Use EXIF data from images:
```bash
exiftool image.jpg
```
PDFs often contain author information and creation dates.
</details>

<details>
<summary>Hint 3: Social Engineering Principles</summary>

Remember Robert Cialdini's principles:
- Reciprocity
- Commitment/Consistency
- Social Proof
- Authority
- Liking
- Scarcity
</details>

## Ethical Guidelines

### DO:
- Practice these techniques only in authorized lab environments
- Understand the psychological principles behind attacks
- Learn to recognize and report social engineering attempts
- Respect privacy and legal boundaries

### DON'T:
- Use these techniques on real people without authorization
- Create fake profiles on real social media platforms
- Send actual phishing emails outside the lab
- Attempt real physical infiltration

## Assessment Criteria

- **Research Quality** (30%): Depth and accuracy of OSINT gathering
- **Creativity** (25%): Innovative approaches to social engineering
- **Technical Execution** (25%): Proper use of tools and techniques
- **Documentation** (20%): Clear reporting and analysis

## Submission Requirements

1. OSINT report with sources and methodology
2. Fake persona profiles with supporting materials
3. Phishing email templates with success metrics
4. Pretexting scenarios and scripts
5. Lessons learned and defensive recommendations

## Defensive Measures

After completing this lab, implement these defenses:
- Security awareness training for employees
- Verify unexpected requests through separate channels
- Implement email authentication (SPF, DKIM, DMARC)
- Restrict information in public directories
- Regular social engineering tests

## Real-World Impact

- 2020: Twitter hack through social engineering of employees
- 2019: Capital One breach started with social engineering
- 2017: Equifax breach included social engineering components
- Ongoing: Business Email Compromise (BEC) costs billions annually

## Tools Included

- **theHarvester**: Email and subdomain enumeration
- **Maltego CE**: OSINT visualization
- **Social-Engineer Toolkit (SET)**: Phishing frameworks
- **ExifTool**: Metadata extraction
- **Custom scripts**: Wikipedia page generator, profile builder

## Clean Up

```bash
docker-compose down
docker volume prune
```

## Additional Resources

- [OSINT Framework](https://osintframework.com/)
- [Social Engineering: The Science of Human Hacking](https://www.wiley.com/en-us/Social+Engineering%3A+The+Science+of+Human+Hacking%2C+2nd+Edition-p-9781119433385)
- [The Art of Deception by Kevin Mitnick](https://sbisc.ut.ac.ir/wp-content/uploads/2015/10/mitnick.pdf)

## Next Lab Preview

Lab 3 will focus on web application exploitation, recreating the E Corp server attacks with SQL injection, XSS, and other OWASP Top 10 vulnerabilities.