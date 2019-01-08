from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from .models import Member, Borrowing, Book, Review


class MemberForm(ModelForm):
    username = forms.CharField()
    password = forms.CharField(required=False)

    class Meta:
        model = Member
        fields = ('code', 'name', 'address', 'username', 'password')

    def clean_username(self):
        User = get_user_model()
        data = self.cleaned_data['username']

        if self.instance.pk is not None and self.instance.user and data == self.instance.user.username:
            return data

        check_username = User.objects.filter(username=data)

        if check_username.exists():
            raise forms.ValidationError('Please choose another username')

        return data

    def clean_password(self):
        data = self.cleaned_data['password']

        if self.instance.pk is not None and self.instance.user and self.instance.user.password:
            return data

        if not data:
            raise forms.ValidationError('This field is required')

        return data

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        instance = super().save()
        if instance.user is None:
            user = get_user_model()()
        else:
            user = instance.user

        user.username = username
        if password:
            user.set_password(password)

        user.save()
        instance.user = user
        instance.save()

        return instance


class BorrowingForm(ModelForm):
    class Meta:
        model = Borrowing
        fields = ('code', 'member', 'book', 'due_date', 'back_date')

    def clean_book(self):
        data = self.cleaned_data['book']

        if self.instance.pk is not None and self.instance.book == data:
            return data

        if data.is_being_borrowed():
            raise forms.ValidationError('This book is being borrowed. Please choose another book to borrow.')

        return data


class RateForm(forms.Form):
    book = forms.ModelChoiceField(required=True, queryset=Book.objects.all())
    rate = forms.IntegerField(required=True)
    review = forms.CharField(required=False)

    def save(self, member):
        data = self.cleaned_data
        book = data['book']
        rate = data['rate']
        review = data['review']

        review_obj = Review.objects.filter(
            member=member,
            book=book,
        )

        if review_obj.exists():
            review_obj = review_obj.first()
        else:
            review_obj = Review()
            review_obj.member = member
            review_obj.book = book

        review_obj.rating = rate
        review_obj.review = review
        review_obj.save()
