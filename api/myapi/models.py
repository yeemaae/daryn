from django.db import models


class DataBase(models.Model):
    daryn_id = models.IntegerField(primary_key=True)
    olymp_id = models.IntegerField()
    school_id = models.IntegerField()
    iin = models.CharField(max_length=12)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    grade = models.IntegerField()
    points = models.IntegerField()
    place = models.CharField(max_length=255)
    teacher_first_name = models.CharField(max_length=255)
    teacher_last_name = models.CharField(max_length=255)
    teacher_father_name = models.CharField(max_length=255, blank=True, null=True)
    cert_register = models.CharField(max_length=255)
    dip_register = models.CharField(max_length=255)
    cert_key = models.CharField(max_length=255)
    dip_key = models.CharField(max_length=255)
    teacher_iin = models.CharField(max_length=12)
    place_update_date = models.DateField()
    printed = models.BooleanField()
    subject_id = models.IntegerField()
    region_kz_txt = models.CharField(max_length=255)
    school_kz_txt = models.CharField(max_length=255)
    teacher_first_name_2 = models.CharField(max_length=255, blank=True, null=True)
    teacher_last_name_2 = models.CharField(max_length=255, blank=True, null=True)
    teacher_father_name_2 = models.CharField(max_length=255, blank=True, null=True)
    teacher_iin_2 = models.CharField(max_length=12, blank=True, null=True)
    pr_id = models.CharField(max_length=255)
    date_of_event = models.DateField()
    send_to_nobd = models.IntegerField()

    def __str__(self):
        return self.first_name
