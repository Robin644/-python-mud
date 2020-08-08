#道具使用
def daoju_7():
    print('='*30)#
    print('-' * 30)#
    print('道具:小纸条_0')#
    import sjk#
    print('描述:不知道什么时候出现在你背包里的一张小纸条')#
    print('稀有程度:*无价之宝*')
    print('价值:0(无法出售)')
    print('-'*30)
    cho=input('确认要阅读它吗？:(Y\\N)').upper()
    if cho=='Y':
        print('你小心翼翼地展开纸条，伸出手指仔细阅读着上面的内容')
        print('你看到上面写着：\n致：亲爱的玩家们\n  欢迎您游玩本游戏。\n        作者\n      2020.8.8')
        sjk.player_things_bag.remove('小纸条_0')
        print('一滴泪水从你眼眶中流出，正当你想再看一次时，纸条突然化作了一缕烟尘，飘散而去。\n你忽而领悟了新的技能，赶紧去看看吧')
        sjk.player_skill0.append('血海无边')
        sjk.player_skill0_level['xuehaiwubian']=0
    else:
        print('你小心翼翼地收好了纸条@@@@@@')
        pass

def daoju_6():

    print('=' * 30)
    print('-' * 30)
    print('道具:新手礼包')
    import sjk
    print('描述:拆开后可以获得:\n最大生命值+100\n白铁素剑*1\n扎甲*1\n银两*100\n称号:内测玩家*1')
    print('稀有程度:平平无奇')
    print('价值:0(无法出售)')
    print('-' * 30)
    cho = input('确认要使用吗？:(Y\\N)').upper()
    if cho == 'Y':
        print('成功使用道具-新手礼包！\n最大生命值+100\n白铁素剑*1\n扎甲*1\n银两*100')
        sjk.player_wear_bag.append('扎甲')
        sjk.player_weapon_bag.append('白铁素剑')
        sjk.player_sx2['银两'] += 100
        sjk.player_describe_bag.append('内测玩家')
        sjk.player_sx0['最大生命值'] += 100
        sjk.player_things_bag.remove('新手礼包')
    else:
        print('你小心翼翼地收好了新手礼包@@@@@@@')
        pass
    print('=' * 30)