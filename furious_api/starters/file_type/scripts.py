import shutil
from pathlib import Path


def start_file_type_project(base_dir: str) -> None:
    """
    Cria uma estrutura base de projeto FastAPI.

    Args:
        base_dir (str): Nome do diretório base do projeto (e prefixo para os imports).
        base_template_dir (str): Diretório contendo os arquivos base (padrão: 'bases').
    """
    source = Path("furious_api/starters/file_type/bases")
    destination = Path(base_dir)


    # Copia a estrutura de diretórios e arquivos
    shutil.copytree(source, destination, dirs_exist_ok=True)

    # Substitui os imports dentro dos arquivos copiados
    for file_path in destination.rglob("*.py"):
        with file_path.open("r", encoding="utf-8") as file:
            content = file.read()

        # Substituir 'app.' pelo nome do projeto (base_dir)
        updated_content = content.replace("from app", f"from {base_dir}")

        with file_path.open("w", encoding="utf-8") as file:
            file.write(updated_content)
