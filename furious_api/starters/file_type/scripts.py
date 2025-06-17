import shutil
from pathlib import Path


def start_file_type_project(base_dir: str) -> None:
    """
    Copia o conteúdo de 'bases' para o diretório atual, renomeando a pasta 'app' para o nome informado,
    e atualizando os imports nos arquivos Python.

    Args:
        base_dir (str): Nome para renomear a pasta 'app' e atualizar os imports.
    """
    source = Path("furious_api/starters/file_type/bases")
    destination = Path.cwd()

    for item in source.iterdir():
        if item.name == "app" and item.is_dir():
            # Renomeia a pasta 'app' para o nome fornecido
            shutil.copytree(item, destination / base_dir, dirs_exist_ok=True)
        else:
            # Copia arquivos e outras pastas normalmente
            target = destination / item.name
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                shutil.copy2(item, target)

    # Substitui os imports nos arquivos .py
    for file_path in destination.rglob("*.py"):
        with file_path.open("r", encoding="utf-8") as file:
            content = file.read()

        # Atualiza importações de 'from django_melhor' e 'import django_melhor'
        updated_content = content.replace("from django_melhor", f"from {base_dir}")
        updated_content = updated_content.replace("import django_melhor", f"import {base_dir}")

        with file_path.open("w", encoding="utf-8") as file:
            file.write(updated_content)
