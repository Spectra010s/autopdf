from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Dada_Setemi.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Dada Setemi", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("MOBILE APP DEVELOPMENT", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Mobile app development is the process of creating applications that run on smartphones, tablets, and other mobile devices. These apps are designed to perform specific functions, entertain users, or provide services, and they are widely used in everyday life.""",

"""Mobile app development involves combining programming, design, and user experience to create functional and visually appealing applications. Apps can be native (designed for a specific platform like Android or iOS), web-based (accessible via browsers), or hybrid (working on multiple platforms).""",

"""There are several types of mobile apps:""",

"""1. Social Media Apps
Examples include Instagram, Facebook, TikTok, and WhatsApp. These apps allow users to communicate, share content, and stay connected.""",

"""2. Gaming Apps
Games like Call of Duty Mobile (CODM), Candy Crush, and PUBG are examples of apps developed to entertain users. Game apps are usually highly interactive and require advanced programming.""",

"""3. Productivity Apps
These apps help users organize tasks, manage schedules, and increase efficiency. Examples include Google Calendar, Notion, and Microsoft To-Do.""",

"""4. Utility Apps
Apps such as banking apps, weather apps, and e-wallet apps provide essential services and make everyday activities easier.""",

"""Mobile app developers use programming languages such as Java, Kotlin, Swift, and Flutter, as well as development tools like Android Studio and Xcode. They focus on creating apps that are user-friendly, responsive, and secure.""",

"""Mobile apps are now an essential part of modern life. They provide entertainment, convenience, communication, and access to information. Learning mobile app development gives the skills to create these digital tools and contribute to technological growth."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN MOBILE APP DEVELOPMENT", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn mobile app development because mobile apps are used by millions of people around the world every day. Apps like Call of Duty Mobile (CODM), TikTok, Instagram, and WhatsApp are widely popular, and creating such apps allows me to reach a large audience with useful or entertaining products.""",

"""One reason I am interested in mobile app development is because it combines creativity and technical skills. Developing apps requires designing interfaces that are attractive and easy to use while also coding the features that make the app work. I enjoy activities that challenge the mind and allow me to turn ideas into functional products.""",

"""Another reason is the financial opportunity this skill offers. Skilled mobile app developers are highly sought after, and they can earn a good income by working for tech companies or freelancing. Apps that solve problems, provide entertainment, or serve businesses can also generate revenue through advertisements, in-app purchases, or subscriptions.""",

"""Learning mobile app development also allows me to be independent. I can create my own apps, start small digital projects, or even develop games like CODM. It provides both a creative outlet and the chance to build a future career in technology.""",

"""Overall, I chose mobile app development because it combines creativity, technical knowledge, and financial potential, making it an exciting and future-oriented skill."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF MOBILE APP DEVELOPMENT", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Demand in the Job Market
As smartphones continue to dominate daily life, companies need skilled developers to create apps for their businesses and services.""",

"""2. Financial Opportunities
Mobile app development can provide income through employment, freelancing, or creating apps that generate revenue.""",

"""3. Creativity and Innovation
Developing apps allows me to design interfaces, create games, and solve real-world problems with technology.""",

"""4. Career Flexibility
With mobile app development skills, I can work for companies, freelance, or even start my own tech projects.""",

"""5. Technical Skill Development
Learning to code, design interfaces, and manage app functionality improves overall digital literacy.""",

"""6. Personal Projects
I can create apps for personal use, games, or small businesses, allowing me to apply my skills practically.""",

"""7. Global Impact
Apps can be used by people worldwide, allowing developers to reach a wide audience and make a meaningful impact.""",

"""Mobile app development is a powerful and versatile skill that opens doors to creativity, career growth, and financial opportunities. Learning it will equip me with tools to participate in the rapidly growing digital world."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)