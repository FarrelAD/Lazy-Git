from pathlib import Path
from datetime import datetime
import subprocess

script_dir = Path(__file__).resolve().parent
text_path = script_dir / "text.txt"

with text_path.open("a", encoding="utf-8") as file:
    file.write("lazy git\n")

subprocess.run(["git", "add", "."], cwd=script_dir, check=True)
subprocess.run(["git", "commit", "-m", f"push commit change at {datetime.now()}"], cwd=script_dir, check=True)
subprocess.run(["git", "push"], cwd=script_dir, check=True)
