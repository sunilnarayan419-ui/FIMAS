from hypothesis import given, strategies as st

from fimas.allocation.allocator import allocate_proportionally


@given(
    supply=st.floats(min_value=0, max_value=1e6, allow_nan=False, allow_infinity=False),
    demands=st.dictionaries(
        keys=st.text(min_size=1, max_size=8),
        values=st.floats(min_value=0, max_value=1e6, allow_nan=False, allow_infinity=False),
        max_size=20,
    ),
)
def test_proportional_allocation_never_exceeds_supply(supply: float, demands: dict[str, float]) -> None:
    allocations = allocate_proportionally(supply, demands)
    assert sum(allocations.values()) <= supply + 1e-6
    assert all(value >= 0 for value in allocations.values())
