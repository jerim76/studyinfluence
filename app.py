import streamlit as st
from datetime import datetime

# Page setup
st.set_page_config(page_title="Global Tutor Hub", page_icon="🌍", layout="wide")

# Title and intro
st.title("🌍 Global Tutor Hub")
st.markdown("Connect, learn, and share ideas with peers across the world — regardless of curriculum.")

# Sidebar for navigation
menu = ["Home", "Discussions", "Live Classrooms", "Resources", "Profile"]
choice = st.sidebar.selectbox("Navigate", menu)

# Home page
if choice == "Home":
    st.subheader("Welcome to Global Tutor Hub")
    st.write("A platform for learners to interact, share knowledge, and collaborate.")
    st.image("https://via.placeholder.com/800x300.png?text=Global+Learning", use_column_width=True)
    st.info("Tip: Use the sidebar to navigate between features.")

# Discussions page
elif choice == "Discussions":
    st.subheader("📢 Global Discussions")
    topic = st.text_input("Start a new topic:")
    if st.button("Post Topic"):
        st.success(f"Topic '{topic}' posted successfully!")
    st.write("---")
    st.write("**Recent Topics:**")
    st.write("- How to solve quadratic equations (Math - Nigeria Curriculum)")
    st.write("- Understanding photosynthesis (Biology - Cambridge Curriculum)")
    st.write("- Physics: Newton's Laws explained (India CBSE)")

# Live Classrooms page
elif choice == "Live Classrooms":
    st.subheader("🎥 Live Classrooms")
    st.write("Join an ongoing class or schedule a new one.")
    class_name = st.text_input("Class Title:")
    class_time = st.time_input("Class Time:", datetime.now().time())
    if st.button("Schedule Class"):
        st.success(f"Class '{class_name}' scheduled for {class_time}.")

# Resources page
elif choice == "Resources":
    st.subheader("📚 Shared Resources")
    uploaded_file = st.file_uploader("Upload a resource file")
    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    st.write("**Available Resources:**")
    st.write("- PDF: 'Algebra Basics.pdf'")
    st.write("- Video: 'Introduction to World History.mp4'")

# Profile page
elif choice == "Profile":
    st.subheader("👤 My Profile")
    name = st.text_input("Full Name")
    curriculum = st.selectbox("Curriculum", ["Cambridge", "IB", "CBSE", "WAEC", "Other"])
    subjects = st.text_area("Subjects of Interest")
    if st.button("Save Profile"):
        st.success("Profile updated successfully!")
