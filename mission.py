import sjk


mission_name_id={"测试任务":0,"测试任务2":1,'新手任务：杀鸡':2}
mission_id_name={}
for key,value in mission_name_id.items():
    mission_id_name[value]=key#配对id与名字
mission_neirong={0:"这里是任务内容，用于debug测试",
                 1:"这里是任务内容，用于debug测试",
                 2:'这应该是你来到游戏后接取的第一个任务吧？\n现在快去醉仙楼，帮助NPC杀鸡吧！！！'}
mission_yaoqiu_describe={0:"装备一项技能",1:"装备两项技能",2:'杀死一只鸡'}
mission_jiangli_describe={0:"巫师权限",1:"攻击力+5",2:'新手礼包'}
#任务完成判定
def mission_yaoqiu_0():
    if 0 in sjk.player_mission_id and len(sjk.player_wearing_skill) >= 1:
        print("+" * 25)
        print("-"*15+"*任务:"+mission_id_name[0]+"-"*15)
        print("状态：完成")

        sjk.player_mission_id.remove(0)#重要方法，remove删除指定元素
        sjk.player_completed_mission_id.append(0)
        mission_jiangli_0()

    else:
        print("*未完成的任务*ID:0")


def mission_yaoqiu_1():
    #print("你现在装备着"+str(len(sjk.player_wearing_skill))+"个技能")
    if 1 in sjk.player_mission_id and len(sjk.player_wearing_skill) >= 2:
        print("+" * 25)
        print("-" * 15 + "*任务:" + mission_id_name[1] + "-" * 15)
        print("状态：完成")

        sjk.player_mission_id.remove(1)  # 重要方法，remove删除指定元素
        sjk.player_completed_mission_id.append(1)
        mission_jiangli_1()

    else:
        print("*未完成的任务*ID:1")
def mission_yaoqiu_2():
    #print("你现在装备着"+str(len(sjk.player_wearing_skill))+"个技能")
    if 2 in sjk.player_mission_id and '鸡的尸体' in sjk.player_things_bag:
        print("+" * 25)
        print("-" * 15 + "*任务:" + mission_id_name[2] + "-" * 15)
        print("状态：完成")
        sjk.player_things_bag.remove('鸡的尸体')

        sjk.player_mission_id.remove(2)  # 重要方法，remove删除指定元素
        sjk.player_completed_mission_id.append(2)
        mission_jiangli_2()

    else:
        print("*未完成的任务*ID:2")
#任务奖励函数如下
def mission_jiangli_0():
    sjk.player_sx1["巫师"]=1
    print("系统:任务完成！成功领得奖励"+mission_jiangli_describe[0])
    print("+"*25)
def mission_jiangli_1():
    sjk.player_sx0["攻击力"]+=5
    print("系统:任务完成！成功领得奖励"+mission_jiangli_describe[1])
    print("+"*25)
def mission_jiangli_2():
    #施工中
    print("系统:任务完成！成功领得奖励"+mission_jiangli_describe[2])
    sjk.player_things_bag.append('新手礼包')
    sjk.player_things_bag.append('小纸条_0')
    print('神秘人:一张小纸条忽而飘进了你的背包中~')

    print("+"*25)

