from django.urls import path
from main.views import show_main
from main.views import show_main, create_item
from main.views import show_main, create_item, show_xml 
from main.views import show_main, create_item, show_xml, show_json
from main.views import show_main, create_item , show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user
from main.views import delete
from main.views import edit_item
from main.views import get_item_json
from main.views import add_item_ajax
from main.views import EditItemAjaxView
from . import views  # Make sure this import is present

app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('edit-item-ajax/', views.EditItemAjaxView.as_view(), name='edit_item_ajax'),
    
]