from pathlib import Path

from src.report.report_builder import generate_report

def test_report_generation():

    path = generate_report("600159", "Moutai", output_dir="tests/unit/test_output")
    assert Path(path).exists(), "Report file was not created"
    assert "Moutai" in path, "Report file name does not contain the stock name"
    