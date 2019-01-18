from django.db import models


class SiteModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    is_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cms_site"
