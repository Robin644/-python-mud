#功能函数大全
from sjk import *
from 战斗 import *
def shiqu(now_id):
    print('='*14+'拾取'+'='*14)
    try:
        
        try:                            
            thingslist=eval('thing_room_'+str(now_id).replace('.','_'))
            print('这里有物品:'+str(thingslist))
        except:
            
            try:                
                thingslist=eval('thing_room_room_'+str(now_id).replace('.','_'))
            except:
                print('地上没有任何物品')
            else:
                thingslist=eval('thing_room_room_'+str(now_id).replace('.','_'))
                print('这里有物品:'+str(thingslist))
    except:
        print('错误')
        pass
    else:
        import sjk
        try:
            xuhao=int(input('输入你想要捡起的物品序号'))
            jianqi_thing=thingslist[xuhao]
            if jianqi_thing != None:
                print('*'*10+'成功捡起'+'*'*10)
                
                if jianqi_thing in list(wear_name_id.keys()):
                    sjk.player_wear_bag.append(thingslist[xuhao])
                    del thingslist[xuhao]
                elif jianqi_thing  in list(weapon_name_id.keys()):
                    sjk.player_weapon_bag.append(thingslist[xuhao])
                    del thingslist[xuhao]
                elif jianqi_thing in list(thing_name_id.keys()):
                    sjk.player_things_bag.append(thingslist[xuhao])
                    del thingslist[xuhao]
            else:
                print('什么玩意傻了吧唧的')
        except:
            print('系统:这里什么东西都没有，你要捡什么?')
     
    
    
    
    
    
    
def hgsz(now_id):    
    try:         
        print('='*25)
        now_zuobiao=str(map_zuobiao_x[now_id])+','+str(map_zuobiao_y[now_id])
        now_id=check_id[now_zuobiao]
        try:

            north_id = check_id[str(map_zuobiao_x[now_id]) + ',' + str(map_zuobiao_y[now_id])]
            center_name = map_room_yzc_name[north_id]
        except:
            print('|你所在的位置竟然没有地点，靠，这个bug必须要加qq2432541891反馈呀|')
            center_name=""
        else:
            pass
        try:
            
            north_id=check_id[str(map_zuobiao_x[now_id])+','+str(map_zuobiao_y[now_id]+1)]
            north_name=map_room_yzc_name[north_id]
        except:
            print('|你的北边没有地点|')
            north_name=""
        else:
            pass
            #print('|你的北边是'+north_name+'        |')
        try:
            north_id=check_id[str(map_zuobiao_x[now_id])+','+str(map_zuobiao_y[now_id]-1)]
            south_name=map_room_yzc_name[north_id]
        except:
            print('|你的南边没有地点|')
            south_name=""
        else:
            #print('|你的南边是'+north_name+'        |')
            pass
        try:
            north_id=check_id[str(map_zuobiao_x[now_id]+1)+','+str(map_zuobiao_y[now_id])]
            east_name=map_room_yzc_name[north_id]
        except:
            print('|你的东边没有地点|')
            east_name=""
        else:
            #print('|你的东边是'+north_name+'        |')
            pass
        try:       
            north_id=check_id[str(map_zuobiao_x[now_id]-1)+','+str(map_zuobiao_y[now_id])]
            west_name=map_room_yzc_name[north_id]
        except:
            west_name=""
            print('|你的西边没有地点|')
        else:
            #print('|你的西边是'+north_name+'        |')
            pass
        #print('|…END…                |')
        #可视化地图
        first_block = (len("|" + west_name + "||") + 1) * " "
        center_block1 = (int(((len(center_name) - len(north_name)) / 2))) * " "
        center_block2 = (int(((len(center_name) - len(south_name)) / 2))) * " "
        center_block3 = (int(((len(north_name) - len(center_name)) / 1))) * " "

        #
        print(first_block + "||" + center_block1 + north_name + center_block1 + "||")  # 北
        print("|" + west_name + "||" +center_block3 +center_name +center_block3 +"||" + east_name + "|")  # 南
        # 东
        print(first_block + "||" + center_block2 + south_name + center_block2 + "||")  # 南








        print('='*25+'\n')
    except:
        
        print('\n***oops，无法环顾四周，出了点小故障***\n')
