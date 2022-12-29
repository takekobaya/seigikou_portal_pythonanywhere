#path関数をインポート
from django.urls import path
#同ディレクトリからview.pyをインポート
from . import views

app_name = "App"

#path関数(アクセスするアドレス、呼び出す処理)を追記
urlpatterns = [
    path('', views.Login, name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('register', views.AccountRegistration.as_view(), name='register'),
    path('home',views.home,name='home'),
    path('eventlist/', views.EventList.as_view(), name='eventlist'),          #イベント一覧画面
    path('eventlist/detail/<int:pk>/',views.EventDetail.as_view(),name='detail'),       #イベント詳細画面
    path('create/',views.EventCreateView.as_view(),name='create'),            #新規登録画面(イベント)
    path('memberlist/', views.MemberList.as_view(), name='memberlist'),          #メンバー一覧画面
    path('memberlist/detail2/<int:pk>/',views.MemberDetail.as_view(),name='detail2'),       #メンバー詳細画面
    path('create2/',views.EventCreateView2.as_view(),name='create2'),         #新規登録画面(メンバー)
    path('kouenlist/', views.KouenList.as_view(), name='kouenlist'),          #講演一覧画面
    path('kouenlist/detail3/<int:pk>/',views.KouenDetail.as_view(),name='detail3'),       #講演詳細画面
    path('create3/',views.EventCreateView3.as_view(),name='create3'),         #新規登録画面(講演)
    path('update/<int:pk>/',views.EventUpdateView.as_view(),name='update'),   #更新画面(イベント)
    path('update2/<int:pk>/',views.EventUpdateView2.as_view(),name='update2'),   #更新画面(メンバー)
    path('update3/<int:pk>/',views.EventUpdateView3.as_view(),name='update3'),   #更新画面(講演)
    path('delete/<int:pk>/',views.EventDeleteView.as_view(),name='delete'),   #削除画面(イベント)
]