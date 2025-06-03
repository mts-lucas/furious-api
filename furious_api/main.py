import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script com um argumento posicional obrigatório.")
    parser.add_argument("project_name", type=str, help="Nome do projeto, primeiro argumento posicional obrigatório.")
    args = parser.parse_args()
    
    from starters import start_file_type_project
    start_file_type_project(base_dir=args.project_name)