from django.shortcuts import render  #import render for rendering html
from . import urls                   #import url for urlpattern
from .models import dataxx           #import models including user's name info
from .models import admin_account
from .models import 질문지
from .models import 제8기동사단
from .models import 정보통신대대
from .models import 직할공병대대
from .models import 직할군수지원대대
from .models import 기갑수색대대
from .models import 보충중대
from .models import 의무대
from .models import 군사경찰대
from .models import 본부대
from .models import 화생방지원대대
from .models import 정보대대
from .models import 사단직할대
from .models import 제101기보대대
from .models import 제122기보대대
from .models import 제137기보대대
from .models import 기갑군수지원대대
from .models import 기갑참모부
from .models import 기갑직할대
from .models import 기갑여단
from .models import 인사처
from .models import 정보처
from .models import 작전처
from .models import 군수처
from .models import 화력실
from .models import 교훈처
from .models import 지통처
from .models import 군종부
from .models import 공보정훈부
from .models import 재정부
from .models import 지휘부
from .models import 작계처
from .models import 감찰부
from .models import 법무부
from .models import 참모처
from .models import 제107기보대대
from .models import 제26전차대대
from .models import 제32전차대대
from .models import 제60군수지원대대
from .models import 제60직할대
from .models import 제60참모부
from .models import 제60여단
from .models import 제123기보대대
from .models import 제125기보대대
from .models import 제57전차대대
from .models import 제73군수지원대대
from .models import 제73직할대
from .models import 제73참모부
from .models import 제73여단
from .models import 제50포병대대
from .models import 제95포병대대
from .models import 제228포병대대
from .models import 제231포병대대
from .models import 포병직할대
from .models import 포병참모부
from .models import 포병여단

import time                          #import time to know time now
import csv                           #import csv to load check.csv
import os.path                       #import os.path for checking whether file exists

def style_decider(all, done): 
        if all == done: return "progress-bar bg-success" 
        else: return "progress-bar bg-danger" 

