from gradio_client import Client
from rich import print
client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/--replicas/ppt5s/")
result = client.predict(
		"Este formato de correo es valido? juandapilo@gmail.com responde solamente si o no,sin explicaciones ",	# str  in 'parameter_7' Textbox component
		"",	# str  in 'Optional system prompt' Textbox component
		0.9,	# int | float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component
		256,	# int | float (numeric value between 0 and 4096) in 'Max new tokens' Slider component
		0.6,	# int | float (numeric value between 0.0 and 1) in 'Top-p (nucleus sampling)' Slider component
		1.2,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
		api_name="/chat"
)
print(result)