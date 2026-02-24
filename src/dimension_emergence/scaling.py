# scaling.py
class CompactificationRadius:
    """Ω.2 Step 3: R_KK = l_P * ln(2/delta)."""
    def get_radius(self, spectral_gap_delta):
        import math
        return math.log(2 / spectral_gap_delta)
