import os


class Config:
    """
    Configuration class for managing environment variables.
    """

    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    DATABASE_URL = os.environ["DATABASE_URL"]


class Routes:
    """
    Class representing the routes used in the application.
    """

    QUERY = "/consulta"
