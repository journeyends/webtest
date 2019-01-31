from django.db import models


class ContentModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    channel_id = models.IntegerField()
    category_id = models.IntegerField()
    is_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = "cms_content"
