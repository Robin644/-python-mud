import sjk
import mission
import save

def mission_check():
    while True:
        print("▂"*20)
        print("-"*10+"任务"+"-"*10)
        import sjk
        print("*"*20)
        print("你现在有"+str(len(sjk.player_mission_id))+"个未完成任务，你已经完成了"+str(len(sjk.player_completed_mission_id))+"个任务")
        print("你未完成的任务:")
        for id in sjk.player_mission_id:

            print(str(mission.mission_id_name[id]).replace('"', '').replace("[","").replace("]", ""))
        print("你已完成的任务:")
        for id in sjk.player_completed_mission_id:
            print(str(mission.mission_id_name[id]).replace('"', '').replace("[", "").replace("]", ""))




        action=str(input("输入0退出,输入1查看未完成任务，输入2查看已完成任务,输入3进行任务进度刷新（重要）: "))
        if action=="0":
            break
        elif action=="1":
            print("-"*20)
            try:
                xuhao=int(input("输入查看任务序号(0-x): "))
            except:
                print("请输入正确的序号!")
                continue
            try:
                print("▆"*30)
                print("-"*10+"任务:"+str(mission.mission_id_name[sjk.player_mission_id[xuhao]])+"-"*10)
                print("任务内容:"+mission.mission_neirong[sjk.player_mission_id[xuhao]])
                print("任务要求："+mission.mission_yaoqiu_describe[sjk.player_mission_id[xuhao]])
                print("任务奖励:"+mission.mission_jiangli_describe[sjk.player_mission_id[xuhao]])
                print()
                print("▆" * 30)

            except:
                print("出bug聊,加QQ2432541891反馈北")
                print("-" * 20)
        elif action == "2":
            print("-" * 20)
            try:
                xuhao = int(input("输入查看已完成任务序号(0-x): "))
            except:
                print("请输入正确的序号！")
                continue
            try:
                print("▆" * 30)
                print("-" * 10 + "任务:" + mission.mission_id_name[sjk.player_completed_mission_id[xuhao]] + "-" * 10)
                print("任务内容:" + mission.mission_neirong[sjk.player_completed_mission_id[xuhao]])
                print("任务要求：" + mission.mission_yaoqiu_describe[sjk.player_completed_mission_id[xuhao]])
                print("任务奖励:" + mission.mission_jiangli_describe[sjk.player_completed_mission_id[xuhao]])
                print()
                print("▆" * 30)

            except:
                print("出bug聊,加QQ2432541891反馈北")
            print("-" * 20)
        elif action == "3":
            try:
                times=len(sjk.player_mission_id)
                while times >0:
                    for id in sjk.player_mission_id:
                        eval("mission.mission_yaoqiu_"+str(id))()
                    times-=1
            except:
                print("oops,又出bug了")










    print("*"*20)
    print("▂" * 20)

def player_selfcheck(describe_list,player_wearing_describe,player_face,player_smz,player_max_smz,player_describe_bag,now_id):
    a=True
    import sjk
    while a: 
        print('------------------------------')
        print('输入0退出，输入1打开背包，输入2查看自己，输入3查看称号,输入4查看属性\n输入5查看技能，输入6打开装备系统，输入7丢下物品，输入8疗伤,输入9打开任务系统,输入10打开存/读档系统\n输入11使用物品\n:')
        player_choose_2=str(input('输入序号'))
        if player_choose_2 == "9" or player_choose_2 == "任务系统":
            mission_check()
        if player_choose_2 == "11" or player_choose_2 == "使用物品":
            print('-'*8+'使用物品'+'-'*8)
            print('-' * 20)
            print('你现在有物品:')
            import sjk
            for thing in sjk.player_things_bag:
                print(thing)
            try:
                num=int(input('请输入你要使用的物品[0-x]:'))
            except:
                print('序号错误！！')
                continue
            else:
                try:
                    if sjk.player_things_bag[num] != None and sjk.player_things_bag[num] != '':
                        thing_id=sjk.thing_name_id[sjk.player_things_bag[num]]
                    else:
                        print('！！背包无此物品！！')
                        continue
                except:
                    print('物品不存在！！！')
                    continue
                try:
                    import daoju
                    eval('daoju.daoju_'+str(thing_id))()
                except:
                    print('\n')
                    print('--\n你拿着'+sjk.player_things_bag[num]+'转来转去，发现它好像并没有什么作用！\n--')
                    print('\n')








            print('-' * 20)
        if player_choose_2 == "10" or player_choose_2 == "存档系统":
            print("游戏数据系统--------------------------------")
            code=input("输入0退出，输入1存档，输入2读档")
            if code=="0":
                pass
            elif code=="1":
                save.cundang()
            elif code=="2":
                sjk.player_name, sjk.player_weapon_bag, sjk.player_mission_id, sjk.player_wearing_skill, sjk.player_completed_mission_id,sjk.player_things_bag, sjk.player_describe_bag, sjk.player_face,sjk.player_skill0, sjk.player_skill1, sjk.player_skill0_level, sjk.player_skill1_level, sjk.player_wearing_skill, sjk.player_wearing_wear, sjk.player_wearing_weapon, sjk.player_wear_bag, sjk.player_sx0, sjk.player_sx1, sjk.player_sx2=save.dudang()
            print("\n"+"-"*30)

        if player_choose_2=='5' or player_choose_2=='查看技能':
            print('-'*30)
            print('*********玩家技能列表*********')
            try:            
                print('战斗技能列表:  '+str(sjk.player_skill0).replace('[','「').replace("'","").replace(']','」'))
            except:
                print('你没有「战斗技能」')
            
            try:                    
                print('生活技能列表:  '+str(sjk.player_skill1).replace('[','「').replace("'","").replace(']','」'))
            except:
                print('你没有「生活技能」')
            print('='*30)
            try:
                print('技能「一」:【'+sjk.player_wearing_skill[0]+'】')
            except:
                print('技能「一」插槽无技能')
            try:
                print('技能「二」:【'+sjk.player_wearing_skill[1]+'】')
            except:                
                print('技能「二」插槽无技能')
            print('*'*30)
            code=str(input('指令:装备技能(0),卸下技能(1),查看技能详细(2)'))
            if code =='0':
                while True:
                    import sjk
                    if sjk.player_wearing_skill != [] and sjk.player_wearing_skill !=None:
                        print('你现在装备着技能*'+str(sjk.player_wearing_skill).replace("'","")+'*')
                    else:
                        print('*你什么技能都没有装备*')
                
                    print('你现在有技能'+str(sjk.player_skill0))
                    try:
                        if sjk.player_skill0 != [] and sjk.player_skill0 != None:
                            wear_skill=str(input('输入装备技能序号(0开始):\n'))
                        else:
                            print('你什么技能都还没有啊！！！')
                            break
                    except:
                        print('错误的序号')
                        break
               
                    if sjk.player_skill0[int(wear_skill)] != None and int(len(sjk.player_skill0))<=2:
                        
                        try:
                            chacao=int(input('输入插槽(0/1):'))
                        except:
                            print('!插槽错误!')
                            break
                        
                        try:
                            try:
                                if sjk.player_wearing_skill[chacao] != None:
                                
                                    del sjk.player_wearing_skill[chacao]
                            except:
                                pass
                            sjk.player_wearing_skill.insert(chacao,sjk.player_skill0[int(wear_skill)])
                        
                        except:
                            print('oops,出错了')
                            break
                        
                        else:
                            print('成功装备技能「'+sjk.player_skill0[int(wear_skill)]+'」')
                            break


            if code=='1':
                
                print('-'*30)
                
                try:
                    
                    if sjk.player_wearing_skill[0] != None or sjk.player_wearing_skill[1] != None:
                        chacao=int(input('输入卸下技能的插槽:\n'))
                        if sjk.player_wearing_skill[chacao] != None:
                            
                            del sjk.player_wearing_skill[chacao]
                            print('*成功卸下技能*')
                        else:
                            print('此技能槽无技能')
                    else:
                        print('你没有装备任何技能')
                except:
                    pass
            elif code=="2":
                while True:
                    try:            
                        print('战斗技能列表:  '+str(sjk.player_skill0).replace('[','「').replace("'","").replace(']','」'))
                    except:
                        print('你没有「战斗技能」')
            
                
                                 
                    print('='*30)
                    code=str(input("输入你想查看的战斗技能序号(从左到右从0开始数) :"))
                    if any((code=="-1" , code=="quit" , code=="q")):
                        break

                    try:
                        print('='*20)
                        #skill_id=print(sjk.skill0_name_id[sjk.player_skill0[int(code)]])
                        print('技能描述:\n'+sjk.skill0_id_describe[sjk.skill0_name_id[sjk.player_skill0[int(code)]]])
                        print('='*20)
                        print('技能等级：'+str(sjk.player_skill0_level[sjk.skill0_name_id[sjk.player_skill0[int(code)]]]))
                        print('=' * 20)
                    except:
                        print("序号错误!!!\n\n")
                        continue
                    #if any(code=="-1" , code=="quit" , code=="q"):
                       # break
                         
                
                
            
                            
                
            
            
            
            
            print('*'*30)
            print('-'*30)
        
        
        import sjk
        if player_choose_2=='1' or player_choose_2=='查看背包':
            import sjk
            print('-----------\n你打开了你的背包查看了起来\n---------')
            print('防具:'+str(sjk.player_wear_bag).replace("'",""))
            print('武器:'+str(sjk.player_weapon_bag).replace("'",""))
            print('物品:'+str(sjk.player_things_bag).replace("'",""))
            while True:
                check_class=str(input('指令:查看防具\武器\道具: '))
                try:
                    
                    
                    if check_class=='查看防具':
                        xuhao=int(input('输入序号: '))
                        print('-'*10+sjk.player_wear_bag[xuhao]+'-'*10)
                        print('描述:'+sjk.wear_id_describe[sjk.wear_name_id[sjk.player_wear_bag[xuhao]]])
                        print('-'*25)
                    elif check_class=='查看武器':
                        xuhao=int(input('输入序号: '))
                        print('-'*10+sjk.player_weapon_bag[xuhao]+'-'*10)
                        print('描述:'+sjk.weapon_id_describe[sjk.weapon_name_id[sjk.player_weapon_bag[xuhao]]])
                        print('-'*25)
                    elif check_class=='查看道具':
                        xuhao=int(input('输入序号: '))
                        try:
                            print('-'*10+sjk.player_things_bag[xuhao]+'-'*10)
                            print('描述:'+sjk.thing_id_describe[sjk.thing_name_id[sjk.player_things_bag[xuhao]]])
                            print('-'*25)
                        except:
                            print('无描述')
                            print('-'*30)
                    else:
                        break
                
                
                except:
                    print('oops,操作错误')
            print('-'*30)

            continue
        if player_choose_2=='0' or player_choose_2=='退出':
            print('-----------\n你重新起身，恢复了战斗状态\n---------')
            break
        if player_choose_2=='2' or player_choose_2=='查看自己':
            import sjk
            print('-----------\n你开始仔细揣摩自己\n---------')
            player_face=sjk.player_sx1['魅力']
            if player_face<=20 :
                player_d='眼斜嘴歪，双目无神，长着副死鱼脸'
            elif player_face>20 and player_face<=30:
                player_d='相貌平平，其貌不扬，典型芸芸众生大众脸'
            elif player_face>30 and player_face<=40:
                player_d='五官端正，不褒不贬，还算可以吧'
            elif player_face>40 and player_face<=50:
                player_d='眉目似剑，双目似星，忍不住让人多看两眼'
            elif player_face>50 and player_face<=60:
                player_d='🐽朱唇红颜，五官被勾勒得犹如画中，让人一眼便怦然心动■■'
            elif player_face>60 and player_face<=70:
                player_d='☆红颜若雪，肌肤雪白，让男女老少看了都好生羡慕☆'
            elif player_face>70 and player_face<=80:
                player_d=' 眉目如星，双目如炬，犹如画中人一般脱离尘世 ●'
            elif player_face>80 and player_face<=90:
                player_d='仙风道骨，眼神深邃，散发出强大的自信，惊为天人，俊美无比  ■'
            elif player_face>90 and player_face<=100:
                player_d=' 仙风道骨，仿佛如天上仙人下凡，无数人为之倾倒 '
            
            ##伤势描述

            if (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100<=20 :
                player_hp_d='打了个踉跄，气息散乱，奄奄一息，似乎随时要昏死过去'
            elif (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100>20 and (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100<=30 :               ##貌不扬'
                player_hp_d='似乎受了极重的伤，不治疗也许会有生命危险'
            elif (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100>30 and (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100<=50 :               ##貌不扬'
                player_hp_d='受伤不轻，看上去有些吃力，不治疗或许会有生命危险'
            elif (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100>50 and (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100<=70 :               ##貌不扬'
                player_hp_d='气息平稳，看上去隐约受了点伤，好在不严重'
            elif (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100>70 and (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100<=90 :               ##貌不扬'

                player_hp_d='气血似乎比较充沛，隐约有些轻伤，不过总体来说并不碍事'
            elif (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100>90 and (sjk.player_sx0["生命值"]//sjk.player_sx0["最大生命值"])*100<=100 :               ##貌不扬'

                player_hp_d='面色红润，气息平稳，气血充沛极了，完全不用担心'
            else:
                player_hp_d="系统也不知道你现在气血是什么状况了，晕"
            
            
            print()
            import sjk
            print("姓名:"+sjk.player_name)
            try:
                print('称号:'+str(player_wearing_describe[0]))
            except:
                print('称号:无')
            print('性别:')
            print('年龄:')
            print('你生得'+player_d+'\n你现在'+str(player_hp_d))
            for wears in sjk.player_wearing_weapon:
                player_wa=wears
                print('你手中拿着:「'+player_wa+'」')
            for wear in sjk.player_wearing_wear:
                player_w=wear
                print('你身上穿着:「'+player_w+'」')
            continue
        
        
            
            
            
        if player_choose_2=='8':
            print('疗伤成功')
            sjk.player_sx0['生命值']=sjk.player_sx0['最大生命值']
        if player_choose_2=='3' or player_choose_2=='查看称号':
            print('你现在的称号有'+str(player_describe_bag))
            ##['创世神[0]','天界界主[1]','人间界界主[2]','冥界界主[3]']
            print('你现在装备的称号有'+str(player_wearing_describe))
            wear_describe=str(input('输入q退出，输入a装备称号，输入u卸下称号'))
            if wear_describe=='a'    :
                xuhao=str(input('输入序号'))
                try:
                    int(xuhao)
                except:
                    print('序号有误！！！')
                    continue
                try:
                    if all((describe_list[int(xuhao)] !=None , len(player_wearing_describe)<1 , player_describe_bag[int(xuhao)] != None)):
                
                        player_wearing_describe.append(player_describe_bag[int(xuhao)])
                    else:
                        print('请输入正确的序号/已装备了称号')
                        continue
                except:
                    print('哪有这个称号？？？错误（001）')
                    continue
            if wear_describe=='q':
                print()
                break
            if wear_describe=='u':
                try:
                    print('你卸下了称号'+str(player_wearing_describe[0]))
                    player_wearing_describe.pop()
                except:
                    print('你什么称号都没装备')
       
        if player_choose_2=='4' or player_choose_2=='查看属性':
            import sjk
            
            print('-'*15+'属性'+'-'*15)
            print('*'*15+'主要属性'+'*'*15)
            print(sjk.player_sx0)
            print('*'*15+'次要属性'+'*'*15)
            print(sjk.player_sx1)
            print('*'*15+'其他属性'+'*'*15)
            print(sjk.player_sx2)
        if player_choose_2=='6':
            while True:
                xitong=str(input('输入0退出，输入1进入装备系统，输入2进入武器系统'))
                if xitong=='0':
                    break
                
                
                if xitong == '1':
                    print('-'*10+'防具'+'-'*10)
                    
                    print('你现在有防具:'+str(sjk.player_wear_bag).replace("'",""))
                    print('你现在装备的防具有'+str(sjk.player_wearing_wear))

                    wear_describe=str(input('输入q退出，输入a装备，输入u卸下'))
                    if wear_describe=='a'    :
                        print('你现在的防具有'+str(sjk.player_wearing_wear))

                        xuhao=str(input('输入序号'))
                    
                        if all((sjk.player_wear_bag[int(xuhao)] !=None , len(sjk.player_wearing_wear)<1 , sjk.player_wear_bag[int(xuhao)] != None)):
                
                            sjk.player_wearing_wear.append(sjk.player_wear_bag[int(xuhao)])
                            del sjk.player_wear_bag[int(xuhao)]
                            print('你穿好了'+str(sjk.player_wearing_wear).replace("'",""))
                            sjk.player_sx0['防御力']+=sjk.wear_id_sx0[sjk.wear_name_id[sjk.player_wearing_wear[0]]]

                        else:
                            print('请输入正确的序号/已装备了防具')
                            continue
                    if wear_describe=='q':
                        break
                    if wear_describe=='u':
                        
                        try:
                            
                            print('你脱下了防具'+str(sjk.player_wearing_wear[0]).replace("'",""))
                       
                            sjk.player_sx0['防御力']-=sjk.wear_id_sx0[sjk.wear_name_id[sjk.player_wearing_wear[0]]]

                            sjk.player_wear_bag.append(sjk.player_wearing_wear[0])
                            sjk.player_wearing_wear.pop()
                        except:
                            print('你什么都没穿，脱个屁呀?')
                    
                    
                    print('-'*30)
                if xitong == '2':
                    
                   
                    print('-'*10+'武器'+'-'*10)
                    print('你现在装备的武器有'+str(sjk.player_wearing_weapon))

                    print('你现在有武器:'+str(sjk.player_weapon_bag).replace("'",""))
                    wear_describe=str(input('输入q退出，输入a装备，输入u卸下'))
                    if wear_describe=='a'    :
                        xuhao=str(input('输入序号'))
                     
                        if all((sjk.player_weapon_bag[int(xuhao)] !=None , len(sjk.player_wearing_weapon)<1 , sjk.player_weapon_bag[int(xuhao)] != None)):
                
                            sjk.player_wearing_weapon.append(sjk.player_weapon_bag[int(xuhao)])
                            del sjk.player_weapon_bag[int(xuhao)]
                            print('你穿好了'+str(sjk.player_wearing_weapon).replace("'",""))
                            sjk.player_sx0['攻击力']+=sjk.weapon_id_sx0[sjk.weapon_name_id[sjk.player_wearing_weapon[0]]]

                        else:
                            print('请输入正确的序号/已装备了武器')
                            continue
                    if wear_describe=='q':
                        break
                    if wear_describe=='u':
                        try:
                            print('你卸下了武器'+str(sjk.player_wearing_weapon[0]).replace("'",""))
                        
                            sjk.player_sx0['攻击力']-=sjk.weapon_id_sx0[sjk.weapon_name_id[sjk.player_wearing_weapon[0]]]
                            sjk.player_weapon_bag.append(sjk.player_wearing_weapon[0])
                            sjk.player_wearing_weapon.pop()
                        except:
                            print('你什么武器都没装备')

                    
                    
                    print('-'*30)
        if player_choose_2 =='7':
            while True:
                which_class=str(input('输入0退出，输入1打开防具背包，输入2打开武器背包，输入3打开物品背包\n'))
                if which_class=='0'     :
                    break
                elif which_class =='1'  :
                    print('防具:'+str(sjk.player_wear_bag).replace("'",""))
                    try:
                        xuhao=int(input('输入丢下的防具序号'))
                        if sjk.player_wear_bag[int(xuhao)] !=None:
                            try:
                                eval('thing_room_'+str(now_id).replace(".","_")).append(sjk.player_wear_bag[xuhao])
                                print('已丢下'+sjk.player_wear_bag[xuhao])
                                del sjk.player_wear_bag[xuhao]
                            except:
                                eval('thing_room_room_'+str(now_id).replace(".","_")).append(sjk.player_wear_bag[xuhao])
                                print('已丢下'+sjk.player_wear_bag[xuhao])
                                del sjk.player_wear_bag[xuhao]
                                
                    except:
                        print('序号不合法')
                        continue 
                elif which_class =='2':
                    print('武器:'+str(sjk.player_weapon_bag).replace("'",""))
                    try:
                        
                        xuhao=int(input('输入丢下的武器序号'))
                        if sjk.player_weapon_bag[int(xuhao)] !=None:
                            try:
                                eval('thing_room_'+str(now_id).replace(".","_")).append(sjk.player_weapon_bag[xuhao])
                                print('已丢下'+sjk.player_weapon_bag[xuhao])
                                del sjk.player_weapon_bag[xuhao]
                            except:
                                eval('thing_room_room_'+str(now_id).replace(".","_")).append(sjk.player_weapon_bag[xuhao])
                                print('已丢下'+sjk.player_weapon_bag[xuhao])
                                
                                del sjk.player_weapon_bag[xuhao]

                    
                    
                    except:
                        print('序号不合法')
                        continue
                elif which_class =='3':
                    print('物品:'+str(sjk.player_things_bag).replace("'",""))
                    try:
                        
                        xuhao=int(input('输入丢下的物品序号'))
                        if sjk.player_things_bag[int(xuhao)] !=None:
                            try:
                                
                                eval('thing_room_'+str(now_id).replace(".","_")).append(sjk.player_things_bag[xuhao])
                                print('已丢下'+sjk.player_things_bag[xuhao])
                                
                                
                                del sjk.player_things_bag[xuhao]
                            except:
                                eval('thing_room_room_'+str(now_id).replace(".","_")).append(sjk.player_things_bag[xuhao])
                                print('已丢下'+sjk.player_things_bag[xuhao])
                                
                                del sjk.layer_things_bag[xuhao]

                    
                    
                    except:
                        print('序号不合法')
                        continue
                    
                    
                    
                    
                    '''
                    player_wearing_describe=[]#已装备称号
player_weapon_bag=[]#武器背包
player_wear_bag=[wear_id_name[0]]#防具背包
player_wearing_weapon=[weapon_id_name[0]]#已装备的武器
player_wearing_wear=[wear_id_name[0]]#
player_things_bag=[]#物品背包
                    '''