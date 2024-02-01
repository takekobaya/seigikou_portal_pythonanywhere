from django import forms
from django.contrib.auth.models import User
from .models import Account,Event,Member,Kouen

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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields =("day","starttime","endtime","location",
              "name","public","contents","question_url","member")
        labels = {"day":"開催日","starttime":"開始時間","endtime":"終了時間","location":"開催場所",
              "name":"イベント名","public":"公開範囲","contents":"次第","question_url":"アンケートURL","member":"参加者"}

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("name", "shikaku", "bumon", "kaiin", "mlmemb",
                  "honbu", "pref", "company", "senmon", "bukai", "other", "image")
        labels = {'name':"名前","shikaku":"資格", "bumon":"部門", "kaiin":"会員種別", "mlmemb":"MLメンバー",
                  "honbu":"地域本部", "pref":"都道府県", "company":"所属", "senmon":"専門分野", "bukai":"部会", "other":"その他", "image":"写真"}
        
class KouenForm(forms.ModelForm):
    class Meta:
        model = Kouen
        fields = ("koushi","company","name","youshi","event")
        labels = {"koushi":"講師","company":"所属","name":"演題","youshi":"要旨","event":"開催イベント"}