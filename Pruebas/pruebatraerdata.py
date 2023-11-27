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
clientIA = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/6q8kt/")

start_time = time.time()

# Crear una instancia de la clase Env
#env = environ.Env()

# Lee el archivo .env en el entorno
#environ.Env.read_env()

client = boto3.client('athena',
    aws_access_key_id='AKIA4JJQAJMFKB3YPMYS',
    aws_secret_access_key='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',
    region_name='us-east-1')


  # Query a ejecutar

for j in range(0,10):
    
    query_base = f'''
    SELECT * FROM "cegid-sql-server-analytics"."user_validated_info" limit 10;
    '''    
    query = query_base

    response = client.start_query_execution(
                QueryString=query,
                QueryExecutionContext={
                    'Database': 'cegid-sql-server-analytics'},
                ResultConfiguration={
                    'OutputLocation':'s3://lilipink-0000-base-poctst-00-analytics/'
                }
            )
    query_execution_id = response['QueryExecutionId']

    # Obtener los resultados de la consulta
    while True:
        response = client.get_query_execution(
        QueryExecutionId=query_execution_id)
        state = response['QueryExecution']['Status']['State']
    
        if state == 'SUCCEEDED':
            data = client.get_query_results(
            QueryExecutionId=query_execution_id)
    
            # Inicializa un diccionario para almacenar los datos formateados
            formatted_data = {}

            # Obtiene la lista de nombres de columna del primer registro
            column_names = [item["VarCharValue"] for item in data["ResultSet"]["Rows"][0]["Data"]]
    
            dataFinal=[];
            correos=[];
            
            for row_data in data["ResultSet"]["Rows"][1:]:
                # Crea un diccionario para almacenar los datos de este registro
                row = {}
                    
                # Itera sobre los datos de este registro y asigna a las columnas correspondientes
                for i, cell_data in enumerate(row_data["Data"]):
                    column_name = column_names[i]
                    cell_value = cell_data["VarCharValue"]
                    row[column_name] = cell_value
                    
                dataFinal.append(row)
            break;

    for i in range(0,len(dataFinal)):
        
        correos.append(dataFinal[i]['email'])

    print(correos)
    """
    openai.api_key = "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"
    for i in range(0,len(correos)):
        
        response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=" Este formato de  correo "+correos[i] +" es valido,tiene un rango entre 6 y 30 caracteres?.Responde solo si o no sin explicaciones con una sola palabra,si no cumple el rango  de caracteres automaticamente di que no"
        )
        print(i,"--"+response["choices"][0]["text"])
        print(i," "+ correos[i]," --",correo.validar_correo(correos[i]))
        time.sleep(10)
    """
    #METODO GRATIS


    for i in range(0,len(correos)):
        prompt= "Este correo: "+correos[i] +"'"+"es valido adicionalmente tiene un rango entre 6 y 30 caracteres?.Responde solo si o no sin explicaciones con una sola palabra,si no ccumple el rango de caracteres automaticamente di que no."
        result = clientIA.predict(
                prompt,	# str  in 'parameter_7' Textbox component
                "",	# str  in 'Optional system prompt' Textbox component
                0.01,	# int | float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component
                256,	# int | float (numeric value between 0 and 4096) in 'Max new tokens' Slider component
                0.01,	# int | float (numeric value between 0.0 and 1) in 'Top-p (nucleus sampling)' Slider component
                1.2,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
                api_name="/chat"
        )
        print(i,"-"+result)#+"--"+correos[i])
        #print(i," "+ correos[i]," --",correo.validar_correo(correos[i]))
        time.sleep(0.5)

# Código que deseas medir
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo transcurrido: {elapsed_time} segundos")
print(f"Tiempo transcurrido: {elapsed_time/60} Minutos")