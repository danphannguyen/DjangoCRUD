from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    if request.POST.get('search'):
        search_str = request.POST.get('search')
        employee_list = Employee.objects.filter(fullname__icontains=search_str)
        context = {'employee_list': employee_list}
        return render(request, 'employee_register/employee_list.html', context)   
    else :
        context = {'employee_list': Employee.objects.all()}
        return render(request, 'employee_register/employee_list.html', context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else : 
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else : 
        if id == 0:
            form = EmployeeForm(request.POST)
        else : 
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')