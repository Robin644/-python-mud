from sjk import *
def player_selfcheck(describe_list,player_wearing_describe,player_money,player_face,player_smz,player_max_smz,player_describe_bag,now_id):
    a=True
    while a: 
        print('------------------------------')
        print('输入0退出，输入1打开背包，输入2查看自己，输入3查看称号,输入4查看属性,输入5查看技能，输入6打开装备系统，输入7丢下物品，输入8疗伤\n:')
        player_choose_2=str(input('输入序号'))
        if player_choose_2=='5' or player_choose_2=='查看技能':
            print('-'*30)
            print('*********玩家技能列表*********')
            try:            
                print('战斗技能列表:  '+str(player_skill0).replace('[','「').replace("'","").replace(']','」'))
            except:
                print('你没有「战斗技能」')
            
            try:                    
                print('生活技能列表:  '+str(player_skill1).replace('[','「').replace("'","").replace(']','」'))
            except:
                print('你没有「生活技能」')
            print('='*30)
            try:
                print('技能「一」:【'+player_wearing_skill[0]+'】')
            except:
                print('技能「一」插槽无技能')
            try:
                print('技能「二」:【'+player_wearing_skill[1]+'】')
            except:                
                print('技能「二」插槽无技能')
            print('*'*30)
            code=str(input('指令:装备技能(0),卸下技能(1),查看技能详细(2)'))
            if code =='0':
                while True:
                    if player_wearing_skill != [] and player_wearing_skill !=None:
                        print('你现在装备着技能*'+str(player_wearing_skill).replace("'","")+'*')
                    else:
                        print('*你什么技能都没有装备*')
                
                    print('你现在有技能'+str(player_skill0))
                    try:
                        wear_skill=str(input('输入装备技能序号(0开始):\n'))
                    except:
                        print('错误的序号')
                        break
               
                    if player_skill0[int(wear_skill)] != None and int(len(player_skill0))<=2:
                        
                        try:
                            chacao=int(input('输入插槽(0/1):'))
                        except:
                            print('!插槽错误!')
                            break
                        
                        try:
                            try:
                                if player_wearing_skill[chacao] != None:
                                
                                    del player_wearing_skill[chacao]
                            except:
                                pass
                            player_wearing_skill.insert(chacao,player_skill0[int(wear_skill)])
                        
                        except:
                            print('oops,出错了')
                            break
                        
                        else:
                            print('成功装备技能「'+player_skill0[int(wear_skill)]+'」')
                            break
                        
            if code=='1':
                
                print('-'*30)
                
                try:
                    
                    if player_wearing_skill[0] != None or player_wearing_skill[1] != None:
                        chacao=int(input('输入卸下技能的插槽:\n'))
                        if player_wearing_skill[chacao] != None:
                            
                            del player_wearing_skill[chacao]
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
                        print('战斗技能列表:  '+str(player_skill0).replace('[','「').replace("'","").replace(']','」'))
                    except:
                        print('你没有「战斗技能」')
            
                
                                 
                    print('='*30)
                    code=str(input("输入你想查看的战斗技能序号(从左到右从0开始数) :"))
                    if any((code=="-1" , code=="quit" , code=="q")):
                        break

                    try:

                        print(skill0_id_describe[skill0_name_id[player_skill0[int(code)]]])
                    except:
                        print("序号错误!!!")
                        continue
                    #if any(code=="-1" , code=="quit" , code=="q"):
                       # break
                         
                
                
            
                            
                
            
            
            
            
            print('*'*30)
            print('-'*30)
        
        
        
        if player_choose_2=='1' or player_choose_2=='查看背包':
            print('-----------\n你打开了你的背包查看了起来\n---------')
            print('防具:'+str(player_wear_bag).replace("'",""))
            print('武器:'+str(player_weapon_bag).replace("'",""))
            print('物品:'+str(player_things_bag).replace("'",""))
            while True:
                check_class=str(input('指令:查看防具\武器\道具: '))
                try:
                    
                    
                    if check_class=='查看防具':
                        xuhao=int(input('输入序号: '))
                        print('-'*10+player_wear_bag[xuhao]+'-'*10)
                        print('描述:'+wear_id_describe[wear_name_id[player_wear_bag[xuhao]]])
                        print('-'*25)
                    elif check_class=='查看武器':
                        xuhao=int(input('输入序号: '))
                        print('-'*10+player_weapon_bag[xuhao]+'-'*10)
                        print('描述:'+weapon_id_describe[weapon_name_id[player_weapon_bag[xuhao]]])
                        print('-'*25)
                    elif check_class=='查看道具':
                        xuhao=int(input('输入序号: '))
                        try:
                            print('-'*10+player_things_bag[xuhao]+'-'*10)
                            print('描述:'+thing_id_describe[thing_name_id[player_things_bag[xuhao]]])
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
            print('-----------\n你开始仔细揣摩自己\n---------')
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
            if (player_smz/player_max_smz)*100<=20 :
                player_hp_d='打了个踉跄，气息散乱，奄奄一息，似乎随时要昏死过去'
            elif (player_smz/player_max_smz)*100>20 and (player_smz/player_max_smz)*100<=30 :               ##貌不扬'
                player_hp_d='似乎受了极重的伤，不治疗也许会有生命危险'
            elif (player_smz/player_max_smz)*100>30 and (player_smz/player_max_smz)*100<=50 :               ##貌不扬'
                player_hp_d='受伤不轻，看上去有些吃力，不治疗或许会有生命危险'
            elif (player_smz/player_max_smz)*100>50 and (player_smz/player_max_smz)*100<=70 :               ##貌不扬'
                player_hp_d='气息平稳，看上去隐约受了点伤，好在不严重'
            elif (player_smz/player_max_smz)*100>70 and (player_smz/player_max_smz)*100<=90 :               ##貌不扬'

                player_hp_d='气血似乎比较充沛，隐约有些轻伤，不过总体来说并不碍事'
            elif player_smz//player_max_smz*100>90 and player_smz//player_max_smz*100<=100 :               ##貌不扬'

                player_hp_d='面色红润，气息平稳，气血充沛极了，完全不用担心'
            
            
            print()
            print('称号:'+str(player_wearing_describe))
            print('性别:')
            print('年龄:')
            print('你生得'+player_d+'\n你现在'+str(player_hp_d))
            for wears in player_wearing_weapon:
                player_wa=wears
                print('你手中拿着:「'+player_wa+'」')
            for wear in player_wearing_wear:
                player_w=wear
                print('你身上穿着:「'+player_w+'」')
            continue
        
        
            
            
            
        if player_choose_2=='8':
            print('疗伤成功')
            player_sx0['生命值']=player_sx0['最大生命值']
        if player_choose_2=='3' or player_choose_2=='查看称号':
            print('你现在的称号有'+str(player_describe_bag))
            ##['创世神[0]','天界界主[1]','人间界界主[2]','冥界界主[3]']
            print('你现在装备的称号有'+str(player_wearing_describe))
            wear_describe=str(input('输入q退出，输入a装备称号，输入u卸下称号'))
            if wear_describe=='a'    :
                xuhao=str(input('输入序号'))
                    
                if all((describe_list[int(xuhao)] !=None , len(player_wearing_describe)<1 , player_describe_bag[int(xuhao)] != None)):
                
                    player_wearing_describe.append(player_describe_bag[int(xuhao)])
                else:
                    print('请输入正确的序号/已装备了称号')
                    continue
            if wear_describe=='q':
                break
            if wear_describe=='u':
                try:
                    print('你卸下了称号'+str(player_wearing_describe[0]))
                    player_wearing_describe.pop()
                except:
                    print('你什么称号都没装备')
       
        if player_choose_2=='4' or player_choose_2=='查看属性':
            
            print('-'*15+'属性'+'-'*15)
            print('*'*15+'主要属性'+'*'*15)
            print(player_sx0)
            print('*'*15+'次要属性'+'*'*15)
            print(player_sx1)
            print('*'*15+'其他属性'+'*'*15)
            print(player_sx2)
        if player_choose_2=='6':
            while True:
                xitong=str(input('输入0退出，输入1进入装备系统，输入2进入武器系统'))
                if xitong=='0':
                    break
                
                
                if xitong == '1':
                    print('-'*10+'防具'+'-'*10)
                    
                    print('你现在有防具:'+str(player_wear_bag).replace("'",""))
                    print('你现在装备的防具有'+str(player_wearing_wear))

                    wear_describe=str(input('输入q退出，输入a装备，输入u卸下'))
                    if wear_describe=='a'    :
                        print('你现在的防具有'+str(player_wearing_wear))

                        xuhao=str(input('输入序号'))
                    
                        if all((player_wear_bag[int(xuhao)] !=None , len(player_wearing_wear)<1 , player_wear_bag[int(xuhao)] != None)):
                
                            player_wearing_wear.append(player_wear_bag[int(xuhao)])
                            del player_wear_bag[int(xuhao)]
                            print('你穿好了'+str(player_wearing_wear).replace("'",""))
                            player_sx0['防御力']+=wear_id_sx0[wear_name_id[player_wearing_wear[0]]]

                        else:
                            print('请输入正确的序号/已装备了防具')
                            continue
                    if wear_describe=='q':
                        break
                    if wear_describe=='u':
                        
                        try:
                            
                            print('你脱下了防具'+str(player_wearing_wear[0]).replace("'",""))
                       
                            player_sx0['防御力']-=wear_id_sx0[wear_name_id[player_wearing_wear[0]]]

                            player_wear_bag.append(player_wearing_wear[0])
                            player_wearing_wear.pop()
                        except:
                            print('你什么都没穿，脱个屁呀?')
                    
                    
                    print('-'*30)
                if xitong == '2':
                    
                   
                    print('-'*10+'武器'+'-'*10)
                    print('你现在装备的武器有'+str(player_wearing_weapon))

                    print('你现在有武器:'+str(player_weapon_bag).replace("'",""))
                    wear_describe=str(input('输入q退出，输入a装备，输入u卸下'))
                    if wear_describe=='a'    :
                        xuhao=str(input('输入序号'))
                     
                        if all((player_weapon_bag[int(xuhao)] !=None , len(player_wearing_weapon)<1 , player_weapon_bag[int(xuhao)] != None)):
                
                            player_wearing_weapon.append(player_weapon_bag[int(xuhao)])
                            del player_weapon_bag[int(xuhao)]
                            print('你穿好了'+str(player_wearing_weapon).replace("'",""))
                            player_sx0['攻击力']+=weapon_id_sx0[weapon_name_id[player_wearing_weapon[0]]]

                        else:
                            print('请输入正确的序号/已装备了武器')
                            continue
                    if wear_describe=='q':
                        break
                    if wear_describe=='u':
                        try:
                            print('你卸下了武器'+str(player_wearing_weapon[0]).replace("'",""))
                        
                            player_sx0['攻击力']-=weapon_id_sx0[weapon_name_id[player_wearing_weapon[0]]]
                            player_weapon_bag.append(player_wearing_weapon[0])
                            player_wearing_weapon.pop()
                        except:
                            print('你什么武器都没装备')

                    
                    
                    print('-'*30)
        if player_choose_2 =='7':
            while True:
                which_class=str(input('输入0退出，输入1打开防具背包，输入2打开武器背包，输入3打开物品背包\n'))
                if which_class=='0'     :
                    break
                elif which_class =='1'  :
                    print('防具:'+str(player_wear_bag).replace("'",""))
                    try:
                        xuhao=int(input('输入丢下的防具序号'))
                        if player_wear_bag[int(xuhao)] !=None:
                            try:
                                eval('thing_room_'+str(now_id).replace(".","_")).append(player_wear_bag[xuhao])
                                print('已丢下'+player_wear_bag[xuhao])
                                del player_wear_bag[xuhao]
                            except:
                                eval('thing_room_room_'+str(now_id).replace(".","_")).append(player_wear_bag[xuhao])
                                print('已丢下'+player_wear_bag[xuhao])
                                del player_wear_bag[xuhao]
                                
                    except:
                        print('序号不合法')
                        continue 
                elif which_class =='2':
                    print('武器:'+str(player_weapon_bag).replace("'",""))
                    try:
                        
                        xuhao=int(input('输入丢下的武器序号'))
                        if player_weapon_bag[int(xuhao)] !=None:
                            try:
                                eval('thing_room_'+str(now_id).replace(".","_")).append(player_weapon_bag[xuhao])
                                print('已丢下'+player_weapon_bag[xuhao])
                                del player_weapon_bag[xuhao]
                            except:
                                eval('thing_room_room_'+str(now_id).replace(".","_")).append(player_weapon_bag[xuhao])
                                print('已丢下'+player_weapon_bag[xuhao])
                                
                                del player_weapon_bag[xuhao]

                    
                    
                    except:
                        print('序号不合法')
                        continue
                elif which_class =='3':
                    print('物品:'+str(player_things_bag).replace("'",""))
                    try:
                        
                        xuhao=int(input('输入丢下的物品序号'))
                        if player_things_bag[int(xuhao)] !=None:
                            try:
                                
                                eval('thing_room_'+str(now_id).replace(".","_")).append(player_things_bag[xuhao])
                                print('已丢下'+player_things_bag[xuhao])
                                
                                
                                del player_things_bag[xuhao]
                            except:
                                eval('thing_room_room_'+str(now_id).replace(".","_")).append(player_things_bag[xuhao])
                                print('已丢下'+player_things_bag[xuhao])
                                
                                del player_things_bag[xuhao]

                    
                    
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