from pathlib import Path
import importlib.util
import sys

# Importa bd.py da pasta functions_bd
base_dir = Path(__file__).resolve().parent
bd_path = base_dir / "functions_bd" / "bd.py"

_spec = importlib.util.spec_from_file_location("bd", bd_path)
bd = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = bd
_spec.loader.exec_module(bd)

# Agora você pode usar bd.app ou bd.get_data() se precisar
if __name__ == "__main__":
    bd.app.run(host="localhost", port=5000, debug=True)
