import os
import streamlit as st
from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD GEMINI API KEY
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI College Campus Assistant",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# COLLEGE INFORMATION
# All project information is stored directly in this code.
# No PDF files are required.
# ============================================================

COLLEGE_DATA = {

    "College Information": {
        "college_name": "ABC Institute of Technology",
        "location": "Hyderabad, Telangana",
        "established": "2005",
        "type": "Engineering and Technology College",
        "affiliation": "ABC University",
        "campus": "Modern campus with academic buildings, library, laboratories, hostel and sports facilities",
        "working_hours": "Monday to Saturday, 9:00 AM to 5:00 PM",
        "email": "info@abccollege.edu",
        "phone": "+91 98765 43210",
        "website": "www.abccollege.edu"
    },

    "Departments": {

        "Computer Science and Engineering": {
            "short_name": "CSE",
            "description": "Focuses on programming, software development, databases, artificial intelligence and computer technologies.",
            "degree": "B.Tech",
            "duration": "4 years"
        },

        "Artificial Intelligence and Data Science": {
            "short_name": "AI & DS",
            "description": "Focuses on artificial intelligence, machine learning, data science and analytics.",
            "degree": "B.Tech",
            "duration": "4 years"
        },

        "Electronics and Communication Engineering": {
            "short_name": "ECE",
            "description": "Focuses on electronics, communication systems, embedded systems and signal processing.",
            "degree": "B.Tech",
            "duration": "4 years"
        },

        "Electrical and Electronics Engineering": {
            "short_name": "EEE",
            "description": "Focuses on electrical systems, power systems, electrical machines and electronics.",
            "degree": "B.Tech",
            "duration": "4 years"
        },

        "Mechanical Engineering": {
            "short_name": "ME",
            "description": "Focuses on mechanical design, manufacturing, thermal engineering and automation.",
            "degree": "B.Tech",
            "duration": "4 years"
        },

        "Civil Engineering": {
            "short_name": "CE",
            "description": "Focuses on construction, structural engineering, transportation and environmental engineering.",
            "degree": "B.Tech",
            "duration": "4 years"
        }
    },

    "Library": {
        "name": "Central College Library",
        "timings": {
            "Monday_to_Friday": "9:00 AM to 7:00 PM",
            "Saturday": "9:00 AM to 5:00 PM",
            "Sunday": "Closed"
        },
        "facilities": [
            "Textbooks",
            "Reference books",
            "Digital library",
            "Research journals",
            "Newspapers",
            "Magazines",
            "Computer systems",
            "Reading hall",
            "Online academic resources"
        ],
        "rules": [
            "Maintain silence inside the library.",
            "Students must carry their college ID card.",
            "Books must be returned before the due date.",
            "Food and drinks are not allowed.",
            "Mobile phones should be kept on silent mode."
        ],
        "membership": "All registered students automatically receive library membership."
    },

    "Examinations": {
        "types": [
            "Internal examinations",
            "Mid-term examinations",
            "Semester examinations",
            "Practical examinations",
            "End-semester examinations"
        ],
        "process": [
            "Students must complete the required attendance.",
            "Students should register for examinations as instructed by the college.",
            "Hall tickets are issued before semester examinations.",
            "Students must carry their hall ticket and college ID.",
            "Students must follow examination hall rules.",
            "Results are published after evaluation is completed."
        ],
        "grading": "Students are evaluated using internal assessment, practical examinations and semester examinations.",
        "important_rule": "Students must not use unauthorized materials during examinations."
    },

    "Placements": {
        "placement_cell": "The Training and Placement Cell coordinates recruitment activities.",
        "facilities": [
            "Placement training",
            "Aptitude test preparation",
            "Programming practice",
            "Communication skills training",
            "Resume preparation",
            "Mock interviews",
            "Group discussion practice",
            "Technical interview preparation",
            "Career guidance"
        ],
        "recruitment_process": [
            "Company registration",
            "Eligibility verification",
            "Aptitude or online test",
            "Technical interview",
            "HR interview",
            "Final selection"
        ],
        "companies": [
            "Software companies",
            "IT services companies",
            "Core engineering companies",
            "Consulting companies",
            "Product-based companies",
            "Startups"
        ]
    },

    "Transport": {
        "facility": "College bus transportation is available for students and staff.",
        "routes": [
            "City Center",
            "Main Railway Station",
            "Central Bus Station",
            "North Campus Route",
            "South Campus Route",
            "East Campus Route",
            "West Campus Route"
        ],
        "timings": {
            "morning": "7:30 AM to 9:00 AM",
            "evening": "4:30 PM to 6:30 PM"
        },
        "rules": [
            "Students must carry their college ID.",
            "Students must follow the assigned bus route.",
            "Students should maintain discipline inside the bus.",
            "Students should not disturb the driver."
        ]
    },

    "Rules and Regulations": {
        "academic_rules": [
            "Students must attend classes regularly.",
            "Students must maintain the required attendance percentage.",
            "Students must complete assignments on time.",
            "Students must follow examination regulations."
        ],
        "campus_rules": [
            "Students must carry their college ID card.",
            "Students must maintain discipline on campus.",
            "Students must keep the campus clean.",
            "Ragging is strictly prohibited.",
            "Students must respect faculty, staff and other students."
        ],
        "technology_rules": [
            "College computer systems should be used for academic purposes.",
            "Students must not access unauthorized systems.",
            "College internet resources must not be misused."
        ]
    },

    "Hostel": {
        "availability": "Separate hostel facilities are available for eligible students.",
        "facilities": [
            "Furnished rooms",
            "Study tables",
            "Wi-Fi",
            "Dining hall",
            "Drinking water",
            "Laundry facilities",
            "Common room",
            "Security",
            "24-hour basic support"
        ],
        "hostel_rules": [
            "Students must follow hostel timings.",
            "Visitors must follow hostel visitor rules.",
            "Students must maintain cleanliness.",
            "Students must maintain discipline.",
            "Unauthorized activities are not permitted."
        ],
        "timings": {
            "entry": "6:00 AM",
            "exit": "9:00 PM"
        }
    }
}


