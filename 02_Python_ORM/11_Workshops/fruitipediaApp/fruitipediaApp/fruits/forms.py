from django import forms

from fruitipediaApp.fruits.models import Fruit, Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        # this form is for model Category
        model = Category
        # takes all field from model Category ( in our case we have only 'name' field)
        fields = '__all__'


class CategoryCreateForm(CategoryBaseForm):
    pass


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    pass
