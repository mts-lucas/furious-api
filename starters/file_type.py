from pathlib import Path


def start_file_type_project(base_dir: str) -> None:
    """
    Cria a estrutura de diretórios e arquivos para um projeto FastAPI.
    
    Args:
        base_dir (str): Nome do diretório base do projeto (padrão: "app").
    """
    # Estrutura de diretórios e arquivos
    structure = {
        base_dir: [
            "__init__.py",
            "main.py",
            "dependencies.py",
            Path("routers") / "__init__.py",
            Path("crud") / "__init__.py",
            Path("schemas") / "__init__.py",
            Path("models") / "__init__.py",
            Path("utils") / "__init__.py",
            Path("utils") / "authentication.py",
            Path("utils") / "validation.py",
            Path("utils") / "pagination.py",
        ],
        "tests": [
            "__init__.py",
            "test_main.py",
        ],
        ".": [
            ".gitignore",
            "README.md",
        ]
    }

    for directory, files in structure.items():
        dir_path = Path(directory)
        dir_path.mkdir(exist_ok=True, parents=True)
        
        for file in files:
            file_path = dir_path / file
            # Garante que o diretório pai existe
            file_path.parent.mkdir(exist_ok=True, parents=True)
            # Cria o arquivo se não existir
            file_path.touch(exist_ok=True)
