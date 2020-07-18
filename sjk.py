#sjk
#player_selfcheck(describe_list,player_wearing_describe,player_money,player_face,player_smz,player_max_smz,player_xb,player_describe_bag)
#游戏物品,道具，武器，装备数据库
#防具
wear_name_id={'布衣':0,'太岁甲':1,'锁甲':2,'扎甲':3,'火烈甲':4}
wear_id_name={}
for key,value in wear_name_id.items():
    wear_id_name[value]=key#配对id与名字 

wear_id_describe={0:'普普通通的一件布衣，普通百姓穿的\n防御+5',1:'上古神兵太岁甲，融合后可肉身无敌\n防御+2000',range(2,6):'描述'}
#防具属性 防具附加属性是防御力，次级属性是价值
wear_id_sx0={0:5,1:2000,2:25,3:35,4:500}
#weapon
weapon_name_id={'白铁素剑':0}
weapon_id_name={}
for key,value in weapon_name_id.items():
    weapon_id_name[value]=key#配对id与名字
weapon_id_describe={0:'普普通通的一把铁剑，江湖侠客必备\n攻击+5'}

#weapon属性 武器附加属性是攻击力,次级属性是价值
weapon_id_sx0={0:5}
#道具或物品
thing_name_id={'答题卡':0,'神香':1,'问道卷○零':2,'问道卷○壹':3}
thing_id_name={}
for key,value in thing_name_id.items():
    thing_id_name[value]=key#配对id与名字
thing_id_describe={0:'！！！祝大家生地中考及期末考试圆满成功！！！\n----------\n|   满    |\n|   分    |\n----------',1:'一支神香，可以在巫师那求取，蕴含着一些神威',2:'看到这个就是出bug了',3:'看到这个就是出bug了'}
#战斗技能
skill0_name_id={'血海无边':'xuehaiwubian','野球拳':'yeqiuquan','太极拳·阴':'taijiquan_yin',"太极拳":"taijiquan"}
skill0_id_name={}
for key,value in skill0_name_id.items():
    skill0_id_name[value]=key#配对id与名字
skill0_id_describe={'xuehaiwubian':'技能内容','yeqiuquan':'技能内容','taijiquan_yin':"技能描述","taijiquan":'马保国老师'}
#生活技能:
skill1_name_id={'厨艺':'chuyi','书法':'shufa'}
skill1_id_name={}
for key,value in skill1_name_id.items():
    skill1_id_name[value]=key#配对id与名字
skill1_id_describe={'chuyi':'技能内容','shufa':'技能内容'}





#玩家数据库
import random
#称号
describe_list=['普通百姓','人皇']
player_wearing_describe=[]#已装备称号
#****************
player_weapon_bag=[weapon_id_name[0]]#武器背包
player_wear_bag=[wear_id_name[2],wear_id_name[3]]#防具背包
player_wearing_weapon=[]#已装备的武器
player_wearing_wear=[]#
player_things_bag=[thing_id_name[0]]#物品背包
player_describe_bag=[describe_list[1]]
player_money=0
player_face=random.randint(0,100)

#玩家属性
player_sx0={'最大内力':100,'最大生命值':1500,'内力':150,'生命值':1100,'攻击力':50,'防御力':5,'闪躲力':10}
player_sx1={'根骨':0,'悟性':0,'身法':0,'臂力':0}
player_sx2={'银两':0,'黄金':0,'是否为巫师':0}
#玩家技能列表:
player_skill0=[skill0_id_name['xuehaiwubian'],skill0_id_name['taijiquan']]#战斗技能
player_skill1=[]#生活技能
player_skill0_level={'xuehaiwubian':0}
player_skill1_level={}
#玩家装备技能(只能装备战斗技能)
player_wearing_skill=[player_skill0[0]]


#玩家任务列表:
player_mission_id=[]



#以下是地图数据库:
map_id_list=list(range(0,70))
#大地图
map_name_id={'扬州城':'yzc','仙界':'xj'}

map_id_name={'yzc':'扬州城','xj':'仙界'}
for key,value in map_name_id.items():
    map_id_name[value]=key
