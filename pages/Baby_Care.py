import streamlit as st
import base64

# --- 1. CONFIG ---
st.set_page_config(page_title="Baby Care - MediBot", layout="wide", initial_sidebar_state="collapsed")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return ""

# --- 2. CSS ---
st.markdown("""
<style>
    .main { background-color: #f9fafc; }
    [data-testid="stHeader"] { display: none; } 
    .custom-header {
        display: flex; justify-content: space-between; align-items: center;
        background: #fff5f8; padding: 15px 40px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .logo { font-size: 26px; font-weight: bold; color: #ff66a3; }
    .product-card {
        background: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); text-align: center;
        margin-bottom: 25px; border: 1px solid #ffeef4;
    }
    .footer {
        display: flex; justify-content: space-around; padding: 30px;
        background: #fff5f8; border-top: 1px solid #ddd; margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown('<div class="custom-header"><div class="logo">Medi-<span>Baby</span></div></div>', unsafe_allow_html=True)
st.title("👶 Gentle Baby Care")
st.write("Safe and soothing products for your little one's delicate skin.")

# --- 4. DATA (Formatted with Why Use, Dosage, and Limitations) ---
# Assumes images are in a folder named 'Baby' as 1.jpg, 2.jpg, etc.
items = [
    {
        "name": "Baby Shampoo", 
        "img": "Baby/1.jpg", 
        "details": """**Why Use:** Tear-free formula designed to clean delicate hair without irritating the eyes or scalp.
        \n**Dosage:** Apply a small amount to wet hair, gently massage, and rinse thoroughly with warm water.
        \n**Limitations:** For external use only. If redness occurs, discontinue use immediately."""
    },
    {
        "name": "Diaper Cream", 
        "img": "Baby/2.jpg", 
        "details": """**Why Use:** Creates a moisture-repellent barrier to protect sensitive skin from wetness and acidity.
        \n**Dosage:** Apply a thick layer to the diaper area during every change, especially at bedtime.
        \n**Limitations:** Do not apply to deep or punctured wounds. Keep out of reach of children."""
    },
    {
        "name": "Baby Wipes", 
        "img": "Baby/3.jpg", 
        "details": """**Why Use:** Alcohol-free and fragrance-free cleaning for the most sensitive newborn skin.
        \n**Dosage:** Use as needed during diaper changes or for cleaning hands and face.
        \n**Limitations:** Do not flush in the toilet. Ensure the pack is sealed tightly to prevent drying out."""
    },
    {
        "name": "Baby Lotion", 
        "img": "Baby/4.jpg", 
        "details": """**Why Use:** Provides 24-hour hydration to prevent dryness and maintain the skin's natural softness.
        \n**Dosage:** Smooth over the baby's entire body after a bath or whenever skin feels dry.
        \n**Limitations:** Avoid contact with the baby's eyes. Store in a cool, dry place."""
    },
    {
        "name": "Baby Oil", 
        "img": "Baby/5.jpg", 
        "details": """**Why Use:** Perfect for baby massage; helps lock in moisture and soothe dry patches or cradle cap.
        \n**Dosage:** Warm a few drops in your hands and gently massage into the baby's skin.
        \n**Limitations:** Can make surfaces slippery. Avoid applying to the face to prevent accidental ingestion."""
    },
    {
        "name": "Baby Powder", 
        "img": "Baby/6.jpg", 
        "details": """**Why Use:** Absorbs excess moisture to keep skin folds dry and prevent friction-based rashes.
        \n**Dosage:** Shake onto your hand (away from the face) and apply to the skin.
        \n**Limitations:** Avoid inhalation; keep away from the baby's nose and mouth. Use sparingly."""
    }
]

# --- 5. GRID ---
cols = st.columns(3)
for i, item in enumerate(items):
    with cols[i % 3]:
        img_b64 = get_base64_image(item['img'])
        
        # Consistent styling: 300x300 fixed frame
        st.markdown(f"""
            <div class="product-card">
                <img src="data:image/jpeg;base64,{img_b64}" style="width:300px; height:300px; object-fit:cover; border-radius:8px;">
                <h3>{item['name']}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("View Medical Details"):
            # Using st.markdown to process the \n new lines and bold text
            st.markdown(item['details'])

# --- 6. FOOTER & BACK ---
st.divider()
st.page_link("app.py", label="Back to Home Page", icon="🏠")
st.markdown('<footer class="footer"><div><h3>Medi Bot</h3><p>Baby Care Division</p></div></footer>', unsafe_allow_html=True)