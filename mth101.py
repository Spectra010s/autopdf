from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import re

def replace_math_symbols(text):
    """Replaces text shorthand with math symbols and cleans spacing."""
    replacements = {
        "AUB": "A ∪ B",
        "AnB": "A ∩ B",
        " n ": " ∩ ",
        " U ": " ∪ ", 
        "sqrt": "√",
        "subset": "⊂",
        "intersection": "∩",
        "union": "∪",
        "infinity": "∞",
        "plusminus": "±",
        "+-": "±",
        "<=": "≤",
        ">=": "≥"
    }
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text

def create_mth101_pdf():
    filename = "MTH-101-by-Spectra010s.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom style for readability: increased leading and space after
    q_style = ParagraphStyle(
        'QStyle', 
        parent=styles['Normal'], 
        spaceAfter=15, 
        leading=16,
        alignment=0
    )
    
    story = []

    # Title
    story.append(Paragraph("MTH 101 Past Questions & Solutions", styles['Title']))
    story.append(Paragraph("By Spectra010s", styles['Heading3']))
    story.append(Spacer(1, 12))

    questions_raw = [
        "1. If A is a subset of a universal set U, the compliment of set A is given as: A. U B. U-A C. U+B D. U-B",
        "2. The set statement (AUB) NC = AU (BN)C is relevant to A. Associative Law B. Cummulative lowa C. Distributibe Law D. Closure",
        "3. If U=(Integers<=20); D = (multiples of 4); E = (multiples of 3), the element of D n E are: A. (1.2) B. {3,6,9,15,18} C. (4,8,16,20) D. (3,6,9,12,15,18)",
        "4. The notation A - B is equivalent to A. AUB B. AUB C. ANB D. AO B",
        "5. The notation (AUB)/ is equivalent to A. An B B. AB C. AUB D. AN B",
        "6. The number of distinct elements found in a given set is called A. Power set of a set B. Order of a set C. Power of a cardinality D. Cardinality of a power set",
        "7. If two sets A and B are subsets of a universal set, then the notation n(A U B) is equal to A. n(A)+n(B) B. n(A)+n(C)-n(A U B) C. n(A)+n(B)+n(A U B) D. n(A)+n(B)-n(A n B)",
        "8. In a survey of 60 students, 60 study botany, 50 zoology and 48 biology. If 38 study all three, how many study only zoology? A. 12 B. 10 C. 0 D. 5",
        "9. How many study non of the three courses? A. 12 B. 10 C. 0 D. 5",
        "10. How many study the Zoology and Botany? A. 12 B. 10 C. 0 D. 5",
        "11. In a sports group, 15 play tennis, 11 swim, 9 do both, 3 do none. How many students swim only? A. 6 B. 2 C. 9 D. 20",
        "12. How many students play lawn tennis only? A. 6 B. 2 C. 9 D. 20",
        "13. How many students are in the group? A. 6 B. 2 C. 9 D. 20",
        "14. In a group of 40: 22 Math, 18 Phys, 14 Stats, 9 M&P, 7 M&S, 5 P&S, 2 all. How many study none? A. 4 B. 5 C. 6 D. 7",
        "15. Simplify 1/(2-sqrt(3)) + 5/(sqrt(3)+2) - 1/(sqrt(3)-sqrt(2)). A. 12-5sqrt(3)-sqrt(2) B. 12-5sqrt(3)+sqrt(2) C. 12+5sqrt(3)+sqrt(2) D. 12+5sqrt(3)-sqrt(2)",
        "16. Find the square root of 7 - sqrt(13). A. 0.8424 B. 1.8424 C. 1.8244 D. 0.8244",
        "17. Find the roots of the equation: x^3 + 5x^2 - 2x - 24. A. -4,3,2 B. -4,-3,-2 C. -4,-3,2 D. 4,3,-2",
        "18. Find the roots of the equation 2x^3 + 11x^2 - 17x - 6. A. -6, -1/2, 2 B. -6, 1/2, 2 C. 6, -1/2, -2 D. 6, 1/2, 2",
        "19. Solve the equation 2x^2 - 5x + 7 = 0. A. (5+-sqrt(31))/4 B. (5+-i*sqrt(31))/4 C. 5+-i*sqrt(31) D. (5+-sqrt(31))/2",
        "20. Determine the value of y^2 + 2y + 1 in the expression provided. A. 5+-sqrt(71) B. 5+-i*sqrt(-71) C. 5+-i*sqrt[2](71) D. (5+-i*sqrt(71))/2",
        "21. The value of k in sqrt(k-1) + 5*sqrt(k-9) = 4*sqrt(k-6)i is: A. 9 B. 10 C. 11 D. 12",
        "22. If 5g^4 + 9g^3 - 12g^2 - 9g + 5 = 0, find R where R = g - 1/g. A. 2 B. 1 C. 1/5 D. -2",
        "23. Values of x, y in x + 2y = 3 & x^2 + 2y^2 = 6. A. 1+sqrt(2), (2-sqrt(2))/2 B. 1+sqrt(2), (2+sqrt(2))/2 C. 1-sqrt(2), (2-sqrt(2))/2 D. 1-sqrt(2), (2+sqrt(2))/2",
        "24. Find a, b, c in 2ab=a+b, 5ac=6c-2a, 3bc=3b+4c. A. 3,1,-1 B. 2, 1/2, -1 C. 3/2, -1 D. 1, 1/2",
        "25. Solve for x in 16^(3x) = (1/32)^(x-1) * 4. A. 1 B. 2 C. -2 D. -1",
        "26. Simplify (216)^(-1/3) * (0.16)^(-1/2). A. 12/17 B. 5/13 C. 12/15 D. 5/12",
        "27. Given y=3x and 3^(x-y) = 1/81, find x. A. 2 B. 3 C. 4 D. 5",
        "28. If 8^(x/2) = 2^(3/8) * 4^(3/4), find 4x. A. 4 B. 5 C. 6 D. 7",
        "29. Solve for x in 3^(2x+1) - 18(3^x) - 81 = 0. A. -1 B. 3 C. -3 D. 2",
        "30. Solve for x in 26(5^(x-1)) = 5^(2x) + 1. A. -1,-2 B. -1,1 C. -1, 2 D. 2,-2",
        "31. Evaluate log_a(256) = 4. A. 2 B. 3 C. 4 D. 5",
        "32. Given log_2(64) = k, find 4k*log_16(32). A. 60 B. 50 C. 40 D. 30",
        "33. The value of x in log_3(x) - 3*log_x(3) = 2 is: A. -1/3 B. -27 C. 27 D. 3",
        "34. Positive value of y in 3*log_8(y) = log_4(y+4). A. -2,3 B. -2,-3 C. 2,-3 D. 2,3",
        "35. If 25^(x+1) = 64(5/2)^6, find x. A. -1 B. 1 C. -2 D. 2",
        "36. Simplify (8/27)^(1/3) - (4/9)^(1/2). A. 0 B. 1 C. 2 D. 3",
        "37. Simplify the complex fraction provided. A. 6 B. 12 C. 1/6 D. 1/12",
        "38. If |x| < p, then: A. p < x < -p B. -p < x < p C. -p > x < p D. -p < x > p",
        "39. Value of x in 5^11 / 2^(8+x) < 1... A. x < 8 B. x < -8 C. x > 8 D. x > -8",
        "40. Range of x for 12 + x - x^2 < 0. A. x<3 or x<-4 B. x<-3 or x<4 C. -3<x<4 D. 3<x<-4",
        "41. Equivalent of (a+b)(a^-1 + b^-1). A. 16sqrt(ab) B. 16 C. 8sqrt(ab) D. 8",
        "42. Equivalent of (a+b)(a^1/2 + b^1/2). A. 16sqrt(ab) B. 16 C. 8sqrt(ab) D. 8",
        "43. Value of P+G in the identity: (x-1)x^2(x+3)=... A. 3 B. 1 C. 7 D. 10",
        "44. First 3 terms of Tn = (n+1)/(3n+2). A. 3/8, 4/11, 5/14 B. 4/11, 5/14, 6/17 C. 2/5, 3/8, 4/11 D. 3/8, 4/11, 6/17",
        "45. Difference between 13th and 1st terms of log_16(n+3). A. 1/2 B. 2 C. 1 D. -1",
        "46. The sum of the terms of a sequence is: A. Series B. AP C. GP D. Sequence",
        "47. Sequence where terms differ by a constant: A. AP B. GP C. Infinity D. Series",
        "48. Expression for common difference in AP: A. T-Tn B. Tn-Tn+1 C. Tn-Tn-1 D. Tn-Tn+2",
        "49. Common difference in K, K+3, K+6... A. 2 B. 3 C. 4 D. -4",
        "50. If first 3 terms are y, 3y+1, 7y-4, find 10th term. A. 66 B. 55 C. 44 D. 33",
        "51. 6th and 13th terms of AP are 0 and 14, find 20th term. A. 18 B. -18 C. 28 D. -28",
        "52. P={factors of 84}, Q={factors of 315}. Find P U Q & P n Q. A. 3,4,5,7,9 & {3,7} B. {3,4,5,7} & {5,7} C. {2,3,5,7} & {3,7} D. {2,3,5,7} & {2,7}",
        "53. Class of 100: 40 Bot, 32 Micro, 44 Zoo... How many study none? A. 32 B. 42 C. 68 D. 24",
        "54. Union A U B is set of elements belonging to: A. either A nor B nor both B. either A or B or both C. neither A nor B or both D. neither A or B nor both",
        "55. The word 'Infinity' is: A. Real B. Complex C. Integer D. Constant",
        "56. 220 students offer Math/Chem. 125 Math, 110 Chem. How many Chem but not Math? A. 80 B. 110 C. 125 D. 95",
        "57. Elements in [(A-B) n (C-(A n C)')]: A. {3,q,r} B. {q,r} C. {3} D. {3,1}",
        "58. If R = {x : x^2=16, x>5}, then R is: A. 0 B. {0} C. Empty D. {0}",
        "59. 22 pupils take C, E, or G... How many take both Chemistry and Government? A. 1 B. 2 C. 3 D. 4",
        "60. If M subset N, find M n (M n N)'. A. M B. Ø C. N D. U",
        "61. Universal set {2..9}, P={even}, Q={odd x^2<50}. Find P n Q. A. {9} B. {0} C. Ø D. U",
        "62. Simplify cube root of (729y^-6)^1/2. A. 1/3y B. 3y C. 3 D. 3/y",
        "63. Evaluate cube root of (0.0024*35000)/0.0105. A. 2x10^1 B. 2x10^2 C. 1x10^2 D. 1x10^1",
        "64. Square root of 3 - sqrt(2) is: A. (1-sqrt(2))/2 B. (2-sqrt(2))/2 C. (1+2sqrt(2))/4 D. (1-2sqrt(2))/2",
        "65. Evaluate 4ab where a, b are positive numbers. A. 32 B. 32sqrt(ab) C. 16 D. 16sqrt(ab)",
        "66. In 5x^4 + 9x^3 - 12x^2 - 9x + 5 = 0, find x - 1/x. A. -1/5, 2 B. 1/2 C. 1/5, -2 D. 5,2",
        "67. Square of the remainder when 3x^4-2x^3-10x-5 is divided by x-4. A. 595 B. 475 C. 354025 D. 225625",
        "68. In resolving 1/(x(x-1)(x-2)) into partial fractions, find A, B, C. A. -2, 1/2, 1/2 B. -1, 1/2, 1/2 C. -1, 1/2, -1 1/2 D. 1/2, -1, 1/2",
        "69. Range of validity for x in 2x/(x^2-1) > 0. A. x<1 or x>0 B. x<0 or x<1 C. x<0 or x<1 D. x>0 or x>1",
        "70. Remainder when x^3 + 3x^2 - 13x - 10 is divided by (x-3). A. 4 B. 4 1/4 C. 6 D. 5",
        "71. Given -2 = A(x-1)^2 + B(x-1)(x-2) + C(x-2), find C. A. 2 B. -2 C. 1 D. -1",
        "72. Resolve (x^3 + x^2 - 5x - 15) / ((x^2-1)(x-2)) and find A, B, C. A. 2,3,4 B. 2,3,0 C. 2,0,3 D. 2, -2, 3",
        "73. Range of values for x where x^2 - 2/(x-2) > x-4. A. x > -4 or x > 2 B. x < -4 or x < 2 C. x < 4 or x > 2 D. x < -4 or x > 2",
        "74. In 5x^4 - x^3 + 9x^2 - x + 5 = 0, find x + 1/x. A. 1 B. 2 C. 3 D. 4",
        "75. Find p & q if (x-1) & (x+2) are factors of 2x^3 + px^2 - x + q. A. p=-5, q=-6 B. p=5, q=6 C. p=5, q=-6 D. p=-6, q=-5",
        "76. Find k if 4x^3 + kx^2 + 7x - 23 has remainder 7 when divided by 2x-5. A. 8 B. -16 C. -8 D. 16",
        "77. Express in partial fractions and find A+B-C. A. -3 B. 2 C. 6 D. 7",
        "78. Solve inequality y/(y-4) > 4/y + 1. A. -4 < y < 0 B. 4 < y < 0 C. 0 > y > -4 D. 0 < y < 4",
        "79. Sum of squares of 3 AP numbers is 165, sum is 21. Find sum of cubes. A. 4 B. 1400 C. 1407 D. 104",
        "80. Sum of first n terms equals half the sum of subsequent n. Find ratio. A. 6 B. 4 C. 8 D. 3",
        "81. Series ln(x), ln(x^2), ln(x^4)... Find 21st term. A. 20ln(x) B. 2^20ln(x) C. 202ln(x) D. 20ln(x^2)",
        "82. Find 8th term and sum of first 8 of GP: 1/2, -1, 2, -4... A. -64, -42.5 B. -64, 42.5 C. 64, 42.5 D. -64, 45.4",
        "83. Sum of first 8 terms of AP: ln(x), ln(x^2), ln(x^3)... A. ln(x^8) B. ln(x^9) C. ln(x^36) D. ln(x^72)",
        "84. Savings problem: each deposit 2x more than previous. Sum of 11 is N20,480. A. N20 B. N25 C. N10 D. N12.50",
        "85. Ratio of 4th to 7th term is 5:8. Find ratio of 3rd to 6th term. A. 4:5 B. 6:5 C. 4:6 D. 4:7",
        "86. AP: 2nd term = 4*1st, last = 13*1st, sum = 70. Find first three terms. A. 2,4,6 B. 2,8,14 C. 2,4,8 D. 8,12,14",
        "87. Polygon 25 sides in AP, perimeter 1100cm, largest side 10x smallest. A. 5cm B. 6cm C. 7cm D. 8cm"
    ]

    for q_text in questions_raw:
        # 1. apply math symbol replacements
        clean_text = replace_math_symbols(q_text)
        
        # 2. Split question from options using regex (Split at A. B. C. or D.)
        parts = re.split(r'\s([A-D]\.)', clean_text)
        
        if len(parts) > 1:
            formatted_q = parts[0]
            for i in range(1, len(parts), 2):
                option_letter = parts[i]
                option_content = parts[i+1]
                # Stacking options with indentation
                formatted_q += f"<br/>&nbsp;&nbsp;&nbsp;&nbsp;{option_letter}{option_content}"
            story.append(Paragraph(formatted_q, q_style))
        else:
            story.append(Paragraph(clean_text, q_style))

    story.append(PageBreak())

    # --- Answers ---
    story.append(Paragraph("Answer Key", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    answers_list = [
        "1. B", "2. A", "3. B", "4. D", "5. A", "6. B", "7. D", "8. C", "9. C", "10. A",
        "11. B", "12. A", "13. D", "14. B", "15. D", "16. B", "17. C", "18. A", "19. B", "20. C",
        "21. B", "22. C", "23. A", "24. B", "25. D", "26. D", "27. A", "28. B", "29. D", "30. B",
        "31. C", "32. D", "33. C", "34. A", "35. D", "36. A", "37. D", "38. B", "39. A", "40. C",
        "41. D", "42. C", "43. B", "44. C", "45. A", "46. A", "47. A", "48. C", "49. B", "50. A",
        "51. C", "52. C", "53. A", "54. B", "55. C", "56. D", "57. C", "58. C", "59. A", "60. B",
        "61. C", "62. D", "63. A", "64. D", "65. B", "66. C", "67. C", "68. B", "69. D", "70. D",
        "71. A", "72. D", "73. A", "74. D", "75. C", "76. C", "77. C", "78. A", "79. C", "80. A",
        "81. B", "82. A", "83. C", "84. C", "85. D", "86. B", "87. D"
    ]

    for i in range(0, len(answers_list), 5):
        row = " | ".join(answers_list[i:i+5])
        story.append(Paragraph(row, styles['Normal']))

    doc.build(story)
    print(f"Created: {filename}")

if __name__ == "__main__":
    create_mth101_pdf()
