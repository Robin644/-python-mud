from sjk import *
from player import *
from random import *
from skl import *
from skl_buff import *
def zhandou(attack_npc_id,now_id=0.1,is_special=1):
    print('='*30)
    print('-'*14+'战斗'+'-'*14)
    level=0#回合重置
    is_zhandou=True
    if is_special==0:
        attack_npc_name=normal_npc_id[attack_npc_id]
        attack_npc_sx=normal_npc_sx
    else:
        attack_npc_name=special_npc_id[attack_npc_id] 
        attack_npc_sx=eval('special_npc_'+str(attack_npc_id)+'_sx')       
    print('你加入了战斗'+'\n敌人'+attack_npc_name+'加入了战斗')
    try:
        print('你们在「'+map_room_yzc_name[now_id]+'」开战了')
    except:
        print('你们在「房间」里战斗')
    player_alive=True
    attack_npc_alive=True
    #赋值buff
    player_attack_buff={}
    attack_npc_buff={}
    while is_zhandou:#开始战斗
        #回合开始
        ##检查敌人血量并赋值描述
        if player_attack_buff != {}:
            #print(player_attack_buff)
            try:
                for key,vaule in player_attack_buff.items():
                    print("你现在有 "+str(key)+" 的buff，时间为 "+str(vaule)+" 回合")
                    #print(player_attack_buff[key])
                    player_attack_buff[key]-=1
                   # print(player_attack_buff[key])
                    if player_attack_buff[key]+1 <= 0:
                        #print(player_attack_buff[key])
                        del player_attack_buff[key]
                    ##buff作用
                    if "血咒" in player_attack_buff:
                        sjk.player_sx0["生命值"]=xuezhou("你", sjk.player_sx0)[0]
                    if "地狱无门" in player_attack_buff:

                        sjk.player_sx0["生命值"]=diyuwumen("你", sjk.player_sx0)[0]
                        
            except:
                pass        
                    
        if attack_npc_buff != {} and attack_npc_buff != None:
            #print(attack_npc_buff)
            try:
                for key,vaule in attack_npc_buff.items():
                    print(str(attack_npc_name)+"现在有 "+str(key)+" 的buff，时间为 "+str(vaule)+" 回合")
                    attack_npc_buff[key]-=1
                    if attack_npc_buff[key] <= 0:
                        del attack_npc_buff[key]
                    
                    ##buff作用
                    if key == "血咒":
                        attack_npc_sx["生命值"]=xuezhou(attack_npc_name,attack_npc_sx)[0]
                    if key == "地狱无门":
                        attack_npc_sx["生命值"]=diyuwumen(attack_npc_name,attack_npc_sx)[0]


                   
                       
            except:


                pass

        hp_bfb = (sjk.player_sx0['生命值'] / sjk.player_sx0['最大生命值']) * 100
        if hp_bfb >= 100:
            enemie_hp_des = '你 看起来气血充裕，一点也没有受伤。'
        elif hp_bfb <= 100 and hp_bfb >= 90:
            enemie_hp_des = '你 看起来气息有些散乱，不过好像并无大碍，。'
        elif hp_bfb <= 90 and hp_bfb >= 80:
            enemie_hp_des = '你 看起来气息有些散乱，状态不是很好'
        elif hp_bfb <= 80 and hp_bfb >= 70:
            enemie_hp_des = '你 看起来呼吸极快，嘴角有许些血迹，好像受了点轻伤'
        elif hp_bfb <= 70 and hp_bfb >= 60:
            enemie_hp_des = '你  看起来气息散乱，呼吸粗重，嘴角流下了血迹，或许受了轻伤'
        elif hp_bfb <= 60 and hp_bfb >= 50:
            enemie_hp_des = '你  双目发红，手中满是鲜血，嘴角有几道血迹，连衣服上都有血迹，或许受伤不轻'
        elif hp_bfb <= 50 and hp_bfb >= 40:
            enemie_hp_des = '你 头发散乱，气息虚弱，衣襟已然被殷红的血浸湿，像是受了重伤'
        elif hp_bfb <= 40 and hp_bfb >= 20:
            enemie_hp_des = '你 披头散发，血迹遍布全身，有几块骨头似乎已经折断，仿佛随时都要昏死过去，状态十分差，似乎已受重伤'
        elif hp_bfb <= 20 and hp_bfb >= 0:
            enemie_hp_des = '你 看起来惨不忍睹，似乎已经没有了气息，差一点就已经万劫不复了'
        else:
            enemie_hp_des = '你 看起来惨不忍睹，似乎已经没有了气息，已经万劫不复了'

        print(enemie_hp_des)
        hp_bfb = (attack_npc_sx['生命值'] / attack_npc_sx['最大生命值']) * 100

        if hp_bfb >= 100:
            enemie_hp_des = attack_npc_name + ' 看起来气血充裕，一点也没有受伤。'
        elif hp_bfb <= 100 and hp_bfb >= 90:
            enemie_hp_des = attack_npc_name + ' 看起来气息有些散乱，不过好像并无大碍，。'
        elif hp_bfb <= 90 and hp_bfb >= 80:
            enemie_hp_des = attack_npc_name + ' 看起来气息有些散乱，状态不是很好'
        elif hp_bfb <= 80 and hp_bfb >= 70:
            enemie_hp_des = attack_npc_name + ' 看起来呼吸极快，嘴角有许些血迹，好像受了点轻伤'
        elif hp_bfb <= 70 and hp_bfb >= 60:
            enemie_hp_des = attack_npc_name + '  看起来气息散乱，呼吸粗重，嘴角流下了血迹，或许受了轻伤'
        elif hp_bfb <= 60 and hp_bfb >= 50:
            enemie_hp_des = attack_npc_name + '  双目发红，手中满是鲜血，嘴角有几道血迹，连衣服上都有血迹，或许受伤不轻'
        elif hp_bfb <= 50 and hp_bfb >= 40:
            enemie_hp_des = attack_npc_name + ' 头发散乱，气息虚弱，衣襟已然被殷红的血浸湿，像是受了重伤'
        elif hp_bfb <= 40 and hp_bfb >= 20:
            enemie_hp_des = attack_npc_name + ' 披头散发，血迹遍布全身，有几块骨头似乎已经折断，仿佛随时都要昏死过去，状态十分差，似乎已受重伤'
        elif hp_bfb <= 20 and hp_bfb >= 0:
            enemie_hp_des = attack_npc_name + ' 看起来惨不忍睹，似乎已经没有了气息，差一点就已经万劫不复了'
        else:
            enemie_hp_des = attack_npc_name + ' 被打得不成人样，可惜已经万劫不复了'

        print(enemie_hp_des)

        ##正式开始战斗
        print('*'*30)
        print('\n现在是第「'+str(level)+'」回合\n')
        player_code=str(input('指令:逃跑(0)，普通攻击(1)，技能(2)'))
        if player_code=='0' or player_code=='逃跑':
            jil=randint(0,1)
            if jil==0 and level >= 1:
                print('逃跑成功')
                return player
            elif jil==1 and level>= 1:
                print('逃跑失败')
            else:
                print('你「刚开始」就要逃跑?')
        elif player_code=='2' or player_code=='技能':
            print('*'*30)
            ac_0=True
            while ac_0==True:
                try:
                    print('你现在装备着技能:'+str(sjk.player_wearing_skill).replace("'",""))
                except:
                    print('你没有任何装备着的技能。')
                    ac_0=False
                else:
                    try:
                        skill_code=int(input('输入使用技能序号("输入-1退出")'))
                        if skill_code==-1:
                            break
                    except:
                        print("**请输入正确的序号")
                        continue
                    try:
                         if sjk.player_wearing_skill[skill_code] != None:
                             pass

                    except:
                        print("哪有这个技能")
                        continue 
                        
                    #print('*******哪有这个技能*********')#报错
                    
                    
                
             
                    if sjk.player_wearing_skill[skill_code] != None:
                    
                 
                        skill_id=sjk.skill0_name_id[player_wearing_skill[skill_code]]
                        back_message=eval(str(skill_id))('player',attack_npc_id,1,is_special)
                      #  back_message=[attack_enemie_sx,user_sx,(buff_name),buff_level]
                      #结算敌人血量
                        sjk.player_sx0['生命值']=back_message[1]['生命值']
                        attack_npc_sx['生命值']=back_message[0]['生命值']
                        try:
                            print("敌人获得了 "+str(back_message[2])+" Buff!")
                            attack_npc_buff[back_message[2]]=back_message[3]
                        except:
                            pass
                      #敌人出招(玩家出技能敌人也出技能)
                        if is_special==1:
                            try:
                                enemie_skill=eval(str(attack_npc_id)+'_skill')[random.randint(0,len(eval(str(attack_npc_id)+'_skill'))-1)]
                            except:
                                enemie_skill=enemie_skill=eval(str(attack_npc_id)+'_skill')[0]

                        elif is_special==0:
                            enemie_skill=normal_npc_skill[0]
                        back_message=eval(sjk.skill0_name_id[enemie_skill])(attack_npc_id,'player',0,is_special)
                        try:
                            print("你获得了 "+str(back_message[2])+" Buff!")
                            player_attack_buff[back_message[2]]=back_message[3]
                        except:
                            pass
                        attack_npc_sx['生命值']=back_message[1]['生命值']
                        sjk.player_sx0['生命值']=back_message[0]['生命值']

                      
                      
                      #---------------
                        level+=1
                        ac_0=False
                        
                    else:
                        print('哪有这个技能')
                        ac_0=False
                 
               
                
                        print('*********出错了**********')
               
                    
                    
                print('*'*30)                                             
        elif player_code=='1' or player_code=='普通攻击':
            while True:
                player_zs=randint(1,4)#随机出招
                if player_zs == 1:
                    player_zs_describe='双手宕起一团真气，向「'+attack_npc_name+'」猛的甩去'
                    shanghai=1.5*(sjk.player_sx0['攻击力']-attack_npc_sx['防御力'])
                elif player_zs == 2:
                    player_zs_describe='随手打出一拳，向「'+attack_npc_name+'」猛的锤去'
                    shanghai=1.25*(sjk.player_sx0['攻击力']-attack_npc_sx['防御力'])
                elif player_zs == 3:
                    player_zs_describe='一道鞭腿，向「'+attack_npc_name+'」猛的砍去'
                    shanghai=randint(1,2)*(sjk.player_sx0['攻击力']-attack_npc_sx['防御力'])
                elif player_zs == 4:
                    player_zs_describe='一掌向前，向「'+attack_npc_name+'」猛的拍去'
                    shanghai=sjk.player_sx0['攻击力']-attack_npc_sx['防御力']+1
            #结算
                if shanghai<0:
                    shanghai=1
                attack_npc_sx['生命值']-=shanghai
                print()
                print('***你'+player_zs_describe)
                print('***你对敌人「'+attack_npc_name+'」造成了'+str(shanghai)+'点伤害')
        #玩家普攻敌人也普攻
                player_zs=randint(1,5)#随机出招
                if player_zs == 1:
                    player_zs_describe='大骂一声，挥拳向「'+'你'+'」猛的打去'
                    shanghai=1.5*(attack_npc_sx['攻击力']-sjk.player_sx0['防御力'])
                elif player_zs == 2:
                    player_zs_describe='随手打出一掌，向「'+'你'+'」猛的拍去'
                    shanghai=1.25*(attack_npc_sx['攻击力']-sjk.player_sx0['防御力'])
                elif player_zs == 3:
                    player_zs_describe='一道鞭腿，向「'+'你'+'」猛的砍去'
                    shanghai=randint(1,2)*(attack_npc_sx['攻击力']-sjk.player_sx0['防御力'])
                elif player_zs == 4:
                    player_zs_describe='一掌向前，向「'+'你'+'」猛的拍去'
                    shanghai=attack_npc_sx['攻击力']-sjk.player_sx0['防御力']+1
                elif player_zs == 5:

                    if is_special == 1:
                        try:
                            enemie_skill = eval(str(attack_npc_id) + '_skill')[
                                random.randint(0, len(eval(str(attack_npc_id) + '_skill')) - 1)]
                        except:
                            enemie_skill=eval(str(attack_npc_id) + '_skill')[0]

                    elif is_special == 0:
                        enemie_skill = normal_npc_skill[0]
                    back_message = eval(skill0_name_id[enemie_skill])(attack_npc_id, 'player', 0, is_special)
                    try:
                        print("你获得了 " + str(back_message[2]) + " Buff!")
                        player_attack_buff[back_message[2]] = back_message[3]
                    except:
                        pass

                    attack_npc_sx['生命值'] = back_message[1]['生命值']
                    sjk.player_sx0['生命值'] = back_message[0]['生命值']
                    shanghai=0


            #结算
                if shanghai<0 and player_zs != 5:#如果伤害小于0了
                    shanghai=0
                    sjk.player_sx0['生命值']-=shanghai
                    print()
                    print('***'+attack_npc_name+player_zs_describe)
                    print('***敌人对「'+'你'+'」造成了'+str(shanghai)+'点伤害')
                    print('未突破防御！不造成伤害！！')
                elif player_zs==5:

                    pass
                elif player_zs != 5 and shanghai>= 0:
                    sjk.player_sx0['生命值'] -= shanghai
                    print('***' + attack_npc_name + player_zs_describe)
                    print('***敌人对「' + '你' + '」造成了' + str(shanghai) + '点伤害')
                level+=1
                break
                
        
        print('-'*30)
                #describe playerhp
        
        hp_bfb=(sjk.player_sx0['生命值']/sjk.player_sx0['最大生命值'])*100
        if hp_bfb >= 100:
            enemie_hp_des='你 看起来气血充裕，一点也没有受伤。'  
        elif hp_bfb <= 100 and hp_bfb>=90:
            enemie_hp_des='你 看起来气息有些散乱，不过好像并无大碍，。'  
        elif hp_bfb <= 90 and hp_bfb>=80:
            enemie_hp_des='你 看起来气息有些散乱，状态不是很好'  
        elif hp_bfb <= 80 and hp_bfb>=70:
            enemie_hp_des='你 看起来呼吸极快，嘴角有许些血迹，好像受了点轻伤'  
        elif hp_bfb <= 70 and hp_bfb>=60:
            enemie_hp_des='你  看起来气息散乱，呼吸粗重，嘴角流下了血迹，或许受了轻伤'  
        elif hp_bfb <= 60 and hp_bfb>=50:
            enemie_hp_des='你  双目发红，手中满是鲜血，嘴角有几道血迹，连衣服上都有血迹，或许受伤不轻'  
        elif hp_bfb <= 50 and hp_bfb>=40:
            enemie_hp_des='你 头发散乱，气息虚弱，衣襟已然被殷红的血浸湿，像是受了重伤'  
        elif hp_bfb <= 40 and hp_bfb>=20:
            enemie_hp_des='你 披头散发，血迹遍布全身，有几块骨头似乎已经折断，仿佛随时都要昏死过去，状态十分差，似乎已受重伤'  
        elif hp_bfb <= 20 and hp_bfb>=0:
            enemie_hp_des='你 看起来惨不忍睹，似乎已经没有了气息，差一点就已经万劫不复了'  
        else:
            enemie_hp_des='你 看起来惨不忍睹，似乎已经没有了气息，差一点就已经万劫不复了'  
       # print(sjk.player_sx0)
        print(enemie_hp_des)
       # print(hp_bfb)
        hp_bfb=(attack_npc_sx['生命值']/attack_npc_sx['最大生命值'])*100

        if hp_bfb >= 100:
            enemie_hp_des=attack_npc_name+' 看起来气血充裕，一点也没有受伤。'  
        elif hp_bfb <= 100 and hp_bfb>=90:
            enemie_hp_des=attack_npc_name+' 看起来气息有些散乱，不过好像并无大碍，。'  
        elif hp_bfb <= 90 and hp_bfb>=80:
            enemie_hp_des=attack_npc_name+' 看起来气息有些散乱，状态不是很好'  
        elif hp_bfb <= 80 and hp_bfb>=70:
            enemie_hp_des=attack_npc_name+' 看起来呼吸极快，嘴角有许些血迹，好像受了点轻伤'  
        elif hp_bfb <= 70 and hp_bfb>=60:
            enemie_hp_des=attack_npc_name+'  看起来气息散乱，呼吸粗重，嘴角流下了血迹，或许受了轻伤'  
        elif hp_bfb <= 60 and hp_bfb>=50:
            enemie_hp_des=attack_npc_name+'  双目发红，手中满是鲜血，嘴角有几道血迹，连衣服上都有血迹，或许受伤不轻'  
        elif hp_bfb <= 50 and hp_bfb>=40:
            enemie_hp_des=attack_npc_name+' 头发散乱，气息虚弱，衣襟已然被殷红的血浸湿，像是受了重伤'  
        elif hp_bfb <= 40 and hp_bfb>=20:
            enemie_hp_des=attack_npc_name+' 披头散发，血迹遍布全身，有几块骨头似乎已经折断，仿佛随时都要昏死过去，状态十分差，似乎已受重伤'  
        elif hp_bfb <= 20 and hp_bfb>=0:
            enemie_hp_des=attack_npc_name+' 看起来惨不忍睹，似乎已经没有了气息，差一点就已经万劫不复了'  
        else:
            enemie_hp_des=attack_npc_name+' 被打得不成人样，可惜已经万劫不复了'  
       # print(hp_bfb)
       # print(attack_npc_sx)
        print(enemie_hp_des)

        
        
        
        print('-'*30)
        if sjk.player_sx0['生命值']<=0:#死亡判断
            player_alive=False
        elif attack_npc_sx['生命值']<=0:
            attack_npc_alive=False
        if player_alive==False:
            print('\n\n')
            print('战 斗 失 败 (๑‾᷅^‾᷅๑) ')
            print('胜败乃兵家常事  还请大侠重新来过')
            print('你已经被'+attack_npc_name+'打败了')
            print("\n\n"+"-"*20)
            back_message=['失败',sjk.player_sx0['生命值']]
            return back_message
        elif attack_npc_alive==False:
            print('')  
            print(enemie_hp_des)
            print('\n\n')
            print('战 斗 胜 利 ^_^Y')
            print('')
            print("\n\n" + "-" * 20)
            print('你已经战胜了'+attack_npc_name)
            back_message=['胜利',sjk.player_sx0['生命值']]
            return back_message
        print('*'*30)
#zhandou('dongfang_youlong', now_id=0.1, is_special=1)
        

#zhandou('chuniang',0.1,1)
