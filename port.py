import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Vemireddy Sivaprasad Reddy | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0b1120;
    color: #f8fafc;
}

/* Hide Streamlit branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hero */

.hero-title {
    font-size: 55px;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 10px;
}

.hero-subtitle {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 20px;
}

.hero-text {
    font-size: 18px;
    color: #94a3b8;
    line-height: 1.8;
}

/* Section titles */

.section-title {
    font-size: 34px;
    font-weight: 800;
    margin-top: 70px;
    margin-bottom: 30px;
}

/* Cards */

.card {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    border-color: #64748b;
    transform: translateY(-3px);
}

.card h3 {
    font-size: 22px;
    margin-bottom: 12px;
}

.card p {
    color: #94a3b8;
    line-height: 1.7;
}

/* Skill */

.skill-card {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-bottom: 15px;
}

.skill-card h4 {
    margin: 8px 0;
}

.skill-card p {
    color: #94a3b8;
    font-size: 14px;
}

/* Project */

.project {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 25px;
}

.project-content {
    padding: 22px;
}

.project-title {
    font-size: 23px;
    font-weight: 700;
}

.project-description {
    color: #94a3b8;
    line-height: 1.7;
}

.tech {
    color: #cbd5e1;
    font-size: 14px;
    margin-top: 12px;
}

/* Stats */

.stat-card {
    background: #111827;
    border: 1px solid #1e293b;
    border-radius: 15px;
    text-align: center;
    padding: 25px;
}

.stat-number {
    font-size: 32px;
    font-weight: 800;
}

.stat-label {
    color: #94a3b8;
}

/* Links */

a {
    text-decoration: none !important;
}

/* Footer */

