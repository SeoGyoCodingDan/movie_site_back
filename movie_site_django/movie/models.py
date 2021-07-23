from django.db import models


class Genre(models.Model):
    genrealt = models.CharField(db_column='genreAlt', max_length=15, blank=True, null=True)  # Field name made lowercase.
    moviecd = models.ForeignKey('Movie', models.DO_NOTHING, db_column='movieCd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genre'


class Movie(models.Model):
    moviecd = models.CharField(db_column='movieCd', primary_key=True, max_length=100)  # Field name made lowercase.
    movienm = models.CharField(db_column='movieNm', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prdtyear = models.CharField(db_column='prdtYear', max_length=10, blank=True, null=True)  # Field name made lowercase.
    opendt = models.DateField(db_column='openDt', blank=True, null=True)  # Field name made lowercase.
    prdtstatnm = models.CharField(db_column='prdtStatNm', max_length=10, blank=True, null=True)  # Field name made lowercase.
    repnationnm = models.CharField(db_column='repNationNm', max_length=15, blank=True, null=True)  # Field name made lowercase.
    posterurl = models.CharField(db_column='posterUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie'