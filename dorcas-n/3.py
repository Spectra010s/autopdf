from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Olarewaju_Faith.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Olarewaju Faith", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("CLOUD COMPUTING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Cloud computing is the delivery of computing services such as storage, databases, networking, software, and processing power over the internet instead of using local computers or physical servers. In simple terms, it allows individuals and organizations to store and access data online rather than on a personal device.""",

"""Traditionally, data and software were stored on physical hardware like hard drives or company servers. However, cloud computing allows users to store their data in secure online data centers managed by cloud service providers. This makes information accessible from anywhere in the world as long as there is an internet connection.""",

"""There are three main types of cloud computing services:""",

"""1. Infrastructure as a Service (IaaS)
This provides virtual servers and storage over the internet. Companies can rent computing infrastructure instead of buying physical hardware.""",

"""2. Platform as a Service (PaaS)
This provides a platform that allows developers to build, test, and deploy applications without managing the underlying infrastructure.""",

"""3. Software as a Service (SaaS)
This allows users to access software applications online without installing them on their devices. Examples include Google Drive, Dropbox, and online email services.""",

"""Cloud computing can also be classified into different deployment models:""",

"""1. Public Cloud – Services provided over the public internet.""",
"""2. Private Cloud – Cloud systems used exclusively by one organization.""",
"""3. Hybrid Cloud – A combination of public and private cloud systems.""",

"""Cloud computing improves efficiency, flexibility, and scalability. Businesses can easily increase or reduce storage and computing power based on their needs. It also enhances collaboration, as multiple users can access and edit files in real time from different locations.""",

"""Today, cloud computing is essential in industries such as banking, healthcare, education, entertainment, and government operations. It supports online banking systems, streaming services, remote work platforms, and large-scale business operations."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN CLOUD COMPUTING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn cloud computing because it is one of the most important technologies supporting the modern digital world. Almost every online service people use today depends on cloud infrastructure. From storing photos and documents to running large business systems, cloud computing makes digital access possible and efficient.""",

"""One major reason I am interested in cloud computing is because it focuses on how large systems are built and managed. I want to understand how data is stored securely, how servers operate remotely, and how companies manage massive amounts of information without relying solely on physical hardware. Learning cloud computing will give me insight into how global digital systems function.""",

"""Another reason is the growing importance of remote work and online collaboration. Cloud computing enables people to work from different locations while accessing shared resources securely. As technology continues to evolve, cloud-based systems will remain essential in business operations. Being skilled in cloud computing means being prepared for the future of digital work environments.""",

"""In addition, cloud computing offers strong financial opportunities. Many organizations rely heavily on cloud services, and there is high demand for professionals who can manage cloud infrastructure, security, and storage systems. Because of this demand, cloud computing provides stable career prospects and competitive income potential.""",

"""Cloud computing also allows specialization in areas such as:""",

"""1. Cloud Architecture""",
"""2. Cloud Security""",
"""3. Cloud Engineering""",

"""Furthermore, cloud computing supports innovation. Startups and large companies use cloud platforms to develop applications, store data, and scale their operations quickly. By learning cloud computing, I would gain the ability to contribute to building and managing powerful digital systems.""",

"""Overall, I chose cloud computing because it combines technical knowledge, future relevance, career stability, and financial growth. It is a foundational technology that supports modern digital transformation."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF CLOUD COMPUTING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Demand in the Technology Industry
As more organizations move their operations online, the demand for cloud professionals continues to increase.""",

"""2. Financial Stability
Cloud computing specialists are well compensated due to their technical expertise and the importance of their role.""",

"""3. Scalability and Flexibility
Cloud systems allow businesses to adjust their computing resources based on demand.""",

"""4. Improved Collaboration
Cloud services enable real-time collaboration and remote access to shared files and systems.""",

"""5. Enhanced Security
Cloud providers invest heavily in advanced security measures to protect data.""",

"""6. Career Opportunities Across Industries
Cloud computing skills are needed in healthcare, finance, education, government, and entertainment sectors.""",

"""7. Continuous Innovation
Cloud platforms support artificial intelligence, big data analytics, and advanced digital services.""",

"""8. Global Accessibility
Cloud systems allow access to data and services from anywhere in the world.""",

"""By learning cloud computing, I will gain a valuable and future-oriented technological skill that supports digital infrastructure, career growth, and financial advancement in a technology-driven world."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)