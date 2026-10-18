from fimas.api.schemas import AllocationRequest, HealthResponse


def test_health_response_default() -> None:
    assert HealthResponse().status == "ok"


def test_allocation_request_accepts_nonnegative_supply() -> None:
    request = AllocationRequest(supply=3, demands={"node-a": 2})
    assert request.supply == 3
