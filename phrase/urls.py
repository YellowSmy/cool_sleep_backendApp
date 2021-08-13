from django.urls import path
from . import views
from .drf_api import Apiviews

urlpatterns = [
    ### API VIEW ###
    path('randomphrase/', Apiviews.randomPhrase),
    path('randomknowledge/', Apiviews.randomKnowledge),


    ### UI ###
    #Main
    path('', views.phraselist, name="phraselist"), #main page

    #Detail Page
    path('showphrase/<int:id>/', views.showPhrase, name="showPhrase"), #개별로 명언 보여주기
    path('showknowledge/<int:id>/',views.showKnowledge, name="showKnowledge"), #개별로 수면지식 보여주기

    #### 명언 출력 path ####
    #Create
    path('newphrase/', views.newphrase, name="newphrase"), #POST 처리 위한 form 생성 
    path('createphrase/', views.createphrase, name="createphrase"), #POST 처리 page
    #Update
    path('editknowledge/', views.editphrase, name="editphrase"),
    path('updatephrase/<int:id>/', views.updatephrase, name="updatephrase"),
    #Delete
    path('deletephrase/<int:id>/', views.deletephrase, name="deletephrase"),


    #### 수면지식출력 path ####
    #Create
    path('newknowledge/', views.newknowledge, name="newknowledge"),
    path('createknowledge/', views.createknowledge, name="createknowledge"),
    #Update
    path('editknowledge/', views.editknowledge, name="editknowledge"),
    path('updateknowledge/<int:id>/', views.updateknowledge, name="updateknowledge"),
    #Delete
    path('deleteknowledge/<int:id>/', views.deleteknowledge, name="deleteknowledge"),
]