import subprocess
from app.main import calculate_sum
from app.utils.string_utils import reverse_string

def test_main():
    result = subprocess.run(["python", "app/main.py"], capture_output=True, text=True)
    output_lines = result.stdout.strip().split("\n")
    assert output_lines[0] == "Bun venit în SAI-SCM!"
    assert output_lines[1] == "SAI-SCM este pregătit pentru testare și extindere!"
    assert "Rezultatul sumei este: 12" in output_lines
    assert "Text inversat: MCS-IAS" in output_lines

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(-1, 1) == 0

def test_reverse_string():
    assert reverse_string("SAI-SCM") == "MCS-IAS"
    assert reverse_string("Python") == "nohtyP"
