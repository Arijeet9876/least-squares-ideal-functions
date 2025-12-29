"""
visualization.py
Creates plots for training data, ideal functions, and test assignments.
"""

import matplotlib.pyplot as plt


def plot_training_vs_ideal(training_df, ideal_df, matches):
    """
    Plot each training function against its selected ideal function.
    """
    _, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for i, match in enumerate(matches):
        train_col = match["train_col"]
        ideal_col = match["ideal_col"]

        axes[i].plot(
            training_df["x"],
            training_df[train_col],
            label=f"Training {train_col}",
            marker="o",
            linestyle=""
        )
        axes[i].plot(
            ideal_df["x"],
            ideal_df[ideal_col],
            label=f"Ideal {ideal_col}",
            linestyle="--"
        )

        axes[i].set_title(f"{train_col} vs {ideal_col}")
        axes[i].set_xlabel("x")
        axes[i].set_ylabel("y")
        axes[i].legend()

    plt.tight_layout()
    plt.show()


def plot_test_assignments(test_results):
    """
    Plot assigned test points colored by ideal function.
    """
    plt.figure(figsize=(10, 6))

    for ideal_func in test_results["ideal_function"].unique():
        subset = test_results[test_results["ideal_function"] == ideal_func]
        plt.scatter(
            subset["x"],
            subset["y"],
            label=ideal_func,
            s=30
        )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Test Data Assignments")
    plt.legend()
    plt.show()


def plot_deviation_histogram(test_results):
    """
    Plot histogram of deviation values.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(test_results["delta_y"], bins=30)
    plt.xlabel("Deviation (Δy)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Test Data Deviations")
    plt.show()
