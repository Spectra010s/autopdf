from decimal import Decimal
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

OUT = Path("NAMTES_Platform_Hosting_Maintenance_Proposal.pdf")
RATE = Decimal("1324.60")
MAINT_NGN = Decimal("30000")
MAINT_USD = (MAINT_NGN / RATE).quantize(Decimal("0.01"))
A_HOST_NGN, B_HOST_NGN = Decimal("397380"), Decimal("79476")
DOMAIN_NGN, EMAIL_NGN = Decimal("20000"), Decimal("1500")
A_NGN = A_HOST_NGN + DOMAIN_NGN + MAINT_NGN
B_NGN = B_HOST_NGN + DOMAIN_NGN + MAINT_NGN
A_USD = Decimal("300") + Decimal("15.10") + MAINT_USD
B_USD = Decimal("60") + Decimal("15.10") + MAINT_USD

pdfmetrics.registerFont(TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

NAVY, BLUE = colors.HexColor("#17324D"), colors.HexColor("#2D6386")
GREY, PALE = colors.HexColor("#64748B"), colors.HexColor("#F2F5F8")
BORDER = colors.HexColor("#D6DEE6")
s = getSampleStyleSheet()
s.add(ParagraphStyle(name="Cover", parent=s["Title"], fontName="DejaVuSans-Bold", fontSize=25, leading=30, textColor=NAVY, alignment=TA_CENTER, spaceAfter=12))
s.add(ParagraphStyle(name="Kicker", parent=s["Normal"], fontName="DejaVuSans-Bold", fontSize=10, textColor=BLUE, alignment=TA_CENTER, spaceAfter=12))
s.add(ParagraphStyle(name="Sub", parent=s["Heading2"], fontName="DejaVuSans-Bold", fontSize=10.5, leading=14, textColor=BLUE, spaceBefore=7, spaceAfter=4, keepWithNext=True))
s.add(ParagraphStyle(name="Sect", parent=s["Heading1"], fontName="DejaVuSans-Bold", fontSize=15, leading=19, textColor=NAVY, spaceBefore=8, spaceAfter=7, keepWithNext=True))
s.add(ParagraphStyle(name="Body2", parent=s["BodyText"], fontName="DejaVuSans", fontSize=8.5, leading=11.5, textColor=colors.HexColor("#1F2937"), spaceAfter=5))
s.add(ParagraphStyle(name="Small2", parent=s["BodyText"], fontName="DejaVuSans", fontSize=7.1, leading=9, textColor=colors.HexColor("#1F2937"), spaceAfter=2))
s.add(ParagraphStyle(name="TH", parent=s["BodyText"], fontName="DejaVuSans-Bold", fontSize=7.2, leading=8.5, textColor=colors.white))

def p(text, style="Body2"):
    return Paragraph(text, s[style])

def fmt(usd, ngn):
    return "$" + format(usd, ",.2f") + " / ₦" + format(ngn, ",.0f")

def table(headers, rows, widths):
    data = [[p(x, "TH") for x in headers]]
    data += [[p(str(x), "Small2") for x in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),NAVY), ("GRID",(0,0),(-1,-1),0.35,BORDER),
        ("VALIGN",(0,0),(-1,-1),"TOP"), ("LEFTPADDING",(0,0),(-1,-1),5),
        ("RIGHTPADDING",(0,0),(-1,-1),5), ("TOPPADDING",(0,0),(-1,-1),5),
        ("BOTTOMPADDING",(0,0),(-1,-1),5),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,PALE])
    ]))
    return t

def page(canvas, doc):
    canvas.saveState()
    w,h=A4
    if doc.page > 1:
        canvas.setStrokeColor(BORDER); canvas.line(18*mm,h-15*mm,w-18*mm,h-15*mm)
        canvas.setFont("DejaVuSans-Bold",7); canvas.setFillColor(NAVY)
        canvas.drawString(18*mm,h-11.5*mm,"NAMTES FUOYE CHAPTER")
        canvas.setFont("DejaVuSans",7); canvas.setFillColor(GREY)
        canvas.drawRightString(w-18*mm,h-11.5*mm,"Hosting, Maintenance & Communications")
    canvas.setStrokeColor(BORDER); canvas.line(18*mm,14*mm,w-18*mm,14*mm)
    canvas.setFont("DejaVuSans",7); canvas.setFillColor(GREY)
    canvas.drawString(18*mm,9*mm,"Proposal dated 23 October 2026")
    canvas.drawRightString(w-18*mm,9*mm,"Page " + str(doc.page))
    canvas.restoreState()

