from src.program_generator import generate_program_table


def test_generate_program_table_normalized():
    data = {
        "target_programs": [
            {"name": "A", "ratio": 70},
            {"name": "B", "ratio": 30},
        ]
    }

    rows = generate_program_table(data, 1000)
    assert len(rows) == 2
    assert rows[0]["area_m2"] == 700
    assert rows[1]["area_m2"] == 300
