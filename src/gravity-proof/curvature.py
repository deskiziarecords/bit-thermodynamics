# curvature.py
class CurvatureEngine:
    """Axiom 7: Curvature is compression failure."""
    def __init__(self, ensemble_S):
        self.S = ensemble_S

    def get_partition_function(self):
        """Gamma(S) = sum(2^-E(s))"""
        return sum(math.pow(2, -s.energy) for s in self.S)

    def calculate_einstein_tensor(self, spatial_gradient):
        """G_mu_nu = -8pi * grad_mu * grad_nu * log(Gamma)"""
        gamma = self.get_partition_function()
        if gamma <= 0:
            return "SINGULARITY: Proof Density Zero"
        return -G_CONSTANT * spatial_gradient(math.log(gamma))
