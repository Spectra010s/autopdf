from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Akanni_Oyindamola.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Akanni Oyindamola", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("DIGITAL MARKETING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Digital marketing is the promotion of products, services, or brands using digital technologies and online platforms. It involves using the internet, social media, search engines, email, and websites to reach and engage customers.""",

"""Unlike traditional marketing, which uses newspapers, radio, or television, digital marketing allows businesses to connect directly with their target audience through digital devices such as smartphones, laptops, and tablets.""",

"""Digital marketing includes several key areas:""",

"""1. Social Media Marketing
This involves promoting products or services on platforms such as Instagram, Facebook, Twitter, and TikTok to attract and engage users.""",

"""2. Search Engine Optimization (SEO)
SEO is the process of improving a website’s visibility on search engines like Google so that it appears higher in search results.""",

"""3. Content Marketing
This focuses on creating valuable content such as blog posts, videos, and graphics to attract and retain customers.""",

"""4. Email Marketing
Businesses use emails to send updates, promotions, and important information to customers.""",

"""5. Online Advertising
This includes paid advertisements on websites, social media, and search engines to increase brand awareness and sales.""",

"""Digital marketing relies on data and analytics to measure performance. Marketers analyze engagement, clicks, views, and customer behavior to improve strategies. In today’s digital world, it is one of the most effective ways for businesses to grow and compete."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN DIGITAL MARKETING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn digital marketing because businesses and brands are increasingly moving online. Almost every company needs a strong online presence to succeed in today’s competitive environment. Understanding digital marketing will allow me to help businesses grow and reach their target audience effectively.""",

"""One reason I am interested in digital marketing is because it combines creativity with strategy. It involves creating engaging content while also analyzing data to understand what works best. I enjoy the idea of influencing how products and services are presented to people online.""",

"""Another reason is the financial opportunity it offers. Digital marketing skills are in high demand, and professionals in this field can earn good income by working for companies or freelancing. Many businesses rely on digital marketing to increase sales, which makes it a valuable and rewarding skill.""",

"""Additionally, digital marketing provides flexibility and independence. With this skill, I can work remotely, manage online campaigns, or even promote my own business in the future. It is a modern skill that keeps me relevant in a technology-driven society.""",

"""Overall, I chose digital marketing because it combines creativity, business knowledge, and financial potential in a rapidly growing digital industry."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF DIGITAL MARKETING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Demand Across Industries
Almost every industry requires digital marketing to attract and retain customers.""",

"""2. Income and Freelancing Opportunities
Skilled digital marketers can work independently or with companies locally and internationally.""",

"""3. Measurable Results
Digital marketing allows businesses to track performance using analytics tools.""",

"""4. Career Flexibility
Professionals can work remotely and manage campaigns online.""",

"""5. Business Growth
Digital marketing helps businesses increase visibility, customer engagement, and sales.""",

"""6. Skill Development
It improves communication skills, creativity, strategic thinking, and data analysis abilities.""",

"""7. Global Reach
Through digital platforms, businesses can reach audiences worldwide.""",

"""By learning digital marketing, I will gain a valuable skill that supports business growth, creativity, and financial development in the modern digital economy."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)