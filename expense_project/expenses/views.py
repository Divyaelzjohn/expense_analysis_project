from django.shortcuts import render, redirect
from .models import Expense
from django.db.models import Sum

# Create your views here.
def home(request):
    if request.method == "POST":
        date = request.POST.get("date")
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        Expense.objects.create(
            date=date,
            category=category,
            amount=amount,
            description=description
        )
        return redirect("home")

    expenses = Expense.objects.all()
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    return render(request, "expenses/home.html", {
        "expenses": expenses,
        "total": total
    })