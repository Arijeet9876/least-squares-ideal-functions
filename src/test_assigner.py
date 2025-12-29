"""
test_assigner.py
Assigns test points to ideal functions using deviation threshold.
"""

import pandas as pd
import math


class TestAssigner:
    """
    Assigns test data points to ideal functions.
    """

    def __init__(self, test_df, training_df, ideal_df, matches):
        self.test_df = test_df
        self.training_df = training_df
        self.ideal_df = ideal_df
        self.matches = matches

    def assign(self):
        results = []

        for _, test_row in self.test_df.iterrows():
            x_val = test_row["x"]
            y_val = test_row["y"]

            for match in self.matches:
                train_col = match["train_col"]
                ideal_col = match["ideal_col"]

                train_y = self.training_df.loc[
                    self.training_df["x"] == x_val, train_col
                ].values

                ideal_y = self.ideal_df.loc[
                    self.ideal_df["x"] == x_val, ideal_col
                ].values

                if len(train_y) == 0 or len(ideal_y) == 0:
                    continue

                max_dev = abs(train_y[0] - ideal_y[0])
                tolerance = math.sqrt(2) * max_dev
                delta_y = abs(y_val - ideal_y[0])

                if delta_y <= tolerance:
                    results.append({
                        "x": x_val,
                        "y": y_val,
                        "ideal_function": ideal_col,
                        "delta_y": delta_y
                    })

        return pd.DataFrame(results)