def build():
    doc=SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=21*mm,bottomMargin=20*mm,title="NAMTES Platform Hosting, Maintenance & Communications Proposal",author="Adeloye Adetayo")
    story=[]
    story += [Spacer(1,20*mm),p("NAMTES • FUOYE CHAPTER","Kicker"),p("Platform Hosting,<br/>Maintenance &amp; Communications","Cover"),p("Proposal for the incoming executive tenure","Body2"),Spacer(1,8*mm),
      p("<b>Prepared for</b><br/>National Association of Mechatronics Engineering Students (NAMTES), Federal University Oye-Ekiti Chapter"),
      p("<b>Prepared by</b><br/>Adeloye Adetayo<br/>Platform Developer &amp; Maintainer"),
      p("<b>Date</b><br/>23 October 2026"),
      p("<b>Purpose</b><br/>Keep the existing NAMTES website and voting platform available, maintained and ready for the incoming executive tenure."),
      p("<b>Decision to make</b><br/>Choose whether to retain Vercel + Supabase or move the applications and database to Railway. The proposal also sets out maintenance, executive email options and file storage."),
      p("This proposal covers ongoing hosting, service costs and routine maintenance. It does not charge NAMTES again for original development or past work."),
      p("<b>Budget approach:</b> recurring subscriptions, annual maintenance and usage-based email sending are shown separately so the association can see what is fixed and what may vary."),PageBreak()]
    story += [p("1. Overview of the service","Sect"),p("NAMTES already has a live website and voting platform. The proposed service keeps both available for students and executives during the incoming tenure, while providing routine technical upkeep and clear ownership of the accounts used to run them."),p("What NAMTES receives","Sub"),
      table(["Service area","What it means for NAMTES"],[
      ["Website and voting platform","The existing website and voting platform remain hosted and available through the association's domain."],
      ["Database and platform records","Application records and voting-related data continue to be hosted and maintained, with routine health and backup checks."],
      ["Routine maintenance and support","Reasonable help with deployment problems, service configuration, monitoring and appropriate dependency/security updates."],
      ["File storage","Store and serve website images and downloadable files, including executive pictures, blog images and documents."],
      ["Executive email forwarding","Planned association-branded addresses forward incoming messages to designated executives; no paid mailbox subscriptions are budgeted."],
      ["Platform-generated emails","Delivery for account verification, voting-related notices and selected announcements, priced by actual sending volume."],
      ["Executive handover","Service ownership, access and basic operating notes kept organised for incoming executives."]],[43*mm,128*mm]),
      Spacer(1,5),p("<b>Outside the recurring fee.</b> New features, major redesigns, new modules, a new election workflow, major migrations beyond an approved hosting move, paid integrations, extra mailboxes and exceptional incident recovery are excluded and would be discussed and priced separately."),
      p("2. Hosting options","Sect"),p("Both options are intended to keep the existing website and voting platform running. The main difference is where the applications and database are hosted and how the recurring bill is structured."),
      p("Option A — Keep Vercel + Supabase","Sub"),p("<b>What it provides:</b> Vercel hosts the web application, while Supabase provides PostgreSQL and related backend services. This avoids moving the existing services."),
      p("<b>Budget:</b> Supabase Pro is $25/month (about ₦33,115/month), or $300/year (about ₦397,380/year). Vercel is budgeted at ₦0 only if the project qualifies for its free Hobby plan. Add the cost of a paid Vercel plan if required."),
      p("<b>Why choose it:</b> It keeps the current hosting arrangement in place and avoids the work and disruption of moving to a new host."),
      p("Option B — Move the applications and database to Railway","Sub"),p("<b>What it provides:</b> Railway would host the website, voting application and PostgreSQL database under one platform subscription."),
      p("<b>Budget:</b> Railway Hobby costs $5/month (about ₦6,623/month), or $60/year (about ₦79,476/year). It includes $5 of monthly resource usage; the bill can rise if usage exceeds that credit."),
      p("<b>Why consider it:</b> The starting subscription cost is lower and application hosting and the database are brought together under one provider."),
      p("<b>Important cost distinction.</b> Railway's $5/month is a minimum subscription, not a guaranteed maximum bill. Vercel's free option is conditional on eligibility.", "Body2"),PageBreak()]
    story += [p("3. Hosting cost comparison","Sect"),p("Estimates use US$1 = ₦1,324.60, dated 23 October 2026. Actual charges may differ due to exchange rates, conversion fees or taxes."),
      table(["Budget line","Option A: Vercel + Supabase","Option B: Railway"],[
      ["Main hosting arrangement","Vercel application; Supabase PostgreSQL and backend services.","Railway application and PostgreSQL database."],
      ["Main subscription","$25/month • ₦33,115/month<br/>$300/year • ₦397,380/year","$5/month minimum • ₦6,623/month<br/>$60/year • ₦79,476/year"],
      ["Additional cost","Vercel is ₦0 only if eligible for free Hobby. Vercel Pro is $20/month (about ₦26,492/month) if required.","Usage above the included $5/month credit can increase the bill."],
      ["Main benefit","Keep current arrangement; no hosting move needed.","Lower starting subscription; app and database on one platform."],
      ["Main consideration","Supabase remains separate; Vercel eligibility must be confirmed.","Actual cost depends on compute, memory, storage and other usage."]],[38*mm,66.5*mm,66.5*mm]),
      Spacer(1,4),p("The annual budget excludes a paid Vercel subscription, Railway usage above its included credit, taxes and payment-conversion fees. Add these if they apply.","Small2"),
      p("4. File storage","Sect"),p("The NAMTES platform needs a place to store and serve images and downloadable files: executive profile pictures, blog post images, other platform images and documents users may view or download."),
      p("Cloudflare R2 is proposed to hold these files so they can be displayed on the website or made available for download whenever needed."),
      p("<b>Cost: $0 / ₦0 within the free usage allowance.</b> Cloudflare R2 includes 10 GB-month standard storage, up to 1 million Class A requests and up to 10 million Class B requests per month in its free tier. These allowances may be sufficient for NAMTES. Charges may apply if usage exceeds the free allowance or uses a non-free storage class."),
      p("5. Email and communications","Sect"),p("The proposal separates executive inboxes from emails sent automatically by the platform or to groups of students."),
      p("A. Executive email forwarding (planned)","Sub"),p("The planned approach is to use association-branded role addresses and forward incoming messages to the designated executives’ existing email destinations. No paid executive mailbox subscription is included in this budget."),
      p("Forwarding is intended for receiving messages. It is not a separate full mailbox and does not by itself provide a standalone inbox, mailbox history or full send-as-mailbox capability. The forwarding provider and DNS configuration will be confirmed during implementation; the budget assumes no additional forwarding subscription fee."),PageBreak()]
    story += [p("5. Email and communications (continued)","Sect"),p("B. Emails sent by the platform","Sub"),p("The platform may send account-verification messages, voting-related notices and selected announcements. A pay-as-you-go service charges by email volume; each recipient counts as one send."),
      p("For planning, the proposal uses an illustrative rate of about $0.23 per 1,000 sends (approximately ₦300). This is a budget assumption, not a confirmed current tariff."),
      table(["Example activity","Emails sent","Illustrative cost"],[
      ["One announcement to 100 recipients","100","$0.02 / ₦30"],["One announcement to 300 recipients","300","$0.07 / ₦90"],
      ["One announcement to 500 recipients","500","$0.11 / ₦150"],["10 announcements to 500 recipients each","5,000","$1.13 / ₦1,500"]],[100*mm,30*mm,41*mm]),
      Spacer(1,4),p("These examples are not a forecast of annual volume. Actual costs depend on message volume and provider. Routine updates can also be posted on the platform, reserving email for important notices, verification and selected announcements."),
      p("6. Annual budget estimate","Sect"),p("The fixed subtotal includes hosting, planned email forwarding (no paid mailbox subscriptions), domain-renewal allowance and annual maintenance. Platform-generated email is separate because its cost depends on usage."),
      table(["Annual budget item","Option A: keep current","Option B: Railway"],[
      ["Hosting/database baseline","$300 / ₦397,380","$60 / ₦79,476"],
      ["Executive email forwarding (planned)","$0 / ₦0*","$0 / ₦0*"],
      ["Domain renewal allowance","$15.10 / ₦20,000","$15.10 / ₦20,000"],
      ["Annual maintenance & administration",fmt(MAINT_USD,MAINT_NGN),fmt(MAINT_USD,MAINT_NGN)],
      ["Estimated fixed annual subtotal",fmt(A_USD,A_NGN),fmt(B_USD,B_NGN)],
      ["Illustrative email scenario: 5,000 sends","$1.13 / ₦1,500","$1.13 / ₦1,500"],
      ["Illustrative subtotal incl. email scenario",fmt(A_USD+Decimal("1.13"),A_NGN+EMAIL_NGN),fmt(B_USD+Decimal("1.13"),B_NGN+EMAIL_NGN)]],[65*mm,53*mm,53*mm]),
      Spacer(1,4),p("*Forwarding budget assumes no additional provider fee and is subject to confirming provider/DNS setup. Costs not included: paid Vercel plan if required; Railway usage above included credit; taxes or conversion fees; paid add-ons; R2 usage above free allowances; and new features or major changes.","Small2"),PageBreak()]
    story += [p("7. Annual maintenance and administration","Sect"),p("<b>Proposed fee: " + fmt(MAINT_USD,MAINT_NGN) + " per year.</b>"),
      p("This fee covers routine upkeep of the existing website and voting platform during the executive tenure: deployment assistance, basic service monitoring, backup checks, configuration maintenance, appropriate routine dependency/security updates and reasonable support for day-to-day platform issues."),
      p("It excludes new feature development, major redesigns, new modules, a new election workflow, additional paid services or exceptional incident recovery outside routine support. These would be scoped and priced separately."),
      p("8. Ownership and approval","Sect"),p("The domain and service accounts should remain under association-controlled ownership wherever practical, with access available to appropriate executives. This helps NAMTES retain control when executive roles change."),
      p("No hosting migration, new paid subscription or provider commitment is treated as already approved. If NAMTES selects Railway, the move would include transfer of the existing application and database, service checks, domain transition planning and a backup/restore check before the old setup is retired."),
      p("Additional spending for new features, redesigns, mailboxes beyond five, unusually high email volume or paid third-party services should be approved by NAMTES before the cost is incurred."),
      p("9. Decision requested","Sect"),p("NAMTES is asked to:<br/>1. Approve the proposed annual maintenance and administration fee of ₦30,000.<br/>2. Select Option A—retain Vercel + Supabase, or Option B—move the applications and PostgreSQL database to Railway.<br/>3. Confirm the role addresses and destination email addresses for forwarding during implementation.<br/>4. Approve the estimated annual budget, noting that provider prices and usage-dependent costs will be confirmed before purchase."),
      Spacer(1,6),table(["For NAMTES FUOYE Chapter","Prepared by"],[["Name: __________________________<br/>Role: ___________________________<br/>Date: ___________________________","Adeloye Adetayo<br/>Platform Developer &amp; Maintainer<br/>Date: 23 October 2026"]],[85.5*mm,85.5*mm]),
      p("Pricing and exchange-rate references","Sub"),p("Exchange-rate reference: US$1 = ₦1,324.60, dated 23 October 2026. Source: Centre for Energy exchange-rate reference, using ExchangeRate-API mid-market data. This is a reference rate, not a promise of the rate applied by a bank or payment provider.","Small2"),
      p("Supabase: https://supabase.com/pricing<br/>Railway: https://railway.com/pricing and https://docs.railway.com/pricing/plans<br/>Vercel: https://vercel.com/pricing and https://vercel.com/legal/terms<br/>Cloudflare R2: https://developers.cloudflare.com/r2/pricing/<br/>Cloudflare Email Routing: https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/","Small2"),
      p("Provider pricing and free-tier terms can change. Figures are estimates based on published information reviewed on 23 October 2026; final plans and eligibility should be confirmed before purchase.","Small2")]
    doc.build(story,onFirstPage=page,onLaterPages=page)
    print("Generated:", OUT.resolve())
    print("Maintenance:",fmt(MAINT_USD,MAINT_NGN))
    print("Option A fixed subtotal:",fmt(A_USD,A_NGN))
    print("Option B fixed subtotal:",fmt(B_USD,B_NGN))
    print("Option A including email scenario:",fmt(A_USD+Decimal("1.13"),A_NGN+EMAIL_NGN))
    print("Option B including email scenario:",fmt(B_USD+Decimal("1.13"),B_NGN+EMAIL_NGN))

if __name__ == "__main__":
    build()
