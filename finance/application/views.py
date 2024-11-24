# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import User , Transaction

# def home(request):
#     return render(request, "index.html")

# def signup(request):
#     return render(request, "signup.html")

# def user(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name', None)
#         if user_name:
#             return render(request, "expense.html")
#         else:
#             return HttpResponse("Error: Missing user_name")
#     else:
#         return HttpResponse("Invalid request method")

# def signup_save(request):
#     if request.method == 'POST':
#         name = request.POST.get('Name')
#         gmail = request.POST.get('gmail')
#         user_name = request.POST.get('user_name')

#         if name and gmail and user_name:
#             # Save the data to the database or perform other actions
#             return render(request, "expense.html")
#         else:
#             return HttpResponse("Error: Missing required fields")
#     else:
#         return HttpResponse("Invalid request method")

# # New view to handle form data submission from the expense form
# def add_entry(request):
#     # Initialize total income and expenses at the top
#     total_income = 0
#     total_expenses = 0

#     if request.method == 'POST':
#         # Extracting form data
#         entry_type = request.POST.get('type')
#         category = request.POST.get('category')
#         amount = request.POST.get('amount')
#         date = request.POST.get('date')
#         description = request.POST.get('description')

#         # Check if all required fields are filled
#         if entry_type and category and amount and date:
#             # Convert amount to a number (float)
#             try:
#                 # Convert amount to float
#                 amount = float(amount)
#             except ValueError:
#                 # Handle the case where amount is not a valid number
#                 return HttpResponse("Error: Amount must be a valid number")

#             # Calculate total income or expenses based on entry type
#             if entry_type == "Income":
#                 total_income += amount  # Adding income
#             elif entry_type == "Expense":
#                 total_expenses += amount  # Adding expenses
#             else:
#                 return HttpResponse("Error: Invalid entry type")

#             # Calculate the balance
#             balance = total_income - total_expenses

#             # Use the current date from the form
#             current_date = date

#             # Render the summary template with these values
#             return render(request, "summary.html", {
#                 'total_income': total_income,
#                 'total_expenses': total_expenses,
#                 'balance': balance,
#                 'current_date': current_date
#             })
#         else:
#             return HttpResponse("Error: Missing required fields")
#     else:
#         return HttpResponse("Invalid request method")


# def user_tab(request):
#     Trans=Transaction.object.all()
#     return render(request,"table.html",context={"current_tab": "readers",
#                                                "trans":"Transaction" })
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Transaction
from django.shortcuts import get_object_or_404, redirect


def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        if user_name:
            return redirect('add_entry')
        else:
            return HttpResponse("Error: Missing user_name")
    else:
        return HttpResponse("Invalid request method")

def signup_save(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        gmail = request.POST.get('gmail')
        user_name = request.POST.get('user_name')

        if name and gmail and user_name:
            User.objects.create(name=name, email=gmail, user_name=user_name)
            return redirect('add_entry')
        else:
            return HttpResponse("Error: Missing required fields")
    else:
        return HttpResponse("Invalid request method")

def add_entry(request):
    if request.method == 'POST':
        entry_type = request.POST.get('type')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        description = request.POST.get('description')

        if entry_type and category and amount and date:
            try:
                amount = float(amount)
            except ValueError:
                return HttpResponse("Error: Amount must be a valid number")

            Transaction.objects.create(
                type=entry_type,
                category=category,
                amount=amount,
                date=date,
                description=description
            )

            transactions = Transaction.objects.all()
            total_income = sum(t.amount for t in transactions if t.type == 'Income')
            total_expenses = sum(t.amount for t in transactions if t.type == 'Expense')
            balance = total_income - total_expenses

            return render(request, "summary.html", {
                'transactions': transactions,
                'total_income': total_income,
                'total_expenses': total_expenses,
                'balance': balance,
                'current_date': date
            })
        else:
            return HttpResponse("Error: Missing required fields")
    return render(request, "expense.html")

def user_tab(request):
    transactions = Transaction.objects.all()
    return render(request, "summary.html", context={"transactions": transactions})



def delete_transaction(request):
    if request.method == "POST":
        # Get the transaction ID from the POST request
        transaction_id = request.POST.get('transaction_id')
        
        
        # Use get_object_or_404 to fetch the transaction or return a 404 if not found
        transaction = get_object_or_404(Transaction, id=transaction_id)
        
        # Delete the transaction
        transaction.delete()
        
        # Redirect to the page that lists all transactions (adjust as necessary)
        return redirect('user_tab')  # Replace 'summary' with the name of your view if needed.
