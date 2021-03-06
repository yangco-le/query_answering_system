from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),  # 首页
    path('createq/', views.create_question),  # 跳转创建问题页面
    path('updateq/<int:id>', views.update_question), # 问题修改页面
    path('question/<int:id>/', views.question_detail, name='question_detail'),  # 问题详情界面
    path('question-delete/<int:id>/', views.question_delete),  # 删除问题
    path('select/', views.select, name='select'),  # 问题筛选页面
    path('selecting/', views.selecting, name='selecting'),  # 筛选问题
    path('select/<int:sequencing>/<int:question_subject>/', views.select_result,  # 问题筛选结果页面 sequencing为0,1,2
         name='select_result'),  # 分别代表按浏览量降序、点赞量降序、发布时间降序排列
    path('all_question/', views.all_question),  # 浏览所有问题 按照时间顺序排列
    path('all_question/<int:sequencing>/', views.all_question2),  # 浏览所有问题 3种排列顺序
    path('question-comment/<int:question_id>/', views.question_comment, name='question_comment'),  # 问题评论
    path('question-tipoff/<int:question_id>/', views.question_tipoff, name='question_tipoff'),  # 举报问题
    path('question-good/<int:question_id>/', views.question_good, name='question_good'),  # 点赞问题
    path('comment-good/<int:question_id>/<int:comment_id>/', views.comment_good, name='comment_good'),  # 点赞评论
    path('search/', views.search),  # 问题搜索单选框
    path('search_both/', views.search_both, name="search_both"),  # 搜索问题新
    path('search_subject/', views.search_subject, name="search_subject"),  # 按科目搜索问题
    path('search_keyword/', views.search_keyword, name='search_keyword'),  # 按关键字搜索问题
    path('login/', views.user_login, name='login'),  # 登陆
    path('register/', views.user_register, name='register'),  # 注册
    path('logout/', views.user_logout, name='logout'),  # 登出
    path('userpage/', views.userpage, name='userpage'),  # 用户主页
    path('userpage/edit/', views.userpage_edit, name='user_edit'),  # 个人信息编辑
    path('userpage/related_discuss/', views.userpage_related_discuss),  # 查看参与的讨论
    path('userpage/collect_question/', views.userpage_collect_question),  # 查看收藏的问题
    path('question_fav/<int:question_id>/', views.question_fav, name='question_fav'),  # 收藏问题
]