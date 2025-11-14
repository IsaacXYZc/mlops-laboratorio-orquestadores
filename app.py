import gradio as gr

def translate_text(text, target_language):
    if(text.strip() == ""):
        raise gr.Error("Por favor ingrese un texto para traducir.", duration=6)
    return f"texto traducido:" + text


with gr.Blocks() as demo:
    gr.Markdown("# Laboratorio de orquestadores de contenedores")
    gr.Markdown("## Traductor de texto")

    with gr.Row():
        languaje_selector = gr.Dropdown(
            choices=["Español", "Inglés", "Francés", "Alemán"], 
            label="Selecciona el idioma", 
            value="Español"
        )
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Texto en español", lines=5)
        with gr.Column():
            output_text = gr.Textbox(label="Texto en inglés", lines=5)
        
    with gr.Row():
        button_translate = gr.Button("Traducir")

        button_translate.click(
            fn=translate_text, 
            inputs=[input_text, languaje_selector], 
            outputs=output_text
        )


if __name__ == "__main__":
    demo.launch()