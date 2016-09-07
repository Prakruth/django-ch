from django.shortcuts import render

# Create your views here.
store = {1:1, 2:1}

def index(request):
	
	#return HttpResponse("Welcome to Tut1 App" )
	
	if request.method == 'POST':
		number = request.POST['number']
		number = getFibanocci(number)
		context = {'Title': 'Fibonacci Number','content':"Nth Fibonacci number is "+ str(number) }
		return render(request, 'index.html', context)			

	context = {'Title': 'Fibanocci Number','content':""}

	return render(request, 'index.html', context)

def getFibanocci(nn):
	n = int(nn)
	if n in store:
		return store[n]
	store[n] = getFibanocci(n-1) + getFibanocci (n-2)
	return store[n]



