all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li(color):
	
	return color["sexy"]

filter_colors = filter(generate_li,all_colors)

def generate_li(color):
	return f"<li>{color['label']}</li>"


lista_final=map(generate_li,filter_colors)
print(list(lista_final))