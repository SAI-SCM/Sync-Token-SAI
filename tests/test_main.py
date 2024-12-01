import subprocess

def test_main():
    # Rulează scriptul principal și capturează ieșirea
    result = subprocess.run(["python", "app/main.py"], capture_output=True, text=True)
    output_lines = result.stdout.strip().split("\n")

    # Verificăm fiecare linie separat
    assert output_lines[0] == "Bun venit în SAI-SCM!", "Testul a eșuat la mesajul principal!"
    assert output_lines[1] == "SAI-SCM este pregătit pentru testare și extindere!", "Testul a eșuat la mesajul secundar!"