#大地图
'''
大地图场景编辑总规则:
    扬州城(yzc)场景房间id大数字为0，任何id尽量避免0.10(等于0.1)类
    仙界(xj)id大数字为1、、、
    目前不允许添加仙界地图
'''
#场景
"""
关于添加场景的说明
0.地图-场景-房间
1.必须于map_room_yzc_id中添加，格式为"名字":在平面直角坐标系的坐标
注意:坐标不可以是0.10，0.200类似的数字
2.必须于map_zuobiao_x\y分别添加相对应的x，y坐标
3.必须于check_id添加坐标


"""
map_room_yzc_id={'魔神殿':0.1,'城东大路':0.2,'城西大路':0.3,'城北大路':0.4,'城南大路':0.5,
'醉仙楼':0.6,'巫师庙':0.7,'城北大路':0.8,'城北大路':0.9,'郊外土路':0.11,'小路':0.12}
map_room_xj_id={'南天门':1.1}
map_room_xj_name={}
#~~~~~~~~~~~~~~~~~~~~~~~~~
map_room_yzc_name={0.1:'魔神殿',0.2:'城东大路',0.3:'城西大路',0.4:'城北大路',
0.5:'城南大路',0.6:'醉仙楼',0.7:'巫师庙',0.8:'城北大路',0.9:'城北大路',0.11:'郊外土路'}
for key,value in map_room_yzc_id.items():
    map_room_yzc_name[value]=key#配对id与名字
for key,value in map_room_xj_id.items():
    map_room_xj_name[value]=key

#~~~~~~~~~~~~~~~~~~~~~~~~
map_room={'扬州城':map_room_yzc_name,'仙界':map_room_yzc_name}
map_zuobiao_x={0.1:0,0.2:1,0.3:-1,0.4:0,0.5:0,0.6:1,0.7:-1,0.8:0,0.9:0,0.11:0,1.1:400,0.12:0}
map_zuobiao_y={0.1:0,0.2:0,0.3:0,0.4:1,0.5:-1,0.6:1,0.7:1,0.8:2,0.9:3,0.11:4,1.1:400,0.12:5}
check_id={'0,0':0.1,'1,0':0.2,'-1,0':0.3,'0,1':0.4,'0,-1':0.5,
'1,1':0.6,'-1,1':0.7,'0,2':0.8,'0,3':0.9,'0,4':0.11,"3,0":0.1,'400,400':1.1,"0,5":0.12}
map_room_nr={
+0.1:'这里就是扬州城的中央广场了，十分热闹，各界人士云集于此，这里也是游戏的主城和总复活点',
+0.2:'这里就是城东大路了，由石砖紧密连接铺成的官道，看起来十分的气派和端庄',
+0.3:'这里就是城西大路了，由石砖紧密连接铺成的官道，看起来十分的气派和端庄',
+0.4:'这里就是城北大路了，由石砖紧密连接铺成的官道，看起来十分的气派和端庄',
+0.5:'这里就是城南大路了，由石砖紧密连接铺成的官道，看起来十分的气派和端庄',
+0.6:'这里是远近闻名的醉仙楼饭店，没有仙人，但是有醉人，里面人山人海，什么人都有，碗筷的声音不绝于耳，饭菜的香味从厨房传来，店小二正在里外忙碌着，看起来十分繁华',
0.7:'这里是大名鼎鼎的巫师庙，据说里面居住着拥有超能力的超级大能，许多人都在跪拜着门口的巫神像',
0.8:'一条朴实无华的石头大路，有岁月沧桑的痕迹，有几块石砖已经被踩裂',
0.9:'',
1.1:'新地图南天门上线辣'
}
#以下是地图进入时触发的事件(打印消息，战斗等)
room_shijjan={0.7:'你走进巫神庙，发现许多人正在地上跪拜着雕像'}
room_room_shijian={}


#以下是群演及特殊npc和地图掉落物品(地图上可互动的东西也算是npc)
#以下是房间里的房间-只有在某个房间里才能看到的房间
#小房间id小数位第一位和最后一位不可以是0，可以跟大地图id重复
room_1_1_name={1.11:'金光道'}
room_1_1_id={'金光道':1.11}
room_room_1_11_name_list=['金光道']#在0.6房间中的房间的名字的列表
room_room_1_11_name='醉仙楼厨房'
#&&&&&&&&&&&&&&&&
room_0_6_name={0.61:'醉仙楼厨房'}#在room0.6中的0.61房间的名字#0_61的_代表.
room_0_6_id={'醉仙楼厨房':0.61}#绑定名字与id0.61
room_room_0_6_name_list=['醉仙楼厨房']#在0.6房间中的房间的名字的列表
room_room_0_61_name='醉仙楼厨房'#小房间0.61的名字
#-------------------------------------
room_0_7_name={0.71:'巫师休息室',0.72:'巫师会客厅'}


room_0_7_id={'巫师休息室':0.71,'巫师会客厅':0.72}

room_room_0_7_name_list=['巫师休息室','巫师会客厅']#在0.6房间中的房间的名字的列表
room_room_0_71_name='巫师休息室'
room_room_0_72_name='巫师会客厅'

