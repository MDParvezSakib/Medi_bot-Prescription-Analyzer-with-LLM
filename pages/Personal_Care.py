import streamlit as st
import base64
import os

# --- 1. CONFIG ---
st.set_page_config(page_title="Personal Care - MediBot", layout="wide", initial_sidebar_state="collapsed")

# Helper for local images in folders
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        return ""
    except:
        return ""

# --- 2. CSS ---
st.markdown("""
<style>
    .main { background-color: #f9fafc; font-family: 'Arial', sans-serif; }
    [data-testid="stHeader"] { display: none; } 

    .custom-header {
        display: flex; justify-content: space-between; align-items: center;
        background: #eaf6ff; padding: 15px 40px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .logo { font-size: 26px; font-weight: bold; color: #0077cc; }
    .logo span { color: #00aaff; }

    /* Product Card Styling */
    .product-card {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 25px;
        border: 1px solid #eee;
    }

    .footer {
        display: flex; justify-content: space-around; padding: 30px;
        background: #eaf6ff; border-top: 1px solid #ddd; margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. TOP HEADER ---
st.markdown('<div class="custom-header"><div class="logo">Medi-<span>Bot</span></div></div>', unsafe_allow_html=True)

st.title("🧴 Personal Care Collection")
st.write("High-quality personal hygiene and wellness products.")

# --- 4. PRODUCT DATA (Using Per/1.jpg order) ---
# Ensure you have a folder named 'Per' with images 1.jpg, 2.jpg...
products = [
    {
        "id": 1, 
        "name": "Antiseptic Liquid", 
        "img": "Per/1.jpg", 
        "details": """**Why Use:** Effective protection against germs and bacteria in wounds or surfaces.
        \n**Dosage:** Dilute 1 capful in 250ml of water for wound cleaning.
        \n**Limitations:** External use only; do not swallow. Avoid contact with eyes."""
    },
    {
        "id": 2, 
        "name": "Hand Sanitizer", 
        "img": "Per/2.jpg", 
        "details": """**Why Use:** Kills 99.9% of germs instantly without water.
        \n**Dosage:** Apply a coin-sized drop to palms and rub until dry.
        \n**Limitations:** Flammable; keep away from fire. Can cause dryness with over-use."""
    },
    {
        "id": 3, 
        "name": "Moisturizing Lotion", 
        "img": "Per/3.jpg", 
        "details": """**Why Use:** Restores skin barrier and provides 24-hour hydration.
        \n**Dosage:** Apply liberally to the body after showering.
        \n**Limitations:** For external use only. Discontinue if rash or irritation occurs."""
    },
    {
        "id": 4, 
        "name": "Electric Toothbrush", 
        "img": "Per/4.jpg", 
        "details": """**Why Use:** Sonic technology removes 10x more plaque than manual brushing.
        \n**Dosage:** Brush twice daily for 2 minutes each session.
        \n**Limitations:** Brush heads must be replaced every 3 months. Avoid excessive pressure."""
    },
    {
        "id": 5, 
        "name": "Organic Face Wash", 
        "img": "Per/5.jpg", 
        "details": """**Why Use:** Deep cleans pores using tea tree oil without harsh chemicals.
        \n**Dosage:** Use 1-2 pumps on wet face every morning and evening.
        \n**Limitations:** May cause initial dryness as skin adjusts to natural oils."""
    },
    {
        "id": 6, 
        "name": "Sunscreen SPF 50", 
        "img": "Per/6.jpg", 
        "details": """**Why Use:** Broad spectrum protection against UVA/UVB rays to prevent aging.
        \n**Dosage:** Apply a nickel-sized amount to face 15 minutes before sun exposure.
        \n**Limitations:** Must be reapplied every 2 hours if outdoors or after swimming."""
    }
]

# --- 5. GRID LAYOUT ---
cols = st.columns(3)

for index, p in enumerate(products):
    with cols[index % 3]:
        img_b64 = get_base64_image(p['img'])
        
        # Display Card
        st.markdown(f"""
            <div class="product-card">
                <img src="data:image/jpeg;base64,{img_b64}" style="width:100%; aspect-ratio:1/1; border-radius:8px; object-fit:cover;">
                <h3>{p['name']}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # View Details Modal-style Expander
        with st.expander(f"View Medical Details"):
            # Using st.markdown to preserve the bold headers and new lines
            st.markdown(p['details'])
# --- 6. BACK TO HOME ---
st.divider()
st.page_link("app.py", label="Back to Home Page", icon="🏠")

# --- 7. FOOTER ---
st.markdown("""
    <footer class="footer">
        <div>
            <h3>Medi Bot</h3>
            <p>About Us | Privacy Policy | Terms</p>
        </div>
        <div>
            <h4>Contact</h4>
            <p>Email: medibot@gmail.com</p>
        </div>
        <div>
            <h4>Address</h4>
            <p>Mirpur, Dhaka, Bangladesh</p>
        </div>
    </footer>
""", unsafe_allow_html=True)