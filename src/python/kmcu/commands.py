from . import KMCU
from pathlib import Path
import json


def build_metadata():
    kmcu = KMCU(basedir=Path("."))
    mcus = kmcu.build_metadata()
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    with (output_dir / "kconfigs.json").open("w") as out_json:
        json.dump([m.to_dict() for m in mcus], out_json, indent=2)






