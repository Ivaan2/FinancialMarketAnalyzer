import subprocess
import sys
import os

# Ruta al directorio raíz del paquete
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, "src")

# Ejecutar el módulo main como paquete
command = [sys.executable, "-m", "src.main"]

print(f"Ejecutando: {' '.join(command)}\n")
subprocess.run(command, cwd=project_root)
