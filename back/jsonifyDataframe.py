"""
Component that takes a DataFrame from the analyzer and converts it to json
The json is then passed to the server to it can be displayed.
"""

import pandas as pd
import numpy as np
import json

def createJsonFromDataframe(df):
    dfJsonObject = json.loads(df.to_json())
    
    for state in dfJsonObject:
        print(state, dfJsonObject[state])
        
    return dfJsonObject