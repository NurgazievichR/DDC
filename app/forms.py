from django import forms
from .models import CashFlow


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ["status", "subcategory", "amount", "comment"]
