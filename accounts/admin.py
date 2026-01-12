from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
# カスタムユーザーの設定方法　変更する必要がある。　2026年1月12日 アカウントappの作成　settingに登録 models を作成　Adminの編集　今ここ　
class CustomUserAdmin(UserAdmin):
    #自作を追加する
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('birthday','height','comment',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('birthday','height','comment',)}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
