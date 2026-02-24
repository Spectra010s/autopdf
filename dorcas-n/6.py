from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

file_path = "Data_Processing_Project_Agboola_Fatiu.pdf"
doc = SimpleDocTemplate(file_path, pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
normal_style = styles["BodyText"]

# ---------------- PAGE 1 ----------------
elements.append(Paragraph("DATA PROCESSING PROJECT", title_style))
elements.append(Spacer(1, 0.6 * inch))

elements.append(Paragraph("<b>Name:</b> Agboola Fatiu", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>Class:</b> SS2", normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("<b>School:</b> Emmanuel College", normal_style))
elements.append(PageBreak())

# ---------------- PAGE 2 ----------------
elements.append(Paragraph("SOFTWARE PROGRAMMING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page2_content = [
"""Software programming, also called coding or software development, is the process of designing, writing, testing, and maintaining instructions (called code) that tell a computer or digital device how to function. Programming is the foundation of the modern digital world, transforming abstract ideas into real applications, games, websites, and systems that people use every day.""",

"""Programming is more than typing commands — it combines logic, problem-solving, creativity, and precision. Every app, website, or tool depends on it. Without programming, smartphones, social media, online banking, and even video games would not exist.""",

"""Core Concepts of Programming""",

"""1. Algorithms – Algorithms are step-by-step procedures for solving problems. For example, finding the largest number in a list involves comparing each number in order and keeping track of the largest one. Programming translates these algorithms into instructions that a computer can understand.""",

"""2. Data Types and Structures – Computers handle different kinds of information. Programmers organize data to use it efficiently:

Variables: Store single pieces of information (e.g., age, name)

Arrays/Lists: Store ordered collections of items (e.g., shopping cart items)

Dictionaries/Hash Maps: Store key-value pairs (e.g., username → email address)""",

"""3. Control Flow – Determines how the program runs:

Conditionals (if-else statements) – Allow decisions based on conditions (“If it’s raining, use an umbrella; else, wear sunglasses”)

Loops (for, while) – Repeat actions automatically (“For each item in the shopping cart, calculate the total price”)""",

"""4. Syntax – Every programming language has rules similar to grammar. Correct syntax ensures the computer understands the instructions.""",

"""5. Debugging – Programming involves testing and fixing errors. Debugging is the process of identifying problems in code and correcting them.""",

"""Software Development Life Cycle (SDLC)""",

"""1. Requirement Gathering & Analysis – Understanding what the software should do.""",

"""2. Design – Planning architecture, databases, and user interfaces.""",

"""3. Implementation (Coding) – Writing the actual code based on the design.""",

"""4. Testing – Checking for errors, bugs, and usability issues.""",

"""5. Deployment – Releasing the software to users.""",

"""6. Maintenance – Updating software, fixing bugs, and adding features over time.""",

"""Programming Languages and Paradigms

Low-Level Languages – Close to machine code (e.g., Assembly). Offer precise hardware control but harder for humans to read.

High-Level Languages – Closer to human language (e.g., Python, Java, JavaScript). Easier to learn, write, and maintain.

Programming Paradigms:

1. Procedural Programming – Step-by-step instructions (C)

2. Object-Oriented Programming (OOP) – Organizes code around objects with data and methods (Java, Python, C++)

3. Functional Programming – Uses mathematical functions, avoids changing data (Haskell, Python features)""",

"""Domains and Languages:

Web Development – JavaScript (React, Angular, Vue), Python (Django, Flask)

Mobile Apps – Swift (iOS), Kotlin (Android), Flutter, React Native

Data Science & Machine Learning – Python, R

Game Development – C++, C#""",

"""Tools Used in Programming

Text Editors/IDEs – VS Code, Sublime Text, IntelliJ IDEA, Eclipse

Version Control – Git tracks code changes; GitHub/GitLab/Bitbucket help teams collaborate

Debuggers – Pause and inspect code to find and fix errors""",

"""Impact of Software Programming

Communication – Apps like WhatsApp, Instagram, and email rely on software programming.

Commerce – Online shopping, banking, and payment systems are all powered by software.

Healthcare – Patient management systems, medical imaging software, and diagnostic tools use programming.

Transportation – GPS apps, navigation systems, and modern vehicles depend on software.

Science & Research – Simulations, data analysis, and discoveries in fields like genomics, climate science, and astronomy rely on custom-built software.""",

"""Software programming is a technical skill, a creative discipline, and a tool for shaping the future. It empowers people to solve problems, innovate, and build systems that affect millions of lives every day."""
]

for para in page2_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 3 ----------------
elements.append(Paragraph("REASONS WHY I WANT TO LEARN SOFTWARE PROGRAMMING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page3_content = [
"""I want to learn software programming because it is one of the most versatile and valuable tech skills in the modern world. Programming allows me to create real solutions from ideas, turning imagination into functional apps, games, and systems. It is a skill that combines logic, creativity, and problem-solving, making it exciting and rewarding.""",

"""1. Problem-Solving and Creativity
Programming challenges the mind and encourages creative thinking. Every project is a puzzle: you must figure out how to solve problems efficiently and elegantly. For example, when building a game, I need to think about how characters interact, how levels progress, and how users experience the game — all while making sure the code runs smoothly. This constant challenge develops critical thinking, patience, and creativity.""",

"""2. High Job Demand
Software programming is in high demand across all industries. Companies need developers to build websites, apps, enterprise systems, and automated tools. Tech startups, banks, healthcare providers, educational platforms, and even governments require skilled programmers to manage their digital operations. This high demand ensures a strong career path and job security.""",

"""3. Financial Opportunities
Learning programming opens doors to financial independence. Skilled developers earn competitive salaries globally, and there are opportunities for freelancing, remote work, and even building your own apps or games that generate income. For instance, creating a popular mobile app or game can lead to revenue from ads, subscriptions, or in-app purchases. This makes programming both a creative and financially rewarding skill.""",

"""4. Versatility Across Industries
Programming is not limited to tech companies. It is used in finance to automate processes, in healthcare to manage patient data, in education to create learning platforms, and in entertainment to develop video games and streaming apps. By learning programming, I gain a skill that can be applied almost anywhere, giving me flexibility in career choices.""",

"""5. Contribution to Innovation
Software developers are innovators. By learning programming, I can create apps, tools, or solutions that improve lives. For example, I could build educational software to help students learn faster, a fitness app to track health, or a scheduling tool that simplifies everyday tasks. Programming gives me the power to create impact and improve the world.""",

"""6. Continuous Learning and Growth
Technology evolves rapidly. Learning programming ensures I stay up-to-date with new languages, frameworks, and tools. This constant learning keeps the career interesting and challenging. I also gain the ability to adapt to different types of projects — from web development to mobile apps, AI, data science, and more.""",

"""7. Independence and Freelancing
Programming allows me to work independently. I can take on freelance projects, develop my own apps, or start a tech business. This flexibility means I am not limited to one type of job or location — I can create opportunities for myself while building my portfolio and gaining real-world experience.""",

"""8. Problem Analysis and Logical Thinking
Programming teaches structured thinking. Before writing code, I must analyze the problem, break it into smaller parts, and plan the solution. This strengthens analytical skills, logical reasoning, and decision-making — abilities that are valuable in every aspect of life, not just tech.""",

"""9. Future Relevance
Software powers almost everything in our daily lives: social media, online banking, education, healthcare, games, and even transportation. By learning programming, I acquire a skill that will remain relevant for decades, preparing me for a future where technology is central to almost every career.""",

"""Overall, I chose software programming because it combines creativity, problem-solving, career opportunities, financial growth, and real-world impact. It is not just a skill — it is a gateway to shaping the future and creating meaningful digital experiences."""
]

for para in page3_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

elements.append(PageBreak())

# ---------------- PAGE 4 ----------------
elements.append(Paragraph("BENEFITS OF SOFTWARE PROGRAMMING", title_style))
elements.append(Spacer(1, 0.4 * inch))

page4_content = [
"""1. High Job Demand
Almost every industry relies on software. Companies, startups, banks, hospitals, educational platforms, and governments all need programmers. This high demand ensures job security and a variety of career opportunities.""",

"""2. Financial Rewards
Skilled programmers are highly paid worldwide. Learning programming opens doors to full-time jobs, freelancing, and entrepreneurship. For example, building a popular mobile app or web platform can generate income through subscriptions, ads, or direct sales.""",

"""3. Versatility Across Fields
Programming skills can be applied in multiple areas:

Web and mobile app development

Game development

Data science and machine learning

Artificial intelligence

Automation and robotics
This versatility allows programmers to explore different careers and work environments.""",

"""4. Creativity and Innovation
Programming is a creative skill. You can develop apps, tools, or games that solve real-world problems or entertain millions. For example, creating an educational app to help students learn faster or a productivity tool to simplify daily tasks.""",

"""5. Problem-Solving Skills
Programming strengthens logical thinking and analytical skills. It teaches how to break large problems into smaller, manageable tasks and solve them systematically. These skills are valuable not only in tech but in daily life and other professions.""",

"""6. Global Opportunities
With programming skills, you can work remotely, freelance, or join international companies. Geography is no longer a barrier; projects and jobs can come from anywhere in the world.""",

"""7. Independence and Entrepreneurship
Programming empowers you to create your own projects, apps, or even startups. You don’t need to rely solely on a company — you can build products, test ideas, and earn income independently.""",

"""8. Continuous Learning
Technology evolves rapidly. Learning programming ensures you remain adaptable, learning new languages, frameworks, and tools. This continuous growth keeps your skills relevant and future-proof.""",

"""9. Societal Impact
Programs and applications created by developers improve everyday life:

Healthcare apps help manage patient care

Educational software improves learning

Automation tools save time and reduce human error
Programming allows you to make meaningful contributions that positively affect society.""",

"""10. Professional Recognition
Being able to write code and build software is a respected skill worldwide. It demonstrates technical ability, creativity, problem-solving, and perseverance — qualities valued in any profession.""",

"""11. Confidence and Empowerment
Learning to code gives a sense of achievement. Being able to build a website, app, or game from scratch boosts confidence and shows that you can create something tangible from an idea.""",

"""12. Future-Proof Career
As technology continues to grow, programming remains a core skill for the digital age. Learning it ensures that you have a skill that will be useful for decades, whether in tech or any other sector that relies on digital solutions.""",

"""By learning software programming, I gain a powerful, versatile, and future-oriented skill that allows me to create, innovate, and succeed. It is not just about writing code — it is about building tools, solving problems, and shaping the digital world around me."""
]

for para in page4_content:
    elements.append(Paragraph(para, normal_style))
    elements.append(Spacer(1, 0.35 * inch))

doc.build(elements)