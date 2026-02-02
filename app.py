import streamlit as st
import json
import random
import pandas as pd
import base64
import numpy as np
import easyocr
from PIL import Image
from transformers import T5Tokenizer, T5ForConditionalGeneration
from streamlit_cropper import st_cropper   # ✅ NEW

# --- 1. CONFIG & SETUP ---
st.set_page_config(page_title="Medi-Bot 💊", layout="wide", initial_sidebar_state="collapsed")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# --- 2. LOAD AI MODEL, OCR & DATA ---
@st.cache_resource
def load_resources():
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")
    reader = easyocr.Reader(['en'], gpu=False)
    return tokenizer, model, reader

@st.cache_data
def load_medicine_data():
    try:
        with open("medicine_data_cleaned.json", "r") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        return df.dropna(subset=["Drug Name"])
    except FileNotFoundError:
        st.error("Data file 'medicine_data_cleaned.json' not found.")
        return pd.DataFrame()

tokenizer, model, reader = load_resources()
df = load_medicine_data()

# --- 3. AI PROMPT & GENERATION LOGIC ---
def build_prompt(item):
    variants = [
        f"Write a medical summary for {item['Drug Name']} by {item['Company Name']}. Include uses and pregnancy safety: {item['Indication']}. Safety: {item['Use in pregnancy']}",
        f"Summarize this medicine: {item['Drug Name']}. Indication: {item['Indication']}. Side effects: {item['Side Effects']}. Pregnancy: {item['Use in pregnancy']}",
    ]
    return random.choice(variants)

def generate_summary_text(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt", truncation=True).input_ids
    output_ids = model.generate(
        input_ids,
        max_length=320,
        num_beams=5,
        no_repeat_ngram_size=3,
        repetition_penalty=1.2,
        early_stopping=True
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# --- 4. CUSTOM STYLING ---
banner_base64 = get_base64_image("banner.png")
promo_base64 = get_base64_image("promo.png")

st.markdown(f"""
<style>
    .main {{ background-color: #f9fafc; font-family: Arial; }}
    [data-testid="stHeader"] {{ display: none; }}
    .custom-header {{
        display:flex; justify-content:space-between; align-items:center;
        background:#eaf6ff; padding:15px 40px;
    }}
    .logo {{ font-size:26px; font-weight:bold; color:#0077cc; }}
    .logo span {{ color:#00aaff; }}
    .banner {{
        width:100%; aspect-ratio:4/1;
        background:url('data:image/png;base64,{banner_base64}') no-repeat center;
        background-size:contain; border-radius:15px; margin:20px 0;
    }}
    .med-card {{
        background:white; padding:25px; border-radius:12px;
        border-left:6px solid #00aaff; box-shadow:0 4px 15px rgba(0,0,0,0.05);
        margin:20px 0;
    }}
</style>
""", unsafe_allow_html=True)

# --- 5. HEADER ---
st.markdown("""
<div class="custom-header">
    <div class="logo">Medi-<span>Bot</span></div>
    <div>Contact</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="banner"></div>', unsafe_allow_html=True)

# --- 6. MAIN CONTENT ---
col_sidebar, col_main = st.columns([1, 3.5])

with col_sidebar:
    st.markdown("### Categories")
    st.page_link("pages/Personal_Care.py", label="Personal Care", icon="🧴")
    st.page_link("pages/Skin_Care.py", label="Skin Care", icon="✨")
    st.page_link("pages/Baby_Care.py", label="Baby Care", icon="👶")
    st.divider()
    st.markdown("### Quick Chat")
    if chat_prompt := st.chat_input("Ask a question..."):
        st.info(f"AI: I'm processing your request about '{chat_prompt}'")

with col_main:
    st.subheader("🔍 Find Medicine Information")
    search_query = st.text_input("Enter drug name(s)", placeholder="Napa, Sergel...")

    found_meds = []

    if search_query:
        for drug in search_query.split(","):
            drug = drug.strip().lower()
            match = df[df["Drug Name"].str.lower() == drug]
            if not match.empty:
                found_meds.append(match.iloc[0])

    # --- Upload Prescription ---
    st.markdown("""
    <div style="background:#fff;padding:20px;border-radius:10px;border:1px dashed #00aaff;margin-top:30px;">
        <h4>Upload Prescription</h4>
        <p>Crop the medicine area for better accuracy</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"], label_visibility="collapsed")

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")

        st.markdown("### ✂️ Crop Prescription (optional but recommended)")
        cropped_img = st_cropper(
            image,
            realtime_update=True,
            box_color="#00aaff",
            aspect_ratio=None
        )

        st.image(cropped_img, caption="Cropped Image Used for OCR", width=350)

        with st.spinner("🔍 Reading prescription..."):
            img_np = np.array(cropped_img)
            results = reader.readtext(img_np)

            for (_, text, prob) in results:
                if prob < 0.4:
                    continue
                word = text.strip().lower()
                match = df[df["Drug Name"].str.lower() == word]
                if not match.empty:
                    item = match.iloc[0]
                    if not any(m['Drug Name'] == item['Drug Name'] for m in found_meds):
                        found_meds.append(item)

        if not found_meds:
            st.info("No medicines detected. Try cropping more tightly or search manually.")

    # --- Results ---
    if found_meds:
        st.divider()
        st.subheader("Results Found")
        for item in found_meds:
            summary = generate_summary_text(build_prompt(item))
            st.markdown(f"""
            <div class="med-card">
                <h2>💊 {item['Drug Name']}</h2>
                <p><i>By {item['Company Name']}</i></p>
                <p>{summary}</p>
                <hr>
                <p><b>Indication:</b> {item['Indication']}</p>
                <p><b>Active Ingredient:</b> {item['Active Ingredient']}</p>
                <p><b>Pregnancy:</b> {item['Use in pregnancy']}</p>
                <p><b>Side Effects:</b> {item['Side Effects']}</p>
            </div>
            """, unsafe_allow_html=True)

# --- 7. FOOTER ---
st.markdown("""
<footer style="padding:30px;background:#eaf6ff;margin-top:40px;">
    <div>Medi Bot | Mirpur, Dhaka | medibot@gmail.com</div>
</footer>
""", unsafe_allow_html=True)