power = {}
def submit(request):
    power = {}
    print(request)
    q1 = request.POST.get("q1",'None')
    q2 = request.POST.get("q2",'None')
    q3 = 0
    print(q1)
    if(int(q3)!=0):
        power['q1'] = q1
        power['q2'] = q2
        power['danger'] = "card mb-4 py-3 border-bottom-danger"
        power['danger_2'] = "card-body"
        power['danger_3'] = "아직 문진표가 완료되지 않았습니다."
        all_key_dict = {}                                   #dict of all user's infomation
        for i in admin_account.objects.all().order_by('name'):
            all_key_dict[i.idd] = i.password             # save all_key_dict that key is usercode, that value is username
        if all_key_dict.get(q1,'NONE')=='NONE':
            return login_admin_re(request)
        if all_key_dict[q1] == q2:
            if q1 == "8div":
                all_list = 제8기동사단.objects.all().order_by('name')
                TEMP = 제8기동사단.objects.all()
            elif q1 == "8divinfo":
                all_list = 정보통신대대.objects.all().order_by('tet')
                TEMP = 정보통신대대.objects.all()
            
                                                                                                             #result dict what will send to html
            all_key_dict = {}                                                                                                           #dict of all user's infomation
            for i in TEMP.order_by('tet'):
                all_key_dict[i.tet.number] = i.tet.name                                                                                         # save all_key_dict that key is usercode, that value is username

            def name_check(lst:list):                                                                                                   # define function of saving all user name
                result =[]
                for i in lst:
                    result.append(i[0])
                return result

            normal = []
            house = []
            p=0
            q=0  
            name = 'check'+str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + '.csv'        # csv file name changed everyday
            result = []                                                                                                                 # 
            non_result = []
            code = 0
            if os.path.exists(name):                                                                                                    # whether file exsist in this path
                f = open(name,'r', encoding = "UTF-8")
                rdr = csv.reader(f)                                                                                                     # if that file exist, open that file and rdr is reader of that csv
                for x in rdr:                                                                                                           # x is row of csv file                                                          
                    if x==[]:
                        pass

                    else:
                        if(all_key_dict.get(int(x[0]),'NONE')!='NONE'):              # because x[0] is usercode, and because all_key_dict's key is usercode, it is true
                            x.insert(0,all_key_dict[int(x[0])])                      # insert username to 0index of x (because usercode's valuse is username)
                            code = x[1]
                            del x[1]                                                 # because x[1] is usercode, delete x[1]
                            result.append(x)                                         # append x to list "result"
                        print(x)
                        if(x[10] == "99"):
                            p=p+1
                            tmp = {}
                            tmp["idx"] = p
                            tmp["name"] = x[0]
                            tmp["usercode"] = code
                            house.append(tmp)
                        else:
                            q=q+1
                            tmp ={}
                            tmp["idx"] = q
                            tmp["name"] = x[0]
                            normal.append(tmp)
                asd=0
                print(normal,"이곳은 노말")
                print(house, "이곳은 집")
                if len(result)==0:
                    asd= 1
                else:
                    asd = len(result)
                power['house'] = house
                power['normal'] = normal

                power['yes'] = len(normal)
                power['no'] = len(house)
                power['per'] = int((len(normal)/asd)*100)
                name_list = name_check(result)                                       #list of user participating poll
                tmpppp = 0
                non_result += all_key_dict.values()                                  #appending values of information dict
                all_name_list = []                                                   #define all_name_list
                for i in TEMP.order_by('tet'):                      
                    all_name_list.append(i.tet.name)                                     #save all name list
                
                tmp = len(all_name_list)                                             #save all name list's length
                silsi = []
                tmppp = 0
                for i in range(0,len(name_list)):
                    for j in non_result:
                        if name_list[i] in j:
                            non_result.remove(j)
                            tmppp+=1
                            diccc = {}
                            diccc['idx']=tmppp
                            diccc['name'] = j
                            silsi.append(diccc)
                non_rere = []
                tmppp = 0
                for i in non_result:
                    tmppp+=1
                    diccc = {}
                    diccc['idx'] = tmppp
                    diccc['name'] = i
                    non_rere.append(diccc)


                power['total'] = len(house) + len(normal) + len(non_rere)         

                power['xx'] = len(non_rere)
                power['current'] = non_rere                                    
                power['result'] =result  
                print(result)
                print(non_result)
                power['silsi'] = silsi
                number_all = 100 - (len(non_result)/tmp) *100
                power['number_all'] = int(number_all)


                """------------send all answer recived by user to html------------"""
                count_1 =0
                for i in result:
                    if(i[1] == '1'):
                        count_1+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_11 = 100 - int(count_1/len(result)*100)
                    power['count_1'] = count_11

                count_2 =0
                for i in result:
                    if(i[2] == '1'):
                        count_2+=1 
                if(len(result)==0):
                    power['count_2'] = 0
                else:
                    count_21 = 100 - int(count_2/len(result)*100)
                    power['count_2'] = count_21

                count_3 =0
                for i in result:
                    if(i[3] == '1'):
                        count_3+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_31 = 100 - int(count_3/len(result)*100)
                    power['count_3'] = count_31

                count_4 =0
                for i in result:
                    if(i[4] == '1'):
                        count_4+=1 
                if(len(result)==0):
                    power['count_4'] = 0
                else:
                    count_41 = 100 - int(count_4/len(result)*100)
                    power['count_4'] = count_41

                count_5 =0
                for i in result:
                    if(i[5] == '1'):
                        count_5+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_51 = 100 - int(count_5/len(result)*100)
                    power['count_5'] = count_51

                count_6 =0
                for i in result:
                    if(i[6] == '1'):
                        count_6+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_61 = 100 - int(count_6/len(result)*100)
                    power['count_6'] = count_61

                count_7 =0
                for i in result:
                    if(i[7] == '1'):
                        count_7+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_71 = 100 - int(count_7/len(result)*100)
                    power['count_7'] = count_71

                count_8 =0
                for i in result:
                    if(i[8] == '1'):
                        count_8+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_81 = 100 - int(count_8/len(result)*100)
                    power['count_8'] = count_81

                count_9 =0
                for i in result:
                    if(i[9] == '1'):
                        count_9+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_91 = 100 - int(count_9/len(result)*100)
                    power['count_9'] = count_91

                """-----------end answer---------------"""   
            else:
                rdr = open(name,'w',encoding="UTF-8")
                rdr.close()
                return check(request)
            
            power['name1'] = str(time.localtime().tm_year) +"년 "+ str(time.localtime().tm_mon)+"월 " + str(time.localtime().tm_mday)+"일 "+" 코로나 문진표 현황"

            return render(request,'polls/check.html',power)
    else:
        power={}
        power['q1'] = q1
        power['q2'] = q2
        power['xx'] = q3
        return render(request, "polls/submit.html",power)


