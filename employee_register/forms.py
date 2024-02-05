from django import forms 
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'mail', 'emp_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'mail': 'E-Mail',
            'emp_code': 'EMP. Code'
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['mail'].required = False
        self.fields['emp_code'].required = False