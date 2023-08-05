from django.urls import path

from StudentApp import views

urlpatterns = [
    path('', views.log_fun, name='log'),     # it will display login.html page
    path('logdata',views.logdata_fun),      # it will read data and verify as superuser and
                                            # redirect to home.html page
    path('reg',views.reg_fun,name='reg'),      # it will redirect to register.htmlpage
    path('regdata',views.regdata_fun),        # it will create superuser acc

    path('home',views.home_fun,name='home'),            # it will redirect to home.html
    path('add_students',views.addstudent_fun,name='add'),   #it will redirect to addstudent.html
    path('readdata',views.readdata_fun),                # it will insert record into student table
    path('display',views.display_fun,name='display'),    #it will display student table data in display.html
    path('update/<int:id>',views.update_fun,name='up'),   # it will update student data
    path('delete/<int:id>',views.delete_fun,name='del'),    #it will delete record from student table
    path('log_out',views.log_out_fun,name='log_out')
]