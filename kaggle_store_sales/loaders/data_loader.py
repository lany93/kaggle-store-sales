class ZipCSVLoader:
    def __init__(self, config_path: str) -> None:
        """Init class."""
        self.config = self.load_config(config_path)
        self.zip_path = self.config["paths"]["zip_path"]
        self.extract_to = self.config["paths"]["extract_to"]
        self.extracted_files = []
