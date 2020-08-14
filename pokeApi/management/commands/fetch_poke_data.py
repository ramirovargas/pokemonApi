from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Indicates id of evolution chain')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        print(id)