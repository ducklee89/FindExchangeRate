from django.db import models

# Create your models here.
class exval(models.Model):
    objects     = models.Manager()  #VS code오류 제거용
    exval_id = models.CharField(max_length=100,primary_key=True) # 날짜 + 통화기호 # 20191111AUD # date+row['cur_unit']
    exval_unit   = models.CharField(max_length=100)
    exval_ttb = models.FloatField()  # 길이 제한이 없는 문자열
    exval_tts   = models.FloatField()
    exval_deal     = models.FloatField()
    exval_bkpr    = models.FloatField() 
    exval_kftc_bk = models.FloatField()
    exval_kftc_de = models.FloatField()
    exval_cur_nm = models.CharField(max_length=100)
    
    
    def __str__(self):
        return str(self.exval_id) #문자만 가능
