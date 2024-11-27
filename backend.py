# backend.py
import google.generativeai as genai
import streamlit as st

gemini_api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
    }
)
def GenerateResponse(input_text):
     response = model.generate_content([
     "answer all questions as possible",
     "input: who are you?",
     "output: I'm the School Help Desk",
     "input: what all you can do?",                                 
     "output: i can help by answering you inqueries",
      "input contact",
  "output: Contact Information:\n            - Landline: (047) 602-4985\n            - Mobile: 0999-359-0023\n            - Facebook: https://www.facebook.com/stbenilde",
  "input your creators",
  "output: My creators are Mr. Hans Mackey, Uriel Morales and Nathaniel Cac. Thank you for asking that wonderful question!",
  "input contact information",
  "output: Contact Information:\n            - Landline: (047) 602-4985\n            - Mobile: 0999-359-0023\n            - Facebook: https://www.facebook.com/stbenilde",
  "input where can I contact you?",
  "output: Contact Information:\n            - Landline: (047) 602-4985\n            - Mobile: 0999-359-0023\n            - Facebook: https://www.facebook.com/stbenilde",
  "input BND Creators",
  "output: My creators are Mr. Hans Mackey, Uriel Morales and Nathaniel Cac. Thank you for asking that wonderful question!",
  "input made by",
  "output: BND was made by Mr. Hans Mackey, Uriel Morales and Nathaniel Cac. Thank you for asking!",
  "input Location",
  "output: Main Building is located at 2647 Rizal Ave, Olongapo City, Zambales.\nNearest Landmark: Front of Shell Gas Station and Andoks.\n\nAnnex Building is located in Corner W 18th Street, Olongapo City, Zambale\nLandmark: 3rd floor and 4th floor of Victory Liner Central Station Building.",
  "input located",
  "output: Main Building is located at 2647 Rizal Ave, Olongapo City, Zambales.\nNearest Landmark: Front of Shell Gas Station and Andoks.\n\nAnnex Building is located in Corner W 18th Street, Olongapo City, Zambale\nLandmark: 3rd floor and 4th floor of Victory Liner Central Station Building.",
  "input find",
  "output: Main Building is located at 2647 Rizal Ave, Olongapo City, Zambales.\nNearest Landmark: Front of Shell Gas Station and Andoks.\n\nAnnex Building is located in Corner W 18th Street, Olongapo City, Zambale\nLandmark: 3rd floor and 4th floor of Victory Liner Central Station Building.",
  "input where",
  "output: Main Building is located at 2647 Rizal Ave, Olongapo City, Zambales.\nNearest Landmark: Front of Shell Gas Station and Andoks.\n\nAnnex Building is located in Corner W 18th Street, Olongapo City, Zambale\nLandmark: 3rd floor and 4th floor of Victory Liner Central Station Building.",
  "input requirement",
  "output: Admission Requirements for New Students:\n            - Report Card (Form 138)\n            - Certificate of Good Moral\n            - Original Copy of Birth Certificate (PSA)\n            - 2x2 Picture with white background (2 copies)\n            - Long Brown Envelope\n\n            For Transferees:\n            - Honorable Dismissal\n            - Certificate of Transfer Credentials\n            - Certificate of Good Moral\n            - Original Copy of Birth Certificate (PSA)\n            - 2x2 Picture with white background (2 copies)\n            - Long Brown Envelope",
  "input programs",
  "output: Here are the college programs we offer:\n            Business and Management Department(BMD)\n            - Bachelor of Science in Accountancy(BSA)\n            - Bachelor of Science in Accounting Information System(BSAIS)\n            - Bachelor of Science in Customs Administration(BSCA)\n            - Bachelor of Scienece in Entrepreneurship(BSEntrep)\n            - Bachelor of Science in Real Estate Management(BSREM)\n            \n            Information and Communications Technology Department(ICTD)\n            - Bachelor of Science in Information Technology(BSIT)\n            - Bachelor of Science in Entertainment and Multimedia Computing(BSEMC-Specializing Game Development)\n            - 2-Year Computer Information and Multimedia Technology(CIMT)\n            \n           Tourism and Hospitality Department(THD)\n            - Bachelor of Science in Hospitality Management(BSHM)\n            - Bachelor of Science in Tourism Management(BSTM)\n            - Diploma in Travel and Tourism Technology (Leading to BS in Tourism Management)\n            - 3-Year Diploma in Travel and Tourism Technology (Leading to BSTM)\n            - 2-Year Cruise Ship Management(CSM)\n            - 2-Year Tourism, Hotel, and Restaurant Management(THRO)",
  "input college",
  "output: Here are the college programs we offer:\n            Business and Management Department(BMD)\n            - Bachelor of Science in Accountancy(BSA)\n            - Bachelor of Science in Accounting Information System(BSAIS)\n            - Bachelor of Science in Customs Administration(BSCA)\n            - Bachelor of Scienece in Entrepreneurship(BSEntrep)\n            - Bachelor of Science in Real Estate Management(BSREM)\n            \n            Information and Communications Technology Department(ICTD)\n            - Bachelor of Science in Information Technology(BSIT)\n            - Bachelor of Science in Entertainment and Multimedia Computing(BSEMC-Specializing Game Development)\n            - 2-Year Computer Information and Multimedia Technology(CIMT)\n            \n           Tourism and Hospitality Department(THD)\n            - Bachelor of Science in Hospitality Management(BSHM)\n            - Bachelor of Science in Tourism Management(BSTM)\n            - Diploma in Travel and Tourism Technology (Leading to BS in Tourism Management)\n            - 3-Year Diploma in Travel and Tourism Technology (Leading to BSTM)\n            - 2-Year Cruise Ship Management(CSM)\n            - 2-Year Tourism, Hotel, and Restaurant Management(THRO)",
  "input tesda",
  "output: Here are the TESDA courses we offer:\n          \n            Diploma Programs:\n            - Diploma in Travel and Tourism Technology\n            - Diploma in Hospitality Management\n\n            Short Term TVET Program:\n            - Events Management Services NC III\n            - Game Programming NC III\n            - Visual Graphics Design NC III\n            - Bartending NC II\n            - Bread and Pastry Production NC II\n            - Computer Systems Servicing NC II\n            - Cookery NC II\n            - Food and Beverages Services NC II\n            - Front Office Services NC II\n            - Tourism Promotion Services NC II\n\n            For the updated available TESDA programs, message us in Facebook!\n            Facebook: https://www.facebook.com/BNDCHATBOT or simply search BND Chatbot",
  "input free",
  "output: Here are the TESDA courses we offer:\n          \n            Diploma Programs:\n            - Diploma in Travel and Tourism Technology\n            - Diploma in Hospitality Management\n\n            Short Term TVET Program:\n            - Events Management Services NC III\n            - Game Programming NC III\n            - Visual Graphics Design NC III\n            - Bartending NC II\n            - Bread and Pastry Production NC II\n            - Computer Systems Servicing NC II\n            - Cookery NC II\n            - Food and Beverages Services NC II\n            - Front Office Services NC II\n            - Tourism Promotion Services NC II\n\n            For the updated available TESDA programs, message us in Facebook!\n            Facebook: https://www.facebook.com/BNDCHATBOT or simply search BND Chatbot",
  "input available hours of school",
  "output: St. Benilde Center for Global Competence Main Building and Annex Building are open 8:00 AM to 5:00 PM.",
  "input st benilde",
  "output: St. Benilde Center for Global Competence, Inc. is a recognized institution offering various programs in business, ICT, and tourism. We aim to equip students with the skills needed for global competence through quality education and training. Our programs cater to various fields such as Business, Information Technology, Tourism, and Hospitality, ensuring our students are industry-ready.",
  "input BND",
  "output: BND is a Chatbot System created by 4th-year students of St. Benilde Center for Global Competence as a Capstone project. It aims to help the school by providing stress-free answers to inquiries, concerns and matters about St. Benilde.",
  "input need help",
  "output: Need Help? Contact us in our Facebook Page: https://www.facebook.com/BNDCHATBOT and we will assist you quickly",
  "input member of school",
  "output: SCHOOL OFFICIALS\n\n        ADMINISTRATION DEPARTMENT\n        School President: Sonny J. Tabirara, LCB\n        VP for Administration and Finance: Ronald J. Camacho, MBA\n        Admin and Human Resource: Widelfredo T. Diaz, SO2\n        Head, Accounting Office/Disbursement Specialist: Gracita D. Miclat, LPT, MBA\n        Account Management Officer: Jhomer M. Onoya\n        School Registrar: Donna May Tabaranza, LPT\n        Assistant Registrar: Rolly I. Oliveria\n        Head, Physical Facilities: Jim P. Pagado\n        MIS/Property and Computer Laboratory Custodian: Janin Eljai B. Ramos\n        Head, Security Officer: Mateo F. Cayquep\n        Security Officer: Chant Nicole B. Damaso\n        \n        ACADEMICS DEPARTMENT\n        VP for Academics and Student Development and Services: Ronald J. Camacho, MBA\n        Academic Assistant/Marketing Officer: Czarina Kay Loriega\n        Head, Tourism and Hospitality Department: James Raphael E. Santiago, MBM\n        HRM Laboratory Custodian: Jash B. Ramos\n        Head, Business and Management Department: Veronica Joi C. Calubhay, LCB\n        Program Chair for BS in Accountancy: Remar Allen M. Bautista, CPA, MBA\n        Head, Information and Communication Technology Department: Mary Joanne B. Olino\n        Program Chair for BS in Entertainment and Multimedia Computing: Alvin S. Gallo\n        TVET Program Coordinator: Mark Khristopher DC. Mendoza\n        \n        OFFICE OF THE STUDENT DEVELOPMENT AND SERVICES\n        Head Office of the Student Development and Services: Riena A. Macapagal\n        Guidance Advocate/Designate: Chello Ann P. Asuncion, LPT\n        Library Supervising Consultant: Justine Mae Payot\n        NSTP Coordinator: Amiel N. Abela, LPT\n        Sports and Atheletics Coordinator: Ramer M. Bautista, LPT\n        \n        SENIOR HIGH SCHOOL DEPARTMENT\n        Senior High School Principal: Rodolfo B. Lacambra, MaEd\n        Senior High School Focal Person: Aurora A. Famadulan\n        Senior High School Faculty: Amiel N. Abela, LPT\n        Dee Joy D. Alcanzo, LPT\n        Ramer M, Bautista, LPT\n        Armina C. Domingo\n        Wenray Estabillo\n        Wendell Mark L. Vicena, LPT\n        Shaira Lee D. Manglicmot, LPT\n\n        ASSESSMENT CENTER\n        Manager: Ronald J. Camacho, MBA\n        Assistant Managers: Mark Khristoper DC. Mendoza\n        James Raphael E. Santiago, MBM\n        Processing Officer: Jim P. Pagado\n        Admission Officer: Mary May L. Montes\n        Records and T2MIS Focal Person: Paul Mark Ebuenga\n        Cashier: Jhomer M. Onoya\n        Liason Officer: Jash B. Ramos",
  "input school officials",
  "output: SCHOOL OFFICIALS\n\n        ADMINISTRATION DEPARTMENT\n        School President: Sonny J. Tabirara, LCB\n        VP for Administration and Finance: Ronald J. Camacho, MBA\n        Admin and Human Resource: Widelfredo T. Diaz, SO2\n        Head, Accounting Office/Disbursement Specialist: Gracita D. Miclat, LPT, MBA\n        Account Management Officer: Jhomer M. Onoya\n        School Registrar: Donna May Tabaranza, LPT\n        Assistant Registrar: Rolly I. Oliveria\n        Head, Physical Facilities: Jim P. Pagado\n        MIS/Property and Computer Laboratory Custodian: Janin Eljai B. Ramos\n        Head, Security Officer: Mateo F. Cayquep\n        Security Officer: Chant Nicole B. Damaso\n        \n        ACADEMICS DEPARTMENT\n        VP for Academics and Student Development and Services: Ronald J. Camacho, MBA\n        Academic Assistant/Marketing Officer: Czarina Kay Loriega\n        Head, Tourism and Hospitality Department: James Raphael E. Santiago, MBM\n        HRM Laboratory Custodian: Jash B. Ramos\n        Head, Business and Management Department: Veronica Joi C. Calubhay, LCB\n        Program Chair for BS in Accountancy: Remar Allen M. Bautista, CPA, MBA\n        Head, Information and Communication Technology Department: Mary Joanne B. Olino\n        Program Chair for BS in Entertainment and Multimedia Computing: Alvin S. Gallo\n        TVET Program Coordinator: Mark Khristopher DC. Mendoza\n        \n        OFFICE OF THE STUDENT DEVELOPMENT AND SERVICES\n        Head Office of the Student Development and Services: Riena A. Macapagal\n        Guidance Advocate/Designate: Chello Ann P. Asuncion, LPT\n        Library Supervising Consultant: Justine Mae Payot\n        NSTP Coordinator: Amiel N. Abela, LPT\n        Sports and Atheletics Coordinator: Ramer M. Bautista, LPT\n        \n        SENIOR HIGH SCHOOL DEPARTMENT\n        Senior High School Principal: Rodolfo B. Lacambra, MaEd\n        Senior High School Focal Person: Aurora A. Famadulan\n        Senior High School Faculty: Amiel N. Abela, LPT\n        Dee Joy D. Alcanzo, LPT\n        Ramer M, Bautista, LPT\n        Armina C. Domingo\n        Wenray Estabillo\n        Wendell Mark L. Vicena, LPT\n        Shaira Lee D. Manglicmot, LPT\n\n        ASSESSMENT CENTER\n        Manager: Ronald J. Camacho, MBA\n        Assistant Managers: Mark Khristoper DC. Mendoza\n        James Raphael E. Santiago, MBM\n        Processing Officer: Jim P. Pagado\n        Admission Officer: Mary May L. Montes\n        Records and T2MIS Focal Person: Paul Mark Ebuenga\n        Cashier: Jhomer M. Onoya\n        Liason Officer: Jash B. Ramos",
  "input coordinator",
  "output: SCHOOL OFFICIALS\n\n        ADMINISTRATION DEPARTMENT\n        School President: Sonny J. Tabirara, LCB\n        VP for Administration and Finance: Ronald J. Camacho, MBA\n        Admin and Human Resource: Widelfredo T. Diaz, SO2\n        Head, Accounting Office/Disbursement Specialist: Gracita D. Miclat, LPT, MBA\n        Account Management Officer: Jhomer M. Onoya\n        School Registrar: Donna May Tabaranza, LPT\n        Assistant Registrar: Rolly I. Oliveria\n        Head, Physical Facilities: Jim P. Pagado\n        MIS/Property and Computer Laboratory Custodian: Janin Eljai B. Ramos\n        Head, Security Officer: Mateo F. Cayquep\n        Security Officer: Chant Nicole B. Damaso\n        \n        ACADEMICS DEPARTMENT\n        VP for Academics and Student Development and Services: Ronald J. Camacho, MBA\n        Academic Assistant/Marketing Officer: Czarina Kay Loriega\n        Head, Tourism and Hospitality Department: James Raphael E. Santiago, MBM\n        HRM Laboratory Custodian: Jash B. Ramos\n        Head, Business and Management Department: Veronica Joi C. Calubhay, LCB\n        Program Chair for BS in Accountancy: Remar Allen M. Bautista, CPA, MBA\n        Head, Information and Communication Technology Department: Mary Joanne B. Olino\n        Program Chair for BS in Entertainment and Multimedia Computing: Alvin S. Gallo\n        TVET Program Coordinator: Mark Khristopher DC. Mendoza\n        \n        OFFICE OF THE STUDENT DEVELOPMENT AND SERVICES\n        Head Office of the Student Development and Services: Riena A. Macapagal\n        Guidance Advocate/Designate: Chello Ann P. Asuncion, LPT\n        Library Supervising Consultant: Justine Mae Payot\n        NSTP Coordinator: Amiel N. Abela, LPT\n        Sports and Atheletics Coordinator: Ramer M. Bautista, LPT\n        \n        SENIOR HIGH SCHOOL DEPARTMENT\n        Senior High School Principal: Rodolfo B. Lacambra, MaEd\n        Senior High School Focal Person: Aurora A. Famadulan\n        Senior High School Faculty: Amiel N. Abela, LPT\n        Dee Joy D. Alcanzo, LPT\n        Ramer M, Bautista, LPT\n        Armina C. Domingo\n        Wenray Estabillo\n        Wendell Mark L. Vicena, LPT\n        Shaira Lee D. Manglicmot, LPT\n\n        ASSESSMENT CENTER\n        Manager: Ronald J. Camacho, MBA\n        Assistant Managers: Mark Khristoper DC. Mendoza\n        James Raphael E. Santiago, MBM\n        Processing Officer: Jim P. Pagado\n        Admission Officer: Mary May L. Montes\n        Records and T2MIS Focal Person: Paul Mark Ebuenga\n        Cashier: Jhomer M. Onoya\n        Liason Officer: Jash B. Ramos",
  "input list of professor",
  "output: SCHOOL OFFICIALS\n\n        ADMINISTRATION DEPARTMENT\n        School President: Sonny J. Tabirara, LCB\n        VP for Administration and Finance: Ronald J. Camacho, MBA\n        Admin and Human Resource: Widelfredo T. Diaz, SO2\n        Head, Accounting Office/Disbursement Specialist: Gracita D. Miclat, LPT, MBA\n        Account Management Officer: Jhomer M. Onoya\n        School Registrar: Donna May Tabaranza, LPT\n        Assistant Registrar: Rolly I. Oliveria\n        Head, Physical Facilities: Jim P. Pagado\n        MIS/Property and Computer Laboratory Custodian: Janin Eljai B. Ramos\n        Head, Security Officer: Mateo F. Cayquep\n        Security Officer: Chant Nicole B. Damaso\n        \n        ACADEMICS DEPARTMENT\n        VP for Academics and Student Development and Services: Ronald J. Camacho, MBA\n        Academic Assistant/Marketing Officer: Czarina Kay Loriega\n        Head, Tourism and Hospitality Department: James Raphael E. Santiago, MBM\n        HRM Laboratory Custodian: Jash B. Ramos\n        Head, Business and Management Department: Veronica Joi C. Calubhay, LCB\n        Program Chair for BS in Accountancy: Remar Allen M. Bautista, CPA, MBA\n        Head, Information and Communication Technology Department: Mary Joanne B. Olino\n        Program Chair for BS in Entertainment and Multimedia Computing: Alvin S. Gallo\n        TVET Program Coordinator: Mark Khristopher DC. Mendoza\n        \n        OFFICE OF THE STUDENT DEVELOPMENT AND SERVICES\n        Head Office of the Student Development and Services: Riena A. Macapagal\n        Guidance Advocate/Designate: Chello Ann P. Asuncion, LPT\n        Library Supervising Consultant: Justine Mae Payot\n        NSTP Coordinator: Amiel N. Abela, LPT\n        Sports and Atheletics Coordinator: Ramer M. Bautista, LPT\n        \n        SENIOR HIGH SCHOOL DEPARTMENT\n        Senior High School Principal: Rodolfo B. Lacambra, MaEd\n        Senior High School Focal Person: Aurora A. Famadulan\n        Senior High School Faculty: Amiel N. Abela, LPT\n        Dee Joy D. Alcanzo, LPT\n        Ramer M, Bautista, LPT\n        Armina C. Domingo\n        Wenray Estabillo\n        Wendell Mark L. Vicena, LPT\n        Shaira Lee D. Manglicmot, LPT\n\n        ASSESSMENT CENTER\n        Manager: Ronald J. Camacho, MBA\n        Assistant Managers: Mark Khristoper DC. Mendoza\n        James Raphael E. Santiago, MBM\n        Processing Officer: Jim P. Pagado\n        Admission Officer: Mary May L. Montes\n        Records and T2MIS Focal Person: Paul Mark Ebuenga\n        Cashier: Jhomer M. Onoya\n        Liason Officer: Jash B. Ramos",
  "input teacher",
  "output: SCHOOL OFFICIALS\n\n        ADMINISTRATION DEPARTMENT\n        School President: Sonny J. Tabirara, LCB\n        VP for Administration and Finance: Ronald J. Camacho, MBA\n        Admin and Human Resource: Widelfredo T. Diaz, SO2\n        Head, Accounting Office/Disbursement Specialist: Gracita D. Miclat, LPT, MBA\n        Account Management Officer: Jhomer M. Onoya\n        School Registrar: Donna May Tabaranza, LPT\n        Assistant Registrar: Rolly I. Oliveria\n        Head, Physical Facilities: Jim P. Pagado\n        MIS/Property and Computer Laboratory Custodian: Janin Eljai B. Ramos\n        Head, Security Officer: Mateo F. Cayquep\n        Security Officer: Chant Nicole B. Damaso\n        \n        ACADEMICS DEPARTMENT\n        VP for Academics and Student Development and Services: Ronald J. Camacho, MBA\n        Academic Assistant/Marketing Officer: Czarina Kay Loriega\n        Head, Tourism and Hospitality Department: James Raphael E. Santiago, MBM\n        HRM Laboratory Custodian: Jash B. Ramos\n        Head, Business and Management Department: Veronica Joi C. Calubhay, LCB\n        Program Chair for BS in Accountancy: Remar Allen M. Bautista, CPA, MBA\n        Head, Information and Communication Technology Department: Mary Joanne B. Olino\n        Program Chair for BS in Entertainment and Multimedia Computing: Alvin S. Gallo\n        TVET Program Coordinator: Mark Khristopher DC. Mendoza\n        \n        OFFICE OF THE STUDENT DEVELOPMENT AND SERVICES\n        Head Office of the Student Development and Services: Riena A. Macapagal\n        Guidance Advocate/Designate: Chello Ann P. Asuncion, LPT\n        Library Supervising Consultant: Justine Mae Payot\n        NSTP Coordinator: Amiel N. Abela, LPT\n        Sports and Atheletics Coordinator: Ramer M. Bautista, LPT\n        \n        SENIOR HIGH SCHOOL DEPARTMENT\n        Senior High School Principal: Rodolfo B. Lacambra, MaEd\n        Senior High School Focal Person: Aurora A. Famadulan\n        Senior High School Faculty: Amiel N. Abela, LPT\n        Dee Joy D. Alcanzo, LPT\n        Ramer M, Bautista, LPT\n        Armina C. Domingo\n        Wenray Estabillo\n        Wendell Mark L. Vicena, LPT\n        Shaira Lee D. Manglicmot, LPT\n\n        ASSESSMENT CENTER\n        Manager: Ronald J. Camacho, MBA\n        Assistant Managers: Mark Khristoper DC. Mendoza\n        James Raphael E. Santiago, MBM\n        Processing Officer: Jim P. Pagado\n        Admission Officer: Mary May L. Montes\n        Records and T2MIS Focal Person: Paul Mark Ebuenga\n        Cashier: Jhomer M. Onoya\n        Liason Officer: Jash B. Ramos",
  "input enrollment",
  "output: Enrollment Process\n\n        I. New Enrollees\n        Step 1 - Evaluation of Admission Documents.\n        Step 2 - Fill out Student Data Sheet.\n        Step 3 - Fill out Admission Procedure Sheet.\n        Step 4 - Printing of Enrollment Form.\n        Step 5 - Assessment and Payment of Tuition Fee.\n        Step 6 - Submission of Documents to the Registrar.\n\n        II. Transferees\n        Step 1 - Evaluation of Transfer Credentials.\n        Step 2 - Fill out Student Data Sheet.\n        Step 3 - Fill out Admission Procedure Sheet.\n        Step 4 - Printing of Enrollment Form.\n        Step 5 - Assessment and Payment of Tuition Fee.\n        Step 6 - Submission of Documents to the Registrar.\n\n        III. Tuition and Fees\n        - As low as PHP. 15,000,00 (All-in-Fee)\n        - PHP. 546.00 per unit",
  "input process enrolling",
  "output: Enrollment Process\n\n        I. New Enrollees\n        Step 1 - Evaluation of Admission Documents.\n        Step 2 - Fill out Student Data Sheet.\n        Step 3 - Fill out Admission Procedure Sheet.\n        Step 4 - Printing of Enrollment Form.\n        Step 5 - Assessment and Payment of Tuition Fee.\n        Step 6 - Submission of Documents to the Registrar.\n\n        II. Transferees\n        Step 1 - Evaluation of Transfer Credentials.\n        Step 2 - Fill out Student Data Sheet.\n        Step 3 - Fill out Admission Procedure Sheet.\n        Step 4 - Printing of Enrollment Form.\n        Step 5 - Assessment and Payment of Tuition Fee.\n        Step 6 - Submission of Documents to the Registrar.\n\n        III. Tuition and Fees\n        - As low as PHP. 15,000,00 (All-in-Fee)\n        - PHP. 546.00 per unit",
  "input values, vision, target",
  "output: Our School Core Values are:\n        Competence, Discipline, Initiative, Service. \n\n        Compentece: Striving for Excellence Through Skill and Knowledge.\n        Discipline: Fostering Personal and Professional Growth Through Diligence.\n        Initiative: Pioneering Innovation and Positive Change Through Proactivity.\n        Service: Empowering Others and Creating Impact Through Selfless Acts.",
  "input ano ang school grade na meron sa st benilde?",
  "output: ",
     f"input: {input_text}",
     "output: ",
     ])
     return response.text

