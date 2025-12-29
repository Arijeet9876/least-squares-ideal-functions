"""
main.py
Main execution file for Ideal Function Assignment.
"""

from visualization import (
    plot_training_vs_ideal,
    plot_test_assignments,
    plot_deviation_histogram
)
from data_loader import load_csv
from function_matcher import FunctionMatcher
from test_assigner import TestAssigner
from database_handler import DatabaseHandler

# Load datasets
train_df = load_csv(
    "data/train.csv", ["x", "y1", "y2", "y3", "y4"]
)

ideal_df = load_csv(
    "data/ideal.csv", ["x"] + [f"y{i}" for i in range(1, 51)]
)

test_df = load_csv(
    "data/test.csv", ["x", "y"]
)

# Select ideal functions
matcher = FunctionMatcher(train_df, ideal_df)
matches = matcher.find_best_matches()

# Assign test data
assigner = TestAssigner(test_df, train_df, ideal_df, matches)
result_df = assigner.assign()

# Store in database
db = DatabaseHandler("ideal.db")
db.save_dataframe(train_df, "training_data")
db.save_dataframe(ideal_df, "ideal_functions")
db.save_dataframe(result_df, "test_results")

print("Process completed successfully.")
print(result_df.head())

# Visualizations
plot_training_vs_ideal(train_df, ideal_df, matches)
plot_test_assignments(result_df)
plot_deviation_histogram(result_df)
