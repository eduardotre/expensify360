from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, HTML
from crispy_forms.bootstrap import FormActions



class mileageEntryForm(forms.Form):
    userID = forms.CharField(label='User ID')
    expenseDate = forms.DateField(label='Expense Date')
    submissionDate = forms.DateField(label='Submission Date')
    organization = forms.CharField(label='Organization')
    project = forms.CharField(label='Project')
    miles = forms.DecimalField(label='Miles Driven',
                               widget=forms.NumberInput(attrs={'onchange' : "UpdateExpenseTotal();"}))
    mileageRate = forms.DecimalField(label='Rate Per Mile',
                                     widget=forms.NumberInput(attrs={'onchange' : "UpdateExpenseTotal();"}))
    mileageTotal = forms.DecimalField(label='Total Cost')


class expenseEntryForm(forms.Form):
    userID = forms.CharField(label='User ID')
    expenseDate = forms.DateField(label='Expense Date')
    submissionDate = forms.DateField(label='Submission Date')
    organization = forms.CharField(label='Organization')
    project = forms.CharField(label='Project')
    file = forms.FileField(label='Receipt Upload')
    expenseCost = forms.DecimalField(label='Item Cost')
    tax = forms.DecimalField(label='Tax')
    shipping = forms.DecimalField(label='Shipping Cost')
    expenseTotal = forms.DecimalField(label='Total Cost')


class timeEntryForm(forms.Form):
    userID = forms.CharField(label='User ID')
    expenseDate = forms.DateField(label='Expense Date')
    submissionDate = forms.DateField(label='Submission Date')
    organization = forms.CharField(label='Organization')
    project = forms.CharField(label='Project')
    hours = forms.DecimalField(label='Hours Worked')
    hourlyRate = forms.DecimalField(label='Hourly Rate')
    hourTotal = forms.DecimalField(label='Total Cost')
