import streamlit as st
from datetime import datetime

# Page setup
st.set_page_config(page_title="Global Tutor Hub", page_icon="🌍", layout="wide")

# Custom CSS for liveliness
st.markdown("""
<style>
    .main {
        background-color: #fefefe;
    }
    h1, h2, h3 {
        color: #1a73e8;
        font-family: 'Arial Rounded MT Bold', sans-serif;
    }
    .stButton button {
        border-radius: 20px;
        background-color: #1a73e8;
        color: white;
        padding: 8px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0c59cf;
    }
</style>
""", unsafe_allow_html=True)

# Title & intro
st.title("🌍 **Global Tutor Hub**")
st.markdown("### Learn. Share. Connect — *wherever you are!* 📚✨")

# Sidebar menu
menu = ["🏠 Home", "💬 Discussions", "🎥 Live Classrooms", "📚 Resources", "👤 Profile"]
choice = st.sidebar.radio("Navigate", menu)

# Home Page
if choice == "🏠 Home":
    st.subheader("🚀 Welcome Learner!")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("Here’s your space to **connect globally**, share ideas, and grow together. 🌱")
        st.write("- 🌍 Collaborate across **different curricula**")
        st.write("- 💡 Share your thoughts & ask questions")
        st.write("- 🎯 Learn interactively with peers and tutors")
        st.button("Start a Discussion")
    with col2:
        st.image("https://via.placeholder.com/300x300.png?text=Learning+Together", use_column_width=True)

# Discussions
elif choice == "💬 Discussions":
    st.subheader("💡 Global Discussions Board")
    st.markdown("Start a conversation or jump into a trending topic! 🔥")
    topic = st.text_input("📝 New Topic:")
    if st.button("📢 Post Topic"):
        st.success(f"Topic '{topic}' posted successfully!")
    st.write("---")
    st.markdown("**🔥 Trending Topics:**")
    trending = [
        "📐 How to solve quadratic equations (Math - Nigeria Curriculum)",
        "🌿 Understanding photosynthesis (Biology - Cambridge)",
        "⚙️ Newton's Laws explained (Physics - CBSE)"
    ]
    for t in trending:
        st.markdown(f"- {t}")

# Live Classrooms
elif choice == "🎥 Live Classrooms":
    st.subheader("🎓 Join or Host a Live Class")
    st.markdown("📢 *Real-time learning with whiteboards, chat, and video*")
    class_name = st.text_input("📌 Class Title")
    class_time = st.time_input("🕒 Class Time", datetime.now().time())
    if st.button("📅 Schedule Class"):
        st.success(f"Class '{class_name}' scheduled for {class_time} 🗓️")

# Resources
elif choice == "📚 Resources":
    st.subheader("📦 Shared Learning Materials")
    uploaded_file = st.file_uploader("📤 Upload Resource File")
    if uploaded_file:
        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")
    st.markdown("**📥 Available Downloads:**")
    resources = ["📄 Algebra Basics.pdf", "🎞️ Intro to World History.mp4"]
    for r in resources:
        st.markdown(f"- {r}")

# Profile
elif choice == "👤 Profile":
    st.subheader("🧑 My Learning Profile")
    name = st.text_input("👤 Full Name")
    curriculum = st.selectbox("📘 Curriculum", ["Cambridge", "IB", "CBSE", "WAEC", "Other"])
    subjects = st.text_area("📚 Subjects of Interest")
    if st.button("💾 Save Profile"):
        st.success("🎉 Profile updated successfully!")
