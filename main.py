import streamlit as st

st.set_page_config(page_title="MBTI Career Matcher 💼", page_icon="🧠", layout="centered")

# 🌈 Title Section
st.markdown("""
    <h1 style='text-align: center; color: #F72585; font-size: 3em;'>🔮 MBTI Career Matcher 🔮</h1>
    <p style='text-align: center; font-size: 1.2em; color: #4361EE;'>
        Pick your MBTI and unlock career ideas that match your vibe! ✨💼🌈
    </p>
""", unsafe_allow_html=True)

# 💡 MBTI Career Dictionary
mbti_careers = {
    "INTJ 🧠": ["Strategist 🧩", "Data Scientist 📊", "Engineer ⚙️", "Architect 🏛️"],
    "INFP 🌸": ["Writer ✍️", "Therapist 💬", "Artist 🎨", "Nonprofit Worker 🤝"],
    "ENTP 🔥": ["Entrepreneur 🚀", "Journalist 🗞️", "Marketer 📣", "Product Manager 🧰"],
    "ESFP 🎉": ["Performer 🎤", "Event Planner 📅", "Sales Rep 💼", "Influencer 📸"],
    "ISFJ 💖": ["Nurse 🏥", "Teacher 📚", "Librarian 📖", "Counselor 🧘"],
    "ESTJ 🛠️": ["Manager 📋", "Project Leader 🧭", "Lawyer ⚖️", "Accountant 💰"],
    # ... add more if desired
}

# 🎯 MBTI Selection
selected_mbti = st.selectbox("💫 Choose your MBTI type:", list(mbti_careers.keys()))

if selected_mbti:
    st.markdown(f"### 🌟 Recommended Careers for **{selected_mbti}**:")
    for career in mbti_careers[selected_mbti]:
        st.markdown(f"- {career}")

# 🎨 Footer with vibes
st.markdown("""
    <hr style="border: 1px solid #ccc;" />
    <p style='text-align: center; font-size: 1.1em; color: #3A0CA3;'>
        🌈✨ Explore who you are. Be proud of it. And find the job that makes your soul sparkle! ✨🌈
    </p>
""", unsafe_allow_html=True)
