from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Scores, Golfer, FiveScores
from .forms import ScoreForm, GolferForm
from django.http import HttpResponseRedirect
from .utils import get_scores

# Create your views here.
def home(request):
	return render(request, 'best_scores/home.html', {})


def add_golfer(request):
	submitted = False
	if request.method == 'POST':
		form = GolferForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_golfer/?submitted=True')
	else:
		form = GolferForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 
		'best_scores/add_golfer.html',
		{'form': form, 'submitted': submitted}
		)

def add_scores(request):
	submitted = False
	if request.method == 'POST':
		form = ScoreForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_scores/?submitted=True')
	else:
		form = ScoreForm()
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 
		'best_scores/add_scores.html',
		{'form': form, 'submitted': submitted}
		)

def all_scores(request):
	score_list = Scores.objects.all().order_by('score_date')

	return render(request, 'best_scores/score_list.html', {
		'score_list':score_list
		})


def league(request):
	golfer_list = Golfer.objects.all()
	
	FiveScores.objects.all().delete()
	golfer_scores = []
	for name in golfer_list:
		golfer_scores.append(name)
		score_list = get_scores(name)
		#for score in score_list:
		#	golfer_scores.append(score)
	# now sort into descending order and slice top 5
	#see utils.py
	# now craete record for the database and write to FiveScores

	#now read from Fivescores.all and return to web page

		
	return render(request, 'best_scores/league_table.html', {
			'score_list':score_list,
			#'golfer_scores': golfer_scores,
			
			
			})