.custom-footer {
    text-align: center;
    padding: 50px 0 20px;
    color: #64748b;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

nav1, nav2, nav3, nav4, nav5 = st.columns(
    [3, 1, 1, 1, 1]
)

with nav1:
    st.markdown("### 📊 **VEMIREDDY SIVAPRASAD REDDY**")

with nav2:
    st.markdown("[About](#about)")

with nav3:
    st.markdown("[Skills](#skills)")

with nav4:
    st.markdown("[Projects](#projects)")

with nav5:
    st.markdown("[Contact](#contact)")


st.divider()


# =========================================================
# HERO SECTION
# =========================================================

hero_left, hero_right = st.columns([2, 1])

with hero_left:

    st.markdown(
        '<div class="hero-title">'
        'Hi, I\'m Sivaprasad Reddy 👋'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Data Analyst | SQL | Python | Power BI | Excel | Machine Learning'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-text">
        I transform raw data into meaningful insights,
        interactive dashboards, and data-driven business solutions.
        <br><br>
        Passionate about data analysis, visualization,
        problem solving, and turning complex datasets into
        simple actionable insights.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/vemireddy-sivaprasad-reddy-a2a717344/",
            use_container_width=True
        )

    with c2:
        st.link_button(
            "💻 GitHub",
            "https://github.com/vemireddysivaprasad567-source",
            use_container_width=True
        )

    with c3:

        try:

            with open("resume/resume siva.pdf", "rb") as file:

                st.download_button(
                    "📄 Resume",
                    file,
                    "Sivaprasad_Reddy_Resume.pdf",
                    "application/pdf",
                    use_container_width=True
                )

        except FileNotFoundError:

            st.button(
                "📄 Resume",
                disabled=True,
                use_container_width=True
            )


with hero_right:

    try:

        st.image(
            "images/Dp.jpeg",
            width=280
        )

    except:

        st.markdown(
            """
            <div style="
                height:280px;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:100px;
                background:#111827;
                border-radius:50%;">
                👨‍💻
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# QUICK STATS
# =========================================================

st.write("")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">5+</div>
        <div class="stat-label">Projects</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">4+</div>
        <div class="stat-label">Tools</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">SQL</div>
        <div class="stat-label">Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">BI</div>
        <div class="stat-label">Dashboards</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ABOUT
# =========================================================

st.markdown(
    '<div id="about" class="section-title">👨‍💻 About Me</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

<p>
I am an aspiring Data Analyst with hands-on experience in
SQL, Python, Power BI, Excel, and data visualization.
</p>

<p>
I enjoy working with raw datasets, cleaning and transforming data,
performing exploratory analysis, creating dashboards, and identifying
patterns that can support business decisions.
</p>

<p>
My focus is on solving real-world business problems using data
and communicating insights in a clear and understandable way.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SKILLS
# =========================================================

st.markdown(
    '<div id="skills" class="section-title">🛠 Technical Skills</div>',
    unsafe_allow_html=True
)

skills = [
    ("🐍", "Python", "Pandas • NumPy • Matplotlib"),
    ("🗄️", "SQL", "MySQL • Joins • CTE • Window Functions"),
    ("📊", "Power BI", "DAX • Power Query • Dashboards"),
    ("📗", "Excel", "Pivot Tables • Lookup • Charts"),
    ("🤖", "Machine Learning", "Regression • Classification • Clustering"),
    ("🔧", "Tools", "Git • GitHub • Jupyter Notebook")
]

cols = st.columns(3)

for i, (icon, name, description) in enumerate(skills):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="skill-card">
                <div style="font-size:30px">{icon}</div>
                <h4>{name}</h4>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PROJECTS
# =========================================================

st.markdown(
    '<div id="projects" class="section-title">📊 Featured Projects</div>',
    unsafe_allow_html=True
)


# ---------------- HR PROJECT ----------------

p1, p2 = st.columns(2)

with p1:

    try:
        st.image("images/hr_dashboard.png")
    except:
        st.info("HR Dashboard image")

    st.markdown("""
    <div class="project-content">

    <div class="project-title">
    👥 HR Analytics & Employee Attrition
    </div>

    <p class="project-description">
    Analyzed employee data to identify key factors affecting
    employee attrition and workforce performance.
    </p>

    <div class="tech">
    <b>Tools:</b> Power BI • DAX • Excel
    </div>

    <br>

    <b>Key Insights</b>

    <p class="project-description">
    Attrition Rate • Department • Job Role • Salary •
    Gender • Age • Performance
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🔗 View Project",
        "https://github.com/vemireddysivaprasad567-source/HR_Analytics_Dashboard",
        use_container_width=True
    )


# ---------------- HOSPITAL PROJECT ----------------

with p2:

    try:
        st.image("images/hospital_dashboard.png")
    except:
        st.info("Hospital Dashboard image")

    st.markdown("""
    <div class="project-content">

    <div class="project-title">
    🏥 Hospital Insights Dashboard
    </div>

    <p class="project-description">
    Built an interactive healthcare dashboard to analyze
    patient admissions, departments, demographics and trends.
    </p>

    <div class="tech">
    <b>Tools:</b> Power BI • DAX • Power Query
    </div>

    <br>

    <b>Key Insights</b>

    <p class="project-description">
    Patients • Admissions • Discharges • Average Stay •
    Departments • Monthly Trends
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🔗 View Project",
        "https://github.com/vemireddysivaprasad567-source/Hospital_Insights_Dashboard",
        use_container_width=True
    )


# ---------------- SQL PROJECT ----------------

p3, p4 = st.columns(2)

with p3:

    try:
        st.image("images/sql_project.png")
    except:
        st.info("SQL Project image")

    st.markdown("""
    <div class="project-content">

    <div class="project-title">
    🗄️ SQL WareHouse project
    </div>

    <p class="project-description">
    Used advanced SQL queries to solve WareHouse Project
    and business-related data problems.
    </p>

    <div class="tech">
    <b>Tools:</b> MySQL
    </div>

    <br>

    <b>Concepts</b>

    <p class="project-description">
    Joins • CTEs • Subqueries • CASE •
    Window Functions • LAG • LEAD • RANK
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/vemireddysivaprasad567-source/sql_datawarehouse_proj",
        use_container_width=True
    )


# ---------------- PYTHON PROJECT ----------------

with p4:

    try:
        st.image("images/python_eda.png")
    except:
        st.info("Python EDA image")

    st.markdown("""
    <div class="project-content">

    <div class="project-title">
    🐍 Python Exploratory Data Analysis
    </div>

    <p class="project-description">
    Cleaned, explored and visualized real-world datasets
    to discover trends and useful business insights.
    </p>

    <div class="tech">
    <b>Tools:</b> Python • Pandas • NumPy • Matplotlib
    </div>

    <br>

    <b>Process</b>

    <p class="project-description">
    Data Cleaning • Missing Values • Outliers •
    EDA • Visualization • Insights
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "💻 GitHub Repository",
        "https://github.com/vemireddysivaprasad567-source/Student_Performance_Analysis",
        use_container_width=True
    )


# ---------------- ML PROJECT ----------------

st.markdown("""
<div class="project">

<div class="project-content">

<div class="project-title">
🤖 House Price Prediction
</div>

<p class="project-description">

Built a machine learning model to predict whether an House Price 
is likely to live an organization.

</p>

<div class="tech">
<b>Tools:</b>
Python • Pandas • Scikit-learn • Matplotlib
</div>

<br>

<b>Models:</b>

<p class="project-description">
Logistic Regression • Decision Tree • Random Forest
</p>

</div>

</div>
""", unsafe_allow_html=True)

st.link_button(
    "💻 View ML Project",
    "https://github.com/vemireddysivaprasad567-source/House_Price_Prediction",
    use_container_width=True
)


# =========================================================
# WHAT I CAN DO
# =========================================================

st.markdown(
    '<div class="section-title">💡 What I Can Do</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class="card">

    ### 🧹 Data Cleaning

    Handle missing values, duplicates,
    inconsistent data and outliers.

    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="card">

    ### 📊 Data Visualization

    Create interactive dashboards and
    meaningful visualizations.

    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="card">

    ### 📈 Business Insights

    Convert data analysis into actionable
    business recommendations.

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RESUME
# =========================================================

st.markdown(
    '<div class="section-title">📄 Resume</div>',
    unsafe_allow_html=True
)

resume_col1, resume_col2 = st.columns([2, 1])

with resume_col1:

    st.markdown("""
    <div class="card">

    <h3>Data Analyst Resume</h3>

    <p>
    View my education, technical skills, projects,
    certifications and professional profile.
    </p>

    </div>
    """, unsafe_allow_html=True)


with resume_col2:

    try:

        with open("resume/resume siva.pdf", "rb") as file:

            st.download_button(
                "⬇️ Download Resume",
                file,
                "Sivaprasad_Reddy_Resume.pdf",
                "application/pdf",
                use_container_width=True
            )

    except:

        st.warning("Add resume.pdf")


# =========================================================
# CONTACT
# =========================================================

st.markdown(
    '<div id="contact" class="section-title">📬 Contact Me</div>',
    unsafe_allow_html=True
)

contact1, contact2 = st.columns(2)

with contact1:

    st.markdown("""
    <div class="card">

    ### Let's Connect 🤝

    📧 **Email**  
    <a href="mailto:vemireddysivaprasad567@gmail.com">
    vemireddysivaprasad567@gmail.com
    </a>

    <br><br>

    💼 **LinkedIn**  
    <a href="https://www.linkedin.com/in/vemireddy-sivaprasad-reddy-a2a717344/" target="_blank">
    View my LinkedIn Profile
    </a>

    <br><br>

    💻 **GitHub**  
    <a href="https://github.com/vemireddysivaprasad567-source" target="_blank">
    View my GitHub Profile
    </a>

    </div>
    """, unsafe_allow_html=True)


with contact2:

    with st.form("contact_form"):

        name = st.text_input("Name")

        email = st.text_input("Email")

        message = st.text_area("Message")

        submitted = st.form_submit_button(
            "Send Message",
            use_container_width=True
        )

        if submitted:

            if name and email and message:

                st.success(
                    "Thank you! Your message has been submitted."
                )

            else:

                st.error(
                    "Please fill in all fields."
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="custom-footer">

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<br>

<b>Vemireddy Sivaprasad Reddy</b>

<br>

Data Analyst | SQL | Python | Power BI | Excel

<br><br>

© 2026 All Rights Reserved

</div>
""", unsafe_allow_html=True)