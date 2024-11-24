import os
from pathlib import Path

env_file = ".envs/.django"

if not Path(env_file).is_file():
    print(f"Creating {env_file}, please wait...")
    os.makedirs(os.path.dirname(env_file), exist_ok=True)
    with open(env_file, "w") as file:
        file.write(
            """USE_DOCKER=yes
IPYTHONDIR=/app/.ipython
"""
        )
    print(f"{env_file} created!")
else:
    print(f"{env_file} already exists.")
