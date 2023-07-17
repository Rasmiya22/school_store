from django.shortcuts import render, redirect


# Create your views here.
def demo(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':

        return redirect('new.html')

    return render(request,'login.html')
def register(request):
    if request.method == 'POST':

        return redirect('login.html')

    return render(request, 'register.html')
def new(request):
    return render(request,'new.html')
def computer_science(request):
    return render(request,'computer.html')
def mechanical(request):
    return render(request,'mech.html')
def electrical(request):
    return render(request,'electrical.html')
def electronics(request):
    return render(request,'electronics.html')
def production(request):
    return render(request,'production.html')