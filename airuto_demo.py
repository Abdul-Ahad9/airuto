import streamlit as st
import google.generativeai as genai

# ========== Configuration ==========
# Replace with your Gemini API key
genai.configure(api_key="AIzaSyBiGHuu5ZehfRVqV7mjiXTqDC-J50Wb48Q")
model = genai.GenerativeModel("gemini-2.0-flash")

# Demo properties and messages
demo_properties = [
    {
    "name": "Urban Escape Loft",
    "id": "urban_escape_loft",
    "context": """
---

📍 Property Name: Urban Escape Loft  
📌 Location: Downtown Toronto, Canada  
🏷️ Property Type: 2-Bedroom Luxury Apartment  
👥 Capacity: Sleeps up to 4 guests  
🛏️ Bedrooms:
- Bedroom 1: Queen bed, closet, full-length mirror  
- Bedroom 2: Double bed, workspace, balcony access  
🛁 Bathrooms:
- 1 Full bathroom with tub and shower  
- 1 Half bath near the entrance  

---

✅ Amenities:
- High-speed Wi-Fi (500 Mbps)  
- Fully equipped kitchen (microwave, oven, fridge, Nespresso)  
- Smart TV with Netflix & Disney+  
- Washer & Dryer  
- Central Heating & Air Conditioning  
- 24/7 concierge service  
- Balcony with city view  
- Elevator access  
- Iron, hair dryer, fresh linens, shampoo, etc.  

---

🔑 Check-in:
- Self check-in via smart lock  
- Code will be sent 24 hours before arrival  
- Check-in time: 3:00 PM  
- Check-out time: 11:00 AM  

---

🚗 Parking:
- 1 free underground parking spot included  
- Additional parking available nearby at $20/night  

---

🚭 House Rules:
- No smoking inside the apartment  
- No parties or events  
- No unregistered guests allowed  
- Quiet hours: 10:00 PM – 8:00 AM  

---

🐾 Pet Policy:
- Pets are not allowed  

---

📍 Nearby Attractions:
- 2-minute walk to Eaton Centre Mall  
- 5-minute subway to CN Tower  
- Dozens of restaurants, cafes, and bars nearby  

---

🆘 Emergency Contacts:
- Building security: +1 416-555-1212  
- Property manager: Jane Doe (+1 416-789-4567)  

---

Please use this information to respond to guest inquiries with clarity and professionalism."""
}
,
    {
    "name": "Willow Lake Retreat",
    "id": "willow_lake_retreat",
    "context": """

---

📍 Property Name: Willow Lake Retreat  
📌 Location: Muskoka Lakes, Ontario, Canada  
🏷️ Property Type: 3-Bedroom Lakeside Cabin  
👥 Capacity: Sleeps up to 6 guests  
🛏️ Bedrooms:
- Master Bedroom: King bed, lake view, ensuite bathroom  
- Bedroom 2: Queen bed, dresser  
- Bedroom 3: Two twin beds (ideal for kids)  
🛁 Bathrooms:
- 2 Full bathrooms (one ensuite, one shared)  

---

✅ Amenities:
- Wi-Fi (limited bandwidth – suitable for email and browsing only)  
- Fully equipped rustic kitchen with wood-burning stove  
- Coffee maker, toaster, dishwasher  
- Fire pit, BBQ grill, canoe, kayak  
- Washer & Dryer  
- Indoor fireplace  
- Board games, books, and puzzles  
- Towels, linens, and basic toiletries provided  

---

🔑 Check-in:
- Self check-in with lockbox  
- Lockbox code sent via message 48 hours before arrival  
- Check-in time: 4:00 PM  
- Check-out time: 10:00 AM  

---

🚗 Parking:
- Free outdoor parking space for up to 3 vehicles  
- No garage access  

---

🚭 House Rules:
- No smoking inside the cabin  
- Please clean up after pets  
- Use firewood responsibly  
- No parties or loud music after 9:00 PM  

---

🐾 Pet Policy:
- Pets are allowed (max 2)  
- Please do not allow pets on beds or furniture  

---

📍 Nearby Attractions:
- 10-minute drive to Port Carling village  
- 15-minute hike to scenic Muskoka lookout  
- Walking distance to Willow Lake beach  

---

🆘 Emergency Contacts:
- Local caretaker: Emily +1 705-555-7890  
- Veterinary clinic (for pets): +1 705-888-1234  

---

Please use this information to respond to guest inquiries with clarity, friendliness, and professionalism, reflecting the calm, nature-focused vibe of the property.
"""
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
