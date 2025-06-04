import argparse
import re
from furious_api.starters import start_file_type_project

def main():
    parser = argparse.ArgumentParser(description="CLI para iniciar projeto FastAPI.")
    parser.add_argument("command", type=str, help="Comando, por ex: startapp")
    parser.add_argument("project_name", type=str, help="Nome do projeto")
    args = parser.parse_args()

    pattern = r"^[a-z]+(_[a-z]+)*$"
    if not re.match(pattern, args.project_name):
        print("Nome do projeto inválido! Use apenas letras minúsculas e underscores (_) para separar palavras.")
        exit(1)

    if args.command == "startapp":
        start_file_type_project(base_dir=args.project_name)
    else:
        print(f"Comando desconhecido: {args.command}")
        exit(1)

if __name__ == "__main__":
    main()
