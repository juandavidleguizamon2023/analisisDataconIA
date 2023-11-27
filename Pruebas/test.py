from gradio_client import Client

client = Client("https://huggingface-projects-llama-2-13b-chat.hf.space/--replicas/vvqcp/")
result = client.predict(
		" dime cual es la Capital de francia?",	# str  in 'Message' Textbox component
		"",	# str  in 'System prompt' Textbox component
		1,	# int | float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
		0.1,	# int | float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
		0.05,	# int | float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
		1,	# int | float (numeric value between 1 and 1000) in 'Top-k' Slider component
		1,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
		api_name="/chat"
)
print(result)