from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc.name),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='Marvel'),
            Workout.objects.create(name='Running', description='Cardio endurance', suggested_for='DC'),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Pushups', duration=20, date=date.today())
        Activity.objects.create(user=users[1], type='Running', duration=30, date=date.today())
        Activity.objects.create(user=users[3], type='Pushups', duration=25, date=date.today())
        Activity.objects.create(user=users[4], type='Running', duration=35, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[3], score=95)
        Leaderboard.objects.create(user=users[4], score=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
