import json
from pathlib import Path
from datetime import datetime


def save_json(data, folder, filename):

    today = datetime.now().strftime("%Y-%m-%d")

    output_dir = (
        Path("data")
        / "raw"
        / today
        / folder
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_dir / filename,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
        )