def check_solo(request):
    power = []
    result = []
    question =[
        "현재 체온이 37.5도 이상입니까?",
        "방역당국(보건소, 지자체)으로부터 PCR 검사대상자로 통보받은 적이 있습니까?",
        "방역당국(보건소, 지자체)으로부터 PCR 검사대상자로 통보받은 적이 있습니까?",
        "고위험 시설을 방문한 적이 있습니까?",
        "확진자등과 만난적이 있습니까?",
        "확진자가 다녀간 장소에 동선이 겹친 적이 있습니까?",
        "외부활동(종교집회, 동호회)에 참여한 적이 있습니까?",
        "동거 가족 중 설문문항 2~8 사항에 해당하는 가족이 있나요?",
        '2~9번 답변 중 "예"라 답변하신 문항이 있으십니까?'
         ]
    if request.method == "POST":                            # receive data to POST method
        q1 = request.POST.get("usercode",'None')            # save q1 to "username" recieved by POST. if "username" doesn't exist, then save None.
        q2 = request.POST.get("username",'None')            # save q1 to "username" recieved by POST. if "username" doesn't exist, then save None.
        for i in range(13):
            def sub_days(year, mon, day, subday):
                is_leap_year = (year % 4 == 0) and (year % 100 != 0)                   # leap year
                is_31 = ([1,3,5,7,8,10,12].count(mon) == 1)                            # length of current month
                if day > subday: return (year, mon, day - subday)                      # if number of days to subtract is less than the day field of current date, simply subtract
                else:                                                                  # moving back to last month
                    subday -= day                                                      # get new number of days to subtract within last month
                    if mon > 1:                                                        # if it's after january, no need to worry about year changing
                        if mon == 3:                                                   # if it's march right now, must consider leap year
                            if is_leap_year:                                           # if leap year, start subtracting from 29th
                                return (year, mon - 1, 29 - subday)     
                            else:                                                      # if not, start subtracting from 28th
                                return (year, mon - 1, 28 - subday)
                        else:
                            if is_31: return (year, mon - 1, 30 - subday)              # if this month is 31 days month, subtract from 30 
                            else: return (year, mon - 1, 31 - subday)                  # else do it the other way
                    else:                                                              
                        return (year - 1, 12, 31-subday)                               # if january was this month, simply go back to last year
            year, mon, day = sub_days(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, i)
            name = 'check' + str(year) + str(mon) + str(day) + '.csv'        # csv file name changed everyday
            date= str(year)+"년 "+str(mon) + "월 "+str(day) +"일 체크항목"
            print(date)
            f = open(name,'r', encoding = "UTF-8")
            rdr = csv.reader(f)
            result = [] 
            for x in rdr:
                                                                                                    # x is row of csv file                                                          
                if x==[]:
                    pass
                else:
                    if(x[0]==q1):
                        idx = 0
                        for i in x[1:]:
                            if(i=='1'):
                                result.append(question[idx])
                            else:
                                pass
                            idx+=1
                        
            temp = {'result':result, 'date': date}
                        #print(temp)       
            power.append(temp)
            print(power)
        tbreturn = {
            'name' : q2,
            'results' : power,
        }
    return render(request, "polls/check_solo.html", tbreturn)


