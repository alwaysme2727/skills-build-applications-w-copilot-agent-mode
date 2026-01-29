from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            app_models.User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel),
            app_models.User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel),
            app_models.User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel),
            app_models.User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc),
            app_models.User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc),
            app_models.User.objects.create(email='barry@dc.com', name='Barry Allen', team=dc),
        ]

        # Create Activities
        activities = [
            app_models.Activity.objects.create(user=users[0], type='Run', duration=30, distance=5),
            app_models.Activity.objects.create(user=users[1], type='Swim', duration=45, distance=2),
            app_models.Activity.objects.create(user=users[2], type='Bike', duration=60, distance=20),
            app_models.Activity.objects.create(user=users[3], type='Run', duration=25, distance=4),
            app_models.Activity.objects.create(user=users[4], type='Swim', duration=50, distance=2.5),
            app_models.Activity.objects.create(user=users[5], type='Bike', duration=70, distance=22),
        ]

        # Create Workouts
        workouts = [
            app_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes'),
            app_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes'),
        ]

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=300)
        app_models.Leaderboard.objects.create(team=dc, points=280)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
