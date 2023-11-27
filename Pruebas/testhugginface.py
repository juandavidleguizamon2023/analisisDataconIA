import time
from rich import print
from gradio_client import Client
import validarCorreo as correo


clientIA = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/")

prompt="['vanessaamariz@gmail.com', 'carolinarpo1905@gmail.com','jenniferba22@hotmail.com','estellysami05@gmail.com','jasminsoje@gmail.com','','carolinasanchez2809@hotmail.com','danval1410@gmail.com','','virna.andrade@gmail.com'] /n dame una lista  respondiendo si los correos son validos adicionalmente tiene un rango entre 6 y 30 caracteres?.Responde solo si o no sin explicaciones con una sola palabra,si no ccumple el rango de caracteres automaticamente di que no. Solo dame  la lista sin ninguna explicacion adicional"

result = clientIA.predict(
            prompt,	# str  in 'parameter_7' Textbox component
            "",	# str  in 'Optional system prompt' Textbox component
            0.01,	# int | float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component
            4096,	# int | float (numeric value between 0 and 4096) in 'Max new tokens' Slider component
            0.01,	# int | float (numeric value between 0.0 and 1) in 'Top-p (nucleus sampling)' Slider component
            2,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
            api_name="/chat"
    )

print(result)

