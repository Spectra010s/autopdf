from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Babatola_Michael.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Babatola Michael", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("DATA ANALYSIS", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Data analysis is the process of collecting, organizing, examining, and interpreting data in order to discover useful information and support decision-making. Data can include numbers, facts, statistics, survey results, or any information gathered for a specific purpose.""",

"""In today’s digital world, large amounts of data are generated every day through websites, businesses, schools, hospitals, banks, and social media platforms. Data analysis helps transform this raw information into meaningful insights.""",

"""There are different types of data analysis:""",

"""1. Descriptive Analysis
This explains what has already happened by summarizing past data. For example, analyzing students’ exam results to see overall performance.""",

"""2. Diagnostic Analysis
This helps explain why something happened. For example, understanding why sales decreased in a particular month.""",

"""3. Predictive Analysis
This uses past data to predict future outcomes, such as forecasting business profits.""",

"""4. Prescriptive Analysis
This suggests possible solutions or actions based on data findings.""",

"""Data analysts use tools and software such as Microsoft Excel, SQL, Power BI, Python, and Tableau to organize and analyze data. They also use charts, graphs, and dashboards to present results clearly.""",

"""Data analysis is important in many fields, including business, healthcare, education, finance, and technology. It helps organizations make informed decisions instead of relying on guesswork."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN DATA ANALYSIS", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn data analysis because data plays a major role in decision-making in today’s world. Almost every organization relies on data to improve performance, understand customers, and plan for the future. Instead of making decisions based on assumptions, companies use data to make informed and accurate choices.""",

"""One reason I am interested in data analysis is because it develops strong problem-solving and critical thinking skills. It involves identifying patterns, interpreting information, and drawing logical conclusions. I enjoy activities that challenge the mind and require careful analysis.""",

"""I am also curious about how businesses use numbers and statistics to understand customer behavior, improve services, and increase efficiency. Learning data analysis will allow me to understand what information truly means and how it influences important decisions.""",

"""In addition, data analysis offers good financial opportunities. Since many industries depend on data-driven strategies, skilled data analysts are in demand and can earn competitive income. This makes it a valuable and rewarding career path."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.4 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF DATA ANALYSIS", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Demand in the Job Market
Many industries require data analysts to help interpret information and guide decision-making.""",

"""2. Strong Earning Potential
Because data-driven decisions are important, skilled analysts are well compensated.""",

"""3. Improved Decision-Making Skills
Data analysis helps individuals make informed and logical decisions based on facts.""",

"""4. Career Versatility
Data analysis skills can be applied in business, healthcare, finance, education, and technology.""",

"""5. Development of Technical Skills
It improves knowledge of tools like Excel, SQL, and data visualization software.""",

"""6. Problem-Solving Ability
It strengthens analytical thinking and the ability to identify patterns and trends.""",

"""7. Contribution to Organizational Growth
By analyzing data correctly, businesses can improve performance and reduce risks."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)