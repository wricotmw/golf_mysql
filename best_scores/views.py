from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'best_scores/home.html', {})