from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Bankole_Ayoyemi.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Bankole Ayoyemi", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("CYBERSECURITY", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Cybersecurity is the practice of protecting computers, mobile devices, networks, software systems, and digital data from cyber threats and unauthorized access. In today’s modern world, almost everything is connected to the internet — banking, communication, education, healthcare, business transactions, and even government operations. Because of this, protecting digital information has become extremely important.""",

"""Cyber threats are malicious activities carried out by hackers or cybercriminals to steal, damage, or disrupt data and systems. Some common types of cyber threats include:""",

"""1. Hacking – Gaining unauthorized access to computer systems or accounts.""",
"""2. Phishing – Sending fake emails or messages to trick people into revealing personal information.""",
"""3. Malware – Harmful software designed to damage or control systems.""",
"""4. Ransomware – A type of attack where hackers lock a system and demand payment to unlock it.""",
"""5. Identity Theft – Stealing someone’s personal information for fraud.""",

"""Cybersecurity focuses on preventing these attacks and protecting sensitive information""",

"""There are several branches of cybersecurity:""",

"""1. Network Security – Protecting internet and internal networks from unauthorized access.""",
"""2. Information Security – Protecting data from being altered or stolen.""",
"""3. Application Security – Ensuring apps and software are safe from vulnerabilities.""",
"""4. Cloud Security – Protecting data stored online in cloud systems.""",
"""5. Ethical Hacking (Penetration Testing) – Professionals legally test systems to identify weaknesses before criminals do.""",

"""Cybersecurity professionals use tools such as firewalls, encryption systems, antivirus software, monitoring systems, and security audits to detect and prevent threats.""",

"""As technology continues to grow, cybersecurity has become one of the most essential fields in the digital world. Without cybersecurity, online services such as banking apps, shopping platforms, and communication systems would not be safe to use."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN CYBERSECURITY", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn cybersecurity because technology is becoming more advanced every day, and cyber threats are increasing rapidly. Many individuals and organizations rely on digital platforms to store and manage sensitive information. Protecting this information is a serious responsibility.""",

"""One reason I am interested in cybersecurity is because it requires intelligence, strategy, and critical thinking. Cybersecurity professionals must constantly analyze systems, identify potential risks, and develop solutions to prevent attacks.""",

"""In addition, cybersecurity offers strong financial opportunities. Because cybercrime is increasing globally, companies, banks, hospitals, and governments invest heavily in cybersecurity professionals. This high demand makes it a stable and well-paying career path.""",

"""Cybersecurity also provides opportunities for career growth and specialization. Some common roles include:""",

"""1. Security Analyst""",
"""2. Penetration Tester""",
"""3. Security Engineer""",
"""4. Cyber Consultant""",

"""Overall, I chose cybersecurity because it combines intellectual challenge, social impact, career stability, and financial growth. It is a future-oriented skill that remains relevant as long as technology exists."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF CYBERSECURITY", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Global Demand – Organizations worldwide require cybersecurity experts to protect their digital systems.""",
"""2. Strong Income Potential – Cybersecurity offers competitive salaries and financial stability.""",
"""3. Job Security – As long as digital systems exist, there will always be a need for security professionals.""",
"""4. Continuous Learning and Growth – Cyber threats constantly evolve, requiring ongoing learning.""",
"""5. Development of Analytical and Technical Skills – It improves logical reasoning and technical knowledge.""",
"""6. Opportunity to Work in Various Industries – Banking, healthcare, government, education, and more.""",

"""By learning cybersecurity, I will gain a powerful technical skill that provides financial stability and allows me to contribute to protecting digital systems in an increasingly connected world."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)