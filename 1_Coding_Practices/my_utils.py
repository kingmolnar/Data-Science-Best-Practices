import os
import pandas as pd

# example of function currying
# https://python-course.eu/advanced-python/currying-in-python.php

def get_shape_func(DATA_DIR: str):
    """
    Comment
    """

    def get_shape(fp):
        df = pd.read_csv(os.path.join(DATA_DIR, fp))
        return fp, *df.shape

    return get_shape


