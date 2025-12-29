"""
database_handler.py
Stores results in SQLite database using SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


class DatabaseHandler:
    """
    Handles SQLite database storage using SQLAlchemy.
    """

    def __init__(self, db_path="ideal.db"):
        # SQLAlchemy engine (required by assignment)
        self.engine = create_engine(f"sqlite:///{db_path}")

    def save_dataframe(self, df, table_name):
        """
        Save a pandas DataFrame to a SQLite table.
        Uses a raw DBAPI connection for pandas compatibility.
        """
        try:
            # Get DBAPI connection from SQLAlchemy engine
            raw_conn = self.engine.raw_connection()
            try:
                df.to_sql(
                    table_name,
                    con=raw_conn,
                    if_exists="replace",
                    index=False
                )
            finally:
                raw_conn.close()
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database write failed: {e}") from e
