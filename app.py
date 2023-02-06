import gradio as gr
import openai

openai.api_key = ""

preset_prompts = ["","Act as an encyclopedia.  attempt to explain things ine two levels of increasing completixy", "what does this error mean?"]
models = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]

def process_prompt(prompt):
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        temperature=0.9,
        max_tokens=200
    )
    return response['choices'][0]['text']

def chatbot_interface(input, preset_choice):
    prompt = preset_choice + " " + input
    output = process_prompt(prompt)
    return output

iface = gr.Interface(
    fn=chatbot_interface,
    inputs=[
        #gr.inputs.Dropdown(label="Select Model", choices=models),
        gr.inputs.Dropdown(label="Preset prompt", choices=preset_prompts),
        gr.inputs.Textbox(label="Additional prompt")
        
    ],
    outputs=gr.outputs.Textbox(label="Response")
    )

if __name__ == "__main__":
    iface.launch()
