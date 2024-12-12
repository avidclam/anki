from pathlib import Path
from src.config import load_config
from src.ingest import load_dataset
from src.design import load_design


def main(top_dir: Path, output_dir: Path = None) -> str | None:
    config_dir = top_dir / "config"
    config_file = config_dir / "config.toml"
    design_dir = top_dir / "design"
    if not output_dir:
        output_dir = top_dir / "output"
    # Load configuration
    cfg = load_config(config_file)
    # Load Dataset
    df = load_dataset(cfg)
    # Load design
    design = load_design(design_dir)
    return None
