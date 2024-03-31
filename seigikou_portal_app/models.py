from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):
    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)
    secret_word = models.CharField(max_length=20, default='')  # デフォルト値を設定

    def __str__(self):
        return self.user.username

#資格情報を格納するテーブル
class Shikaku(models.Model):
    name    = models.CharField(max_length=20)

    class Meta:
        db_table = 'Shikaku'
    def __str__(self):
        return self.name

#部門情報を格納するテーブル
class Bumon(models.Model):
    name    = models.CharField(max_length=20)

    class Meta:
        db_table = 'Bumon'
    def __str__(self):
        return self.name

#会員種別を格納するテーブル
class Kaiin(models.Model):
    name    = models.CharField(max_length=20)

    class Meta:
        db_table = 'Kaiin'

    def __str__(self):
        return self.name
        
#会員種別を格納するテーブル
class Mlmemb(models.Model):
    name    = models.CharField(max_length=20)

    class Meta:
        db_table = 'Mlmemb'

    def __str__(self):
        return self.name

#メンバー情報を格納するテーブル
class Member(models.Model):
    membercode = models.CharField(max_length=4,blank=True,null=True)
    name    = models.CharField(max_length=20)
    shikaku   = models.ForeignKey(Shikaku,on_delete=models.PROTECT,blank=True,null=True)
    bumon   = models.ManyToManyField(Bumon,related_name='bumon',blank=True)
    kaiin  = models.ForeignKey(Kaiin,related_name='kaiin',on_delete=models.PROTECT,blank=True,null=True)
    mlmemb = models.ForeignKey(Mlmemb,related_name='mlmemb',on_delete=models.PROTECT,blank=True,null=True)
    honbu = models.CharField(max_length=20,blank=True,null=True)
    pref = models.CharField(max_length=20,blank=True,null=True)
    company = models.CharField(max_length=20,blank=True,null=True)
    senmon = models.CharField(max_length=50,blank=True,null=True)
    bukai = models.CharField(max_length=20,blank=True,null=True)
    other = models.CharField(max_length=256,blank=True,null=True)
    image = models.ImageField(upload_to="profile_pics",blank=True)

    class Meta:
        db_table = 'Member'

    def __str__(self):
        return self.name

#イベント情報を格納するテーブル
class Event(models.Model):
    eventcode = models.CharField(max_length=7,blank=True,null=True)
    day       = models.DateField()
    starttime = models.TimeField()
    endtime   = models.TimeField()
    location  = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=50)
    public = models.CharField(max_length=20,blank=True,null=True)
    contents = models.TextField(max_length=512,blank=True,null=True)
    question_url = models.URLField(max_length=100,blank=True,null=True)
    member = models.ManyToManyField(Member,related_name='Members',blank=True)
    SNSLink_url = models.CharField(max_length=1024,blank=True,null=True)

    class Meta:
        db_table = 'Event'

    def __str__(self):
        return self.name

#講演情報を格納するテーブル
class Kouen(models.Model):
    kouencode = models.CharField(max_length=7,blank=True,null=True)
    koushi = models.CharField(max_length=256)
    company = models.CharField(max_length=100,blank=True,null=True)
    name    = models.CharField(max_length=256)
    youshi   = models.TextField(max_length=512,blank=True,null=True)
    event = models.OneToOneField(Event,related_name='kouen',on_delete=models.CASCADE)

    class Meta:
        db_table = 'Kouen'

    def __str__(self):
        return self.name
        