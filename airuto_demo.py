import streamlit as st
import google.generativeai as genai

# ========== Configuration ==========
# Replace with your Gemini API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-pro")

# Demo properties and messages
demo_properties = [
    {
        "name": "Modern City Apartment",
        "id": "prop1",
        "context": """Welcome to our modern city apartment!
- Check-in: 2 PM | Check-out: 11 AM
- Wi-Fi: Yes
- Pets: Not allowed
- Parking: Underground parking available
- Key: Collected from lockbox using code sent after booking"""
    },
    {
        "name": "Cozy Beachside Bungalow",
        "id": "prop2",
        "context": """Relax in our cozy beach bungalow.
- Check-in: 3 PM | Check-out: 10 AM
- Wi-Fi: Yes
- Pets: Allowed
- Parking: Free street parking
- Key: Smart lock (code sent on check-in day)"""
    }
]

demo_guest_messages = [
    "Hi! Can we check in early on Friday?",
    "Is there a place to park our car?",
    "Do you allow pets in the apartment?",
    "How do we get the keys when we arrive?"
]

# ========== Streamlit UI ==========
st.set_page_config(page_title="Airbnb AI Auto-Responder", layout="centered")
st.title("🏡 Gemini-Powered Airbnb Auto-Responder")

# Property Selector
property_names = [p["name"] for p in demo_properties]
selected_property = st.selectbox("Select a Property", property_names)
prop = next(p for p in demo_properties if p["name"] == selected_property)

# Guest Message Selector or Input
use_demo_msg = st.toggle("Use Demo Guest Message", value=True)
if use_demo_msg:
    guest_msg = st.selectbox("Choose a Guest Message", demo_guest_messages)
else:
    guest_msg = st.text_area("Enter a Guest Message")

# Button to Generate AI Response
if st.button("Generate Auto-Reply"):
    with st.spinner("Thinking..."):
        chat = model.start_chat(history=[{"role": "user", "parts": [prop["context"]]}])
        response = chat.send_message(guest_msg)
        st.success("🤖 Gemini's Auto-Reply:")
        st.write(response.text)

# Optional: Display full context
with st.expander("🔍 View Property Context"):
    st.code(prop["context"], language="markdown")
