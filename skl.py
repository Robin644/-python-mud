#技能类
from random import *
from sjk import *
#外功 is_player(是否为玩家使用，默认为不是)
#只有特殊npc可以用技能
def xuehaiwubian(user_id,attack_id,is_player=1,is_special=None):
    #wg:血海无边
   
   #赋值攻击者与被攻击者属性
    if is_player == 1:#如果使用者是玩家
        user_id=None#id为玩家
        user_name='你'
        if is_special==1:
            attack_enemie_name=special_npc_id[attack_id]
            attack_enemie_sx=eval('special_npc_'+attack_id+'_sx')
        elif is_special==0:
            attack_enemie_sx=normal_npc_sx
            attack_enemie_name=normal_npc_id[attack_id]
        user_sx=player_sx0#赋值攻击者属性
        
    else:
        user_id=user_id
        if is_special==1:
            user_name=special_npc_id[user_id] 
            user_sx=eval('special_npc_'+user_id+'_sx')
      #  attack_enemie_name='你'
        else:
            user_name=normal_npc_id[user_id] 
            user_sx=normal_npc_sx
        attack_enemie_name='你'
                   
            
        attack_enemie_sx=player_sx0
    print('*'*30)
    print('「'+user_name+'」 对 「'+attack_enemie_name+'」 使用了技能「血海无边」')
    zhaoshi=randint(1,2)
    if zhaoshi==1:
        print('◇'+user_name+'使出一招「血云乌雨」，无边无际的血云忽然袭来，将'+attack_enemie_name+'笼罩其中，看起来十分可怖')
       
        panduan=randint(1,2)
        if panduan==1:
            attack=user_sx['攻击力']
            print('\n---'+user_name+'这一击无视了敌人的防御!!!造成了'+str(attack)+'点伤害')
        else:
            attack=user_sx['攻击力']-attack_enemie_sx['防御力']
            print('\n==='+user_name+'这一击造成了'+str(attack)+'点伤害')
        if attack<0:
            attack=0
            print(user_name+'的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值']-=attack
        
    
    elif zhaoshi==2:
        print('◇'+user_name+'使出一招「血刀无边」，一道浑身赤红的刀影袭来，忽然袭来。'+attack_enemie_name+'手足无措，正想防御')
        panduan=randint(1,2)
        if panduan==1:
            attack=user_sx['攻击力']*2
            print('\n---'+user_name+'身轻如燕，向前冲去，使得敌人手足无措。这一击得到了双倍伤害!!!造成了'+str(attack)+'点伤害')
        else:
            attack=user_sx['攻击力']-attack_enemie_sx['防御力']
            print('\n==='+user_name+'这一击造成了'+str(attack)+'点伤害')
        if attack<0:
            attack=0
            print(user_name+'的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值']-=attack
    buff_level=5
    buff_name="血咒"
    back_message=[attack_enemie_sx,user_sx,buff_name,buff_level]
    return back_message
    print('*'*30)
def yeqiuquan(user_id,attack_id,is_player=1,is_special=None):#wg:血海无边
   
   #赋值攻击者与被攻击者属性
    if is_player == 1:#如果使用者是玩家
        user_id=None#id为玩家
        user_name='你'
        if is_special==1:
            attack_enemie_name=special_npc_id[attack_id]
            attack_enemie_sx=eval('special_npc_'+attack_id+'_sx')
        else:
            attack_enemie_sx=normal_npc_sx
            attack_enemie_name=normal_npc_id[attack_id]
        user_sx=player_sx0#赋值攻击者属性
        
    else:
        user_id=user_id
        if is_special==1:
            user_name=special_npc_id[user_id] 
            user_sx=eval('special_npc_'+user_id+'_sx')
      #  attack_enemie_name='你'
        else:
            user_name=normal_npc_id[user_id] 
            user_sx=normal_npc_sx
        attack_enemie_name='你'
                   
            
        attack_enemie_sx=player_sx0
    print('*'*30)
    print('「'+user_name+'」 对 「'+attack_enemie_name+'」 使用了技能「野球拳」')
    zhaoshi=randint(1,2)
    if zhaoshi==1:
        print('◇'+user_name+'使出一招「打鸡血」，无边无际的拳头将'+attack_enemie_name+'打得措手不及')
       
        panduan=randint(1,2)
        if panduan==1:
            attack=user_sx['攻击力']
            print('\n---'+user_name+'这一击无视了敌人的防御!!!造成了'+str(attack)+'点伤害')
        else:
            attack=user_sx['攻击力']-attack_enemie_sx['防御力']
            print('\n==='+user_name+'这一击造成了'+str(attack)+'点伤害')
        if attack<0:
            attack=0
            print(user_name+'的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值']-=attack
        
    
    elif zhaoshi==2:
        print('◇'+user_name+'使出一招「市井流氓」,蓄势待发,'+attack_enemie_name+'手足无措，正想防御')
        panduan=randint(1,2)
        if panduan==1:
            attack=user_sx['攻击力']*2
            print('\n---'+user_name+'身轻如燕，向前冲去，使得敌人手足无措。这一击得到了双倍伤害!!!造成了'+str(attack)+'点伤害')
        else:
            attack=user_sx['攻击力']-attack_enemie_sx['防御力']
            print('\n==='+user_name+'这一击造成了'+str(attack)+'点伤害')
        if attack<0:
            attack=0
            print(user_name+'的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值']-=attack
    back_message=[attack_enemie_sx,user_sx]
    return back_message
    print('*'*30)
    
