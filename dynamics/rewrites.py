# dynamics/rewrites.py
class RewriteSemigroup:
    """Axiom A2: Universal Rewrite Dynamics (s -> s')"""
    def is_legal(self, s_old, s_new, engine):
        """The Bit Second Law: Delta E >= 0."""
        return engine.calculate_micro_energy(s_new) >= \
               engine.calculate_micro_energy(s_old)
