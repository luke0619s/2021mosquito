from django.shortcuts import render
from django.http import HttpResponse

import json
from pyecharts import options as opts
from pyecharts.charts import Bar
from rest_framework.views import APIView
from django.template.context_processors import request
from main import models

def main(request):
    return render(request, 'main/index.html', locals())

def maps(request):
    return render(request, 'main/map.html', locals())

def base(request):
    return render(request, 'main/base.html', locals())

def search(request): 
    num1 = range(1960,2021)
    num2 = range(1,13)
    num3 = range(1,32)
    try:
        name  = request.GET['name']
        year  = request.GET['year']
        month  = request.GET['month']
        day  = request.GET['day']
        result = models.local.objects.filter(name=name, year=year, month=month, day=day)
    except:
        name = 'fail'      
        
    return render(request, 'main/search.html', locals())

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)

def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)

JsonResponse = json_response
JsonError = json_error

def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8" ,"9", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30"])
        .add_yaxis("溫度", [30,25,27,29,32,30,31,28,27,25,26,28,30,31,33,29,27,28,30,33,32,31,30,28,29,28,30,33,32,28,30,26,27,31,35,34,30])
        .set_global_opts(title_opts=opts.TitleOpts(title="°C"))
        .dump_options_with_quotes()
    )
    return c
def bar_base2() -> Bar:
    c = (
        Bar()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8" ,"9", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30"])
        .add_yaxis("濕度", [28,23,25,27,30,28,29,27,25,23,24,26,28,29,25,27,24,26,24,28,30,29,27,28,26,25,30,24,27,28,30,26,27,25,24,23,27])
        .set_global_opts(title_opts=opts.TitleOpts(title="m3"))
        .dump_options_with_quotes()
    )
    return c
def bar_base3() -> Bar:
    c = (
        Bar()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8" ,"9", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30"])
        .add_yaxis("SO2", [1.2,1.3,1.6,1.6,1.9,2.4,2.3,1.8,1.9,2.2,1.5,1.4,1.6,1.8,2.3,2.4,2.1,1.8,1.9,2.2,1.8,1.4,1.6,1.8,2.3,2.4,2.0,1.8,1.9,1.6  ])
        .set_global_opts(title_opts=opts.TitleOpts(title="ppb"))
        .dump_options_with_quotes()
    )
    return c
def bar_base4() -> Bar:
    c = (
        Bar()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8" ,"9", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30"])
        .add_yaxis("PM2.5", [66,68,69,70,67,66,66,67,68,70,73,75,76,75,76,78,80,82,83,85,87,89,90,91,95,94,97,100,103,105,103,106,108,110,118,120,120])
        .set_global_opts(title_opts=opts.TitleOpts(title="μg/m3"))
        .dump_options_with_quotes()
    )
    return c
def bar_base5() -> Bar:
    c = (
        Bar()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8" ,"9", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30"])
        .add_yaxis("O3", [240,243,245,239,238,240,243,245,248,250,248,249,248,245,244,240,238,237,235,236,236,237,238,238,239,240,241,242,241,242,245,243,240,239,245,243,241])
        .set_global_opts(title_opts=opts.TitleOpts(title="ppb"))
        .dump_options_with_quotes()
    )
    return c
def bar_base6() -> Bar:
    c = (
        Bar()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8" ,"9", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23", "24","25", "26", "27","28", "29", "30"])
        .add_yaxis("本土及境外確診病例", [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1])
        .set_global_opts(title_opts=opts.TitleOpts(title="例"))
        .dump_options_with_quotes()
    )
    return c

class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base()))

class ChartView2(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base2()))
class ChartView3(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base3()))
class ChartView4(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base4()))
class ChartView5(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base5()))
class ChartView6(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar_base6()))  

class data(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/data.html')