from fimas.physics.conservation import conservation_error


def test_mass_balance_residual_zero_for_balanced_node() -> None:
    assert conservation_error(inflow=10, outflow=7, accumulation=3) == 0
