# pages/tests.py
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from .models import Member, Author, Publisher, Book, Review, Borrowing


class AppTest(TestCase):
    def setUp(self):
        User = get_user_model()
        # create member
        self.user_aditya = User.objects.create(username='aditya', password='aditya')
        self.member_aditya = Member.objects.create(name='Aditya', address='Jl in aja dulu aditya', user=self.user_aditya)

        self.user_supriati = User.objects.create(username='supriati', password='supriati')
        self.member_supriati = Member.objects.create(name='Supriati', address='Jl in aja dulu supriati', user=self.user_supriati)

        self.user_tyas = User.objects.create(username='tyas', password='tyas')
        self.member_tyas = Member.objects.create(name='Tyas', address='Jl in aja dulu tyas', user=self.user_tyas)

        self.user_nadia = User.objects.create(username='nadia', password='nadia')
        self.member_nadia = Member.objects.create(name='Nadia', address='Jl in aja dulu nadia', user=self.user_nadia)

        self.user_ara = User.objects.create(username='ara', password='ara')
        self.member_ara = Member.objects.create(name='Ara', address='Jl in aja dulu ara', user=self.user_ara)

        # create author
        self.author_fahd = Author.objects.create(first_name='Fahd', last_name='Pahdepie')
        self.author_arswendo = Author.objects.create(first_name='Arswendo', last_name='Atmowiloto')
        self.author_tere = Author.objects.create(first_name='Tere', last_name='Liye')
        self.author_yusuf = Author.objects.create(first_name='Yusuf', last_name='Qaradawi')
        self.author_felix = Author.objects.create(first_name='Felix', last_name='Siauw')
        self.author_andi = Author.objects.create(first_name='Andi', last_name='Rif')
        self.author_nhdini = Author.objects.create(first_name='N.H.', last_name='Dini')
        self.author_abdul = Author.objects.create(first_name='Abdul', last_name='Abulbulamir')

        # create publisher
        self.publisher_andi = Publisher.objects.create(name='Andi Publishing', address='Jl. Antah Berantah Andi Publishing')
        self.publisher_erlangga = Publisher.objects.create(name='Erlangga', address='Jl. Antah Berantah Erlangga')
        self.publisher_kendangsari = Publisher.objects.create(name='Kendangsari', address='Jl. Antah Berantah Kendangsari')
        self.publisher_proumedia = Publisher.objects.create(name='Pro U Media', address='Jl. Antah Berantah Pro U Media')
        self.publisher_gigal = Publisher.objects.create(name='Gigal', address='Jl. Antah Berantah Gigal')

        # create book
        self.book_menjadi_suamimu = Book.objects.create(isbn='123', title='Menjadi Suamimu dan Suaminya', author=self.author_fahd, publisher=self.publisher_andi)
        self.book_asal_ada = Book.objects.create(isbn='456', title='Asal Ada', author=self.author_arswendo, publisher=self.publisher_erlangga)
        self.book_mengada = Book.objects.create(isbn='879', title='Mengada', author=self.author_tere, publisher=self.publisher_kendangsari)
        self.book_jadi = Book.objects.create(isbn='243', title='Jadi', author=self.author_felix, publisher=self.publisher_gigal)
        self.book_kurang = Book.objects.create(isbn='235', title='Kurang', author=self.author_abdul, publisher=self.publisher_proumedia)

        # review
        Review.objects.create(member=self.member_aditya, book=self.book_asal_ada, rating=5, review='Oke banget')
        Review.objects.create(member=self.member_ara, book=self.book_asal_ada, rating=3, review='Oke banget deh')
        Review.objects.create(member=self.member_supriati, book=self.book_asal_ada, rating=2, review='Nggak asik')

        # borrowing
        Borrowing.objects.create(member=self.member_aditya, book=self.book_asal_ada, due_date='2018-01-20', back_date='2018-01-20')
        Borrowing.objects.create(member=self.member_aditya, book=self.book_mengada, due_date='2018-01-20')
        Borrowing.objects.create(member=self.member_supriati, book=self.book_jadi, due_date='2018-02-01')
        Borrowing.objects.create(member=self.member_tyas, book=self.book_kurang, due_date='2018-01-12')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'librarious/index.html')

    def test_member_correct_data(self):
        member_aditya = Member.objects.get(user__username='aditya')
        member_supriati = Member.objects.get(user__username='supriati')
        member_tyas = Member.objects.get(user__username='tyas')
        member_nadia = Member.objects.get(user__username='nadia')
        member_ara = Member.objects.get(user__username='ara')

        self.assertEqual(member_aditya.name, 'Aditya')
        self.assertEqual(member_supriati.name, 'Supriati')
        self.assertEqual(member_tyas.name, 'Tyas')
        self.assertEqual(member_nadia.name, 'Nadia')
        self.assertEqual(member_ara.name, 'Ara')

        # code not null
        self.assertIsNotNone(member_aditya.code)
        self.assertIsNotNone(member_supriati.code)
        self.assertIsNotNone(member_tyas.code)
        self.assertIsNotNone(member_nadia.code)
        self.assertIsNotNone(member_ara.code)

    def test_member_correct_count(self):
        self.assertEqual(Member.objects.count(), 5)

    def test_author_correct_data(self):
        author_fahd = Author.objects.get(pk=1)
        author_arswendo = Author.objects.get(pk=2)
        author_tere = Author.objects.get(pk=3)
        author_yusuf = Author.objects.get(pk=4)
        author_felix = Author.objects.get(pk=5)
        author_andi = Author.objects.get(pk=6)
        author_nhdini = Author.objects.get(pk=7)
        author_abdul = Author.objects.get(pk=8)

        self.assertEqual(author_fahd.first_name, 'Fahd')
        self.assertEqual(author_arswendo.first_name, 'Arswendo')
        self.assertEqual(author_tere.first_name, 'Tere')
        self.assertEqual(author_yusuf.first_name, 'Yusuf')
        self.assertEqual(author_felix.first_name, 'Felix')
        self.assertEqual(author_andi.first_name, 'Andi')
        self.assertEqual(author_nhdini.first_name, 'N.H.')
        self.assertEqual(author_abdul.first_name, 'Abdul')

        self.assertIsNotNone(author_fahd.code)
        self.assertIsNotNone(author_arswendo.code)
        self.assertIsNotNone(author_tere.code)
        self.assertIsNotNone(author_yusuf.code)
        self.assertIsNotNone(author_felix.code)
        self.assertIsNotNone(author_andi.code)
        self.assertIsNotNone(author_nhdini.code)
        self.assertIsNotNone(author_abdul.code)

    def test_publisher_correct_data(self):
        publisher_andi = Publisher.objects.get(name='Andi Publishing')
        publisher_erlangga = Publisher.objects.get(name='Erlangga')
        publisher_kendangsari = Publisher.objects.get(name='Kendangsari')
        publisher_proumedia = Publisher.objects.get(name='Pro U Media')
        publisher_gigal = Publisher.objects.get(name='Gigal')

        self.assertEqual(publisher_andi.address, 'Jl. Antah Berantah Andi Publishing')
        self.assertEqual(publisher_erlangga.address, 'Jl. Antah Berantah Erlangga')
        self.assertEqual(publisher_kendangsari.address, 'Jl. Antah Berantah Kendangsari')
        self.assertEqual(publisher_proumedia.address, 'Jl. Antah Berantah Pro U Media')
        self.assertEqual(publisher_gigal.address, 'Jl. Antah Berantah Gigal')

        self.assertIsNotNone(publisher_andi.code)
        self.assertIsNotNone(publisher_erlangga.code)
        self.assertIsNotNone(publisher_kendangsari.code)
        self.assertIsNotNone(publisher_proumedia.code)
        self.assertIsNotNone(publisher_gigal.code)

    def test_book_correct_data(self):
        book_menjadi_suamimu = Book.objects.get(isbn='123')
        book_asal_ada = Book.objects.get(isbn='456')
        book_mengada = Book.objects.get(isbn='879')
        book_jadi = Book.objects.get(isbn='243')
        book_kurang = Book.objects.get(isbn='235')

        self.assertEqual(book_menjadi_suamimu.title, 'Menjadi Suamimu dan Suaminya')
        self.assertEqual(book_asal_ada.title, 'Asal Ada')
        self.assertEqual(book_mengada.title, 'Mengada')
        self.assertEqual(book_jadi.title, 'Jadi')
        self.assertEqual(book_kurang.title, 'Kurang')

        self.assertIsNotNone(book_menjadi_suamimu.code)
        self.assertIsNotNone(book_asal_ada.code)
        self.assertIsNotNone(book_mengada.code)
        self.assertIsNotNone(book_jadi.code)
        self.assertIsNotNone(book_kurang.code)

    def test_rating_count(self):
        book_asal_ada = Book.objects.get(pk=self.book_asal_ada.pk)

        rating = (5 + 3 + 2) / 3
        self.assertEqual(book_asal_ada.get_rating(), rating)

    def test_book_is_being_borrowed(self):
        self.assertEqual(self.book_menjadi_suamimu.is_being_borrowed(), False)
        self.assertEqual(self.book_asal_ada.is_being_borrowed(), False)
        self.assertEqual(self.book_mengada.is_being_borrowed(), True)
        self.assertEqual(self.book_jadi.is_being_borrowed(), True)
        self.assertEqual(self.book_kurang.is_being_borrowed(), True)