def normal_npc_hd(npc_name,now_id):
    import random
    sentence=0
    random_number=random.randint(0,3)
    
    if random_number == 0:
        sentence =npc_name+'打了个哈欠，说：你找我有什么事吗？我现在正正闲得慌呢' 
    if random_number == 1:
        sentence =npc_name+'春风满面，说：今天的你也分外精神呢，你找我有什么事情吗？'
    if random_number == 2:
        sentence =npc_name+'稍微有些不耐烦，说：你找我有事吗？'
    if random_number ==3:
        sentence =npc_name+sentence
    print('--------------普通NPC:'+npc_name+'('+normal_npc_name[npc_name]+')---------------')
    print(normal_npc_describe[normal_npc_name[npc_name]])
   
   
   
    print('-'*25)
    print(sentence)
    print('*'*25)
    while True:
        hudong=input('指令：闲聊，道别，战斗：')
        if hudong=='战斗':
            print('你对着「'+npc_name+'」大喊:“阁下领教壮士高招!”')
            message=zhandou(normal_npc_name[npc_name],now_id,is_special=0)
            if message[0]=='胜利':
                print('\n\n你战胜了'+npc_name)
            elif message[0]=='失败':
                print('\n\n'+npc_name+'把你打得满地找牙')
            sjk.player_sx0['生命值']=message[1]
        if hudong=='闲聊':
            random_number=random.randint(0,5)
            if random_number == 0:
                sentence='你也是太无聊了吧，还是去到处逛逛吧，听说扬州城很大的'
            elif random_number==5:
                sentence='你听说最近的新闻了没有，真是铁马冰河入梦来啊，这世道不太平了'
            elif random_number==4:
                sentence='据说扬州的醉仙楼在300年前就已经开业了啊，当时也许真的有仙人去吃过呢，哈哈哈哈'
            
            
            
            elif random_number == 1:
                sentence='今天天气不算太好啊，至少我不喜欢'
            elif random_number == 2:
                sentence='我就是一普通小老百姓，你还是找其他人聊天吧'
            elif random_number == 3:
                sentence='不知道远方的故友如何了，与君离别意，同是宦游人'
            print('*'*20+'\n'+npc_name+'对着你说：'+sentence+'\n'+'*'*20)
        if hudong=='道别':
            print('---你与'+npc_name+'道别后离开了')
            break


#以下是特殊NPC函数
def sishen():
    import random
    npc_name='死神'
    sentence=0
    random_number=random.randint(0,2)
    
    if random_number == 0:
        sentence =npc_name+'双眸爆出一阵黑芒,说:“你找我有什么事情吗？”' 
    if random_number == 1:
        sentence =npc_name+'嘴角勾勒出挑逗的笑容，问:“你找我有什么事吗？”'
    if random_number == 2:
        sentence =npc_name+'闭上双眼，仿佛早已知道了你的来意，说：“汝有何求”？'
    try:
        print('--------------特殊NPC:'+special_npc_wear_describe[npc_name]+npc_name+'('+special_npc_name[npc_name]+')---------------')
    except:
        print('--------------特殊NPC:'+npc_name+'('+special_npc_name[npc_name]+')---------------')
    print(special_npc_describe[special_npc_name[npc_name]])
    
    try:
        print('他看起来约莫已经'+special_npc_old['sishen']+'岁了')
    except:
        print('你没看出来他的年龄')
    print('-'*25)
    print(sentence)
    while True:
        hudong=input('指令：闲聊，道别，战斗：')
        if hudong=='战斗':
            print('你对着「'+npc_name+'」大喊:“阁下领教壮士高招!”')
            message=zhandou('sishen',0.6,is_special=1)
            if message[0]=='胜利':
                print('\n\n你战胜了'+npc_name)
            elif message[0]=='失败':
                print('\n\n'+npc_name+'把你打得满地找牙')
            sjk.player_sx0['生命值']=message[1]

        if hudong=='闲聊':
            random_number=random.randint(0,3)
            if random_number == 0:
                sentence='我是死亡之化身，当年我可是嬴政大王手下的第一名将，人称我白起'
            elif random_number == 1:
                sentence='我曾经与你一样，也是一个普通的侠客，直到我身陨后被赐予了不死不灭之身'
            elif random_number == 2:
                sentence='我现在在地府为阎王工作，曾经我可是阎王手下的第一得力干将呢:)'
            elif random_number == 3:
                sentence='不知道曾经已远去的故友如何了，长生不老也不是什么好事情啊，哈哈😄'
            print(npc_name+'对着你说：'+sentence+'\n···············')
        if hudong=='道别':
            print('---你与'+npc_name+'道别后离开了')
            break