def taijiquan_yin(user_id,attack_id,is_player=1,is_special=1):
    #wg:太极掌·阴
   
   #赋值攻击者与被攻击者属性
    if is_player == 1:#如果使用者是玩家
        user_id=None#id为玩家
        user_name='你'
        if is_special==1:
            attack_enemie_name=special_npc_id[attack_id]
            attack_enemie_sx=eval('special_npc_'+attack_id+'_sx')
        elif is_special==0:
            attack_enemie_sx=normal_npc_sx
            attack_enemie_name=normal_npc_id[attack_id]
        user_sx=player_sx0#赋值攻击者属性
        
    else:
        user_id=user_id
        if is_special==1:
            user_name=special_npc_id[user_id] 
            user_sx=eval('special_npc_'+user_id+'_sx')
      #  attack_enemie_name='你'
        else:
            user_name=normal_npc_id[user_id] 
            user_sx=normal_npc_sx
        attack_enemie_name='你'
                   
            
        attack_enemie_sx=player_sx0
    #以下部分可以自由修改
    print('*'*30)
    print('「'+user_name+'」 对 「'+attack_enemie_name+'」 使用了技能「太极拳*阴」')
    zhaoshi=randint(1,2)
    if zhaoshi==1:
        print('◇'+user_name+'使出一招「阴极流转」，八卦阵从远方忽然袭来，将'+attack_enemie_name+'笼罩其中，圣洁的光芒不断冲刷着他的身躯')
       
        panduan=randint(1,2)
        if panduan==1:#触发暴击
            attack=user_sx['攻击力']
            print('\n---'+user_name+'这一击无视了敌人的防御!!!造成了'+str(attack)+'点伤害')
        else:
            attack=user_sx['攻击力']-attack_enemie_sx['防御力']
            print('\n==='+user_name+'这一击造成了'+str(attack)+'点伤害')
        if attack<0:
            attack=0
            print(user_name+'的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值']-=attack
        
    
    elif zhaoshi==2:
        print('◇'+user_name+'使出一招「五阴聚顶」，一道黑白相间的拳影高速袭来，仿佛千丈之长。'+attack_enemie_name+'手足无措，正想防御，却被打了个措手不及')
        panduan=randint(1,2)
        if panduan==1:#触发暴击
            attack=user_sx['攻击力']*2
            print('\n---'+user_name+'的太极拳·阴打出了暴击，这一击得到了双倍伤害!!!造成了'+str(attack)+'点伤害')
        else:
            attack=user_sx['攻击力']-attack_enemie_sx['防御力']
            print('\n==='+user_name+'这一击造成了'+str(attack)+'点伤害')
        if attack<0:
            attack=0
            print(user_name+'的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值']-=attack
    #添加buff---------首
    buff_name="太极拳印_阴"
    buff_level=3
    
    
    #添加buff---------尾
    back_message=[attack_enemie_sx,user_sx,buff_name,buff_level]
    return back_message
    print('*'*30)


