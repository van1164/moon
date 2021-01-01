from django.shortcuts import render
from . import urls
from .models import dataxx
import time
import csv
import os.path
# Create your views here.
def home(request):
    return render(request,'polls/home.html',{})

def finish(request):
    if request.method == "POST":
        q1 = request.POST.get("quest_1",'None')
        q2 = request.POST.get("quest_2", '2')
        q3 = request.POST.get("quest_3", '2')
        q4 = request.POST.get("quest_4", '2')
        q5 = request.POST.get("quest_5", '2')
        q6 = request.POST.get("quest_6", '2')
        q7 = request.POST.get("quest_7", '2')
        q8 = request.POST.get("quest_8", '2')
        q9 = request.POST.get("quest_9", '2')
        q10 = request.POST.get("quest_10", '2')
        lst = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
        name = 'check'+str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + '.csv'
        if os.path.exists(name):
            pass
        else:
            f = open(name,'w')
            f.close()

        f = open(name,'a', encoding="UTF-8")
        rdr = csv.writer(f)
        rdr.writerow(lst)
        f.close()

    return render(request, 'polls/finish.html',{})

def check(request):
    power = {}
    all_key_dict = {}
    all_list = dataxx.objects.all().order_by('name') # 전체 사람 리스트
    for i in dataxx.objects.all().order_by('name'):
        all_key_dict[i.number] = [i.name,i.unit,i.rank]
    def name_check(lst:list):
        result =[]
        for i in lst:
            result.append(i[0])
        return result
    name = 'check'+str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + '.csv'
    result = []
    non_result = []
    if os.path.exists(name):
        f = open(name,'r', encoding = "UTF-8")
        rdr = csv.reader(f)
        for x in rdr:
            if x==[]:
                pass

            else:
                if(all_key_dict.get(int(x[0]),'NONE')!='NONE'):
                    x.insert(0,all_key_dict[int(x[0])][0])
                    x.insert(1,all_key_dict[int(x[1])][1])
                    x.insert(2,all_key_dict[int(x[2])][2])
                    del x[3]
                    result.append(x)

        name_list = name_check(result) #현재 설문에 참여한 사람 리스트
        for i in all_key_dict.values():
            non_result.append(i)
        all_name_list = []
        for i in dataxx.objects.all().order_by('name'):
            all_name_list.append(i.name)
        tmp = len(all_name_list)
        for i in range(0,len(name_list)):
            for j in non_result:
                if name_list[i] in j:
                    all_name_list.remove(name_list[i])
                    non_result.remove(j)
        power['current'] = non_result  # 미실시자
        power['result'] =result


        number_all = 100 - (len(all_name_list)/tmp) *100
        power['number_all'] = int(number_all)


        print(non_result)
        count_1 =0
        for i in result:
            if(i[3] == '1'):
                count_1+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_11 = 100 - int(count_1/len(result)*100)
            power['count_1'] = count_11

        count_2 =0
        for i in result:
            if(i[4] == '1'):
                count_2+=1 
        if(len(result)==0):
            power['count_2'] = 0
        else:
            count_21 = 100 - int(count_2/len(result)*100)
            power['count_2'] = count_21

        count_3 =0
        for i in result:
            if(i[5] == '1'):
                count_3+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_31 = 100 - int(count_3/len(result)*100)
            power['count_3'] = count_31

        count_4 =0
        for i in result:
            if(i[6] == '1'):
                count_4+=1 
        if(len(result)==0):
            power['count_4'] = 0
        else:
            count_41 = 100 - int(count_4/len(result)*100)
            power['count_4'] = count_41

        count_5 =0
        for i in result:
            if(i[7] == '1'):
                count_5+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_51 = 100 - int(count_5/len(result)*100)
            power['count_5'] = count_51

        count_6 =0
        for i in result:
            if(i[8] == '1'):
                count_6+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_61 = 100 - int(count_6/len(result)*100)
            power['count_6'] = count_61

        count_7 =0
        for i in result:
            if(i[9] == '1'):
                count_7+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_71 = 100 - int(count_7/len(result)*100)
            power['count_7'] = count_71

        count_8 =0
        for i in result:
            if(i[10] == '1'):
                count_8+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_81 = 100 - int(count_8/len(result)*100)
            power['count_8'] = count_81

        count_9 =0
        for i in result:
            if(i[11] == '1'):
                count_9+=1 
        if(len(result)==0):
            power['count_1'] = 0
        else:
            count_91 = 100 - int(count_9/len(result)*100)
            power['count_9'] = count_91






        
            
    else:
        rdr = open(name,'w',encoding="UTF-8")
        rdr.close()
    
    power['name1'] = str(time.localtime().tm_year) +"년 "+ str(time.localtime().tm_mon)+"월 " + str(time.localtime().tm_mday)+"일 "+" 8사단 코로나 문진표 현황"

    return render(request,'polls/check.html',power)