def div(request):                                                                                                                 #
    name = 'check' + str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + '.csv' 
    num_done_comm = num_done_50 = num_done_95 = num_done_gong = num_done_medic = num_done_cop = num_done_hqb = num_done_champ = 0
    num_done_ppl = 0
    if os.path.exists(name):                                                                                                    # whether file exsist in this path
        f = open(name,'r', encoding = "UTF-8")
        rdr = csv.reader(f)
        for x in rdr:                                                                                                           # x is row of csv file                                                          
            if x==[]:
                pass
            else:
                num_done_ppl += 1
                person = 제8기동사단.objects.get(number = x[0])
                if 정보통신대대.objects.filter(tet = person)[0]: num_done_comm += 1
           #     elif 제50포병대대.objects.filter(tet = person)[0]: num_done_50 += 1
            #    elif 제95포병대대.objects.filter(tet = person)[0]: num_done_95 += 1
             #   elif 직할공병대대.objects.filter(tet = person)[0]: num_done_gong += 1
              #  elif 의무대.objects.filter(tet = person)[0]: num_done_medic += 1
              #  elif 군사경찰대.objects.filter(tet = person)[0]: num_done_cop += 1
               # elif 본부대.objects.filter(tet = person)[0]: num_done_hqb += 1
                #else: num_done_champ += 1
    num_comm = len(정보통신대대.objects.all())
    '''num_50 = len(제50포병대대.objects.all())
    num_95 = len(제95포병대대.objects.all())
    num_gong = len(직할공병대대.objects.all())
    num_medic = len(의무대.objects.all())
    num_cop = len(군사경찰대.objects.all())
    num_hqb = len(본부대.objects.all())
    num_champ = len(참모처.objects.all())'''
    num_all = num_comm #+ num_50 + num_95 + num_gong + num_medic + num_cop + num_hqb + num_champ + num_all
    def style_decider(all, done): 
        if all == done: return "progress-bar bg-success" 
        else: return "progress-bar bg-danger" 
    style_all = style_decider(num_all, num_done_ppl)
    style_정보통신대대 = style_decider(num_comm, num_done_comm)
    # style_50포병대대 = style_decider(num_50, num_done_50)
    # style_95포병대대 = style_decider(num_95, num_done_95)
    # style_직할공병대대 = style_decider(num_gong, num_done_gong)
    # style_의무대 = style_decider(num_medic, num_done_medic)
    # style_군사경찰대 = style_decider(num_cop, num_done_cop)
    # style_본부대 = style_decider(num_hqb, num_done_hqb)
    # style_참모처 = style_decider(num_champ, num_done_champ)
    year, mon, day = time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday
    return render(request, 'polls/div.html',{ 
        "number_all" : int(num_done_ppl/num_all * 100),
        "number_정보통신대대" : int(num_done_comm/num_comm * 100),
        "year" : year,
        "month": mon,
        "day": day,
  #      "number_50포병대대" : num_done_50/num_50 * 100,
   #     "number_95포병대대" : num_done_95/num_95 * 100, 
    #    "number_직할공병대대" : num_done_gong/num_gong * 100, 
  #      "number_의무대" : num_done_medic/num_medic * 100, 
   #     "number_군사경찰대" : num_done_cop/num_cop * 100, 
    #    "number_본부대" : num_done_hqb/num_hqb * 100, 
     #   "number_참모처" : num_done_champ/num_champ * 100,
       "style_all" : style_all,
       "style_정보통신대대" : style_정보통신대대,
    #   "style_50포병대대" : style_50포병대대,
    #       "style_95포병대대" : style_95포병대대, 
    #       "style_직할공병대대" : style_직할공병대대, 
    #       "style_의무대" : style_의무대, 
    #       "style_군사경찰대" : style_군사경찰대, 
    #       "style_본부대" : style_본부대, 
    #       "style_참모처" : style_참모처,
    })


