from django.db import models


class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    channel_id = models.IntegerField()
    parent_id = models.IntegerField()
    is_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cms_category"
