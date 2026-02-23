from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Olusanya_Olayinka.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Olusanya Olayinka", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("VIDEO EDITING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Video editing is the process of arranging, cutting, modifying, and enhancing video clips to create a final, polished visual production. It involves combining different video scenes, audio, effects, text, and transitions to communicate a clear and engaging message.""",

"""Video editing plays a major role in digital media today. Almost everything we watch — movies, YouTube videos, advertisements, documentaries, music videos, and social media content — goes through video editing before being published.""",

"""There are several important aspects of video editing:""",

"""1. Cutting and Trimming
This involves removing unwanted parts of a video and selecting the best clips to create a smooth flow.""",

"""2. Transitions and Effects
Editors use transitions to connect scenes smoothly and apply visual effects to improve the overall appearance.""",

"""3. Audio Editing
This includes adjusting sound quality, adding background music, and synchronizing audio with video.""",

"""4. Color Correction and Grading
This improves lighting, brightness, and color balance to make videos look professional.""",

"""5. Text and Graphics
Editors can add subtitles, captions, and animated text to make content clearer and more engaging.""",

"""Video editors use software such as CapCut, Adobe Premiere Pro, Final Cut Pro, and DaVinci Resolve to produce high-quality videos. In today’s digital age, video content is one of the most powerful forms of communication, making video editing an important technical skill."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN VIDEO EDITING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn video editing because video content has become one of the most effective ways of communicating information and entertainment. Social media platforms, online businesses, and content creators rely heavily on videos to attract and engage audiences.""",

"""One reason I am interested in video editing is because it combines creativity with technical skills. It allows me to transform ordinary recordings into professional and engaging content. I enjoy the idea of shaping a story through visuals, sound, and effects.""",

"""Another reason is the growing demand for video content in today’s world. Businesses use videos for advertisements, product promotions, and brand awareness. Content creators use edited videos to grow their online presence. Learning video editing will allow me to contribute to this digital space confidently.""",

"""Video editing also offers financial opportunities. Skilled video editors can work with companies, content creators, or freelance independently. Since video content continues to grow across platforms, it creates a steady demand for professional editors.""",

"""Overall, I chose video editing because it allows creative expression while also providing career growth and income potential in the digital media industry."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF VIDEO EDITING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Demand in Digital Media
As online platforms continue to grow, the demand for video editors increases.""",

"""2. Income Opportunities
Video editors can earn money through freelancing, working for media companies, or collaborating with content creators.""",

"""3. Creativity Development
It improves storytelling ability, creativity, and attention to detail.""",

"""4. Technical Skill Development
Learning editing software enhances digital and technical knowledge.""",

"""5. Career Flexibility
Video editors can work remotely and manage projects independently.""",

"""6. Personal Branding
With video editing skills, one can create professional content for personal projects or businesses.""",

"""7. Communication Skills
Video editing helps in presenting ideas clearly through visual storytelling.""",

"""By learning video editing, I will gain a valuable digital skill that is relevant in modern communication, business, and entertainment industries."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)