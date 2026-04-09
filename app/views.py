from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import math
def home(request):
    d={}
    if request.method == "POST":
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))

        gcd = math.gcd(num1,num2)
        snum1 = num1//gcd
        snum2 = num2//gcd

        d={
        'res':f"{snum1}:{snum2}",
        'num1':num1,
        'num2':num2,
        'gcd':gcd,
        'snum1':snum1,
        'snum2':snum2,
        }
    return render(request,'home.html',d)
