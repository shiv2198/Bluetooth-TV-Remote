from django.shortcuts import render,redirect

# Create your views here.
def api(request):
	return redirect('/api/post/Show/')
