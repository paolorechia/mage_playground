import io
import pandas as pd
import json
import requests
from software_jobs.utils.path_utils import remotive_file_exists, get_today_remotive_path
import logging
from mage_ai.io.file import FileIO

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    logger = logging.getLogger(__name__)
    url = 'https://remotive.com/api/remote-jobs'

    if remotive_file_exists():
        logger.info("Skipping pull")
        return FileIO().load(get_today_remotive_path())

    logger.info("File %s not found, pulling from API", get_today_remotive_path())
    response = requests.get(url)
    jobs = response.json()["jobs"]
    jobs_json = json.dumps(jobs)
    return pd.read_json(io.StringIO(jobs_json))

@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
