import pytest
import os
import json
import subprocess
import time

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")

if os.name == 'nt':
    WEBOTS_PATH = "C:/Program Files/Webots/msys64/mingw64/bin/webots.exe"
else:
    WEBOTS_PATH = "webots"

WORLD_PATH = os.path.abspath("simulation/pick_and_place.wbt")

@pytest.fixture(scope="session", autouse=True)
def run_simulation():
    if os.name != 'nt' and os.path.exists(RESULTS_PATH):
        print(f"\n JSON déjà présent, simulation ignorée.")
        return
    if os.path.exists(RESULTS_PATH):
        os.remove(RESULTS_PATH)
    print(f"\n Lancement simulation Webots...")
    cmd = [WEBOTS_PATH, "--mode=fast", "--batch", "--no-rendering", WORLD_PATH]
    start = time.time()
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        pass
    elapsed = round(time.time() - start, 1)
    print(f"  Simulation terminée en {elapsed}s")

def load_results():
    assert os.path.exists(RESULTS_PATH), "Fichier résultats non trouvé !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)
