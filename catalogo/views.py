from django.shortcuts import render
from django.core.serializers import serialize
from django.template import RequestContext, loader, TemplateDoesNotExist
from django.http import HttpResponse, JsonResponse
from catalogo.models import Game, GameMechanism, GameXGameMechanism
import json
# Create your views here.


def index(request):
    mechanisms = GameMechanism.objects.all()
    games = Game.objects.all().order_by("?")[:5]
    context = RequestContext(request, {"mechanisms": mechanisms, "games":games})
    context.push(locals())
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context=locals(), request=request))


def advanced(request):
    mechanisms = GameMechanism.objects.all()
    context = RequestContext(request, {"mechanisms": mechanisms})
    context.push(locals())
    template = loader.get_template('advanced.html')
    return HttpResponse(template.render(context=locals(), request=request))


def game(request,_id):
    mechanisms = GameMechanism.objects.all()
    game = games = Game.objects.get(id=_id)
    context = RequestContext(request, {"mechanisms": mechanisms, "game":game})
    context.push(locals())
    template = loader.get_template('game.html')
    return HttpResponse(template.render(context=locals(), request=request))


def all(request):

    games = Game.objects.all()
    j=[]

    for g in games:
        x={}
        for i in ["name", "description", "image", "min_players", "max_players",
        "manual", "min_best_for", "max_best_for", "difficulty_level", "time"]:
            x[i]=g.__dict__[i]    
        types = []

        for t in g.gamexgamemechanism_set.all():
            types.append(t.game_mechanism.name)

        x['types']= types
        j.append(x)


    
    return JsonResponse(j, safe=False)
