from rest_framework import serializers
from .models import memoBoard
from crawling.models import exval

class MemoBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = memoBoard
        fields = (   'memo_no'
                    ,'memo_id'
                    ,'memo_priority'
                    ,'memo_productname'
                    ,'memo_cur_unit'
                    ,'memo_price'
                    ,'memo_producturl'
                    ,'memo_memo'
                    ,'memo_regdate'
                    ,'memo_lastdate')    

class ExvalSerializer(serializers.ModelSerializer):
    class Meta:
        model = exval
        fields = ('exval_id'     
,'exval_unit'   
,'exval_ttb'    
,'exval_tts'    
,'exval_deal'   
,'exval_bkpr'   
,'exval_kftc_bk'
,'exval_kftc_de'
,'exval_cur_nm' )