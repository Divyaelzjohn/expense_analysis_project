from django.shortcuts import render, redirect
from .models import Expense
from django.db.models import Sum
from django.shortcuts import get_object_or_404

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

def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == "POST":
        expense.date = request.POST.get("date")
        expense.category = request.POST.get("category")
        expense.amount = request.POST.get("amount")
        expense.description = request.POST.get("description")
        expense.save()
        return redirect("home")

    return render(request, "expenses/edit.html", {"expense": expense})


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect("home")