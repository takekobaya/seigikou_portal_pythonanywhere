from django import forms
from django.contrib.auth.models import User
from .models import Account,Event,Member,Kouen
from django.forms.widgets import DateInput,TimeInput

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
        labels = {"day":"開催日  ","starttime":"開始時間","endtime":"終了時間","location":"開催場所",
              "name":"イベント名","public":"公開範囲","contents":"次第","question_url":"アンケートURL","member":"参加者"}
        widgets = {
            'day': DateInput(format='%Y/%m/%d', attrs={'type': 'date'}),
            'starttime': TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'endtime': TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:  # インスタンスが存在する場合
            initial_data = {
                'day': self.instance.day.strftime('%Y-%m-%d') if self.instance.day else None,
                'starttime': self.instance.starttime.strftime('%H:%M') if self.instance.starttime else None,
                'endtime': self.instance.endtime.strftime('%H:%M') if self.instance.endtime else None,
                # 他のフィールドも同様に追加
            }
            self.initial.update(initial_data)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("name", "shikaku", "bumon", "kaiin", "mlmemb",
                  "honbu", "pref", "company", "senmon", "bukai", "other", "image")
        labels = {'name':"名前","shikaku":"資格", "bumon":"部門", "kaiin":"会員種別", "mlmemb":"MLメンバー",
                  "honbu":"地域本部", "pref":"都道府県", "company":"所属", "senmon":"専門分野", "bukai":"部会", "other":"自己紹介", "image":"写真"}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'shikaku': forms.Select(attrs={'class': 'form-control'}),
            'bumon': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'kaiin': forms.Select(attrs={'class': 'form-control'}),
            'mlmemb': forms.Select(attrs={'class': 'form-control'}),
            'honbu': forms.TextInput(attrs={'class': 'form-control'}),
            'pref': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'senmon': forms.TextInput(attrs={'class': 'form-control'}),
            'bukai': forms.TextInput(attrs={'class': 'form-control'}),
            'other': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:  
            # インスタンスが存在する場合、写真の初期値を設定する
            self.fields['image'].initial = self.instance.image.url if self.instance.image else None

class KouenForm(forms.ModelForm):
    class Meta:
        model = Kouen
        fields = ("koushi","company","name","youshi","event")
        labels = {"koushi":"講師","company":"所属","name":"演題","youshi":"要旨","event":"開催イベント"}
        widgets = {
            'koushi': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'youshi': forms.Textarea(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
        }