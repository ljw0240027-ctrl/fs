from src.scale_calculator import calculate_scale_review


def test_calculate_scale_review():
    data = {
        "site_area_m2": 1000,
        "building_coverage_ratio": 50,
        "floor_area_ratio": 300,
        "max_height_m": 60,
        "floor_height_m": 4,
    }

    result = calculate_scale_review(data)
    assert result.max_building_area_m2 == 500
    assert result.max_gfa_m2 == 3000
    assert result.possible_floor_count == 15
    assert result.average_floor_area_m2 == 200
