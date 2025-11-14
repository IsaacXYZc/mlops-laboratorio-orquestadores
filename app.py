import gradio as gr
import mlflow
import provider.gemini_provider as translator
from dotenv import load_dotenv
import os
import time

load_dotenv(override=True)
mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

def translate_text(text, target_language):
    if(text.strip() == ""):
        raise gr.Error("Por favor ingrese un texto para traducir.", duration=6)
    
    start_time = time.perf_counter()
    output_text = translator.get_traduction(text, target_language)
    end_time = time.time()
    latency = end_time - start_time

    mlflow.set_tracking_uri(mlflow_tracking_uri)
    mlflow.set_experiment("text-translator-experiment")
    with mlflow.start_run():
        # Log de los parametros
        mlflow.log_param("target_language", target_language)
        mlflow.log_param("model", translator.model_name)

        # Log de las métricas
        mlflow.log_metric("latency", latency)
        mlflow.log_metric("input_text_length", len(text))
        mlflow.log_metric("output_text_length", len(output_text))

        # Log de los artefactos
        mlflow.log_text(text, "input_text.txt")
        mlflow.log_text(output_text, "output_text.txt")
    
    return output_text  


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