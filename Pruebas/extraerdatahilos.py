import threading
# Librerías de terceros
#import environ
import os
import boto3
from botocore.exceptions import NoCredentialsError
import time
from rich import print
from gradio_client import Client
from rich import print
import validarCorreo as correo
import openai

# Función que será ejecutada por cada hilo

client = boto3.client('athena',
    aws_access_key_id='AKIA4JJQAJMFKB3YPMYS',
    aws_secret_access_key='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',
    region_name='us-east-1')
clientIA = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/")

 # Query a ejecutar
        
query_base = f'''
SELECT * FROM "cegid-sql-server-analytics"."user_validated_info" limit 10;
'''    
query = query_base

def traerConsulta():
    
    print("########################## HILO 1 #########################################")
    result2 = clientIA.predict(
    "Capitales de LATAM",	# str  in 'parameter_7' Textbox component
    "",	# str  in 'Optional system prompt' Textbox component
    0.01,	# int | float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component
    4096,	# int | float (numeric value between 0 and 4096) in 'Max new tokens' Slider component
    0.01,	# int | float (numeric value between 0.0 and 1) in 'Top-p (nucleus sampling)' Slider component
    2,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
    api_name="/chat"
    )
    print(result2)


def traerConsulta2():
    print("############################## HILO 2 #####################################")
    result = clientIA.predict(
    "ciudades de latam",	# str  in 'parameter_7' Textbox component
    "",	# str  in 'Optional system prompt' Textbox component
    0.01,	# int | float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component
    4096,	# int | float (numeric value between 0 and 4096) in 'Max new tokens' Slider component
    0.01,	# int | float (numeric value between 0.0 and 1) in 'Top-p (nucleus sampling)' Slider component
    2,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
    api_name="/chat"
    )
    print(result)

# Crear dos hilos
hilo1 = threading.Thread(target=traerConsulta)
hilo2 = threading.Thread(target=traerConsulta2)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Hilos terminados.")
