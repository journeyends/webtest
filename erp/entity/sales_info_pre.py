from django.db import models


class SalesInfoPre(models.Model):
    pre_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=150)
    project_key_name = models.CharField(max_length=20)
    customer_id = models.IntegerField()
    customer_key_name = models.CharField(max_length=20)
    area_id = models.IntegerField()
    address = models.CharField(max_length=150)
    status = models.IntegerField()
    is_clash = models.IntegerField()
    clash_info_id = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    info_id = models.IntegerField()
    is_del = models.IntegerField()
    is_post = models.IntegerField()
    post_date = models.DateTimeField()
    check_status = models.IntegerField()
    create_user_id = models.IntegerField()
    create_date = models.DateTimeField()
    last_update_user = models.IntegerField()
    last_update_time = models.DateTimeField(null=True)
    is_warn = models.IntegerField()
    is_mobile = models.IntegerField()

    class Meta:
        managed = False
        db_table = "sales_info_pre"
