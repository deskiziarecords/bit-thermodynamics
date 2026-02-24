# engine/latency_gate.py
class CausalLatencyGate:
    """Enforces the 'No-Superluminal-Residue-Drop' Principle."""
    def __init__(self, coord: tuple, current_residue: float):
        self.coord = coord
        self.R = current_residue # Normalized proof distance [14]
        self.history = []

    def request_actualization(self, target_residue: float, current_time: float, tokens: list):
        """Axiom A4: Only actualize if enough proof bits have arrived."""
        delta_R = self.R - target_residue
        available_bits = sum(t.payload for t in tokens if t.birth_time + t.travel_time(self.coord) <= current_time)
        
        if available_bits >= delta_R:
            self.R = target_residue
            return True # State change "proven"
        return False # "Latency Error": Proof pending