#============小房间的描述===============
room_room_describe={0.61:'这里是醉仙楼饭店的厨房，浓浓的菜香和烟火味充斥着整个厨房，许多伙计在灶台边忙活着，看起来十分热闹，厨娘站在水池旁监督着工作',
0.71:'这里是巫师庙的巫师休息室，看起来十分富丽堂皇，连地板砖都是由上好的上品玉石铺成。一名巫师坐在休息室的椅子上闭目歇息',
0.72:'这里是巫师会客厅，十分明亮，富丽堂皇又奢华典雅，但是巫师目前并不在此处',
1.11:'测试房间'}
######################################

#普通npc
#普通npc的战斗属性
normal_npc_sx={'最大生命值':100,'生命值':100,'攻击力':20,'防御力':10,'闪躲力':10}


#
normal_npc_list=['老王','乞丐']
normal_npc_name={normal_npc_list[0]:'laowang',normal_npc_list[1]:'qigai'}

normal_npc_id={'laowang':normal_npc_list[0],'qigai':normal_npc_list[1]}
for key,value in normal_npc_name.items():
    normal_npc_id[value]=key#配对id与名字




#普通npc描述内容
normal_npc_describe={'laowang':'他看起来贼眉鼠眼，嘴歪眼斜，身高七尺，看上去气血充盈，并没有受伤。',
'qigai':'他看起来面容枯瘦，嘴歪眼斜，浑身散发着恶臭，让人看起来就很不舒服，你心里提醒你还是离他远一些吧'}#玩家看到普通npc时的形容
#特殊npc
special_npc_list=['死神','巫师','厨娘','debug']
special_npc_name={special_npc_list[0]:'sishen',special_npc_list[1]:'wushi',special_npc_list[2]:'chuniang',special_npc_list[3]:'debug'}
special_npc_id={'sishen':special_npc_list[0],'wushi':special_npc_list[1],'chuniang':special_npc_list[2],'debug':special_npc_list[3]}
for key,value in special_npc_name.items():
    special_npc_id[value]=key#配对id与名字



special_npc_describe={'sishen':'他看起来倾国倾城，无数人为之倾倒，身披黑衣，一团黑暗的浓雾缠绕他周身。周围充斥着无形的威压，冰冷到极致，让人几乎无法呼吸',
'wushi':'他是全国鼎鼎有名的大巫神，据说武功已经达到了神境，肉身据说已经达到了金身等级，犹如一尊真神',
'chuniang':'这位是酒楼的厨娘，看起来貌美如花，手中拿着竹扇子，正在缓缓地扇动着，美眸不时朝你看来',
'debug':'debug'}#玩家看到普通npc时的形容
#以下是特殊npc的属性
special_npc_old={'sishen':'五千六百三十一','wushi':'三百','chuniang':'四十五','debug':'debug'}
special_npc_wear_describe={'死神':'「不死不灭」','巫师':'「肉身真神」','厨娘':'「富可敌国」','debug':'「加油」'}
#特殊npc战斗属性
special_npc_sishen_sx={'最大生命值':1000,'生命值':1000,'攻击力':2005,'防御力':2005,'闪躲力':10}
special_npc_wushi_sx={'最大生命值':1000,'生命值':1000,'攻击力':25,'防御力':25,'闪躲力':10}
special_npc_chuniang_sx={'最大生命值':1000,'生命值':1000,'攻击力':25,'防御力':25,'闪躲力':10}
special_npc_debug_sx={'最大生命值':10000,'生命值':10000,'攻击力':2005,'防御力':2005,'闪躲力':10}
#普通npc技能列表
normal_npc_skill=[skill0_id_name['yeqiuquan']]


#特殊npc技能列表
sishen_skill=[skill0_id_name['xuehaiwubian']]
chuniang_skill=[skill0_id_name['xuehaiwubian']]
wushi_skill=[skill0_id_name['xuehaiwubian']]




#0_1的_号是代表.
npc_room_0_6=[normal_npc_id['qigai']]
npc_room_0_2=[normal_npc_id['laowang']]
npc_room_room_0_61=[normal_npc_id['laowang']]
# special_npc_room_x_x
special_npc_room_room_0_71=[special_npc_id['wushi']]
special_npc_room_room_0_61=[special_npc_id['chuniang']]
special_npc_room_0_7=[]
special_npc_room_0_1=[special_npc_list[0],special_npc_list[3]]
#以下是地图房间上散落的东西，如果没有这个就丢不了东西
thing_room_0_11=[weapon_id_name[0]]
thing_room_0_1=[wear_id_name[0]]


#以下是房间房间上散落的东西
thing_room_room_0_61=[wear_id_name[0]]
















######################################
"""
***Coding UTF-8***
	Last code time = 202007051247
	By Robin
qq2432541891
"""