"""---------------------------- def login window-------------------------------------"""

def login(request):
    if request.session.get('userid','NONE')=='NONE':        # check whether session named 'userd' exists. if session doesn't exist, then return 'None'
        return render(request, 'polls/login.html',{})       # render login.html
    else:              
        return home(request)                                # if session exist, then return home(request) 

def login_re(request):
    return render(request, 'polls/login_re.html',{})

def login_re2(request):
    return render(request, 'polls/login_re2.html',{})

def login_admin(request):
    return render(request, 'polls/login_admin.html',{})

def login_admin_re(request):
    return render(request, 'polls/login_admin_re.html',{})

"""---------------------------- def logout window-------------------------------------"""

def logout(request):
    del request.session['userid']                           # To logout, session remained in browser delete
    request.session.modified = True                         # save session now
    return render(request, 'polls/login.html',{})           # render login window again


"""---------------------------- def home poll window-------------------------------------"""

def home(request):
    if request.method == "POST":                            # receive data to POST method
        q1 = request.POST.get("username",'None')            # save q1 to "username" recieved by POST. if "username" doesn't exist, then save None.
        q2 = request.POST.get("password",'None')
        all_key_dict = {}                                   #dict of all user's infomation
        for i in 제8기동사단.objects.all().order_by('name'):
            all_key_dict[i.number] = i.password             # save all_key_dict that key is usercode, that value is username
        if all_key_dict.get(int(q1),'NONE')=='NONE':
            return login_re2(request)
        if all_key_dict[int(q1)] == q2:
            request.session['userid'] = q1                      # save q1 in session named 'userid'
            x= {'usercode':q1}                                  # make dict for usercode
            lst = 질문지.objects.filter(부대명 = "정보통신대대")[0]           #user code 범위 지정해서 유저마다 질문지 바꿔줘야함
            idx = 0
            result = []
            for q in lst.get_all_qs():
                idx+=1
                name = "quest_" + str(idx+1) 
                result.append({'idx': idx, 'Q':q, 'name':name, 'id1':name+"_1",'id0':name+"_0"})
            #     result = [
            #     {'idx' :1, 'Q':lst.Q1},
            #     {'idx' :2, 'Q':lst.Q2}
            #     {'idx' :3, 'Q':lst.Q3}
            #     {'idx' :4, 'Q':lst.Q4}
            #     {'idx' :5, 'Q':lst.Q5}
            #     {'idx' :6, 'Q':lst.Q6}
            #     {'idx' :7, 'Q':lst.Q7}
            #     {'idx' :8, 'Q':lst.Q8}
            #     {'idx' :9, 'Q':lst.Q9}
            
            # ]
            x['results'] = result
            return render(request,'polls/home.html',x)              # render home.html (polls window)
        else:
            return login_re(request)
    else:
        print("rrr")
        x={}
        lst = 질문지.objects.filter(부대명 = "정보통신대대")[0]           #user code 범위 지정해서 유저마다 질문지 바꿔줘야함
        idx = 0
        result = []
        for q in lst.get_all_qs():
            idx+=1
            name = "quest_" + str(idx+1) 
            result.append({'idx': idx, 'Q':q, 'name':name, 'id1':name+"_1",'id0':name+"_0"})
        x['results'] = result
        print(result)
        x['usercode']=request.session['userid']           # if session exist already, then nake dict for usercode
        return render(request,'polls/home.html',x)              # render home.html (polls window)



