from django.contrib import admin
# モデルをインポート
from . models import (Member,Event,Kouen,Shikaku,Bumon,Kaiin,Mlmemb,Account)
#from import_export import resources
#from import_export.admin import ImportExportMixin
'''
class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

        #import_order = ('id', 'name', 'shikaku')
        #import_id_fields = ['id']


class MemberAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'shikaku','company')
    resource_class = MemberResource
'''
# 管理ツールに登録
#admin.site.register(Member,MemberAdmin)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Kouen)
admin.site.register(Shikaku)
admin.site.register(Bumon)
admin.site.register(Kaiin)
admin.site.register(Mlmemb)
admin.site.register(Account)