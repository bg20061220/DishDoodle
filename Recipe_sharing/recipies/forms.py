from django import forms

class RecipeForm(forms.Form):
    author = forms.CharField(
        label="Author",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    recipename = forms.CharField(
        label="Recipe Name",
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    majoringredients = forms.CharField(
        label="Major Ingredients",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
    )
    recipe = forms.CharField(
        label="Recipe",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'cols': 200})
    )
