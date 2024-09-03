from dataclasses import dataclass
from pathlib import Path

"""
    Creates a structured class for storing data, the dataclass provides an in built __init__() constructor to classes which handle the data and object creation for them.
"""

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path