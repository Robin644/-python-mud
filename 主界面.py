#走路游戏
from sjk import *
from gn_hs import *
from player import *
import jq
import json
replace=[0,0]
is_in_room=0
now_id=0.1

now_zuobiao='0,0'
now_map=map_room_yzc_name
#
import sjk


###
''' 

with open('liveplace.txt','r') as fileobj:
    now_zuobiao=fileobj.readline()         
    
    now_id=check_id[now_zuobiao]
'''
try:
    print('欢迎回到游戏，你上次退出是在'+now_map[now_id])
except:
    print("欢迎回来")
while True:
    '''map_zuobiao_x={0.1:0,0.2:1,0.3:-1}
map_zuobiao_y={0.1:0,0.2:0,0.3:0}
map_room_xsc_id={'村口':0.1}
map_room_xsc_name={0.1:'村口'}
    '''
    print('*\n你现在位于'+now_map[now_id]+'('+now_zuobiao+')')#打印地图名称
    
    print('-'*18+now_map[now_id]+'-'*18)#获取地图名称
    try:#尝试打印描述
        print(map_room_nr[now_id])#打印描述
    except:#如果没有描述
        print('本地点没有描述')#输出反馈
    print('-'*40)
    print('#############周围地点################')
    hgsz(now_id)#使用功能函数查看周围地点
    print('################################')
    try:
        try:
            normal_list=str(eval('npc_room_'+(str(now_id).replace('.','_'))))            
        except:
            print('这没有普通NPC。')
        else:
            print('这里有普通npc:'+str(eval('npc_room_'+(str(now_id).replace('.','_')))))

        try:
            special_npc_list=str(eval('special_npc_room_'+(str(now_id).replace('.','_'))))        
        except:
            print('这里没有特殊NPC。')
        else:       
            print('这里有特殊NPC:'+special_npc_list)

        try:
            '''
            room_0_6_name={0.61:'后厨'}#在room0.6中的0.61房间的名字#0_61的_代表.
room_0_6_id={'后厨':0.61}#绑定名字与id0.61
room_room_0_6_name_list=['后厨']
            '''                
            roomslist=eval('room_room_'+str(now_id).replace('.','_')+'_name_list')
        except:
            print('这里没有可以进入的房间')
        else:
            
            print('这里有房间:'+str(roomslist))
        try:                
            thingslist=eval('thing_room_'+str(now_id).replace('.','_'))
        except:
            print('地上没有任何物品')
        else:
            thingslist=eval('thing_room_'+str(now_id).replace('.','_'))
            print('这里有物品:'+str(thingslist))