# ============================================================
# GEMINI CLIENT
# ============================================================

if API_KEY:
    client = genai.Client(api_key=API_KEY)
else:
    client = None


# ============================================================
# HEADER
# ============================================================

st.title("🎓 AI College Campus Assistant")

st.write(
    "Ask questions about college information, departments, "
    "library, examinations, placements, transport, rules and hostel."
)


# ============================================================
# INFORMATION DASHBOARD
# ============================================================

st.subheader("📚 Campus Information")

col1, col2 = st.columns(2)

with col1:
    st.info("🏫 College Information")
    st.info("🎓 Departments")
    st.info("📚 Library")
    st.info("📝 Examinations")

with col2:
    st.info("💼 Placements")
    st.info("🚌 Transport")
    st.info("📜 Rules & Regulations")
    st.info("🏠 Hostel")


# ============================================================
# QUICK INFORMATION
# ============================================================

st.subheader("🔎 Quick Information")

selected_category = st.selectbox(
    "Select a category:",
    list(COLLEGE_DATA.keys())
)

if st.button("View Information", use_container_width=True):

    st.write("###", selected_category)

    information = COLLEGE_DATA[selected_category]

    st.json(information)


# ============================================================
# AI ASSISTANT
# ============================================================

st.subheader("🤖 Ask the AI Assistant")

question = st.text_input(
    "Ask your college-related question:",
    placeholder="Example: What departments are available?"
)


# ============================================================
# ASK ASSISTANT
# ============================================================

if st.button("Ask Assistant", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")

    elif not API_KEY:
        st.error(
            "Gemini API key was not found. "
            "Please add GEMINI_API_KEY to your .env file."
        )

    else:

        with st.spinner("🤖 AI Assistant is thinking..."):

            college_information = str(COLLEGE_DATA)

            prompt = f"""
You are an AI College Campus Assistant.

Answer the student's question using ONLY the college
information provided below.

If the answer is not available in the information,
say:

"Sorry, I don't have that information in the college
database."

Do not invent college information.

Give the answer clearly and use bullet points when useful.

COLLEGE INFORMATION:
{college_information}

STUDENT QUESTION:
{question}
"""

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success("🤖 AI Assistant Answer")

                st.write(response.text)

            except Exception as e:

                st.error(
                    "Unable to get a response from Gemini."
                )

                st.write(str(e))


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎓 AI College Campus Assistant | "
    "College information is stored directly in the application."
)