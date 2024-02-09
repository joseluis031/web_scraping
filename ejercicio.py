from bs4 import BeautifulSoup

def leer_contenido_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        return file.read()

def encontrar_matricula(soup):
    # Encontrar la línea que contiene la matrícula
    matricula_line = [line for line in soup.get_text().split('\n') if 'Matricula' in line]

    if matricula_line:
        # Extraer la matrícula
        matricula = matricula_line[0].split(':')[-1].strip()
        return matricula
    else:
        return None

def main():
    # Ruta del archivo 'Inbox'
    ruta_inbox = 'Inbox'

    # Leer el contenido del archivo
    inbox_content = leer_contenido_archivo(ruta_inbox)

    # Parsear el contenido del archivo con BeautifulSoup
    soup = BeautifulSoup(inbox_content, 'html.parser')

    # Encontrar la matrícula
    matricula = encontrar_matricula(soup)

    if matricula:
        print("Matrícula encontrada:", matricula)
    else:
        print("No se encontró la matrícula")

if __name__ == "__main__":
    main()
