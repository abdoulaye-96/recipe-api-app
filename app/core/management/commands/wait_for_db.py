"""
django command to wait for db to be a vailable 
""" 
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("waiting for database ...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError) as e:
                self.stdout.write(self.style.ERROR(e))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database avilable!'))
