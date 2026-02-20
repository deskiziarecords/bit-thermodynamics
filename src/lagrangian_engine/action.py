# action.py
class UniversalAction:
    """The Single Lagrangian S = Integral(dt(L_matter - lambda(proof_bound)))"""
    def __init__(self, speed_limit=1.0):
        self.c = speed_limit

    def calculate_action(self, trajectory, lambda_multiplier):
        """Axiom 2.1: Extremization of S."""
        # Integrates <nabla psi, psi_dot> - lambda(|sigma_dot|^2 - c^2)
        pass

    def variation_wrt_lambda(self, sigma_dot):
        """Enforces |sigma_dot|^2 = c^2 constraint."""
        return abs(sigma_dot**2 - self.c**2)
