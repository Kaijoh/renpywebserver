from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Score
import json
import requests

import logging
logger = logging.getLogger(__name__)
logger.info('submit_score called')


@csrf_exempt
def submit_score(request):
    if request.method == 'POST':
        player_name = request.POST['player_name']
        player_score = request.POST['player_score']

        score = Score.objects.create(player_name=player_name, player_score=player_score)
        score.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
    
# @csrf_exempt
# def score_board(request):
#     player_score = Score.objects.order_by('-player_score')
#     return render(request, 'score_board.html', {'player_score': player_score})
                                                                  
@csrf_exempt
def score_board(request):
    player_score = Score.objects.order_by('-player_score').values('player_name', 'player_score')
    return render(request, 'score_board.html', {'player_score': player_score})


































# def base(request):

#     return

# @csrf_exempt
# def score_board(request):
#     if request.method == 'POST':
#         player_name = request.POST.get('player_name')
#         player_score = request.POST.get('player_score')
#         if player_name and player_score:
#             score = Score.objects.create(player_name=player_name, player_score=player_score)
#             score.save()
#             return JsonResponse({'status': 'success'})
#     return JsonResponse({'status': 'error'})

# @csrf_exempt
# def score_board(request):
#     if request.method == 'POST':
#         player_name = request.POST.get('player_name')
#         player_score = request.POST.get('player_score')

#         # create a new Score object and save it in the database
#         score = Score(player_name=player_name, player_score=player_score)
#         score.save()

#         # return a JSON response to Ren'Py indicating that the score has been saved
#         response_data = {'status': 'success'}
#         return JsonResponse(response_data)

#     # if the request method is not POST, return a 404 error
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=404)
    



































# sir may i ask for a little help and check my code whats wrong or do you know what's the problem here? i made a web server using django python to act as my database on my renpy visual novel game already, and want to store the inputed name and final score of the user. here are the codes:


# in django views.py:

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Score

# def submit_score(request):

#     if request.method == "POST":

#         player_name = request.POST.get('player_name')
#         player_score = request.POST.get('player_score')
#         PlayerScore = Score.objects.create(player_name=player_name, player_score=player_score)
#         PlayerScore.save()

#     return render(request, 'submit_score.html')


# in django templates folder submit_score.html:

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>

#     <form action="" method="post">
#         {% csrf_token %}
#         <button type="submit">Submit</button>
#     </form>
    
# </body>
# </html>


# in renpy game project:

# label Act2:

#     "aaaaaaa [player_score]"

#     init python:
#         import urllib.parse
#         import urllib.request

#         def submit_score(name, score):
#             url = 'http://localhost:8000/submit_score/'
#             data = urllib.parse.urlencode({'player_name': player_name, 'player_score': player_score}).encode()
#             req = urllib.request.Request(url, data)
#             response = urllib.request.urlopen(req)
#             return response.read().decode()
