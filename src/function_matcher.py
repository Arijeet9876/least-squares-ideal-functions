"""
function_matcher.py
Selects best ideal functions using least squares.
"""

import numpy as np


class FunctionMatcher:
    """
    Matches training functions to ideal functions
    using sum of squared deviations.
    """

    def __init__(self, training_df, ideal_df):
        self.training_df = training_df
        self.ideal_df = ideal_df

    def find_best_matches(self):
        """
        Find best ideal function for each training function.

        Returns:
            list of dicts
        """
        matches = []

        for i in range(1, 5):
            train_col = f"y{i}"
            best_func = None
            min_error = float("inf")

            for j in range(1, 51):
                ideal_col = f"y{j}"
                error = np.sum(
                    (self.training_df[train_col] - self.ideal_df[ideal_col]) ** 2
                )

                if error < min_error:
                    min_error = error
                    best_func = ideal_col

            matches.append({
                "train_col": train_col,
                "ideal_col": best_func,
                "error": min_error
            })

        return matches
