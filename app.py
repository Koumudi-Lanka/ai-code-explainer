
import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load Salesforce CodeT5 model
model_name = "Salesforce/codet5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def explain_and_run(code):
    prompt = f"""
Explain the following Python code in simple English.

Code:
{code}
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150
    )

    explanation = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Code execution is disabled for safety
    output = "Execution disabled for safety"

    return explanation, output


interface = gr.Interface(
    fn=explain_and_run,
    inputs=gr.Textbox(
        lines=12,
        label="Paste Your Python Code"
    ),
    outputs=[
        gr.Textbox(label="AI Code Explanation"),
        gr.Textbox(label="Program Output")
    ],
    title="AI Code Explainer (CodeT5)",
    description=(
        "Paste Python code. The AI explains it in simple English. "
        "(Execution disabled for safety)"
    )
)

interface.launch()
