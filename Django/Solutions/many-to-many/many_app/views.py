from django.shortcuts import redirect, render
from . models import *
#https://stackoverflow.com/questions/44433834/how-do-i-iterate-through-a-manytomanyfield-in-django-jinja-project
# Create your views here.
def home(request):
    # all_players = Player.objects.all()
    # players_in_teams = Player.objects.get(id=2).team_name.all() ## returns all teams associated with a player
    # # ## I give you a team, find all players:
    # players_linked_to_teams = Team.objects.get(id=1).player_set.all()
    # print(players_linked_to_teams)
    all_players = Player.objects.all()
    all_teams = Team.objects.all()
    context = {
        "all_players": all_players,
        "all_teams": all_teams
    }
    return render(request, 'home.html', context)

def add_to_team(request, id):
    team = Team.objects.get(id=id)
    player = Player.objects.get(id=request.POST['team-select'][-1])
    player.team_name.add(team)
    print(team, player)
    return redirect('home')

def players(request):
    all_players = Player.objects.all()
    return render(request, 'players.html', {"all_players": all_players})

def teams(request):
    all_teams = Team.objects.all()
    return render(request, 'teams.html', {"all_teams": all_teams})

def remove_from_team(request,id):
    if request.method=='GET':
        return render(request,'players.html')
    elif request.method == 'POST':
        team_id = request.POST['team_name']
        print('player id', id)
        print('team id', team_id)
        player = Player.objects.get(id=id)
        team = Team.objects.get(id=team_id)
        player.team_name.remove(team)
        return redirect('players')