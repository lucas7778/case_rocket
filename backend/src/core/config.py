import os


class Config:
    """
    Configuration class for managing environment variables.
    """

    POSTGRES_USER="user"
    POSTGRES_PASSWORD=123
    POSTGRES_DB="pokedex"
    DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/{POSTGRES_DB}"


class Routes:
    """
    Class representing the routes used in the application.
    """

    QUERY = "/consulta"
