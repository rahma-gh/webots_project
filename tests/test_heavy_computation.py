"""
Tests lourds / calculs intensifs pour démontrer le problème de temps d'exécution
dans l'architecture classique (exécution séquentielle de tous les tests).

Ces tests ne sont PAS lancés automatiquement par défaut.
Utilise -m heavy ou --run-heavy pour les exécuter.
"""

import pytest
import numpy as np
import time

# Option pour activer/désactiver facilement ces tests longs
def pytest_configure(config):
    config.addinivalue_line("markers", "heavy: marque les tests très lourds en calculs")


# ────────────────────────────────────────────────
# Test 1 : Multiplication de très grandes matrices
# ────────────────────────────────────────────────
@pytest.mark.heavy
@pytest.mark.parametrize("size", [1500, 3000, 5000])
def test_heavy_matrix_multiplication(size):
    """
    Multiplication de deux matrices carrées aléatoires de taille N×N.
    Temps approximatif (selon machine) :
    - 1500 → ~2–8 s
    - 3000 → ~10–40 s
    - 5000 → ~40–180 s (souvent >1 min)
    """
    start = time.perf_counter()
    print(f"\n[Heavy] Multiplication matrice {size}×{size} ...")

    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    C = np.dot(A, B)  # opération très coûteuse

    duration = time.perf_counter() - start
    print(f"  → Terminée en {duration:.1f} secondes (shape = {C.shape})")
    assert C.shape == (size, size)


# ────────────────────────────────────────────────
# Test 2 : Estimation de π par Monte-Carlo (beaucoup d'itérations)
# ────────────────────────────────────────────────
@pytest.mark.heavy
@pytest.mark.parametrize("n_points", [10_000_000, 50_000_000, 100_000_000])
def test_monte_carlo_pi(n_points):
    """
    Estimation de π avec la méthode Monte-Carlo (points aléatoires dans un carré).
    Temps approximatif :
    - 10M  → ~3–12 s
    - 50M  → ~15–60 s
    - 100M → ~30–120 s
    """
    start = time.perf_counter()
    print(f"\n[Heavy] Monte-Carlo π avec {n_points:,} points...")

    x = np.random.uniform(-1, 1, n_points)
    y = np.random.uniform(-1, 1, n_points)

    inside = np.sum(x**2 + y**2 <= 1)
    pi_est = 4 * inside / n_points

    duration = time.perf_counter() - start
    print(f"  → π ≈ {pi_est:.6f}   (terminé en {duration:.1f} s)")
    assert 3.0 < pi_est < 3.3


# ────────────────────────────────────────────────
# Test 3 : Chaîne de calculs lourds combinés (plus réaliste CPS)
# ────────────────────────────────────────────────
@pytest.mark.heavy
@pytest.mark.slow
def test_combined_heavy_pipeline():
    """
    Simule une chaîne de traitements lourds qu'on pourrait avoir dans un vrai pipeline CPS :
    - Grande multiplication matricielle
    - FFT sur signal très long
    - Décomposition SVD
    - Calcul statistique sur grand dataset
    """
    start_total = time.perf_counter()
    print("\n[Heavy] Chaîne complète de calculs intensifs...")

    results = []

    # Étape 1 : Matrice 4000×4000
    A = np.random.rand(4000, 4000)
    B = np.random.rand(4000, 4000)
    C = np.dot(A, B)
    results.append(C.trace())

    # Étape 2 : FFT sur 8 millions d'échantillons
    signal = np.random.randn(2**23)  # ~8 millions
    fft_result = np.abs(np.fft.fft(signal)).max()
    results.append(fft_result)

    # Étape 3 : SVD sur matrice 2500×2500
    U, S, Vt = np.linalg.svd(A[:2500, :2500], full_matrices=False)
    results.append(S.sum())

    # Étape 4 : Statistiques sur 50 millions de valeurs
    big_data = np.random.normal(0, 1, 50_000_000)
    results.append(np.mean(big_data) + np.std(big_data))

    duration = time.perf_counter() - start_total
    print(f"  → Chaîne terminée en {duration:.1f} secondes")
    assert all(np.isfinite(r) for r in results)


# ────────────────────────────────────────────────
# Pour tester facilement depuis la ligne de commande
# ────────────────────────────────────────────────
if __name__ == "__main__":
    pytest.main(["-m", "heavy", "-v"])
