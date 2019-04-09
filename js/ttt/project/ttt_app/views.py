from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'ttt_app/tictactoe.html')
