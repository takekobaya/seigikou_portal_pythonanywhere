from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  TemplateView)
from . import models
import os

'''
#ホーム画面
class Home(ListView):
    model = models.Event
    template_name = "Home.html"
'''
#一覧画面
class EventList(ListView):
    #Companyテーブル連携
    model = models.Event
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "event_list"
    #テンプレートファイル連携
    template_name = "Event_list.html"

#詳細画面
class EventDetail(DetailView):
    #Companyテーブル連携
    model = models.Event
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "event_detail"
    #テンプレートファイル連携
    template_name = "Event_detail.html"

#Create(イベント)画面
class EventCreateView(CreateView):
    #Companyテーブル連携
    model = models.Event
    #入力項目定義
    fields = ("day","starttime","endtime","location",
              "name","public","contents","question_url","member")
    #テンプレートファイル連携
    template_name = "Event_form.html"
    #更新後のリダイレクト先
    def get_success_url(self):
        return reverse('App:detail', kwargs={'pk': self.object.pk})

#メンバーリスト画面
class MemberList(ListView):
    #Companyテーブル連携
    model = models.Member
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "member_list"
    #テンプレートファイル連携
    template_name = "member_list.html"

#詳細画面
class MemberDetail(DetailView):
    #Companyテーブル連携
    model = models.Member
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "member_detail"
    #テンプレートファイル連携
    template_name = "Member_detail.html"

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_staff:
            return redirect('/home')
        return super().get(request)

#Create(メンバー)画面
class EventCreateView2(CreateView):
    #Companyテーブル連携
    model = models.Member
    #入力項目定義
    fields = ("name","shikaku","bumon","kaiin","mlmemb",
              "honbu","pref","company","senmon","bukai","other")
    #テンプレートファイル連携
    template_name = "Event_form.html"
    #作成後のリダイレクト先
    success_url = reverse_lazy("App:memberlist")

#講演リスト画面
class KouenList(ListView):
    #Companyテーブル連携
    model = models.Kouen
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "kouen_list"
    #テンプレートファイル連携
    template_name = "kouen_list.html"

#詳細画面
class KouenDetail(DetailView):
    #Companyテーブル連携
    model = models.Kouen
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "kouen_detail"
    #テンプレートファイル連携
    template_name = "kouen_detail.html"

#Create(講演)画面
class EventCreateView3(CreateView):
    #Companyテーブル連携
    model = models.Kouen
    #入力項目定義
    fields = ("koushi","name","youshi","event")
    #テンプレートファイル連携
    template_name = "Event_form.html"
    #作成後のリダイレクト先
    success_url = reverse_lazy("App:kouenlist")

#Upadate画面(イベント情報)
class EventUpdateView(UpdateView):
    #入力項目定義
    fields =  ("day","starttime","endtime","location",
              "name","public","contents","question_url","member")
    #Companyテーブル連携
    model = models.Event
    #テンプレートファイル連携
    template_name = "Event_form.html"
    #更新後のリダイレクト先
    def get_success_url(self):
        return reverse('App:detail', kwargs={'pk': self.object.pk})

#更新画面(メンバー情報)
class EventUpdateView2(UpdateView):
    #入力項目定義
    fields =  ("name","shikaku","bumon","kaiin","mlmemb",
              "honbu","pref","company","senmon","bukai","other")
    #メンバーテーブル連携
    model = models.Member
    #テンプレートファイル連携
    template_name = "Event_form.html"
    #更新後のリダイレクト先
    success_url = reverse_lazy("App:memberlist")

#更新(講演)画面
class EventUpdateView3(UpdateView):
    #入力項目定義
    fields = ("koushi","name","youshi","event")
    #テーブル連携
    model = models.Kouen
    #テンプレートファイル連携
    template_name = "Event_form.html"
    #作成後のリダイレクト先
    success_url = reverse_lazy("App:kouenlist")

#削除画面
class EventDeleteView(DeleteView):
    #イベントテーブル連携
    model = models.Event
    #テンプレートファイル連携
    template_name = "Event_delete.html"
    #削除後のリダイレクト先
    success_url = reverse_lazy("App:eventlist")

    def get(self, request, **kwargs):
        if not request.user.is_staff:
            return redirect('/eventlist')
        return super().get(request)


#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('App:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'login.html')


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('App:Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "home.html",context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            #if 'account_image' in request.FILES:
            #    add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)
    

def download_ppt(request):
    # ダウンロードするファイルのパス
    file_path = os.path.join(settings.MEDIA_ROOT, 'template.pptx')
    
    # ファイルをバイナリ形式で読み込む
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    # HttpResponseオブジェクトを作成して、ファイルをダウンロードさせる
    response = HttpResponse(file_data, content_type='application/vnd.ms-powerpoint')
    response['Content-Disposition'] = 'attachment; filename="template.pptx"'
    return response


