import pytest
from render import transparency_oit as mod

CASES = [
    ("weight_near", "m.depth_weight(0.0, 1.0) == approx(1.0)"),
    ("weight_far", "m.depth_weight(1.0, 1.0) == approx(0.5)"),
    ("depth_test_on", "m.depth_test(True) is True"),
    ("depth_test_off", "m.depth_test(False) is False"),
    ("transmission_sum", "m.combine_transmission((1.0, 2.0), (3.0, 4.0)) == (4.0, 6.0)"),
    ("particle_far_first", "m.particle_order([1.0, 3.0, 2.0]) == [3.0, 2.0, 1.0]"),
    ("store_pair", "m.store_rgba_depth((1.0, 2.0, 3.0, 4.0), 5.0) == ((1.0, 2.0, 3.0, 4.0), 5.0)"),
    ("msaa_average", "m.resolve_msaa([(0.0, 0.0), (2.0, 2.0)]) == approx((1.0, 1.0))"),
    ("capture_current", "m.capture_frame('current', 'previous') == 'current'"),
    ("weights_sum", "sum(m.normalize_weights([2.0, 2.0])) == approx(1.0)"),
    ("weights_half", "m.normalize_weights([2.0, 2.0])[0] == approx(0.5)"),
    ("stereo_left", "m.stereo_buffer(0) == 0"),
    ("stereo_right", "m.stereo_buffer(1) == 1"),
    ("weight_zero", "m.depth_weight(0.0, 4.0) == approx(1.0)"),
    ("particle_single", "m.particle_order([2.0]) == [2.0]")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
