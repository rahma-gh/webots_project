import os
import pytest

def test_reports_directory_exists():
    assert os.path.exists("reports"), "Dossier reports manquant !"
    print(" Dossier reports présent")
