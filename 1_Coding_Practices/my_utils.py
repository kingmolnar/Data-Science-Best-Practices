import os
import pandas as pd

# example of function currying
# https://python-course.eu/advanced-python/currying-in-python.php

def get_shape_func(DATA_DIR, print_messages=False):

    def get_shape(fp):
        if print_messages:
            print(f"Processing file: {fp}")
        df = pd.read_csv(os.path.join(DATA_DIR, fp))
        return fp, *df.shape

    return get_shape


