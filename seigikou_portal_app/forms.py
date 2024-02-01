from django import forms
from django.contrib.auth.models import User
from .models import Account
from .models import Member

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"Ｅメール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        #fields = ('last_name','first_name')
        #labels = {'last_name':"苗字",'first_name':"名前"}
        fields = ('last_name','first_name','account_image','secret_word')
        labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",'secret_word':"秘密の言葉"}

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("name", "shikaku", "bumon", "kaiin", "mlmemb",
                  "honbu", "pref", "company", "senmon", "bukai", "other", "image")
        labels = {'name':"名前","shikaku":"資格", "bumon":"部門", "kaiin":"会員種別", "mlmemb":"MLメンバー",
                  "honbu":"地域本部", "pref":"都道府県", "company":"所属", "senmon":"専門分野", "bukai":"部会", "other":"その他", "image":"写真"}