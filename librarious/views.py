from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse_lazy
from .models import *


class HomeView(TemplateView):
    template_name = 'librarious/index.html'


class BorrowingListView(ListView):
    model = Borrowing
    template_name = 'librarious/borrowing_list.html'


class BorrowingDetailView(DetailView):
    model = Borrowing
    template_name = 'librarious/borrowing_detail.html'


class BorrowingAddView(CreateView):
    template_name = 'librarious/borrowing_form.html'
    model = Borrowing
    fields = ['code', 'member', 'book', 'due_date', 'back_date']
    success_url = reverse_lazy('borrowing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['member_list'] = Member.objects.all()

        return context


class BorrowingUpdateView(UpdateView):
    template_name = 'librarious/borrowing_form.html'
    model = Borrowing
    fields = ['code', 'member', 'book', 'due_date', 'back_date']
    success_url = reverse_lazy('borrowing_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['member_list'] = Member.objects.all()

        return context


class BorrowingDeleteView(DeleteView):
    model = Borrowing
    success_url = reverse_lazy('borrowing_list')


class BookListView(ListView):
    model = Book
    template_name = 'librarious/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'librarious/book_detail.html'


class BookAddView(CreateView):
    template_name = 'librarious/book_form.html'
    model = Book
    fields = ['code', 'isbn', 'title', 'author', 'publisher', 'published_year']
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        context['publisher_list'] = Publisher.objects.all()

        return context


class BookUpdateView(UpdateView):
    template_name = 'librarious/book_form.html'
    model = Book
    fields = ['code', 'isbn', 'title', 'author', 'publisher', 'published_year']
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        context['publisher_list'] = Publisher.objects.all()

        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class MemberListView(ListView):
    model = Member
    template_name = 'librarious/member_list.html'


class MemberDetailView(DetailView):
    model = Member
    template_name = 'librarious/member_detail.html'


class MemberAddView(CreateView):
    template_name = 'librarious/member_form.html'
    model = Member
    fields = ['code', 'name', 'address']
    success_url = reverse_lazy('member_list')


class MemberUpdateView(UpdateView):
    template_name = 'librarious/member_form.html'
    model = Member
    fields = ['code', 'name', 'address']
    success_url = reverse_lazy('member_list')


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')


class AuthorListView(ListView):
    model = Author
    template_name = 'librarious/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'librarious/author_detail.html'


class AuthorAddView(CreateView):
    template_name = 'librarious/author_form.html'
    model = Author
    fields = ['code', 'first_name', 'last_name']
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    template_name = 'librarious/author_form.html'
    model = Author
    fields = ['code', 'first_name', 'last_name']
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')


class PublisherListView(ListView):
    model = Publisher
    template_name = 'librarious/publisher_list.html'


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'librarious/publisher_detail.html'


class PublisherAddView(CreateView):
    template_name = 'librarious/publisher_form.html'
    model = Publisher
    fields = ['code', 'name', 'address']
    success_url = reverse_lazy('publisher_list')


class PublisherUpdateView(UpdateView):
    template_name = 'librarious/publisher_form.html'
    model = Publisher
    fields = ['code', 'name', 'address']
    success_url = reverse_lazy('publisher_list')


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')


# from django.http import HttpResponse
# from oauth2_provider.views.generic import ProtectedResourceView

# class ApiEndpoint(ProtectedResourceView):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Protected with OAuth2')


# # http://localhost:8000/o/authorize?response_type=code&client_id=123456&redirect_uri=http://example.com/