def taijiquan(user_id, attack_id, is_player=1, is_special=1):
    # wg:太极掌

    # 赋值攻击者与被攻击者属性
    if is_player == 1:  # 如果使用者是玩家
        user_id = None  # id为玩家
        user_name = '你'
        if is_special == 1:
            attack_enemie_name = special_npc_id[attack_id]
            attack_enemie_sx = eval('special_npc_' + attack_id + '_sx')
        elif is_special == 0:
            attack_enemie_sx = normal_npc_sx
            attack_enemie_name = normal_npc_id[attack_id]
        user_sx = player_sx0  # 赋值攻击者属性

    else:
        user_id = user_id
        if is_special == 1:
            user_name = special_npc_id[user_id]
            user_sx = eval('special_npc_' + user_id + '_sx')
        #  attack_enemie_name='你'
        else:
            user_name = normal_npc_id[user_id]
            user_sx = normal_npc_sx
        attack_enemie_name = '你'

        attack_enemie_sx = player_sx0
    # 以下部分可以自由修改
    print('*' * 30)
    print('「' + user_name + '」 对 「' + attack_enemie_name + '」 使用了技能「太极拳*阴」')
    zhaoshi = randint(1, 2)
    if zhaoshi == 1:
        print('◇' + user_name + '大喊一声，使出<接,化,发>' + attack_enemie_name + '被打飞到数十米开外')
        print()
        print("接!")
        print("化!")
        print("发!")
        if is_player==1:
            pd_0=input("你大喝一声，喊出了第一式：")
            pd_1 = input("你大喝一声，喊出了第二式：")
            pd_2 = input("你大喝一声，喊出了第三式：")
            if all((pd_0=="接",pd_1=="化",pd_2=="发")):
                print("❀*＊☂☃☄♨")
                print("tql,你触发了一个小彩蛋！你打出了十万吨伤害！！！")
                yes=1



        panduan = randint(1, 2)
        if panduan == 1:  # 触发暴击
            attack = user_sx['攻击力']
            print('\n---' + user_name + '这一击无视了敌人的防御!!!造成了' + str(attack) + '点伤害')
            user_sx["生命值"]+=100
            attack_enemie_sx["生命值"]-=100
            print(user_name+"吸走了敌人的100滴血量！")
        else:
            attack = user_sx['攻击力'] - attack_enemie_sx['防御力']
            print('\n===' + user_name + '这一击造成了' + str(attack) + '点伤害')
        if attack < 0:#未造成暴击
            attack = 0
            print(user_name + '的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值'] -= attack


    elif zhaoshi == 2:
        print('◇' + user_name + '使出一招「五阴聚顶」，一道黑白相间的拳影高速袭来，仿佛千丈之长。' + attack_enemie_name + '手足无措，正想防御，却被打了个措手不及')
        panduan = randint(1, 2)
        if panduan == 1:  # 触发暴击
            attack = user_sx['攻击力'] * 2
            print('\n---' + user_name + '的太极拳打出了暴击，这一击得到了双倍伤害!!!造成了' + str(attack) + '点伤害')
        else:
            attack = user_sx['攻击力'] - attack_enemie_sx['防御力']
            print('\n===' + user_name + '这一击造成了' + str(attack) + '点伤害')
        if attack < 0:
            attack = 0
            print(user_name + '的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值'] -= attack
    if yes == 1:
        attack_enemie_sx["生命值"] -= 10000000

    # 添加buff---------首
    buff_name = "太极拳印_阴"
    buff_level = 3

    # 添加buff---------尾
    back_message = [attack_enemie_sx, user_sx, buff_name, buff_level]
    return back_message
    print('*' * 30)


