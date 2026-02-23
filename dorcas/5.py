from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Jimoh_Olakishi.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Jimoh Olakishi", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("GRAPHIC DESIGNING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Graphic designing is the art and practice of creating visual content to communicate ideas, messages, and information. It involves combining text, images, colors, shapes, and layouts to produce designs that are visually appealing and meaningful.""",

"""Graphic design plays an important role in communication because people understand visuals faster than plain text. Businesses, schools, organizations, and individuals use graphic design to promote their services, build brand identity, and attract attention.""",

"""There are different areas of graphic designing, including:""",

"""1. Logo Design
This involves creating unique symbols or marks that represent a company or brand.""",

"""2. Branding and Identity Design
This includes designing brand colors, business cards, letterheads, and other materials that create a consistent image.""",

"""3. Social Media Design
Graphic designers create posts, banners, and advertisements for platforms like Instagram and Facebook.""",

"""4. Print Design
This includes posters, flyers, brochures, magazines, and packaging.""",

"""5. Digital Design
This involves creating website banners, online ads, and digital illustrations.""",

"""Graphic designers use software tools such as Canva, Adobe Photoshop, Adobe Illustrator, and CorelDRAW to create professional designs. They apply design principles like balance, contrast, alignment, repetition, and hierarchy to ensure their work looks organized and attractive.""",

"""In today’s digital age, graphic designing is a powerful skill because visuals are everywhere — in advertisements, websites, billboards, and social media."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("BENEFITS OF GRAPHIC DESIGNING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""Graphic designing offers many benefits both personally and professionally.""",

"""1. Income Opportunities
Graphic designers can earn money through freelancing, working in companies, or starting their own design business.""",

"""2. High Demand
Many businesses, organizations, and influencers require graphic designers for branding and marketing.""",

"""3. Creativity Development
It enhances artistic skills and encourages innovation.""",

"""4. Career Flexibility
Graphic designers can work remotely or independently.""",

"""5. Personal Branding
With this skill, I can create professional designs for my own projects or business.""",

"""6. Communication Skills
Graphic design improves the ability to communicate ideas clearly through visuals.""",

"""7. Continuous Growth
Technology and design trends keep evolving, which allows designers to continuously learn and improve."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN GRAPHIC DESIGNING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""I want to learn graphic designing because I have a strong interest in creativity and visual expression. I enjoy combining colors, images, and text to create something attractive and meaningful. Graphic designing allows me to turn ideas into visual reality.""",

"""Another major reason I want to learn graphic designing is the financial opportunity it offers. Many businesses need graphic designers to promote their products and services. With this skill, I can earn money by working for companies or by freelancing online. It is a skill that can generate income even while I am still a student.""",

"""Graphic designing also gives me independence. Instead of depending only on traditional jobs, I can create designs for clients, manage my own projects, and even build my personal brand. It provides flexibility because I can work from home and connect with clients globally.""",

"""Additionally, graphic design improves creativity and critical thinking. It challenges me to think about how to communicate messages clearly and effectively through visuals. It also helps develop patience, attention to detail, and problem-solving skills.""",

"""Furthermore, in today’s digital world, visual communication is very important. Learning graphic designing will help me stay relevant in a technology-driven society and open doors to many career opportunities."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)