import datetime
from django.db import models
from django.db.models import Avg
from django.utils.crypto import get_random_string
from django.utils import timezone

from django.contrib.gis.db import models as gis_models


def set_code():
    return get_random_string(length=10).upper()


class Member(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user = models.OneToOneField('auth.User', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = set_code()

        super().save(*args, **kwargs)

    def has_ever_borrowed(self, book):
        check_borrowing = Borrowing.objects.filter(
            book=book,
            member=self
        )

        return check_borrowing.exists()

    def is_borrowing(self, book=None):
        check_borrowing = self.get_borrowing_list()

        if book:
            check_borrowing = check_borrowing.filter(book=book)

        return check_borrowing.exists()

    def get_borrowing_list(self):
        now = timezone.now()
        borrowing = Borrowing.objects.filter(
            member=self,
            created_gte=now,
            due_date_lte=now
        )

        return borrowing


class Author(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = set_code()

        super().save(*args, **kwargs)


class Publisher(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = set_code()

        super().save(*args, **kwargs)


class Book(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=True)
    isbn = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', null=True, blank=True, on_delete=models.CASCADE)
    published_year = models.PositiveIntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = set_code()

        super().save(*args, **kwargs)

    def is_being_borrowed(self, member=None):
        borrowing_list = Borrowing.objects.filter(
            book=self,
            back_date__isnull=True
        )

        if member:
            borrowing_list = borrowing_list.filter(
                member=member
            )

        return borrowing_list.exists()

    def get_rating(self, member=None):
        review_list = self.get_review_list(member=member)

        return review_list.aggregate(Avg('rating'))['rating__avg'] or 0

    def get_review_list(self, member=None):
        review_list = Review.objects.filter(
            book=self
        )

        if member:
            review_list = review_list.filter(
                member=member
            )

        return review_list


# class BookItem(models.Model):
#     code_item = models.PositiveIntegerField()
#     book = models.ForeignKey('Book', on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('created',)

#     def __str__(self):
#         return '%s - %s' % (self.book.title, self.code_item)


class Review(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # between 1 to 5
    review = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '%s - %s' % (self.member.user.first_name)


class Borrowing(models.Model):
    code = models.CharField(max_length=100, unique=True, blank=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    due_date = models.DateField()
    back_date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if self.id is None:
            self.code = set_code()

        super().save(*args, **kwargs)

    def is_overdue(self):
        if self.back_date:
            return False

        now = timezone.now()
        now = datetime.date(now.year, now.month, now.day)

        return now > self.due_date


# class WorldBorder(gis_models.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = gis_models.CharField(max_length=50)
#     area = gis_models.IntegerField()
#     pop2005 = gis_models.IntegerField('Population 2005')
#     fips = gis_models.CharField('FIPS Code', max_length=2)
#     iso2 = gis_models.CharField('2 Digit ISO', max_length=2)
#     iso3 = gis_models.CharField('3 Digit ISO', max_length=3)
#     un = gis_models.IntegerField('United Nations Code')
#     region = gis_models.IntegerField('Region Code')
#     subregion = gis_models.IntegerField('Sub-Region Code')
#     lon = gis_models.FloatField()
#     lat = gis_models.FloatField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = gis_models.MultiPolygonField()

#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name


# from django.contrib.gis.db import models


class WorldBorder(gis_models.Model):
    fips = gis_models.CharField(max_length=2)
    iso2 = gis_models.CharField(max_length=2)
    iso3 = gis_models.CharField(max_length=3)
    un = gis_models.IntegerField()
    name = gis_models.CharField(max_length=50)
    area = gis_models.IntegerField()
    pop2005 = gis_models.BigIntegerField()
    region = gis_models.IntegerField()
    subregion = gis_models.IntegerField()
    lon = gis_models.FloatField()
    lat = gis_models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name


# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}