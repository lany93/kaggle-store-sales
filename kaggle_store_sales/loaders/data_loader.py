"""Zip to csv class."""

import zipfile
import os
import pandas as pd
import logging


class ZipCSVLoader:
    def __init__(self, config_path: str) -> None:
        """Init class."""
        self.config = config_path
        self.zip_path = self.config.paths_zip_path
        self.extract_to = self.config.paths_extract_to
        self.extracted_files = []

    def extract_zip(self):
        """Extracts the zip file to the specified directory."""
        logging.info("Extract zip file.")
        with zipfile.ZipFile(self.zip_path, "r") as zip_ref:
            zip_ref.extractall(self.extract_to)
            self.extracted_files = zip_ref.namelist()
        return self.extracted_files

    def load_csv_files(self):
        """Loads all CSV files from the extracted directory into a dictionary of DataFrames."""
        logging.info("Extract csv to pandas dataframe.")
        data_frames = {}
        for file_name in self.extracted_files:
            if file_name.endswith(".csv"):
                file_path = os.path.join(self.extract_to, file_name)
                data_frames[file_name] = pd.read_csv(file_path)
        return data_frames

    def clean_up(self):
        """Removes the extracted files and directory."""
        logging.info("Removing extracted data files.")
        for file_name in self.extracted_files:
            file_path = os.path.join(self.extract_to, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
        if os.path.exists(self.extract_to):
            os.rmdir(self.extract_to)
