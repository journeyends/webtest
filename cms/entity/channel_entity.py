from django.db import models


class ChannelModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=30)
    site_id = models.IntegerField()
    parent_id = models.IntegerField()
    is_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cms_channel"
