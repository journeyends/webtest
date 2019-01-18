from django.db import models


class SysRes(models.Model):
    res_id = models.AutoField(primary_key=True, db_column="RESID")
    res_name = models.CharField(max_length=128, db_column="RESNAME")
    alias = models.CharField(max_length=128, db_column="ALIAS")
    sn = models.IntegerField(db_column="SN")
    icon = models.CharField(max_length=100, db_column="ICON")
    parent_id = models.IntegerField(db_column="PARENTID")
    default_url = models.CharField(max_length=256, db_column="DEFAULTURL")
    is_folder = models.IntegerField(db_column="ISFOLDER")
    is_display_in_menu = models.IntegerField(db_column="ISDISPLAYINMENU")
    is_open = models.IntegerField(db_column="ISOPEN")
    system_id = models.IntegerField(db_column="SYSTEMID")
    is_new_open = models.IntegerField(db_column="ISNEWOPEN")
    path = models.CharField(max_length=500, db_column="PATH")
    is_common = models.IntegerField()
    is_only_hyperlink = models.IntegerField()
    is_button = models.IntegerField()
    button_type = models.IntegerField()
    icon_class = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = "sys_res"