def wushi():    
    import random
    npc_name='巫师'
    sentence=0
    random_number=random.randint(0,2)
    
    if random_number == 0:
        sentence =npc_name+'带着令人窒息的威压,缓缓地说:“你找我有什么事情吗？”' 
    if random_number == 1:
        sentence =npc_name+'双目半睁，犹如一尊神像，半晌后说:“你找我有什么事吗？”'
    if random_number == 2:
        sentence =npc_name+'释放一道无形的真气，让你不由自主的打了个寒战。他仿佛早已知道了你的来意，用真气向你传音：“汝有何求与吾”？'
    try:
        print('--------------特殊NPC:'+special_npc_wear_describe[npc_name]+npc_name+'('+special_npc_name[npc_name]+')---------------')
    except:
        print('--------------特殊NPC:'+npc_name+'('+special_npc_name[npc_name]+')---------------')
    try:
        print('他看起来约莫已经'+special_npc_old['wushi']+'岁了')
    except:
        print('你没看出来他的年龄')
    print(special_npc_describe[special_npc_name[npc_name]])
    print('-'*25)
    print(sentence)
    while True:
        hudong=input('指令：闲聊，道别，求香，战斗：')
        if hudong=='战斗':
            print('你对着「'+npc_name+'」大喊:“阁下领教壮士高招!”')
            message=zhandou('wushi',0.6,is_special=1)
            if message[0]=='胜利':
                print('\n\n你战胜了'+npc_name)
            elif message[0]=='失败':
                print('\n\n'+npc_name+'把你打得满地找牙')
            sjk.player_sx0['生命值']=message[1]

       
        if hudong=='闲聊':
            random_number=random.randint(0,3)
            if random_number == 0:
                sentence='我是巫师庙的代理人，人们喜欢叫我巫神'
            elif random_number == 1:
                sentence='神明并非遥不可及，只要你专心修炼，当大机缘成熟，便可收获果实'
            elif random_number == 2:
                sentence='我已经将近300岁了，但是远远比不上那些长生不老的神明，不过长生也并非好事'
            elif random_number == 3:
                sentence='我来自京城的巫师殿，我只不过是巫师荟荟众生的其中之一罢了。'
            print(npc_name+'对着你说：'+sentence+'\n···············')
        if hudong=='道别':
            print('---你对'+npc_name+'鞠躬后道别后离开了')
            break
        if hudong =='求香':
            player_things_bag.append(thing_id_name[1])
            print(npc_name + "对你说：心诚则灵，小施主")

            
            
            
