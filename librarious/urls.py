"""librarious URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('book/list/', BookListView.as_view(), name='book_list'),
    path('book/detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/add/', BookAddView.as_view(), name='book_add'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('borrowing/list/', BorrowingListView.as_view(), name='borrowing_list'),
    path('borrowing/detail/<int:pk>/', BorrowingDetailView.as_view(), name='borrowing_detail'),
    path('borrowing/add/', BorrowingAddView.as_view(), name='borrowing_add'),
    path('borrowing/update/<int:pk>/', BorrowingUpdateView.as_view(), name='borrowing_update'),
    path('borrowing/delete/<int:pk>/', BorrowingDeleteView.as_view(), name='borrowing_delete'),

    path('member/list/', MemberListView.as_view(), name='member_list'),
    path('member/detail/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('member/add/', MemberAddView.as_view(), name='member_add'),
    path('member/update/<int:pk>/', MemberUpdateView.as_view(), name='member_update'),
    path('member/delete/<int:pk>/', MemberDeleteView.as_view(), name='member_delete'),

    path('author/list/', AuthorListView.as_view(), name='author_list'),
    path('author/detail/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/add/', AuthorAddView.as_view(), name='author_add'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),

    path('publisher/list/', PublisherListView.as_view(), name='publisher_list'),
    path('publisher/detail/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publisher/add/', PublisherAddView.as_view(), name='publisher_add'),
    path('publisher/update/<int:pk>/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisher/delete/<int:pk>/', PublisherDeleteView.as_view(), name='publisher_delete'),

    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
