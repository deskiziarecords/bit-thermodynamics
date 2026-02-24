# metrics.py
class MetricSignature:
    """Ensures Lorentzian signature based on the c-bound."""
    def enforce_signature(self, entropy_flow):
        """Axiom 3.4: Time is the direction of residue decrease."""
        if entropy_flow > 0:
            return "Lorentzian (-+++)"
        return "Unstable Geometry"
