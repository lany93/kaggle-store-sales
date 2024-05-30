"""Config class."""

import toml
import logging


class Config:
    def __init__(self, config_file):
        # Load and parse the config.toml file
        self._config = self._parse_config(config_file)

        # Dynamically set attributes based on the config file
        logging.info("Read config.toml file.")
        self._set_attributes()

    def _parse_config(self, config_file):
        """Load and parse the TOML configuration file."""
        return toml.load(config_file)

    def _set_attributes(self):
        """Dynamically set attributes based on the parsed configuration."""
        for section, settings in self._config.items():
            for key, value in settings.items():
                setattr(self, f"{section}_{key}", value)

    def get(self, section, key, default=None):
        """Get a specific configuration value with a default."""
        return getattr(self, f"{section}_{key}", default)
