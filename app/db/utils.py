from sqlalchemy import text
from sqlalchemy.engine import create_engine, make_url
from app.core.config import Settings


def create_database() -> None:
    """Create a databse."""
    db_url = Settings.DATABASE_URL
    engine = create_engine(db_url, isolation_level="AUTOCOMMIT")

    with engine.connect() as conn:
        database_existance = conn.execute(
            text(
                f"SELECT 1 FROM pg_database WHERE datname='{Settings.POSTGRES_DB}'",  # noqa: E501, S608
            ),
        )
        database_exists = database_existance.scalar() == 1

    if database_exists:
        drop_database()

    with engine.connect() as conn:  # noqa: WPS440
        conn.execute(
            text(
                f'CREATE DATABASE "{Settings.POSTGRES_DB}" ENCODING "utf8" TEMPLATE template1',  # noqa: E501
            ),
        )


def drop_database() -> None:
    """Drop current database."""
    db_url = make_url(str(Settings.DATABASE_URL.with_path("/postgres")))
    engine = create_engine(db_url, isolation_level="AUTOCOMMIT")
    with engine.connect() as conn:
        disc_users = (
            "SELECT pg_terminate_backend(pg_stat_activity.pid) "  # noqa: S608
            "FROM pg_stat_activity "
            f"WHERE pg_stat_activity.datname = '{Settings.POSTGRES_DB}' "
            "AND pid <> pg_backend_pid();"
        )
        conn.execute(text(disc_users))
        conn.execute(text(f'DROP DATABASE "{Settings.POSTGRES_DB}"'))