def chuniang():    
    import random
    npc_name='厨娘'
    sentence=0
    random_number=random.randint(0,2)
    
    if random_number == 0:
        sentence =npc_name+'咯咯一笑，问:你来找我干嘛?”' 
    if random_number == 1:
        sentence =npc_name+'扇了扇扇子，说:“你找我有什么事吗？”'
    if random_number == 2:
        sentence =npc_name+'有些欢快地说：“汝有何求与吾”？'
    try:
        print('--------------特殊NPC:'+special_npc_wear_describe[npc_name]+npc_name+'('+special_npc_name[npc_name]+')---------------')
    except:
        print('--------------特殊NPC:'+npc_name+'('+special_npc_name[npc_name]+')---------------')
    try:
        print('他看起来约莫已经'+special_npc_old['chuniang']+'岁了')
    except:
        print('你没看出来他的年龄')
    print(special_npc_describe[special_npc_name[npc_name]])
    print('-'*25)
    print(sentence)
    while True:
        hudong=input('指令：闲聊，道别，战斗：')
        if hudong=='战斗':
            print('你对着「'+npc_name+'」大喊:“阁下领教壮士高招!”')
            message=zhandou('chuniang',0.6,is_special=1)
            if message[0]=='胜利':
                print('\n\n你战胜了'+npc_name)
            elif message[0]=='失败':
                print('\n\n'+npc_name+'把你打得满地找牙')
            sjk.player_sx0['生命值']=message[1]

        
        
        
        if hudong=='闲聊':
            random_number=random.randint(0,3)
            if random_number == 0:
                sentence='我是醉仙楼的老板，是的，这是我祖上传下来的生意，已经有300年了'
            elif random_number == 1:
                sentence='听说巫神庙可以找巫师要神香然后进行祈福呢'
            elif random_number == 2:
                sentence='来尝尝我们醉仙楼的招牌菜八仙过海吗？当年皇帝也来吃过哦'
            elif random_number == 3:
                sentence='逝者如斯夫，不舍昼夜啊，转眼我已经不是从前那个少女了，哎'
            print(npc_name+'对着你说：'+sentence+'\n···············')
        if hudong=='道别':
            print('---你对'+npc_name+'挥手道别后离开了')
            break
def xinliyisheng():    
    import random
    npc_name='首席大弟子'
    sentence=0
    random_number=random.randint(0,2)
    
    if random_number == 0:
        sentence =npc_name+'说:”' 
    if random_number == 1:
        sentence =npc_name+'望着你说:“你找我有什么事吗？”'
    if random_number == 2:
        sentence =npc_name+'说：“汝有何求与吾”？'
    try:
        print('--------------特殊NPC:'+special_npc_wear_describe[npc_name]+npc_name+'('+special_npc_name[npc_name]+')---------------')
    except:
        print('--------------特殊NPC:'+npc_name+'('+special_npc_name[npc_name]+')---------------')
    try:
        print('他看起来约莫已经'+special_npc_old['wushi']+'岁了')
    except:
        print('你没看出来他的年龄')
    print(special_npc_describe[special_npc_name[npc_name]])
    print('-'*25)
    print(sentence)
    while True:
        print("||||||||||||||||||||||")
        hudong=input('指令：闲聊，道别：')
        if hudong=='闲聊':
            random_number=random.randint(0,3)
            if random_number == 0:
                sentence='我是巫师庙的代理人，人们喜欢叫我巫神'
            elif random_number == 1:
                sentence='神明并非遥不可及，只要你专心修炼，当大机缘成熟，便可收获果实'
            elif random_number == 2:
                sentence='我已经将近300岁了，但是远远比不上那些长生不老的神明，不过长生也并非好事'
            elif random_number == 3:
                sentence='我来自京城的巫师殿，我只不过是巫师荟荟众生的其中之一罢了。'
            print(npc_name+'对着你说：'+sentence+'\n···············')
        if hudong=='道别':
            print('---你对'+npc_name+'鞠躬后道别后离开了')
            break
        if hudong =='求香':
            player_things_bag.append(thing_id_name[1])
            print(npc_name+"对你说：心诚则灵，小施主")
        print("||||||||||||||||||||||")