#special_npc_room_0_7=[special_npc_id['sishen
            
        
    except:
        pass
    else:
        print('####################')
        #打印地图事件
    print('='*30)
    try:
        print(str(room_shijjan[now_id]))
    except:
        print()
    print('='*30)
    player_code=input('>>>\n指令:退出游戏，东\西\南\北，普通npc，特殊npc，个人，进入房间，拾取\n:')
    try:
                    
            
        if player_code=='北':
            y_zuobiao=map_zuobiao_y[now_id]
            y_zuobiao+=1
            
            now_zuobiao=str(map_zuobiao_x[now_id])+','+str(y_zuobiao)
            
            
        elif player_code=='东':
            x_zuobiao=map_zuobiao_x[now_id]
            x_zuobiao+=1
            now_zuobiao=str(x_zuobiao)+','+str(map_zuobiao_y[now_id])
            
        
            
        elif player_code=='南':
            y_zuobiao=map_zuobiao_y[now_id]
            y_zuobiao-=1
            now_zuobiao=str(map_zuobiao_x[now_id])+','+str(y_zuobiao)
            
            
        elif player_code=='西':
            x_zuobiao=map_zuobiao_x[now_id]
            x_zuobiao-=1
            now_zuobiao=str(x_zuobiao)+','+str(map_zuobiao_y[now_id])
        else:
            pass
        last_id=now_id
        now_id=check_id[now_zuobiao]
        print('[*当前地图ID:*'+str(now_id)+']')
        
    except:
        '''
        map_zuobiao_x={0.1:0,0.2:1,0.3:-1}
map_zuobiao_y={0.1:0,0.2:0,0.3:0}
        '''
        now_id=last_id
        now_zuobiao=str(map_zuobiao_x[now_id])+','+str(map_zuobiao_y[now_id])
        print('>>>>\n'+player_code+'边没有路了，你打了个踉跄勉强停了下来\n>>>>')
        continue 
    else:
        pass
    if player_code=='debug0':
        now_id=1.1
        now_zuobiao="400,400"
        now_map=map_room_xj_name
            
    elif player_code=="debug1":
        now_id=0.1
        now_zuobiao="0,0"
        now_map=map_room_yzc_name
        
    if player_code=='普通npc' or player_code=='nrnpc':
        try:
            npc_id=int(input('输入互动npc的序号:\n'))
        except:
            print('序号错误')
            continue 
        else:
            pass
        try:
            dt_normal_npc_list=eval('npc_room_'+(str(now_id).replace('.','_')))
            if dt_normal_npc_list[npc_id] != None:
                normal_npc_hd(dt_normal_npc_list[npc_id],now_id)
            else:
                print('npc不在此地图上')
        except:
            print('oops,出错了')
            continue 
    if player_code == '个人':
        #player_selfcheck(describe_list,player_wearing_describe,player_face,player_smz,player_max_smz,player_xb,player_describe_bag)
        player_selfcheck(describe_list,player_wearing_describe,player_face,player_sx0['生命值'],player_sx0['最大生命值'],player_describe_bag,now_id)
    if player_code =='进入房间':
        try:
            room_id=int(input('输入要进入房间的序号:\n'))
        except:
            print('\n€€€€€€€€€€€序号格式不合法€€€€€€€€€€\n')
    
        try:
            '''
            room_0_6_name={0.61:'后厨'}#0_6代表0.6
room_0_6_id={'后厨':0.61}
room_room_0_6=['后厨']
            '''
            dt_rooms_list=eval('room_room_'+(str(now_id).replace('.','_'))+'_name_list')
            
        except:
            print('€€€€€€€€\n请输入正确的序号\n')
            continue 
        else:
            try:
            
            
                
                
                if dt_rooms_list[room_id] != None:
                    
                    last_id=now_id
                    now_id=eval('room_'+str(now_id).replace('.','_')+'_id')[dt_rooms_list[0]]
                    while True:
                        is_in_room=1
                        print('-'*30)
                        print('*************** 你处于房间中 *******************')
                        print('\n你现在位于'+eval('room_room_'+str(now_id).replace('.','_')+'_name'))
                        print('-'*30)
                        try:
                            print(room_room_describe[now_id])
                        except:
                            pass
                        print('-'*15+eval('room_room_'+str(now_id).replace('.','_')+'_name')+'-'*15)
                        try:
                            normal_list0=str(eval('npc_room_room_'+(str(now_id).replace('.','_'))))            
                        except:
                            print('这没有普通NPC。')
                        else:
                            print('这里有普通npc:'+str(normal_list0))
                        try:
                            special_npc_list0=str(eval('special_npc_room_room_'+str(now_id).replace('.','_')))        
                        except:
                            print('这里没有特殊NPC。')
                        else:       
                            print('这里有特殊NPC:'+str(special_npc_list0))
                        try:                
                            thingslist=eval('thing_room_room_'+str(now_id).replace('.','_'))
                        except:
                            print('地上没有任何物品')
                        else:
                            thingslist=eval('thing_room_room_'+str(now_id).replace('.','_'))
                            print('这里有物品:'+str(thingslist))

                        print('-'*30)
                        try:
                            print(room_room_shijian[now_id])
                        except:
                            pass
                        print('='*30)
                        code=input('指令:离开，普通npc，特殊npc:')
                        
                        if code=='离开':
                            is_in_room=0
                            print('你转过身去，离开了房间'+eval('room_room_'+str(now_id).replace('.','_')+'_name'))
                            now_id=last_id
                            break
                        if code=='普通npc' or code=='普通npc互动':
                            try:
                                npc_id=int(input('输入互动npc的序号:\n'))
                            except:
                                print('序号错误')
                                continue 
                            
                            try:
                                dt_normal_npc_list=eval('npc_room_room_'+(str(now_id).replace('.','_')))
                                if dt_normal_npc_list[npc_id] != None:
                                    normal_npc_hd(dt_normal_npc_list[npc_id],now_id)
                                else:
                                    print('npc不在此地图上')
                            except:
                                print('oops,出错了')
                                continue 
                        
                        if code=='特殊npc' or code=='spnpc':
                            try:
                                npc_id=int(input('输入互动特殊npc的序号:\n'))
                            except:
                                print('序号错误')
                                continue 
                            else:
                                pass
                            try:
                                dt_normal_npc_list=eval('special_npc_room_room_'+(str(now_id).replace('.','_')))
                                if dt_normal_npc_list[npc_id] != None:
                                    npc_id=special_npc_name[dt_normal_npc_list[npc_id]]
                                    eval(npc_id)()
                                else:
                                    print('此特殊npc不在此地图上')
                            except:
                                print('oops,出错了')
                                continue               
                
                
                else:
                    print('此地图上没有这个房间')
                    continue
            except:
                pass   
    if player_code=='退出游戏' and is_in_room !=1:
        print('正在退出游戏')
        with open('liveplace.txt','w') as fileobj:
            fileobj.write(now_zuobiao)
        break     
    elif is_in_room == 1:
        print('¥¥¥在房间内时无法退出游戏¥¥¥')
    if player_code=='特殊npc' or player_code=='spnpc':
        try:
            npc_id=int(input('输入互动特殊npc的序号:\n'))
        except:
            print('序号错误')
            continue 
        else:
            pass
        try:
            dt_normal_npc_list=eval('special_npc_room_'+(str(now_id).replace('.','_')))
            if dt_normal_npc_list[npc_id] != None:
                npc_id=special_npc_name[dt_normal_npc_list[npc_id]]
                eval(npc_id)()
            else:
                print('此特殊npc不在此地图上')
        except:
            print('oops,出错了')
            continue
    if player_code =='拾取':
        print('拾取---------------------------') 
        shiqu(now_id)            
               
#The last coding time is 2020.4.12.22:56
#***coding UTF-8***
#By Robin qq 2432541891
        