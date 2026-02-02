import streamlit as st
import base64

# --- 1. CONFIG ---
st.set_page_config(page_title="Skin Care - MediBot", layout="wide", initial_sidebar_state="collapsed")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return ""

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
    .product-card {
        background: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); text-align: center;
        margin-bottom: 25px; border: 1px solid #eee;
    }
    .footer {
        display: flex; justify-content: space-around; padding: 30px;
        background: #eaf6ff; border-top: 1px solid #ddd; margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown('<div class="custom-header"><div class="logo">Medi-<span>Bot</span></div></div>', unsafe_allow_html=True)
st.title("✨ Premium Skin Care")
st.write("Dermatologist-approved formulas for glowing, healthy skin.")


# --- 4. DATA (Formatted with separate lines for Why Use, Dosage, and Limitations) ---
items = [
    {
        "name": "Vitamin C Serum", 
        "img": "Skin/1.jpg", 
        "details": """**Why Use:** Neutralizes free radicals, brightens dark spots, and boosts collagen production.
        \n**Dosage:** Apply 3-5 drops in the morning after cleansing but before moisturizing.
        \n**Limitations:** Can cause tingling; not ideal for extremely sensitive skin. Degrades if exposed to sunlight."""
    },
    {
        "name": "Hyaluronic Acid", 
        "img": "Skin/2.jpg", 
        "details": """**Why Use:** Acts as a humectant to pull moisture into the skin, reducing fine lines.
        \n**Dosage:** Apply to damp skin twice daily (morning and night).
        \n**Limitations:** In dry climates, it can pull moisture out of skin if not sealed with moisturizer."""
    },
    {
        "name": "Night Repair Cream", 
        "img": "Skin/3.jpg", 
        "details": """**Why Use:** Supports the skin's natural circadian rhythm of repair and DNA recovery.
        \n**Dosage:** Apply a pea-sized amount as the final step of your nighttime routine.
        \n**Limitations:** Contains heavier oils; may cause breakouts for very oily or acne-prone skin."""
    },
    {
        "name": "Gentle Cleanser", 
        "img": "Skin/4.jpg", 
        "details": """**Why Use:** Removes dirt and pollutants without stripping the acid mantle (skin barrier).
        \n**Dosage:** Use 1 pump on wet face; massage for 60 seconds and rinse.
        \n**Limitations:** May not effectively remove heavy waterproof makeup or water-resistant sunscreens."""
    },
    {
        "name": "Exfoliating Scrub", 
        "img": "Skin/5.jpg", 
        "details": """**Why Use:** Physically removes dead skin cells to prevent clogged pores and dullness.
        \n**Dosage:** Use only 1-2 times per week on clean, wet skin.
        \n**Limitations:** Avoid using on active acne or broken skin. Over-exfoliation can lead to redness."""
    },
    {
        "name": "Toning Mist", 
        "img": "Skin/6.jpg", 
        "details": """**Why Use:** Instantly restores skin pH and prepares skin to better absorb serums.
        \n**Dosage:** Spray 2-3 pumps over face after cleansing or throughout the day.
        \n**Limitations:** Does not replace a moisturizer. Avoid mists with high alcohol content."""
    }
]

# --- 5. GRID ---
cols = st.columns(3)
for i, item in enumerate(items):
    with cols[i % 3]:
        img_b64 = get_base64_image(item['img'])
        st.markdown(f"""<div class="product-card">
            <img src="data:image/jpeg;base64,{img_b64}" style="width:300px; height:300px; object-fit:cover; border-radius:8px;">
            <h3>{item['name']}</h3></div>""", unsafe_allow_html=True)
        
        with st.expander("View Medical Details"):
            # st.markdown ensures the \n creates a visible new line
            st.markdown(item['details'])

# --- 6. FOOTER & BACK ---
st.divider()
st.page_link("app.py", label="Back to Home Page", icon="🏠")
st.markdown('<footer class="footer"><div><h3>Medi Bot</h3><p>Skin Care Division</p></div></footer>', unsafe_allow_html=True)