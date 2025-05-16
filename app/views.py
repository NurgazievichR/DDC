from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from app.forms import CashFlowForm
from app.models import CashFlow

@login_required
def index(request):
    user_cashflows = CashFlow.objects.filter(user=request.user)
    return render(request, 'app/index.html', {'cashflows': user_cashflows})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_cashflow(request):
    if request.method == 'POST':
        form = CashFlowForm(request.POST)
        if form.is_valid():
            cashflow = form.save(commit=False)
            cashflow.user = request.user
            cashflow.save()
            return redirect('index')
    else:
        form = CashFlowForm()
    return render(request, 'app/add.html', {'form': form})