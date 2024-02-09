import requests

file_path = 'C:/Users/usuario/Downloads/CC17-PCO-03_AnalisisCorreos/thundebird/ccnsqul8.default/Mail/pop-mail.outlook.com'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print(f"El archivo en la ruta '{file_path}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al intentar leer el archivo: {e}")