from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Oseni_Ireayomi.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Oseni Ireayomi", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("ETHICAL HACKING (Everything About It)", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""What is Ethical Hacking?
Ethical hacking is the practice of testing computer systems, networks, or applications to find security weaknesses — legally and with permission — before real hackers can exploit them.""",

"""An ethical hacker is also called a white-hat hacker. Unlike cybercriminals (black-hat hackers), ethical hackers work to protect organizations by identifying vulnerabilities and helping to fix them.""",

"""Ethical hacking is a major part of cybersecurity.""",

"""What Do Ethical Hackers Do?
Ethical hackers:
- Test websites for security loopholes
- Check networks for weaknesses
- Find system vulnerabilities
- Perform penetration testing (simulated attacks)
- Identify malware risks
- Test mobile app security
- Help companies strengthen their security systems
They basically think like criminals — but act legally to prevent attacks.""",

"""Types of Ethical Hacking
- Web Application Hacking
Testing websites for issues like SQL injection, broken authentication, and data leaks.
- Network Hacking
Checking routers, servers, and firewalls for weaknesses.
- System Hacking
Testing operating systems for vulnerabilities.
- Mobile App Hacking
Testing Android and iOS apps for security flaws.
- Social Engineering Testing
Testing how vulnerable employees are to phishing and scams.""",

"""Common Tools Used in Ethical Hacking
Ethical hackers use professional tools like:
- Kali Linux
- Wireshark
- Metasploit
- Burp Suite
- Nmap
These tools help scan networks, analyze traffic, and simulate attacks.""",

"""Skills Needed to Become an Ethical Hacker
To succeed in ethical hacking, one needs:
- Strong knowledge of networking
- Understanding of operating systems (Linux, Windows)
- Programming skills (Python, C, JavaScript)
- Knowledge of cybersecurity principles
- Problem-solving skills
- Analytical thinking
Ethical hacking requires patience, attention to detail, and critical thinking.""",

"""Why Ethical Hacking is Important Today
With the rise of digital banking, online businesses, social media, and cloud storage, cybercrime has increased significantly. Companies, governments, and individuals store sensitive data online.
Without ethical hackers, organizations would be more vulnerable to:
- Data breaches
- Identity theft
- Financial fraud
- Ransomware attacks
- Privacy violations
Ethical hackers help prevent financial loss and protect people's personal information."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("WHY I CHOSE ETHICAL HACKING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I chose ethical hacking because it is a powerful and respected tech skill in today’s digital world. As technology continues to grow, cybersecurity has become one of the most important fields globally.""",

"""One major reason I am interested in ethical hacking is the strong demand for cybersecurity professionals. Almost every company — from banks to schools to tech firms — needs security experts to protect their systems. This makes it a highly relevant and future-proof career.""",

"""Another reason is the intellectual challenge it provides. Ethical hacking requires deep thinking, problem-solving, and creativity. It is not a boring or repetitive job; instead, it constantly presents new challenges because hackers are always developing new methods. This means there is continuous learning and growth in the field.""",

"""I am also interested in ethical hacking because of the financial opportunities it offers. Cybersecurity professionals are highly paid due to the critical nature of their work. Since organizations depend heavily on secure systems, they are willing to invest in skilled ethical hackers. This makes it a financially rewarding career path.""",

"""Additionally, ethical hacking gives a sense of responsibility and impact. Knowing that your skills are being used to protect people’s data and prevent cybercrime is meaningful. It allows one to contribute positively to society by fighting digital threats.""",

"""Overall, I chose ethical hacking because it combines intelligence, responsibility, high demand, career growth, and strong financial potential."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF ETHICAL HACKING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Job Demand
Cybersecurity experts are needed worldwide. This creates strong job security and career stability.""",

"""2. Competitive Salary
Ethical hackers earn high salaries because their skills are rare and highly valuable.""",

"""3. Global Opportunities
Cybersecurity skills are universal. Ethical hackers can work for international companies or even remotely.""",

"""4. Career Growth
The field offers many certifications and specializations such as:
- Penetration testing
- Network security
- Cloud security
- Security analysis
This allows continuous career advancement.""",

"""5. Personal Skill Development
Ethical hacking improves:
- Critical thinking
- Logical reasoning
- Technical knowledge
- Attention to detail
- Problem-solving skills""",

"""6. Protection of Society
Ethical hackers help prevent cybercrime, fraud, and identity theft. Their work protects individuals, businesses, and governments.""",

"""7. Freelance and Consulting Opportunities
Many ethical hackers work independently as consultants, offering security services to different organizations."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)