def dongfang_youlong():
    import random
    npc_name = '东方游龙'
    sentence = 0
    random_number = random.randint(0, 2)

    if random_number == 0:
        sentence = npc_name + '说:”'
    if random_number == 1:
        sentence = npc_name + '望着你说:“你找我有什么事吗？”'
    if random_number == 2:
        sentence = npc_name + '说：“汝有何求与吾”？'
    try:
        print('--------------特殊NPC:' + special_npc_wear_describe[npc_name] + npc_name + '(' + special_npc_name[
            npc_name] + ')---------------')
    except:
        print('--------------特殊NPC:' + npc_name + '(' + special_npc_name[npc_name] + ')---------------')
    try:
        print('他看起来约莫已经' + special_npc_old['dongfang_youlong'] + '岁了')
    except:
        print('你没看出来他的年龄')
    print(special_npc_describe[special_npc_name[npc_name]])
    print('-' * 25)
    print(sentence)
    while True:
        print("||||||||||||||||||||||")
        hudong = input('指令：闲聊，道别，新手礼包：')
        if hudong == '闲聊':
            random_number = random.randint(0, 3)
            if random_number == 0:
                sentence = '我是'
            elif random_number == 1:
                sentence = '神明并非遥不可及，只要你专心修炼，当大机缘成熟，便可收获果实'
            elif random_number == 2:
                sentence = '我'
            elif random_number == 3:
                sentence = '我来自'
            print(npc_name + '对着你说：' + sentence + '\n···············')
        if hudong == '道别':
            print('---你对' + npc_name + '鞠躬后道别后离开了')
            break
        if hudong=='战斗':
            print('你对着「'+npc_name+'」大喊:“阁下领教壮士高招!”')
            message=zhandou('dongfang_youlong',0.0,is_special=1)
            if message[0]=='胜利':
                print('\n\n你战胜了'+npc_name)
            elif message[0]=='失败':
                print('\n\n'+npc_name+'把你打得满地找牙')
            sjk.player_sx0['生命值']=message[1]
        if hudong=='新手礼包':
            if 2 not in sjk.player_completed_mission_id and 2 not in sjk.player_mission_id:
                print(npc_name+'笑嘻嘻地对着你说道：你去帮我完成一个任务，事成之后你就可以得到新手礼包了，如何？')
                sjk.player_mission_id.append(2)
                print('\n\n系统:你获得了一项新任务，快去个人界面查看吧！')
            else:
                print(npc_name+'对你说：你之前不是已经接过这个任务了吗？你还想做一次？我可没有那么多奖励给你啊！！！')
                continue
def chicken():
    import random
    npc_name = '肉鸡'
    sentence = 0
    random_number = random.randint(0, 2)

    if random_number == 0:
        sentence = npc_name + '说:咕咕咕”'
    if random_number == 1:
        sentence = npc_name + '望着你说:“咕咕咕咕咕？咕咕咕”'
    if random_number == 2:
        sentence = npc_name + '说：“咕咕咕咕咕咕咕，呼呼'
    try:
        print('--------------特殊NPC:' + special_npc_wear_describe[npc_name] + npc_name + '(' + special_npc_name[
            npc_name] + ')---------------')
    except:
        print('--------------特殊NPC:' + npc_name + '(' + special_npc_name[npc_name] + ')---------------')
    try:
        print('他看起来约莫已经' + special_npc_old['dongfang_youlong'] + '岁了')
    except:
        print('你没看出来他的年龄')
    print(special_npc_describe[special_npc_name[npc_name]])
    print('-' * 25)
    print(sentence)
    while True:
        print("||||||||||||||||||||||")
        hudong = input('指令：宰杀，道别')

        if hudong == '道别':
            print("你离开了咕咕咕")

            break
        if hudong=='宰杀':
            print('你对着「'+npc_name+'」大喊:“小鸡崽子哪里跑？!”')
            message=zhandou('chicken',0.6,is_special=1)
            if message[0]=='胜利':
                print('\n\n你宰杀了'+npc_name+'\n你获得了鸡的尸体*1')
                sjk.player_things_bag.append('鸡的尸体')

            elif message[0]=='失败':
                print('\n\n'+npc_name+'把你打得满地找牙')
                print('\n吐槽：不是吧？一只鸡你都打不过？你也太菜了吧，天啊。。。')
            sjk.player_sx0['生命值']=message[1]


#sishen()
#normal_npc_hd("乞丐",0.1)