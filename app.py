
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(page_title="AI Code Explainer", page_icon="💻")

@st.cache_resource
def load_model():
    model_name = "Salesforce/codet5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

st.title("💻 AI Code Explainer")
st.write("Paste Python code to get a simple English explanation.")

try:
    tokenizer, model = load_model()

    code = st.text_area("Paste your Python code", height=250)

    if st.button("Explain Code"):
        if code.strip():
            prompt = (
                "Explain the following Python code in simple English.\n\n"
                f"Code:\n{code}"
            )
            inputs = tokenizer(
                prompt, return_tensors="pt", truncation=True
            )
            outputs = model.generate(**inputs, max_new_tokens=150)
            explanation = tokenizer.decode(
                outputs[0], skip_special_tokens=True
            )
            st.subheader("AI Code Explanation")
            st.write(explanation)
            st.info("Program execution is disabled for safety.")
        else:
            st.warning("Please enter some Python code.")

except Exception as e:
    st.error("The model could not be loaded.")
    st.caption(f"Technical details: {e}")
