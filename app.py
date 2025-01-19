import streamlit as st
from PIL import Image


# Set page configuration
st.set_page_config(page_title="Muhammad Arif Rubbani Portfolio", layout="wide", initial_sidebar_state="collapsed")

# Add custom CSS for the services section
st.markdown("""
    <style>
        .service-btn {
            display: inline-block;
            padding: 20px;
            margin: 10px 10px;
            background-color: #1ecdf8;
            color: white;
            border-radius: 8px;
            text-align: center;
            cursor: pointer;
            width: 200px;
            font-size: 1.1rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease-in-out;
        }

        .service-btn:hover {
            background-color: #1497b2;
        }

        .service-btn-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }

        .service-description {
            background-color: #1ecdf8;
            color: black;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Services Section
def service_section():
    st.markdown('<h2 class="section-title">What I Do</h2>', unsafe_allow_html=True)
    st.write("Click on any service to see the description:")

    # Service List and Descriptions
    services = {
        "📊 Data Analysis and Visualization": "Perform data cleaning, preprocessing, and analysis to uncover actionable insights. Create visually compelling dashboards and reports using tools like Python, Matplotlib, Seaborn, and Tableau.",
        "🤖 Machine Learning Model Development": "Build predictive and classification models using Scikit-learn, TensorFlow, and Keras. Expertise in NLP, Deep Learning, and model optimization for better performance.",
        "🔗 ETL and Data Pipeline Development": "Design and implement robust ETL pipelines using PySpark, KNIME, and Pentaho. Automate data workflows to ensure smooth data integration and management.",
        "🗄️ Database Management and SQL Development": "Optimize database queries for performance and maintain data integrity. Develop and manage SQL databases, including complex queries and stored procedures.",
        "💻 Custom Software and Application Development": "Develop scalable and efficient software applications using Python, Django, and Java. Strong understanding of OOP principles and design patterns for software architecture.",
        "👨‍🏫 Freelance Python Tutoring and Programming Assistance": "Teach Python programming at all levels, from beginner to advanced, including DSA and OOP concepts. Provide one-on-one and group training tailored to specific learning goals.",
        "📈 Business Intelligence and Data Dashboard Creation": "Design interactive dashboards for real-time decision-making using tools like Power BI and Tableau. Integrate multiple data sources for comprehensive business reporting.",
        "🧑‍💻 Project Consultation and Guidance": "Assist in building custom solutions like Diet Plan Recommendation Engines or Movie Advisory Systems. Offer mentorship and support for capstone and academic projects in data science.",
        "🌐 Web Scraping and Data Collection Services": "Scrape large-scale data from websites and APIs for business and research needs. Utilize Python libraries like BeautifulSoup and Selenium for efficient data extraction.",
        "📑 Professional Documentation and Report Writing": "Deliver detailed and professional technical documentation and business reports. Support with academic writing in the field of data science and analytics."
    }

    # Create a container for the service buttons and the description
    col1, col2 = st.columns([2, 3])

    with col1:
        # Create buttons for each service
        for service in services.keys():
            if st.button(service):
                st.session_state.service_description = services[service]

    with col2:
        # Display the description of the selected service
        if 'service_description' in st.session_state:
            st.markdown(f"<div class='service-description'>{st.session_state.service_description}</div>", unsafe_allow_html=True)


# Home Section
def home_section():
    st.markdown("<h1 class='header-title'>HI! I am Muhammad Arif Rubbani</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='header-subtitle'>Python Programmer & Data Analyst</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])  # Image on the left (1/3 of the width), text on the right (2/3 of the width)
    with col1:
        st.image("image.png", width=200)  # Resize the image for better fit

    with col2:
        st.markdown("""
            <div class="image-description">
                Welcome to my digital portfolio! Here’s a bit more about me:
                <ul>
                    <li><strong>Data Analyst</strong> with experience in statistical analysis and visualization.</li>
                    <li><strong>Python Programmer</strong> specializing in data science and machine learning projects.</li>
                    <li>Skilled in transforming data into actionable insights using Python and SQL.</li>
                    <li>Strong passion for solving real-world problems using data-driven solutions.</li>
                </ul>
                Explore my work, and let’s connect to build something amazing together!
            </div>
        """, unsafe_allow_html=True)

    st.button("Visit My Works", on_click=lambda: st.write("Redirect to Projects"))


# About Section
def about_section():
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

    # Create a layout with 2 columns: One for Education and One for Experience
    col1, col2 = st.columns(2)
    
    # Left Column: Education Section
    with col1:
        st.markdown("<h3 class='section-subtitle'>Education</h3>", unsafe_allow_html=True)
        st.markdown("""
            - **Bachelor's in Data Science** • University of Central Punjab, Lahore *(2022 – Present)*  
            - **Intermediate (ICS with Physics)** • PGC, Lahore *(2020 – 2022)*
        """)
    
    # Right Column: Experience Section
    with col2:
        st.markdown("<h3 class='section-subtitle'>Experience</h3>", unsafe_allow_html=True)
        st.markdown("""
            - **Data Analyst** • Freelancing • Lahore *(July 2023 – Present)*  
            - **Data Analyst** • SCBS *(April 2024 – December 2024)*  
            - **Data Scientist** • Prodigy Tech *(October 2024 – Present)*  
            - **Python Tutor** • Freelancing • Lahore *(August 2021 – Present)*  
            - **Python Online Tutor** • NOON Islamic Centre • Peshawar *(November 2021 – February 2023)*  
            - **Python & Scratch Tutor** • Home Tuition • Lahore *(January 2022 – October 2022)*  
        """)

# Skills Section
def skills_section():
    st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)

    # In-demand skills with progress bars
    st.markdown("<h3 class='section-subtitle'>In-Demand Skills</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Python**")
        st.progress(0.9)
        st.write("Proficient in Python programming for data analysis, machine learning, and automation.")

        st.write("**Data Science**")
        st.progress(0.85)
        st.write("Experienced in statistical analysis, data visualization, and predictive modeling.")
    with col2:
        st.write("**Machine Learning**")
        st.progress(0.8)
        st.write("Skilled in using machine learning algorithms for data prediction and analysis.")
        
        st.write("**MySQL**")
        st.progress(0.8)
        st.write("Skilled in using MYsql queries to fetch data more swiftly.")
        
        

    st.markdown("<h3 class='section-subtitle'>Other Skills</h3>", unsafe_allow_html=True)
    st.markdown("""
        - **Programming Languages:** Python, C++, Scratch, Java
        - **Tools & Libraries:** Matplotlib, Seaborn, Django, Pandas, Numpy, Scikit-learn, Keras, TensorFlow
        - **Software Development:** Strong OOP concepts, knowledge of design patterns, software development principles
        - **Other Skills:** Microsoft Office, strong analytical and problem-solving skills, good communication skills (written and oral)
    """)

# Projects Section
def projects_section():
    st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
    st.write("Here are some of the projects I have worked on:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("📊 **Diet Plan Recommendation Engine**")
        st.write("A recommendation engine for personalized diet plans based on user preferences.")

    with col2:
        st.markdown("🎥 **Movie Advisor**")
        st.write("A recommendation system based on user's likes, dislikes, and most watched movies.")
    
    # New Projects with Emojis
    st.markdown("<h3 class='section-subtitle'>More Projects</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("📊 **Sales Performance Dashboard**")
        st.write("A dashboard to track sales performance, key metrics, and trends for better decision-making.")
    
    with col2:
        st.markdown("🖼️ **Image Classification Model**")
        st.write("An image classification model built using deep learning techniques for categorizing images.")

# Pricing Section
def pricing_section():
    st.subheader("Pricing Plans")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Free Plan")
        st.markdown("$0.00/month")
        st.markdown("- 1 Project")
        st.markdown("- 5GB Storage")
        st.markdown("- Basic Support")
        st.button("Sign Up", key="free_plan")

    with col2:
        st.markdown("### Standard Plan")
        st.markdown("$9.99/month")
        st.markdown("- 10 Projects")
        st.markdown("- 50GB Storage")
        st.markdown("- Premium Support")
        st.button("Sign Up", key="standard_plan")

    with col3:
        st.markdown("### Premium Plan")
        st.markdown("$49.99/month")
        st.markdown("- Unlimited Projects")
        st.markdown("- 200GB Storage")
        st.markdown("- 24/7 Support")
        st.button("Sign Up", key="premium_plan")

# Contact Section
def contact_section():
    st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
    st.write("Feel free to get in touch with me! Fill out the form below and I will get back to you as soon as possible.")

    # Creating a form with Streamlit's native form widget
    with st.form(key="contact_form"):
        # Input fields
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        # Submit button for the form
        submit_button = st.form_submit_button(label="Send Message")

        # Handle the form submission
        if submit_button:
            if name and email and message:
                st.success("Thank you for reaching out! Your message has been sent.")
            else:
                st.error("Please fill in all fields before submitting.")

# Footer Section
def footer_section():
    st.markdown("""
    <footer>
        <p>Follow me on:</p>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/arifrubbani/">LinkedIn</a>
            <a href="https://github.com/ARIF-rb">GitHub</a>
            <a href="#">Twitter</a>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# Tab-like Navigation with st.tabs
tabs = st.tabs(["Home", "About", "Projects", "Skills", "Services", "Pricing", "Contact"])

with tabs[0]:
    home_section()
with tabs[1]:
    about_section()
with tabs[2]:
    projects_section()
with tabs[3]:
    skills_section()
with tabs[4]:
    service_section()
with tabs[5]:
    pricing_section()
with tabs[6]:
    contact_section()

footer_section()
