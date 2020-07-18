import time
from gn_hs import *
def jq_start():
    print("■"*30)
    print("渊 天 纪 : 元 年")
    print("   三界浩劫刚刚过去,三界百废待兴，千疮百孔。不久前得一子的地界界主魔帝被浩劫虚空重伤，险些致命，只得在家中打坐疗伤。\n暗流涌动，地界未知的危机悄然而至.......")
    print()
    input()
    
    print("魔帝殿   殿内")
    print("^"*30)
    print("---你位于魔帝殿内，正如平时一般，勤恳地做着打扫后殿的工作。")
    #time.sleep(1000)
    go=str(input("你要去前殿内看一下吗? Y/N :"))
    if go =='y' or go =='yes':
        print('---你来到前殿，眼前的景象富丽堂皇，而魔帝此时不在这里')
        print('---你又回到了后殿中')
    elif go=='n' or go=='no':
        print("你碰到了魔帝儿子的老师与魔帝的大弟子，要上前看看吗？")
        go=str(input('[Y/N]:'))
        if go =='Y':
            print("********")
            xinliyisheng()
        
        elif go =='N':
            pass
    print("你步行回到休息室")
   
    print()
    print('----一阵术法的响声响起')
    print()
    print('一支穿云箭射入你的颈，你失去了意识')
    print("---")
    print("■"*30)
    jq_zhandou_0()
def jq_zhandou_0():
    print("金色的箭雨不偏不倚如潮水般朝你涌来，你爆呵一声闪避躲开\n死神望着你，空洞的嘴角微微扬起，露出嗜血的笑容")
    print()
    print("暗  夜  将  至")
    zhandou(attack_npc_id="sishen",now_id=0.1,is_special=1)
    print("魔帝被偷袭\n陨落...\n魔帝之子不知所踪...\n搜寻无果....\n地界的命运陷入了未知中........")
    print("..................\n壹佰年后")
    player_name=input("你是魔帝之子，名为:")
    print("你已经一百多岁了，却不知为何身体与容貌都保持在年轻时的样貌，你记得你之前还是在天劫的封魔谷自爆元神，可现在却来到了一个陌生的城池，四处看看吧")
    import 主界面