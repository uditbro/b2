from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    #Path for home page.
    path('',views.index,name = 'index'),
    # path for topics page.
    path('topics/',views.topics, name="topics"),
    # individual detail topic page.
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    # Page for adding a new topic.
    path('new_topic/',views.new_topic, name="new_topic"),
    #path for new entry.
    path('new_entry/<int:topic_id>/',views.new_entry, name="new_entry"),
    #Page for editing entries.
    path('edit_entry/<int:entry_id>/',views.edit_entry, name="edit_entry"),
]
