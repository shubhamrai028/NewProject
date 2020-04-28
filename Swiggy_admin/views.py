from django.shortcuts import render,redirect
from Swiggy_admin.models import AdminLoginModel
from django.contrib import messages
from Swiggy_admin.forms import *
from Swiggy_admin.models import *

# Create your views here.
def admin_login(request):
    return render(request, "swiggy_admin/login.html")


def adminLogin_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername,password=apassword)
        request.session['status'] = True
        return redirect('admin_home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request,"Sorry Invalid Username or Password")
        return redirect('admin_login')



def admin_home(request):
    return render(request, "swiggy_admin/admin_home.html")


def admin_logout(request):
    request.session['status'] = False
    return redirect('admin_login')


def open_state(request):
    return render(request, 'swiggy_admin/open_state.html', {"sf": StateForm(), "sdata": StateModel.objects.all()})


def save_state(request):
    sf = StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request, "swiggy_admin/open_state.html", {"sf": sf})


def update_state(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno": sno, "sname": sname}
    return render(request, "swiggy_admin/open_state.html", {"update_data": d1, "sdata": StateModel.objects.all()})


def update_state_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    StateModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


def open_city(request):
    return render(request, 'swiggy_admin/open_city.html', {"sf": CityForm(), "sdata": CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, "swiggy_admin/open_city.html", {"sf": sf})


def update_city(request):
    cno=request.GET.get("cno")
    cname=request.GET.get("cname")
    d2={"cno":cno,"cname":cname}
    return render(request, "swiggy_admin/open_city.html", {"update_data": d2, "sdata": CityModel.objects.all()})


def update_city_data(request):
    cno=request.POST.get("v1")
    cname=request.POST.get("v2")
    CityModel.objects.filter(city_no=cno).update(city_name=cname)
    return redirect('open_city')


def delete_city(request):
    cno = request.GET.get("cno")
    CityModel.objects.filter(city_no=cno).delete()
    return redirect('open_city')


def open_area(request):
    return render(request, 'swiggy_admin/open_area.html', {"sf": AreaForm(), "sdata": AreaModel.objects.all()})


def save_area(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        return render(request, "swiggy_admin/open_city.html", {"sf": sf})


def update_area(request):
    ano = request.GET.get("areano")
    aname = request.GET.get("areaname")
    d3 = {"ano": ano, "aname": aname}
    return render(request, "swiggy_admin/open_area.html", {"update_data": d3, "sdata": AreaModel.objects.all()})


def update_area_data(request):
    ano = request.POST.get("r1")
    aname = request.POST.get("r2")
    AreaModel.objects.filter(area_no=ano).update(area_name=aname)
    return redirect('open_area')


def delete_area(request):
    ano = request.GET.get("areano")
    AreaModel.objects.filter(area_no=ano).delete()
    return redirect('open_area')


def open_type(request):
    return render(request, 'swiggy_admin/open_type.html', {"sf": RestaurantTypeForm(), "sdata": RestaurantTypeModel.objects.all()})


def save_type(request):
    sf = RestaurantTypeForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_type')
    else:
        return render(request, "swiggy_admin/open_type.html", {"sf": sf})


def update_type(request):
    typeno = request.GET.get("typeno")
    typename = request.GET.get("typename")
    d4 = {"tno":typeno,"tname":typename}
    return render(request, "swiggy_admin/open_type.html", {"update_data": d4, "sdata": RestaurantTypeModel.objects.all()})


def update_type_data(request):
    tyno = request.POST.get("p1")
    tyname = request.POST.get("p2")
    RestaurantTypeModel.objects.filter(no=tyno).update(type_name=tyname)
    return redirect('open_type')