"""---------------------------- def save poll server-------------------------------------"""
def finish(request):
    if request.method == "POST":
        q1 = request.POST.get("quest_1",'None')             # q1 is recived from login or home (userid) to auto login
        q2 = request.POST.get("quest_2", '2')               # recive answer by poll
        q3 = request.POST.get("quest_3", '2')
        q4 = request.POST.get("quest_4", '2')
        q5 = request.POST.get("quest_5", '2')
        q6 = request.POST.get("quest_6", '2')
        q7 = request.POST.get("quest_7", '2')
        q8 = request.POST.get("quest_8", '2')
        q9 = request.POST.get("quest_9", '2')
        q10 = request.POST.get("quest_10", '2')
        lst = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]          #save list of answer recieved by home.html through POST
        print(lst)
        x={}
        if lst[1:].count('1')>=1:
            x['result'] = "자가대기 및 지휘계통으로 보고바람."
            lst.append('99')
        else:
            x['result'] = "정상출근"
            lst.append('100')
            

        name = 'check'+str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + '.csv'        #csv file name save 
        if os.path.exists(name):                                                                                                    # whether file exsist in this path
            pass
        else:
            f = open(name,'w')                                                                                                      # if file not exist, then create file "name"
            f.close()

        f = open(name,'a', encoding="UTF-8")                                                                                        # open csv file to modify file
        rdr = csv.writer(f)                                                                                                         # defination rdr is csv writer
        rdr.writerow(lst)                                                                                                           # writerow in csvfile                                                        
        f.close()

    return render(request, 'polls/finish.html', x)                                                                                  # finish!


