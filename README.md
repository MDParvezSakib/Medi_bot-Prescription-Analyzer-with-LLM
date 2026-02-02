# 🩺 Medi-bot: Prescription Analyzer with LLM

Medi-bot is an AI-powered intelligent prescription reader that helps users understand medical prescriptions easily. It extracts medicine names from prescription images using OCR and generates clear, user-friendly medical descriptions using Large Language Models (LLMs).

---

## 🚀 Features
- 📷 Upload handwritten or printed prescription images
- 🔍 Extract medicine names using OCR
- 🤖 Generate simplified medical descriptions using LLM
- 📄 Show medicine purpose, usage, and possible side effects
- 🌐 Web-based interface (easy to use)

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Framework:** Flask / Streamlit  
- **OCR:** EasyOCR  
- **AI Models:** Transformer-based LLM  
- **Database:** JSON-based medicine dataset  
- **Frontend:** HTML, CSS  

---

## 📌 System Workflow
1. User uploads a prescription image  
2. Image preprocessing is applied  
3. OCR extracts medicine names  
4. Extracted data is matched with medicine database  
5. LLM generates readable medical descriptions  
6. Results are displayed on the web interface  

---

## 🖼️ User Interface Preview

### 🔹 Prescription Upload Interface
![Prescription Upload UI](images/ui_upload.png)

### 🔹 Generated Medicine Description Output
![Generated Output UI](images/ui_output.png)

> 📁 **Note:** Place your screenshots inside an `images/` folder and rename them as:
> - `ui_upload.png`
> - `ui_output.png`

---

## 🧠 Generated Output Details
For each detected medicine, Medi-bot generates:
- ✅ Medicine name
- ✅ Purpose of the medicine
- ✅ How and when to take it
- ✅ Possible side effects (basic level)
- ✅ Easy-to-understand language for non-technical users

This helps patients avoid confusion caused by handwritten prescriptions or medical abbreviations.

---

## ⚙️ How to Run the Project

```bash
# Clone the repository
git clone https://github.com/your-username/Medi-bot-Prescription-Analyzer-with-LLM.git

# Navigate to project directory
cd Medi-bot-Prescription-Analyzer-with-LLM

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
