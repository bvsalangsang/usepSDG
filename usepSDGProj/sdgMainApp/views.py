from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'themes/index.html')

def commitment(request):
    return render(request, 'themes/commitment.html')

def strategy(request):
    return render(request, 'themes/strategy.html')

def sustainPPA(request):
    return render(request, 'themes/sustainability-ppa.html')

def contact(request):
    return render(request, 'themes/contact.html')

def goal4(request):
    return render(request,'themes/goal4.html')

def goalTopic(request):
    return render(request,'themes/goal-topic.html')



def test(request):
    return render(request,'themes/test.html')
