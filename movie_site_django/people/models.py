from django.db import models

class Filmo(models.Model):
    moviepartnm = models.CharField(db_column='moviePartNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    peoplecd = models.ForeignKey('People', models.DO_NOTHING, db_column='peopleCd', blank=True, null=True)  # Field name made lowercase.
    moviecd = models.ForeignKey('movie.Movie', models.DO_NOTHING, db_column='movieCd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filmo'


class People(models.Model):
    peoplecd = models.CharField(db_column='peopleCd', primary_key=True, max_length=100)  # Field name made lowercase.
    peoplenm = models.CharField(db_column='peopleNm', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(max_length=2, blank=True, null=True)
    reprolenm = models.CharField(db_column='repRoleNm', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'people'
