from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, LongTable, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_gst_pdf():
    doc = SimpleDocTemplate("GST103-by-Spectra010s.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=20)
    q_style = ParagraphStyle('QuestionStyle', parent=styles['Normal'], fontName='Helvetica-Bold', spaceBefore=12)
    opt_style = ParagraphStyle('OptionStyle', parent=styles['Normal'], leftIndent=25, spaceBefore=2)

    # [span_0](start_span)Full Question Data[span_0](end_span)
    data = [
        ["A library can be defined as_____________", "An educational resource centre", "A 'nest' where scholars are hatched", "A storehouse of knowledge", "All of the above", "All of the above"],
        ["The Use of Library and Introduction to ICT (GST 103) is_____________", "A compulsory course", "A required course", "An elective course", "All of the above", "A compulsory course"],
        ["A library that is attached to a tertiary institution is:", "A School library", "A National library", "An Academic library", "A Research library", "An Academic library"],
        ["One known component of a typical library is _____________", "Circulation", "Reference", "Cataloguing", "Clientele", "Clientele"],
        ["Newspapers, journals and magazines are examples of _____________", "Books", "Pamphlet", "Serials", "None of the above", "Serials"],
        ["A printed reading material of less than 49 pages is _____________", "Serials", "Book", "Jotter", "Pamphlet", "Pamphlet"],
        ["When a printed reading material is more than 49 pages, it is _____________", "Pamphlet", "Book", "Serials", "Jotter", "Book"],
        ["Punch, Guardian and Tribune are examples of _____________", "Books", "Serials", "Pamphlet", "Documents", "Serials"],
        ["Films, Slides and Television are examples of ____________", "Instruments", "Equipment", "Audio-Visual materials", "Objects", "Audio-Visual materials"],
        ["_____________________ is the apex library of a country", "Academic library", "Special library", "Research library", "National library", "National library"],
        ["_____________ library is personally owned by an individual or an organization.", "Special", "Private", "Self", "Academic", "Private"],
        ["The library aids _____________", "Learning", "Research", "Teaching", "All of the above", "All of the above"],
        ["The Library serial collection include the following except___________", "Journals", "Newspapers", "Magazines", "Encyclopedia", "Encyclopedia"],
        ["_______________ is a selection tool used for selecting serials in the library", "Memoir", "Publisher’s catalogue", "Year book", "Accession register", "Publisher’s catalogue"],
        ["Reference books can be ______________", "Directional or Non directional", "Active or Passive", "Direct or Indirect", "Open access or Closed access", "Direct or Indirect"],
        ["Reference section contains the following except_____________.", "Dictionary", "Yearbook", "Gazettes", "Atlas", "Gazettes"],
        ["Reference books in the library usually bears the symbol before their call mark", "RB", "RBK", "RE", "REF", "REF"],
        ["____________ is the exclusive right accorded by law to the creator...", "Publishing law", "Copyright", "Cataloguing rule", "Piracy", "Copyright"],
        ["Works that are eligible for copyright protection are the following except", "Literary work", "Statistical work", "Musical work", "Artistic work", "Statistical work"],
        ["_____________ are periodic government publications...", "Handbook", "Manual", "Directory", "Gazettes", "Gazettes"],
        ["_____________is when fake copies of an author’s work are reproduced...", "Piracy", "Plagiarism", "Referencing", "Counterfeit", "Piracy"],
        ["_____________is an act of violating copyright law when people illegally reproduce...", "Piracy", "Plagiarism", "Referencing", "Counterfeit", "Piracy"],
        ["A book to which you can refer for authoritative facts and quick info is", "Electronic books", "Textbook", "Reference book", "Classification scheme", "Reference book"],
        ["An act of violating the copyright law when people take other people’s idea...", "Piracy", "Plagiarism", "Referencing", "Counterfeits", "Plagiarism"],
        ["The library management software adopted by FUOYE Library is _____________", "TEEAL", "AGORA", "HINARI", "KOHA", "KOHA"],
        ["The University website is _____________ ", "ww.fuoye.edu.ng", "www.fouye.edu.ng", "www.fuoye.edu.ng", "www.fuye.edu.ng", "www.fuoye.edu.ng"],
        ["_____________ and _____________ are computer operating systems", "Linux & Koha", "TEEAL & Windows", "Ubuntu & AGORA", "Linux & Windows", "Linux & Windows"],
        ["FUOYE Wifi hotpot name is _____________", "hotspot.edu.ng", "fuoye.net .hotspot", "fuoye.net", "fuoye.edu.ng", "fuoye.net"],
        ["All these are Microsoft Office desktop applications except _____________", "Word", "Excel", "Windows", "Powerpoint", "Windows"],
        ["All these are the databases available in FUOYE Library except _____________", "Science Direct", "TEEAL", "KOHA", "HINARI", "KOHA"],
        ["All these are approaches by which information could be accessed on OPAC except", "Author", "Editor", "Subject", "Title", "Editor"],
        ["_____________ is the department in the library that handles automation...", "Information Technology", "Technology", "ICT Department", "Automation Department", "Information and Communication Technology Department"],
        ["_____________ is an electronic device which is capable of receiving data...", "Zinox", "Computer", "ICT", "DELL", "Computer"],
        ["_____________ is the IP address to access OPAC on KOHA in FUOYE", "www.koha.fuoye.edu.ng", "www.fuoye.koha.edu.ng", "www.fuoye.opac.edu.ng", "www.opac.fuoye.edu.ng", "www.opac.fuoye.edu.ng"],
        ["_____________ are materials accessed only with ICT application", "Information materials", "Electronic materials", "Technological Materials", "ICT materials", "Electronic materials"],
        ["One of the following is not an anti-virus", "Smadav", "Avast", "E-set", "V-prune", "V-prune"],
        ["Cataloguing is describing a book whereby all the _____________ details are highlighted", "Author", "Pagination", "Bibliographic", "Publication", "Bibliographic"],
        ["Library catalogue is the _____________ to the content of the holding", "Key pointer", "Identification", "Call mark", "Copies", "Key pointer"],
        ["To locate a book on the shelf, what do you need from KOHA?", "Authors name", "Call mark", "Title of the book", "Pagination", "Call mark"],
        ["The classification scheme used in FUOYE library is ________________", "Library of Congress", "Dewey Decimal", "MOIS Scheme", "Universal Decimal", "Library of Congress Classification Scheme"],
        ["____________ is a unique number assigned as soon as it arrives the library", "Classification number", "Pagination Number", "Accession Number", "Call mark", "Accession Number"],
        ["_____________ and _____________ are the two types of catalogue you know", "Cataloguing & Classification", "Call mark & Classification", "Card & OPAC", "Card & Classification", "Card catalogue and Online Public Access Catalogue"],
        ["The section in which books are processed in the library is called _____________", "Circulation", "Cataloguing", "Reference", "ICT", "Cataloguing section"],
        ["The section that is responsible for the training of staff is _____________", "Acquisition", "Cataloguing", "Technical", "Administrative", "Administrative section"],
        ["_____________ and _____________ are services rendered in circulation", "Stamping & Budget", "Training & Systems", "Printing & Internet", "Charging/Discharging", "Charging and discharging of books"],
        ["_____________ is the section where Encyclopedea, Atlases and Handbooks are kept", "Cataloguing", "Reference", "Acquisition", "Administrative", "Reference section"],
        ["The approaches to library catalogue include _____________", "Author, Title & Subject", "Call mark & Accession", "Title & Subject", "Title & Call mark", "Author’s name, Title & Subject"],
        ["One of the functions of library catalogue is _____________", "Registered users help", "Issue tickets", "Provides bibliographic details", "Charging penalties", "It provides full bibliographic details"],
        ["_____________ describing a book in such a way that important details are highlighted", "Classification", "Cataloguing", "Indexing", "Abstracting", "Cataloguing"],
        ["_____________ arranging library materials into subjects for easy accessibility", "Classification", "Cataloguing", "Indexing", "Abstracting", "Classification"],
        ["Imprint in bibliographic details of a book contains:", "Title & Edition", "Pagination & Illustrations", "Pagination & Height", "Place, Publisher & Year", "Place of publication, Publisher and Year of Publication"],
        ["Collation in bibliographic details of a book contains:", "Title & Edition", "Pagination & Illustrations", "Pagination & Height", "Place, Publisher & Year", "Pagination, Height of book and Illustration"],
        ["Information materials in the library are well _____________for easy _____________ ", "Retrieved, access", "Accessed, retrieval", "Organised, retrieval and access", "None of the above", "Organised, retrieval and access"],
        ["_____________ guide library users so they can maximally utilise resources", "Library skills", "Study skills", "User skills", "Reading skills", "Library skills"],
        ["_____________ skills guide in the studying and understanding info in a book", "Library skills", "Study skills", "User skills", "Reading skills", "Study skills"],
        ["The letter “S” in study skills stands for _____________", "Study", "Service", "Survey", "Skill", "Survey"],
        ["The letter “R” in study skills stands for _____________ except ", "None of the above", "Recite", "Review", "Recall", "None of the above"],
        ["Which students are allowed to use the library?", "Postgraduate", "Registered", "Undergraduates", "Pre-degree", "Registered"],
        ["Overdue books are charged at N50 per day is one of the _____________", "Library rules", "Library regulations", "Library routines", "Library sanctions", "Library regulations"],
        ["Access to library electronic resources in FUOYE refers to:", "books & journals", "usernames/passwords", "library/information", "encyclopedia", "user names and passwords , library"],
        ["Call mark can also be referred to as", "Cutter number", "Accession number", "Location mark", "Class number", "Class number"],
        ["Cutter number is a/an ________________ added to classification", "Alphanumeric symbol", "Classification scheme", "Author symbol", "Call mark", "Alphanumeric symbol"],
        ["In the library of congress classification scheme D is for", "General works", "Music", "History", "Law", "History"],
        ["M is for", "Medicine", "Science", "Technology", "Music", "Music"],
        ["S is for", "Law", "Education", "Medicine", "Agriculture", "Agriculture"],
        ["Q is for", "Science", "Political science", "Technology", "Law", "Science"],
        ["AG is for", "Dictionaries", "Geography", "History", "Religion", "Dictionaries"],
        ["AN is for", "Agriculture", "Medicine", "Science", "Newspapers", "Newspapers"],
        ["BD is for", "Logic", "Ethics", "Bible", "Metaphysics", "Metaphysics"],
        ["BR is for", "Islam", "Christianity", "Quran", "Aesthetics", "Christianity"],
        ["HB is for", "Economic Theory", "Banking/Finance", "Public Finance", "Economic Condition", "Economic Theory"],
        ["HC is for", "Statistics", "Economic Condition", "Public Finance", "Economic Theory", "Economic condition"],
        ["HJ is for", "Public Finance", "Banking/Finance", "Statistics", "Socialism", "Public finance"],
        ["LA is for", "Astronomy", "English Lit", "History of Education", "Theory/Practice", "History of Education"],
        ["LC is for", "Special Aspects", "Socialism", "Economic Theory", "Bible", "Special Aspects in Education"],
        ["PA is for", "Chemistry", "Geology", "English Lit", "Greek and Latin", "Greek and Latin"],
        ["PS is for", "American Lit", "African Lit", "Greek and Latin", "Public Finance", "American Literature"],
        ["QL is for", "Physics", "Biology", "Zoology", "Botany", "Zoology"],
        ["QK is for", "Physics", "Biology", "Zoology", "Botany", "Botany"],
        ["Full meaning of OPAC is ______________", "Open Public Access", "Online Printed Access", "Online Public Access Catalogue", "Open Personal Access", "Online Public Access Catalogue"],
        ["____________ is not an element of library catalogue?", "Database", "ISBN", "Author", "Title", "Database"],
        ["Series of instructions designed for a computer to carry out specific functions", "Digital Library", "Software", "Database", "Programming", "Software"],
        ["Online database of materials held by a library or group of libraries", "Computer", "Cataloguing", "OPAC", "Software", "OPAC"],
        ["The two main types of computer software are ______________ and ______________", "System & Analogue", "Digital & Application", "Digital & Analogue", "System & Application", "System and application software"],
        ["A list of all information materials held by a library", "Shelf", "Library Catalogue", "Library Card", "Library Resources", "Library Catalogue"],
        ["____________ is an example of system software?", "MS Office", "Photoshop", "Library software", "Operating system", "Operating system"],
        ["Android is an example of ______________", "Library Software", "Facebook", "Phone App", "Operating system", "Operating system"],
        ["Software developed to handle basic housekeeping functions of a library", "Library software", "System software", "Adobe", "PDF", "Library software"],
        ["Two types of library software are ______________ and _______________", "System/App", "App/Open Source", "Digital/Coded", "Proprietary/Open Source", "Proprietary and Open source software"],
        ["Library software that requires payment of subscription fee", "System", "Proprietary software", "Digital", "Coded", "Proprietary software"],
        ["Software managing variety of independent hardware components?", "MS Word", "Digital", "System software", "Application", "System software"],
        ["_____________ is not an example of Open source library software?", "Koha", "SLAM", "Windows", "Virtua", "Windows"],
        ["____________ is not an example of Application software?", "Corel Draw", "MS Office", "Library software", "None of the above", "None of the above"],
        ["Library software that does not require subscription fee", "Proprietary", "System", "Open Source software", "Digital", "Open Source software"],
        ["____________ is not an example of operating system?", "Windows", "Desktop computer", "Mac OS", "Linux", "Desktop computer"],
        ["___________ is not an example of proprietary software", "Symphony", "Millennium", "Aleph", "SLIM", "SLIM"],
        ["Koha is an example of ___________", "Database", "Library material", "Proprietary", "Open source", "Open source software"],
        ["Collection of data organized for rapid search and retrieval", "Software", "Catalogue", "Database", "Index", "Database"],
        ["______________ is not an example of Internet browser", "Chrome", "Photoshop", "Opera", "Explorer", "Photoshop"],
        ["Linus is an example of ___________", "Operating system", "Software", "Database", "Catalogue", "Operating system"],
        ["___________ is an example of library database", "Koha", "Virtua", "SLAM", "AGORA", "AGORA"],
        ["TEEAL is an example of ____________", "Library Database", "Library catalogue", "Library software", "Computer", "Library Database"],
        ["DOAJ stands for ___________", "Directory Online", "Directory Open Access Journals", "Directory Offline", "Directory Open App", "Directory Open Access Journals"],
        ["______________ is not an example of library database", "Ebscohost", "Science Direct", "Pubmed", "Greenstone", "Greenstone"],
        ["Default password for your portal?", "Matric No", "Surname", "Fuoye123", "FUOYE", "Fuoye123"],
        ["Computer sizes except", "Micro", "Midrange", "Mainframes", "Tower Computer", "Tower Computer"],
        ["One of the examples of Micro Computer is", "Laptop computer", "Ubuntu", "Fedora", "Macintoch", "Laptop computer"],
        ["Types of Wireless Communication network except?", "Cellular", "Local Area Network", "Wireless LAN", "Bluetooth", "Local Area Network"],
        ["Full meaning of SSID is", "Service set Identifier", "Set service", "Service Set Identity", "Set Identity", "Service set Identifier"],
        ["An example of an Academic Library is?", "Fuoye Library", "Ekiti State", "Central Bank", "IITA", "Fuoye Library"],
        ["An example of a Public Library is ", "Fuoye", "Ekiti State Library", "Central Bank", "Wole Soyinka", "Ekiti State Library"],
        ["An example of a National Library is?", "Fuoye", "Ekiti State", "Central Bank", "National Library of Nigeria", "National Library of Nigeria"],
        ["Various means of book acquisition in the Library except", "Purchase", "Beaqueath", "Exchange", "Antiquity", "Antiquity"],
        ["Classification can simply be defined as", "Grouping Materials", "Location", "Assesioning", "Stamping", "Means of grouping Materials"],
        ["06825 on a Library Material means", "Class Mark", "Catalogue No", "Accession No", "Library No", "Accession No"],
        ["Classification Scheme using both Alphabet and Number", "Library of Congress", "Moy's", "Dewey Decimal", "", "Library of Congress Classification Scheme"],
        ["Classification Scheme using only Number", "UDC", "Colon", "LC", "Dewey Decimal", "Dewey Decimal Classification Scheme"],
        ["What gives the full Bibliographic details of a book", "Cataloguing", "Assessioning", "Stamping", "Classifying", "Cataloguing"],
        ["Copy Right covers the following except", "Literary", "Cinematograph", "Artistic", "Photocopy", "Photocopy"],
        ["Copy Right law violation except", "Printing", "Counterfeits", "Piracy", "Plagiarism", "Printing"],
        ["Full Meaning of APA is", "American Psychological Association", "American Philosophy", "African Psychological", "Association of Psych", "American Psychological Association"],
        ["An example of Malicious code is", "Virus", "Trojan", "Logic Bomb", "All of the above", "All of the above"],
        ["Security Measure to Computer Threat", "Antivirus", "Anti-Spyware", "Fire Wall", "All of the above", "All of the above"],
        ["Example of Operating System except", "Linux", "Fedora", "Macintoch", "Window", "Window"],
        ["Full Meaning of UTP is ", "Unshielded Twisted Pair", "Untouchable", "Unshielded Twined", "Untouchable Twined", "Unshielded Twisted Pair"],
        ["Steps for books to shelf", "I,ii,iii,iv", "iv,I,ii,iii", "iii,I,iv,ii", "iv,I,ii,iii", "iv,I,ii,iii"],
        ["Ways to Protect Data", "Backup", "Detect Virus", "Warn others", "All of the above", "All of the above"],
        ["Not Earlier Writing Materials", "Papyrus", "Clay Table", "Parchment", "Ms Word", "Ms Word"],
        ["Inventor of Printing Machine in 1468 was", "Newton", "Faraday", "Johannes Gutenberg", "Gates", "Johannes Gutenberg"],
        ["Unit where Users are Registered", "Reception", "Circulation", "Cataloging", "Registration", "Circulation"],
        ["The Mother of all Libaries in Nigera is  ", "State", "National Library", "Fuoye", "Senatorial", "National Library"],
        ["Fine for keeping materials beyond period", "Legal fine", "Date due Fine", "Penalty fine", "Library fine", "Library fine"],
        ["Weeding in the Library is an act of ________________ Materials ", "Adding", "Removing", "Complementing", "Supplimenting", "Removing"],
        ["Journals classified under _____________", "Reference", "Serials", "Reserved", "Book", "Serials"],
        ["Encyclopedia classified under ", "Reference", "Serials", "Reserved", "Books", "Reference"],
        ["Back of title page with date/publisher info", "Recto", "Verso page", "Preface", "ToC", "Verso page"],
        ["Page where author briefly discusses book", "Text", "Dedication", "Preface", "Acknowledgement", "Preface"],
        ["Pages preceding main text in Roman numerals", "Title", "Preliminary page", "Copyright", "Initial", "Preliminary page"],
        ["Right hand page with odd numbers", "Right", "Recto", "Transformation", "Verso", "Recto"],
        ["Brief remark by someone familiar with subject", "Introduction", "Foreword", "Appendix", "Index", "Foreword"],
        ["Geographical dictionary with cultural info", "Gazettes", "Gazetteers", "Directories", "Yearbook", "Gazetteers"],
        ["Government publications referred to as ", "Gazettes", "Gazzetteer", "Yearbook", "Directories", "Gazettes"],
        ["All these are type of serials except _________", "Periodical", "Journals", "Biographies", "Magazine", "Biographies"],
        ["ICT version of libraries except", "Automated", "Digital", "Traditional library", "Virtual", "Traditional library"]
    ]
    
    story.append(Paragraph("GST 103: Use of Library and Introduction to ICT", title_style))
    story.append(Paragraph("Tutorial Questions By Spectra", title_style))
    story.append(Spacer(1, 15))

    # Questions and Options
    for i, item in enumerate(data, 1):
        q_text = f"{i}. {item[0]}"
        story.append(Paragraph(q_text, q_style))
        story.append(Spacer(1, 4))
        story.append(Paragraph(f"A. {item[1]}", opt_style))
        story.append(Paragraph(f"B. {item[2]}", opt_style))
        story.append(Paragraph(f"C. {item[3]}", opt_style))
        story.append(Paragraph(f"D. {item[4]}", opt_style))

    story.append(PageBreak())
    story.append(Paragraph("ANSWERS", title_style))
    story.append(Spacer(1, 15))
    
    answer_table_data = []
    temp_row = []
    for i, item in enumerate(data, 1):
        temp_row.append(f"{i}. {item[5]}")
        if len(temp_row) == 2: 
            answer_table_data.append(temp_row)
            temp_row = []
    if temp_row:
        answer_table_data.append(temp_row)

    ans_table = LongTable(answer_table_data, colWidths=[3*inch, 3*inch])
    ans_table.setStyle(TableStyle([
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    
    story.append(ans_table)
    
    doc.build(story)
    print(f"Success! GST103-by-Spectra010s.pdf has been created.")

if __name__ == "__main__":
    generate_gst_pdf()