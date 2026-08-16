import os
import subprocess

# Ruta local de tu repo
repo_path = r"C:\Users\karla\HEX-GITHUB"

# URL de tu repo remoto en GitHub
remote_url = "https://github.com/resendizkarlakaren/HEX.git"

def run_cmd(cmd, cwd=None):
    """Ejecuta un comando en PowerShell y muestra salida."""
    result = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)

def main():
    # Cambiar a carpeta del repo
    os.chdir(repo_path)

    # Inicializar git si no existe
    run_cmd("git init")

    # Agregar remoto (si no existe ya)
    run_cmd(f"git remote add origin {remote_url}")

    # Agregar todos los archivos
    run_cmd("git add .")

    # Commit inicial
    run_cmd('git commit -m "chore: initial HEX structure upload"')

    # Configurar branch principal
    run_cmd("git branch -M main")

    # Push al remoto
    run_cmd("git push -u origin main")

if __name__ == "__main__":
    main()




