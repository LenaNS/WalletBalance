import os

from pyliquibase import Pyliquibase


def run_migrations():
    """
    Применяет миграции Liquibase.
    """
    liquibase = Pyliquibase()

    liquibase.addarg("--url",
                     f'jdbc:postgresql://{os.getenv("HOST", "localhost")}/{os.getenv("DB", "DBWalletBalance")}')
    liquibase.addarg("--driver", "org.postgresql.Driver")
    liquibase.addarg("--username", os.getenv("USERNAME", "postgres"))
    liquibase.addarg("--password", os.getenv("PASSWORD", "admin"))
    liquibase.addarg("--changeLogFile", "liquibase/changelog.xml")

    liquibase.update()
