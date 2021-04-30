
from django.shortcuts import render
from joblib import  load
from django.template import Context , Template

def home(request):
    return render (request,'home.html')

def prediction(request):
    return render (request,'prediction.html')

def result(request):
    try:
        var1 = float(request.GET['n1'])
        var2 = float(request.GET['n2'])
        var3 = float(request.GET['n3'])
        var4 = float(request.GET['n4'])
        var5 = float(request.GET['n5'])
        var6 = float(request.GET['n6'])
        var7 = float(request.GET['n7'])
        var8 = float(request.GET['n8'])
        m3 = load('preprocessing/Quad.joblib')
        m4 = load('preprocessing/neigh.joblib')
        m5 = load('preprocessing/dummy_clf.joblib')
        m6 = load('preprocessing/Quad.joblib')

        p1 = m3.predict([[var1,var2,var3,var4,var5,var6,var7,var8]])
        p2 = m4.predict([[var1,var2,var3,var4,var5,var6,var7,var8]])
        p3 = m5.predict([[var1,var2,var3,var4,var5,var6,var7,var8]])
        p4 = m6.predict([[var1,var2,var3,var4,var5,var6,var7,var8]])
        result1 =""
        result2= ""
        result3= ""
        result4= ""

        if p1 == [1]:
            result1= "positive"
        else:
            result1 = "negative"

        if p1 == [1]:
            result2= "positive"
        else:
            result2 = "negative"

        if p1 == [1]:
            result3= "positive"
        else:
            result3 = "negative"


        if p1 == [1]:
            result4= "positive"
        else:
            result4 = "negative"



        return render(request,'prediction.html',{"doctor1":result1,"doctor2":result2,"doctor3":result3,"doctor4":result4})
    except Exception:
        return render(request,'prediction.html')















