import io
import pandas as pd
import json
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://remotive.com/api/remote-jobs'

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