"""---------------------------- def checking window-------------------------------------"""
def check(request):
    power = {}
    if request.method == "POST":                            # receive data to POST method
        q1 = request.POST.get("username",'None')            # save q1 to "username" recieved by POST. if "username" doesn't exist, then save None.
        q2 = request.POST.get("password",'None')
        all_key_dict = {}                                   #dict of all user's infomation
        power['q1'] = q1
        power['q2'] = q2
        for i in admin_account.objects.all().order_by('name'):
            all_key_dict[i.idd] = i.password             # save all_key_dict that key is usercode, that value is username
        if all_key_dict.get(q1,'NONE')=='NONE':
            return login_admin_re(request)
        if all_key_dict[q1] == q2:
            if q1 == "8div":
                all_list = 제8기동사단.objects.all().order_by('name')
                TEMP = 제8기동사단.objects.all()
            elif q1 == "8divinfo":
                all_list = 정보통신대대.objects.all().order_by('tet')
                TEMP = 정보통신대대.objects.all()
                print(all_list)
            
                                                                                                             #result dict what will send to html
            all_key_dict = {}                                                                                                           #dict of all user's infomation
            for i in TEMP.order_by('tet'):
                all_key_dict[i.tet.number] = i.tet.name                                                                                         # save all_key_dict that key is usercode, that value is username

            def name_check(lst:list):                                                                                                   # define function of saving all user name
                result =[]
                for i in lst:
                    result.append(i[0])
                return result

            normal = []
            house = []
            p=0
            q=0  
            name = 'check'+str(time.localtime().tm_year) + str(time.localtime().tm_mon) + str(time.localtime().tm_mday) + '.csv'        # csv file name changed everyday
            result = []                                                                                                                 # 
            non_result = []
            code = 0
            if os.path.exists(name):                                                                                                    # whether file exsist in this path
                f = open(name,'r', encoding = "UTF-8")
                rdr = csv.reader(f)                                                                                                     # if that file exist, open that file and rdr is reader of that csv
                for x in rdr:                                                                                                           # x is row of csv file                                                          
                    if x==[]:
                        pass

                    else:
                        if(all_key_dict.get(int(x[0]),'NONE')!='NONE'):              # because x[0] is usercode, and because all_key_dict's key is usercode, it is true
                            x.insert(0,all_key_dict[int(x[0])])                      # insert username to 0index of x (because usercode's valuse is username)
                            code = x[1]
                            del x[1]                                                 # because x[1] is usercode, delete x[1]
                            result.append(x)                                         # append x to list "result"
                        if(x[10] == "99"):
                            p=p+1
                            tmp = {}
                            tmp["idx"] = p
                            tmp["name"] = x[0]
                            tmp["usercode"] = code
                            house.append(tmp)
                        else:
                            q=q+1
                            tmp ={}
                            tmp["idx"] = q
                            tmp["name"] = x[0]
                            normal.append(tmp)
                asd=0
                print(normal,"이곳은 노말")
                print(house, "이곳은 집")
                if len(result)==0:
                    asd= 1
                else:
                    asd = len(result)
                power['house'] = house
                power['normal'] = normal

                power['yes'] = len(normal)
                power['no'] = len(house)
                power['per'] = int((len(normal)/asd)*100)
                name_list = name_check(result)                                       #list of user participating poll
                tmpppp = 0
                non_result += all_key_dict.values()                                  #appending values of information dict
                all_name_list = []                                                   #define all_name_list
                for i in TEMP.order_by('tet'):                      
                    all_name_list.append(i.tet.name)                                     #save all name list
                
                tmp = len(all_name_list)                                             #save all name list's length
                silsi = []
                tmppp = 0
                for i in range(0,len(name_list)):
                    for j in non_result:
                        if name_list[i] in j:
                            non_result.remove(j)
                            tmppp+=1
                            diccc = {}
                            diccc['idx']=tmppp
                            diccc['name'] = j
                            silsi.append(diccc)
                non_rere = []
                tmppp = 0
                for i in non_result:
                    tmppp+=1
                    diccc = {}
                    diccc['idx'] = tmppp
                    diccc['name'] = i
                    non_rere.append(diccc)


                power['total'] = len(house) + len(normal) + len(non_rere)         

                power['xx'] = len(non_rere)
                power['current'] = non_rere                                    
                power['result'] =result  
                print(result)
                print(non_result)
                power['silsi'] = silsi
                number_all = 100 - (len(non_result)/tmp) *100
                power['number_all'] = int(number_all)


                """------------send all answer recived by user to html------------"""
                count_1 =0
                for i in result:
                    if(i[1] == '1'):
                        count_1+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_11 = 100 - int(count_1/len(result)*100)
                    power['count_1'] = count_11

                count_2 =0
                for i in result:
                    if(i[2] == '1'):
                        count_2+=1 
                if(len(result)==0):
                    power['count_2'] = 0
                else:
                    count_21 = 100 - int(count_2/len(result)*100)
                    power['count_2'] = count_21

                count_3 =0
                for i in result:
                    if(i[3] == '1'):
                        count_3+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_31 = 100 - int(count_3/len(result)*100)
                    power['count_3'] = count_31

                count_4 =0
                for i in result:
                    if(i[4] == '1'):
                        count_4+=1 
                if(len(result)==0):
                    power['count_4'] = 0
                else:
                    count_41 = 100 - int(count_4/len(result)*100)
                    power['count_4'] = count_41

                count_5 =0
                for i in result:
                    if(i[5] == '1'):
                        count_5+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_51 = 100 - int(count_5/len(result)*100)
                    power['count_5'] = count_51

                count_6 =0
                for i in result:
                    if(i[6] == '1'):
                        count_6+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_61 = 100 - int(count_6/len(result)*100)
                    power['count_6'] = count_61

                count_7 =0
                for i in result:
                    if(i[7] == '1'):
                        count_7+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_71 = 100 - int(count_7/len(result)*100)
                    power['count_7'] = count_71

                count_8 =0
                for i in result:
                    if(i[8] == '1'):
                        count_8+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_81 = 100 - int(count_8/len(result)*100)
                    power['count_8'] = count_81

                count_9 =0
                for i in result:
                    if(i[9] == '1'):
                        count_9+=1 
                if(len(result)==0):
                    power['count_1'] = 0
                else:
                    count_91 = 100 - int(count_9/len(result)*100)
                    power['count_9'] = count_91

                """-----------end answer---------------"""   
            else:
                rdr = open(name,'w',encoding="UTF-8")
                rdr.close()
                return check(request)
            
            power['name1'] = str(time.localtime().tm_year) +"년 "+ str(time.localtime().tm_mon)+"월 " + str(time.localtime().tm_mday)+"일 "+" 코로나 문진표 현황"
            power['style_all'] = style_decider(number_all, 100)
            return render(request,'polls/check.html',power)
        else:
            return login_admin_re(request)
    else:
        return login_admin_re(request)
