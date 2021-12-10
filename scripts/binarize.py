import pandas as pd
import numpy as np

def binarize_treatment(df, treat):
    new_df = df.copy()
    new_df[treat] = (df[treat] >= np.median(df[treat])).astype(int)
    return new_df
    