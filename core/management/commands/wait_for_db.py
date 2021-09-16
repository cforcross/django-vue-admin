from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time,os
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for the the database")
        conn = None

        while not conn:
            try:
                conn = connections['default']
                print(conn)
            except OperationalError:
                self.stdout.write("Database unavailable,waiting for 1 sec")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))