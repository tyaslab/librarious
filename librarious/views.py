from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views.generic.edit import *
from django.urls import reverse_lazy
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required

from .forms import *


class HomeView(TemplateView):
    template_name = 'librarious/index.html'


class BorrowingListView(ListView):
    model = Borrowing
    template_name = 'librarious/borrowing_list.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BorrowingDetailView(DetailView):
    model = Borrowing
    template_name = 'librarious/borrowing_detail.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BorrowingAddView(CreateView):
    template_name = 'librarious/borrowing_form.html'
    model = Borrowing
    form_class = BorrowingForm
    success_url = reverse_lazy('borrowing_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['member_list'] = Member.objects.all()

        return context


class BorrowingUpdateView(UpdateView):
    template_name = 'librarious/borrowing_form.html'
    model = Borrowing
    form_class = BorrowingForm
    success_url = reverse_lazy('borrowing_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        context['member_list'] = Member.objects.all()

        return context


class BorrowingDeleteView(DeleteView):
    model = Borrowing
    success_url = reverse_lazy('borrowing_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookListView(ListView):
    model = Book
    template_name = 'librarious/book_list.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BookDetailView(DetailView):
    model = Book
    template_name = 'librarious/book_detail.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Book.objects.get(pk=self.kwargs.get('pk'))
        obj = self.get_object()
        form = RateForm(data={
            'rate': self.request.POST.get('rate'),
            'review': self.request.POST.get('review'),
            'book': obj.pk,
        })

        if form.is_valid():
            member = Member.objects.get(pk=self.request.user.member.pk)
            form.save(member)

            return self.get(request, *args, **kwargs)
            # return HttpResponseRedirect(reverse_lazy('book_detail', args=(obj.pk,)))

        context = self.get_context_data(**kwargs)
        context['form'] = form

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RateForm()

        # get review
        obj = self.get_object()
        member = Member.objects.get(pk=self.request.user.member.pk)
        review = obj.get_review_list(member)

        if review.exists():
            review = review.first()
            form = RateForm(data={
                'rate': review.rating,
                'review': review.review,
                'book': obj.pk,
            })

        context['form'] = form

        return context


class BookAddView(CreateView):
    template_name = 'librarious/book_form.html'
    model = Book
    fields = ['code', 'isbn', 'title', 'author', 'publisher', 'published_year']
    success_url = reverse_lazy('book_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

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

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        context['publisher_list'] = Publisher.objects.all()

        return context


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MemberListView(ListView):
    model = Member
    template_name = 'librarious/member_list.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MemberDetailView(DetailView):
    model = Member
    template_name = 'librarious/member_detail.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MemberAddView(CreateView):
    template_name = 'librarious/member_form.html'
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MemberUpdateView(UpdateView):
    template_name = 'librarious/member_form.html'
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy('member_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MemberDeleteView(DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AuthorListView(ListView):
    model = Author
    template_name = 'librarious/author_list.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'librarious/author_detail.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AuthorAddView(CreateView):
    template_name = 'librarious/author_form.html'
    model = Author
    fields = ['code', 'first_name', 'last_name']
    success_url = reverse_lazy('author_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AuthorUpdateView(UpdateView):
    template_name = 'librarious/author_form.html'
    model = Author
    fields = ['code', 'first_name', 'last_name']
    success_url = reverse_lazy('author_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublisherListView(ListView):
    model = Publisher
    template_name = 'librarious/publisher_list.html'

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'librarious/publisher_detail.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublisherAddView(CreateView):
    template_name = 'librarious/publisher_form.html'
    model = Publisher
    fields = ['code', 'name', 'address']
    success_url = reverse_lazy('publisher_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublisherUpdateView(UpdateView):
    template_name = 'librarious/publisher_form.html'
    model = Publisher
    fields = ['code', 'name', 'address']
    success_url = reverse_lazy('publisher_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list')

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class MemberAreaExploreBookListView(ListView):
    title = 'Explore Books'
    template_name = 'librarious/member_area_book_list.html'
    model = Book

    @method_decorator(user_passes_test(lambda user: user.is_authenticated))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Book.objects.all()


class MemberAreaMyBorrowingListView(MemberAreaExploreBookListView):
    title = 'My Borrowings'
    template_name = 'librarious/member_area_book_list.html'

    def get_queryset(self):
        User = get_user_model()
        user = User.objects.get(pk=self.request.user.pk)

        borrowing_list = Borrowing.objects.filter(
            member=user.member
        )

        return Book.objects.filter(pk__in=borrowing_list.values('book'))
