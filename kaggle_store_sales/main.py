"""Main file."""

from utils.config import Config
from loaders.data_loader import ZipCSVLoader

if __name__ == "__main__":
    # Read config file
    config_file_path = "config/config.toml"
    cfg = Config(config_file=config_file_path)

    # Read zip files
    zip_loader = ZipCSVLoader(cfg)
    extracted_files = zip_loader.extract_zip()
    data_frames = zip_loader.load_csv_files()
