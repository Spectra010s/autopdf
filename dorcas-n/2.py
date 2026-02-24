from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Ijaduola_Ibukunoluwa.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Ijaduola Ibukunoluwa", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("ARTIFICIAL INTELLIGENCE (AI)", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Artificial Intelligence (AI) is a branch of computer science that focuses on creating machines and computer systems that can perform tasks that normally require human intelligence. These tasks include learning, reasoning, problem-solving, decision-making, understanding language, and recognizing patterns.""",

"""In simple terms, AI allows computers to “think” and “learn” from experience instead of only following fixed instructions.""",

"""Artificial Intelligence works by using algorithms and large amounts of data to train computer systems. Through a process called machine learning, AI systems can improve their performance over time without being manually programmed for every task.""",

"""There are different types of Artificial Intelligence:""",

"""1. Machine Learning (ML)
Machine learning enables computers to learn from data and improve automatically. For example, recommendation systems on streaming platforms suggest movies based on previous viewing history.""",

"""2. Natural Language Processing (NLP)
This allows machines to understand and respond to human language. It is used in chatbots, voice assistants, and translation tools.""",

"""3. Computer Vision
This enables machines to recognize images and objects. Facial recognition systems and medical image analysis use computer vision.""",

"""4. Robotics
AI is used in robots to perform tasks such as manufacturing, surgery, or automated delivery.""",

"""AI is used in many industries, including healthcare, finance, education, transportation, and entertainment. For example.""",

"""As technology advances, Artificial Intelligence continues to grow and influence nearly every aspect of modern life."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN ARTIFICIAL INTELLIGENCE", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn Artificial Intelligence because it is one of the most advanced and rapidly growing fields in technology. AI is shaping the future, and many modern innovations depend on intelligent systems. Learning AI will allow me to understand how smart technologies work and how they are developed.""",

"""One reason I am interested in AI is because it combines mathematics, programming, and logical thinking. It challenges the mind and requires deep analytical skills.""",

"""Another reason is the impact AI has on society. AI systems are used to improve healthcare, increase business efficiency, enhance security systems, and make daily tasks easier. Being part of a field that contributes to major technological advancements is highly motivating.""",

"""In addition, Artificial Intelligence offers strong financial opportunities. Due to its complexity and demand, AI professionals are highly valued in the job market. Many companies invest heavily in AI research and development, making it a financially rewarding career path.""",

"""AI also provides opportunities for specialization, such as:""",

"""1. Machine Learning Engineering""",
"""2. AI Research""",
"""3. Robotics Engineering""",
"""4. Data Science""",

"""Overall, I chose Artificial Intelligence because it represents the future of technology. It combines innovation, intellectual challenge, global impact, and financial growth in one powerful field."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF ARTIFICIAL INTELLIGENCE", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Global Demand
AI professionals are needed in many industries worldwide.""",

"""2. Strong Earning Potential
Because AI requires advanced knowledge and skills, it offers competitive salaries.""",

"""3. Innovation and Creativity
AI allows the creation of intelligent systems that solve complex real-world problems.""",

"""4. Career Growth Opportunities
There are many roles in AI, including AI engineer, machine learning specialist, robotics engineer, and data scientist.""",

"""5. Problem-Solving Development
Studying AI improves logical reasoning, analytical thinking, and technical skills.""",

"""6. Contribution to Technological Advancement
AI drives innovation in healthcare, transportation, education, and communication.""",

"""By learning Artificial Intelligence, I will gain a highly advanced and respected technological skill that prepares me for future innovations and opportunities in the digital world."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)