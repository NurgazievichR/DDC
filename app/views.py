from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from app.forms import CashFlowForm
from app.models import CashFlow, Category, Status, Subcategory, Type

@login_required
def index(request):
    user = request.user

    filters = {'user': user}

    selected_type_id = request.GET.get('type')
    selected_category_id = request.GET.get('category')
    selected_subcategory_id = request.GET.get('subcategory')
    selected_status_id = request.GET.get('status')

    types = Type.objects.all()

    if selected_type_id and selected_type_id != 'all':
        categories = Category.objects.filter(type_id=selected_type_id)
        filters['subcategory__category__type_id'] = selected_type_id
    else:
        categories = Category.objects.all()

    if selected_category_id and selected_category_id != 'all':
        subcategories = Subcategory.objects.filter(category_id=selected_category_id)
        filters['subcategory__category_id'] = selected_category_id
    else:
        subcategories = Subcategory.objects.all()

    if selected_subcategory_id and selected_subcategory_id != 'all':
        filters['subcategory_id'] = selected_subcategory_id
    
    statuses = Status.objects.all()
    if selected_status_id and selected_status_id != 'all':
        filters['status_id'] = selected_status_id

    cashflows = CashFlow.objects.filter(**filters)

    context = {
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        'statuses': statuses,
        'cashflows': cashflows,

        'selected_type_id': selected_type_id or 'all',
        'selected_category_id': selected_category_id or 'all',
        'selected_subcategory_id': selected_subcategory_id or 'all',
        'selected_status_id': selected_status_id or 'all',
    }

    user_cashflows = CashFlow.objects.filter(user=request.user)
    return render(request, 'app/index.html', context)

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