from django.contrib import admin
from catalogo.models import Game, GameMechanism, GameXGameMechanism
# Register your models here.

admin.site.register(Game)
admin.site.register(GameMechanism)
admin.site.register(GameXGameMechanism)