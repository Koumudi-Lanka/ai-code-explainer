# AI Code Explainer

**AI Code Explainer** is a Python project that uses **AI models** to analyze and explain Python code in a **clear, human-readable way**. This project demonstrates hands-on experience with **AI code understanding** and interactive interfaces.

---

## 🔹 Features

- Explains Python code **line by line** using AI.  
- Interactive **Gradio interface** for inputting Python code.  
- Helps beginners and developers **understand complex Python code**.  
- Lightweight and runs locally without heavy setup.  

---

## 🔹 Tools & Technologies Used

- **Python 3.x** – Core programming language.  
- **CodeT5 (Hugging Face)** – Pre-trained AI model used to understand Python code.  
- **Gradio** – Web interface to interact with the AI model.  
- **Git & GitHub** – Version control and project hosting.  

---

## 🔹 How I Built It

1. Used **CodeT5** to generate explanations for Python code.  
2. Built a **Gradio interface** for users to input Python code and get explanations instantly.  
3. Organized project files properly and **excluded `venv` and unnecessary files** from GitHub to reduce repo size.  
4. Managed version control with **Git** and hosted the project on **GitHub**.  

---

## 🔹 Project Structure

AI-CODE-EXPLAINER/
│
├── app.py                 # Main Python script to run the AI Code Explainer
├── requirements.txt       # Python packages needed for the project
├── README.md              # This project documentation
└── .gitignore             # To ignore venv and other unnecessary files

## 🔹 How to Run the Project

```bash
# Clone the repo
git clone https://github.com/Koumudi-Lanka/ai-code-explainer.git
cd ai-code-explainer

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

