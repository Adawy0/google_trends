import json
import pandas as pd


def convert_queryset_to_json(qs):
    df = pd.DataFrame(list(qs))
    result = df.to_json()
    return json.loads(result)