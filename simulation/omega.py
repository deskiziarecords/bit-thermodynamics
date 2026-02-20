# simulation/omega.py
class FixedPointDetector:
    """Detects the Omega Point where Gamma = 1."""
    def is_at_equilibrium(self, gamma_val):
        return abs(gamma_val - 1.0) < 1e-9
