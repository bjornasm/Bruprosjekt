import os
import shutil

if os.environ.get("QUARTO_PROFILE") == "publish":
    src = os.environ["QUARTO_PROJECT_OUTPUT_DIR"]
    dst = r"\\webedit.ntnu.no\bjornbsm"  # your real target folder
    shutil.copytree(src, dst, dirs_exist_ok=True)
    print(f"Copied {src} -> {dst}")
