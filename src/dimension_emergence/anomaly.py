# anomaly.py
class AnomalyCanceller:
    """Axiom Ω.2: Unitarity requires c_tot = 0."""
    def calculate_central_charge(self, spatial_dims):
        """c_tot = c_graviton + c_ghosts + c_matter"""
        matter_charge = spatial_dims * MATTER_DOF_PER_SLICE
        return GRAVITON_CHARGE + GHOST_CHARGE + matter_charge

    def is_stable(self, spatial_dims):
        """Returns True if c_tot == 0."""
        return self.calculate_central_charge(spatial_dims) == 0
