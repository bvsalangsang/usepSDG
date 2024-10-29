from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

from .sqlparams import *
from .sqlcommands import * 

# Create your views here.
def index(request):
    return render(request,'themes/index.html')

def commitment(request):
    return render(request, 'themes/commitment.html')

def strategy(request):
    return render(request, 'themes/strategy.html')

def sustainPPA(request):
    return render(request, 'themes/sustainability-ppa.html')

def contact(request):
    return render(request, 'themes/contact.html')

def scorecard(request):
    return render(request, 'themes/sdg-scorecard.html')


def goal1(request):
    return render(request,'themes/goal1.html')

def goal2(request):
    return render(request,'themes/goal2.html')

def goal3(request):
    return render(request,'themes/goal3.html')

def goal4(request):
    return render(request,'themes/goal4.html')


def goal5(request):
    return render(request,'themes/goal5.html')

def goal6(request):
    return render(request,'themes/goal6.html')

def goal7(request):
    return render(request,'themes/goal7.html')

def goal8(request):
    return render(request,'themes/goal8.html')

def goal9(request):
    return render(request,'themes/goal9.html')

def goal10(request):
    return render(request,'themes/goal10.html')

def goal11(request):
    return render(request,'themes/goal11.html')

def goal12(request):
    return render(request,'themes/goal12.html')

def goal13(request):
    return render(request,'themes/goal13.html')

def goal14(request):
    return render(request,'themes/goal14.html')

def goal15(request):
    return render(request,'themes/goal15.html')

def goal16(request):
    return render(request,'themes/goal16.html')

def goal17(request):
    return render(request,'themes/goal17.html') 

def goalTopic(request):
    return render(request,'themes/goal-topic.html')

def goalJsonFetchPerId(request,id):
    sgdParams['sdgId'] = id
    with connection.cursor() as cursor:
        cursor.execute(sdgDetailsViewPerId(**sgdParams))
        rows = cursor.fetchall()

        sdg = {}
        target_map = {}
        indicators_map = {}

        for row in rows:
            sdgId = row[0]
            if sdgId not in sdg:
                sdg[sdgId] = {
                    "sdgId": row[0],
                    "sdgName": row[1],
                    "description": row[2],
                    "isActive": row[3],
                    "targets": []
                }

            targetId = row[4]
            if targetId:
                if targetId not in target_map:
                    tgt = {
                        "sdgId": row[0],
                        "targetId": row[4],
                        "targetCode": row[6],
                        "targetDesc": row[7],
                        "isActive": row[8],
                        "indicators": []
                    }
                    sdg[sdgId]["targets"].append(tgt)
                    target_map[targetId] = tgt
                else:
                    tgt = target_map[targetId]

                ind_id = row[9]
                if ind_id and ind_id not in indicators_map:
                    ind = {
                        "indId": row[9],
                        "targetId": row[10],
                        "indCode": row[11],
                        "indDesc": row[12],
                        "isActive": row[13],
                    }
                    tgt["indicators"].append(ind)
                    indicators_map[ind_id] = ind

        data = list(sdg.values())
        return JsonResponse({"data": data}, json_dumps_params={'indent': 2})


def test(request):
    return render(request,'themes/test.html')