def kuhaiwubian(user_id, attack_id, is_player=1, is_special=1):
    # wg:太极掌·阴

    # 赋值攻击者与被攻击者属性
    if is_player == 1:  # 如果使用者是玩家
        user_id = None  # id为玩家
        user_name = '你'
        if is_special == 1:
            attack_enemie_name = special_npc_id[attack_id]
            attack_enemie_sx = eval('special_npc_' + attack_id + '_sx')
        elif is_special == 0:
            attack_enemie_sx = normal_npc_sx
            attack_enemie_name = normal_npc_id[attack_id]
        user_sx = player_sx0  # 赋值攻击者属性

    else:
        user_id = user_id
        if is_special == 1:
            user_name = special_npc_id[user_id]
            user_sx = eval('special_npc_' + user_id + '_sx')
        #  attack_enemie_name='你'
        else:
            user_name = normal_npc_id[user_id]
            user_sx = normal_npc_sx
        attack_enemie_name = '你'

        attack_enemie_sx = player_sx0
    # 以下部分可以自由修改
    print('*' * 30)
    print('「' + user_name + '」 对 「' + attack_enemie_name + '」 使用了技能***「苦海无边」***')
    zhaoshi = randint(1, 2)
    if zhaoshi == 1:
        print('█' + user_name + '使出一招「我入地狱」，无边的阴煞之气从远方忽然袭来，将' + attack_enemie_name + '笼罩其中，不断啃食着'+attack_enemie_name+'的身躯')
        print('凄凄凄凄凄凄的声音在'+attack_enemie_name+'的耳边响起，令他毛骨悚然！！！')
        panduan = randint(1, 2)
        if panduan == 1:  # 触发暴击
            attack = user_sx['攻击力']
            print('\n---' + user_name + '这一击无视了敌人的防御，造成了' + str(attack) + '点伤害')
        else:
            attack = user_sx['攻击力'] - attack_enemie_sx['防御力']
            print('\n===' + user_name + '这一击造成了' + str(attack) + '点伤害')
        if attack < 0:
            attack = 0
            print(user_name + '的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值'] -= attack


    elif zhaoshi == 2:
        print('◇' + user_name + '使出一招「地狱无门」，一道猩红的利刃高速袭来，仿佛千丈之长。' + attack_enemie_name + '手足无措，正想防御，却被打了个措手不及，一口鲜血喷出')
        panduan = randint(1, 2)
        if panduan == 1:  # 触发暴击
            attack = user_sx['攻击力'] * randint(1,20000)
            print('\n---' + user_name + '的苦海无边打出了暴击，这一击得到了双倍伤害!!!造成了' + str(attack) + '点伤害')
        else:
            attack = user_sx['攻击力'] - attack_enemie_sx['防御力']
            print('\n===' + user_name + '这一击造成了' + str(attack) + '点伤害')
        if attack < 0:
            attack = 0
            print(user_name + '的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值'] -= attack
    # 添加buff---------首
    buff_name = "地狱无门"
    buff_level = 15

    # 添加buff---------尾
    back_message = [attack_enemie_sx, user_sx, buff_name, buff_level]
    return back_message
    print('*' * 30)


def gugugu(user_id, attack_id, is_player=1, is_special=None):
    # wg:咕咕咕

    # 赋值攻击者与被攻击者属性
    if is_player == 1:  # 如果使用者是玩家
        user_id = None  # id为玩家
        user_name = '你'
        if is_special == 1:
            attack_enemie_name = special_npc_id[attack_id]
            attack_enemie_sx = eval('special_npc_' + attack_id + '_sx')
        elif is_special == 0:
            attack_enemie_sx = normal_npc_sx
            attack_enemie_name = normal_npc_id[attack_id]
        user_sx = player_sx0  # 赋值攻击者属性

    else:
        user_id = user_id
        if is_special == 1:
            user_name = special_npc_id[user_id]
            user_sx = eval('special_npc_' + user_id + '_sx')
        #  attack_enemie_name='你'
        else:
            user_name = normal_npc_id[user_id]
            user_sx = normal_npc_sx
        attack_enemie_name = '你'

        attack_enemie_sx = player_sx0
    print('*' * 30)
    print('「' + user_name + '」 对 「' + attack_enemie_name + '」 使用了技能「！咕咕咕！」')
    zhaoshi = randint(1, 2)
    if zhaoshi == 1:
        print('◇' + user_name + '使出一招「小鸡啄米」张开鸡喙向着' + attack_enemie_name + '叮去')

        panduan = randint(1, 2)
        if panduan == 1:
            attack = user_sx['攻击力']
            print('\n---' + user_name + '这一击无视了敌人的防御!!!造成了' + str(attack) + '点伤害')
        else:
            attack = user_sx['攻击力'] - attack_enemie_sx['防御力']
            print('\n===' + user_name + '这一击造成了' + str(attack) + '点伤害')
        if attack < 0:
            attack = 0
            print(user_name + '的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值'] -= attack


    elif zhaoshi == 2:
        print('◇' + user_name + '使出一招「真★打鸡血」极力张开喙向着' + attack_enemie_name + '大声鸣叫！！！')
        panduan = randint(1, 2)
        if panduan == 1:
            attack = user_sx['攻击力'] * 2
            print('\n---' + user_name + '使得敌人手足无措。这一击得到了双倍伤害!!!造成了' + str(attack) + '点伤害')
        else:
            attack = user_sx['攻击力'] - attack_enemie_sx['防御力']
            print('\n===' + user_name + '这一击造成了' + str(attack) + '点伤害')
        if attack < 0:
            attack = 0
            print(user_name + '的攻击没有突破防御，未造成伤害')
        attack_enemie_sx['生命值'] -= attack
    buff_level = 5
    buff_name = "害怕"
    back_message = [attack_enemie_sx, user_sx, buff_name, buff_level]
    return back_message
    print('*' * 30)