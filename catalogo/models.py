from django.db.models import DateTimeField, CharField, ImageField, Model, TextField, IntegerField, FloatField, ImageField, FileField, ForeignKey, BooleanField, CASCADE
from django.utils import timezone


class Game(Model):
    """docstring for Request"""
    name = CharField(max_length=255,)
    description = TextField(blank=True, null=True)
    created_date = DateTimeField(default=timezone.now())
    image = ImageField(upload_to="pic_folder/imgs/", blank=True, null=True)
    min_players = IntegerField(default=1)
    max_players = IntegerField(default=100)
    manual = FileField(upload_to="file_folder/manual", blank=True, null=True)
    min_best_for = IntegerField(default=0)
    max_best_for = IntegerField(default=100)
    difficulty_level = CharField(max_length=25, choices=(
        ('very_easy', 'muito fácil'),
        ('easy', 'facil'),
        ('normal', 'normal'),
        ('hard', 'difícil'),
        ('very_hard', 'muito difícil'),
    ))
    time = IntegerField(default=0)

    def __str__(self):
        return self.name

    def no_space_name(self):
        return self.name.replace(' ', '-')

    def mechanisms(self):
        return GameXGameMechanism.objects.filter(game=self)


class GameMechanism (Model):
    """docstring for Request"""
    name = CharField(max_length=255,)
    description = TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def no_space_name(self):
        return self.name.replace(' ', '-')

    def games(self):
        games = []
        for i in self.gamexgamemechanism_set.all():
            games.append(i.game)
        return games

class GameXGameMechanism (Model):
    """docstring for game_x_game_type"""
    game = ForeignKey(Game, on_delete=CASCADE)
    game_mechanism = ForeignKey(GameMechanism, on_delete=CASCADE)

    def __str__(self):
        return (self.game.name + " - " + self.game_mechanism.name)
