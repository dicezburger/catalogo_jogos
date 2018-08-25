from django.shortcuts import render
from django.core.serializers import serialize
from django.template import RequestContext, loader, TemplateDoesNotExist
from django.http import HttpResponse, JsonResponse
from catalogo.models import Game, GameMechanism, GameXGameMechanism
import json
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    mechanisms = GameMechanism.objects.all()
    games = Game.objects.all().order_by("?")[:5]
    context = RequestContext(request, {"mechanisms": mechanisms, "games": games})
    context.push(locals())
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context=locals(), request=request))


def games(request):
    mechanisms = GameMechanism.objects.all()
    try:
        games = Game.objects.filter(name__contains=request.POST['name'])
    except ObjectDoesNotExist as e:
        games = {}

    context = RequestContext(request, {"mechanisms": mechanisms, "games": games})
    context.push(locals())
    template = loader.get_template('games.html')
    return HttpResponse(template.render(context=locals(), request=request))


def advanced(request):
    mechanisms = GameMechanism.objects.all()
    context = RequestContext(request, {"mechanisms": mechanisms})
    context.push(locals())
    template = loader.get_template('advanced.html')
    return HttpResponse(template.render(context=locals(), request=request))


def game(request, name):
    mechanisms = GameMechanism.objects.all()
    game = Game.objects.get(name=name.replace('-', ' '))
    context = RequestContext(request, {"mechanisms": mechanisms, "game": game})
    context.push(locals())
    template = loader.get_template('game.html')
    return HttpResponse(template.render(context=locals(), request=request))


def mechanisms(request, name):
    mechanisms = GameMechanism.objects.all()
    try:
        mechanism = GameMechanism.objects.get(name=name.replace('-', ' '))
    except ObjectDoesNotExist as e:
        mechanism = {}

    context = RequestContext(request, {"mechanisms": mechanisms, "mechanism": mechanism})
    context.push(locals())
    template = loader.get_template('mechanism.html')
    return HttpResponse(template.render(context=locals(), request=request))


def all(request):

    games = Game.objects.all()
    j = []

    for g in games:
        x = {}
        for i in ["name", "description", "image", "min_players", "max_players",
                  "manual", "min_best_for", "max_best_for", "difficulty_level", "time"]:
            x[i] = g.__dict__[i]
        types = []

        for t in g.gamexgamemechanism_set.all():
            types.append(t.game_mechanism.name)

        x['types'] = types
        j.append(x)

    return JsonResponse(j, safe=False)
