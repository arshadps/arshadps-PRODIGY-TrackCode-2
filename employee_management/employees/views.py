from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

def home(request):
   return render(request, 'home.html')

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})
@login_required
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})
@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})
@login_required
def employee_update(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})
@login_required
def employee_delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return redirect('home') 
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return redirect('home') 