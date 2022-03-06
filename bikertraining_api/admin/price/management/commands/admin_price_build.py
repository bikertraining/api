from django.core.management import base

from admin.price import serializers
from utils import worker


class Command(base.BaseCommand):
    help = 'Admin Price: Create Prices.'

    def handle(self, *args, **options):
        serializer = serializers.BuildPriceSerializer(
            data={}
        )

        if serializer.is_valid():
            serializer.save()

            self.stdout.write('Admin Price: Created Prices.')
        else:
            self.stdout.write(worker.error_to_human_readable(serializer.errors))
