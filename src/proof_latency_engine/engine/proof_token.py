# engine/proof_token.py
class ProofToken:
    """Axiom 3.2: The certificate sigma(t) required for residue drops."""
    def __init__(self, energy_bits: int, origin: tuple):
        self.payload = energy_bits
        self.origin = origin
        self.birth_time = None

    def travel_time(self, destination: tuple):
        """Theorem 3.1: delta_t >= distance / c."""
        from math import dist
        return dist(self.origin, destination) / C_LOGIC
