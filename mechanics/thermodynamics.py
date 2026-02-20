# 
class AlgorithmicThermodynamics:
    """Accounting for Heat, Work, and the Partition Function."""
    def get_partition_function(self, macro_state_S, engine):
        """Gamma(S) = sum(2^-E(s)). Curvature is the gradient of log Gamma."""
        import math
        energies = [engine.calculate_micro_energy(s) for s in macro_state_S]
        return sum(math.pow(2, -e) for e in energies)

    def landauer_cost(self, bits_erased):
        """Erasing 1 bit costs Q >= 1 bit of heat."""
        return bits_erased
