from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Azeez_Victoria.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Azeez Victoria", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("DATA VISUALIZATION", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Data visualization is the process of turning raw data into visual formats such as charts, graphs, dashboards, and interactive reports. Instead of looking at plain numbers, people can understand information quickly and make better decisions when it is presented visually.""",

"""In today’s world, data is everywhere. Companies, schools, hospitals, banks, and governments collect massive amounts of information daily. Data visualization helps make sense of all this data so it can be interpreted easily and accurately.""",

"""Types of Data Visualization""",

"""- Bar Charts – Compare categories of data side by side""",
"""- Line Charts – Show trends over time""",
"""- Pie Charts – Show proportions or percentages of a whole""",
"""- Scatter Plots – Show relationships between two variables""",
"""- Heat Maps – Show data intensity or density using colors""",
"""- Dashboards – Combine multiple visualizations in one interactive display""",

"""Tools for Data Visualization""",

"""- Microsoft Excel – Basic charts and graphs""",
"""- Tableau – Interactive and professional dashboards""",
"""- Power BI – Business-focused data visualization""",
"""- Google Data Studio – Online interactive dashboards""",
"""- Python (Matplotlib, Seaborn) – Programming-based visualization""",

"""These tools help analysts transform complex datasets into visuals that are easy to understand and interpret.""",

"""Importance of Data Visualization""",

"""- Simplifies complex information – Large datasets can be confusing in raw form, but visualization makes it clear""",
"""- Supports decision-making – Businesses use visual data to understand trends, identify problems, and make better strategies""",
"""- Improves communication – Charts and dashboards help explain insights clearly to teams, clients, or management""",
"""- Identifies patterns and trends – Visualization makes hidden patterns visible, guiding predictions and strategies""",
"""- Saves time – Visual data is faster to interpret than large tables of numbers""",

"""Applications of Data Visualization""",

"""- Business – Analyze sales, customer behavior, and market trends""",
"""- Healthcare – Track patient data, disease trends, and treatment outcomes""",
"""- Education – Monitor student performance and curriculum effectiveness""",
"""- Government – Present census data, population statistics, and public service information""",
"""- Sports – Track player performance and team statistics""",

"""Data visualization is not just about making pretty graphs. It combines analytical thinking, creativity, and technical skills to present data in a meaningful way. Being able to visualize data effectively is a highly valuable skill in the modern digital world."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN DATA VISUALIZATION", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn data visualization because it combines creativity with analytical thinking. It is not just about numbers — it is about designing visuals that make sense and communicate information clearly.""",

"""Understanding information quickly – In today’s fast-paced world, businesses and organizations cannot spend hours interpreting data. Visualization makes insights easy to see and act upon.""",

"""Versatility – Data visualization is used everywhere: analyzing sales trends, predicting customer behavior, tracking social media performance, helping scientists understand research results, and more. Learning this skill will give me the ability to work in many industries and solve real-world problems.""",

"""Creativity and technical skill – Data visualization involves understanding data, choosing the right visualization type, designing appealing visuals, and presenting information effectively. This combination makes it a fun, rewarding, and intellectually stimulating skill.""",

"""Career growth – Professionals skilled in data visualization are highly sought after in business intelligence, finance, marketing, healthcare, education, and tech industries.""",

"""Financial opportunities – Organizations value employees who can turn data into actionable insights, which leads to competitive salaries and career stability.""",

"""Problem-solving – Learning data visualization improves analytical thinking and decision-making skills, as it requires identifying patterns, trends, and insights in large datasets.""",

"""Future relevance – As data continues to grow globally, the ability to interpret and present it visually will remain a crucial and in-demand skill.""",

"""Overall, I chose data visualization because it combines problem-solving, creativity, career growth, and financial potential. It is a modern, practical, and highly relevant skill for the future."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF DATA VISUALIZATION", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""- Clear communication of information – It turns complex data into visuals that are easy to understand.""",
"""- Faster decision-making – Businesses and organizations can make better decisions quickly.""",
"""- Career opportunities – Skilled professionals are needed in data analysis, business intelligence, marketing, and healthcare.""",
"""- Creativity and technical skill development – It combines design skills with analytical thinking.""",
"""- Problem-solving skills – Learning to choose the right chart or visualization type improves critical thinking.""",
"""- Better data understanding – Visualization helps identify patterns, trends, and outliers that might be missed in raw data.""",
"""- Presentation skills – Data visualization improves the ability to present data professionally to others.""",
"""- Versatility across industries – Data visualization is used in business, education, government, healthcare, sports, and tech.""",
"""- Decision support – Data visualization allows companies to spot risks, opportunities, and trends quickly.""",

"""By learning data visualization, I will gain a skill that helps interpret information, communicate clearly, make smarter decisions, and remain valuable in the modern technology-driven world."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)