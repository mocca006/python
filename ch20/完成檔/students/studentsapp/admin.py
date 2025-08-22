from django.contrib import admin
from studentsapp.models import student

class studentAdmin(admin.ModelAdmin):
    # �ĤT�ؤ覡�A�[�J ModelAdmin ���O�A�w�q������B���L�o��ơB�j�M�M�Ƨ�
 	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
 	list_filter=('cName','cSex')
 	search_fields=('cName',)
 	ordering=('id',)
 	
admin.site.register(student,studentAdmin)

	
# �Ĥ@�ؤ覡�A���[�J ModelAdmin ���O 
# admin.site.register(student)	

# �ĤG�ؤ覡�A�[�J ModelAdmin ���O�A�w�q������
# class studentAdmin(admin.ModelAdmin):
# 	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
# admin.site.register(student,studentAdmin)