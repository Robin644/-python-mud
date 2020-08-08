#存档功能的实现
#导入json函数
def cundang():
    import json
    import sjk
    print("-"*30)
    print("存                           档")
    file_name="save_data.json"
    code=input("存档会删除以前的存档，确定要存档吗？(0/1)")
    if code=="0":
        print("取消存档~~")
    elif code=="1":


#保存内容

        nr=[sjk.player_name,sjk.player_weapon_bag,sjk.player_mission_id,sjk.player_wearing_skill,sjk.player_completed_mission_id,sjk.player_things_bag,sjk.player_describe_bag,sjk.player_face,sjk.player_skill0,sjk.player_skill1,sjk.player_skill0_level,sjk.player_skill1_level,sjk.player_wearing_skill,sjk.player_wearing_wear,sjk.player_wearing_weapon,sjk.player_wear_bag,sjk.player_sx0,sjk.player_sx1,sjk.player_sx2]
        #print("MESSAGE:"+str(nr)+"\n")
        with open(file_name,"w") as file:
            file.write("")
            print("旧存档已清除")
        with open(file_name,"a") as file_object:


            json.dump(nr,file_object)
            print("\n\n存档成功！数据已保存！！")


def dudang():
    import json
    import sjk
    print("-"*30)
    print("读                           档")
    file_name="save_data.json"
    try:
        with open(file_name) as f:
            nr=json.load(f)
            print("\n\n读档成功！数据已读取！！")

        print("\n恢复数据中。。。\n")

        #print("MESSAGE:"+str(nr))
        return nr
        #sjk.player_name, sjk.player_weapon_bag, sjk.player_mission_id, sjk.player_wearing_skill, sjk.player_completed_mission_id, sjk.player_things_bag, sjk.player_describe_bag, sjk.player_face, sjk.player_skill0, sjk.player_skill1, sjk.player_skill0_level, sjk.player_skill1_level, sjk.player_wearing_skill, sjk.player_wearing_wear, sjk.player_wearing_weapon, sjk.player_wear_bag, sjk.player_sx0, sjk.player_sx1, sjk.player_sx2=nr
    except:
        print("警告：未发现存档数据\n强制存档中。。。")
        nr = [sjk.player_name, sjk.player_weapon_bag, sjk.player_mission_id, sjk.player_wearing_skill,
              sjk.player_completed_mission_id, sjk.player_things_bag, sjk.player_describe_bag,
              sjk.player_face, sjk.player_skill0, sjk.player_skill1, sjk.player_skill0_level, sjk.player_skill1_level,
              sjk.player_wearing_skill, sjk.player_wearing_wear, sjk.player_wearing_weapon, sjk.player_wear_bag,
              sjk.player_sx0, sjk.player_sx1, sjk.player_sx2]
        #print("MESSAGE:" + str(nr) + "\n")
        with open(file_name, "w") as file:
            file.write("")
            print("旧存档已清除")
        with open(file_name, "a") as file_object:

            json.dump(nr, file_object)
            print("\n\n强制存档成功！数据已保存！！")
            dudang()



#加载内容
    #nr=[sjkplayer_name,sjk.player_weapon_bag,sjk.player_mission_id,sjk.player_wearing_skill,sjk.player_completed_mission_id,sjk.player_things_bag,sjk.player_describe_bag,sjk.player_face,sjk.player_skill0,sjk.player_skill1,sjk.player_skill0_level,sjk.player_skill1_level,sjk.player_wearing_skill,sjk.player_wearing_wear,sjk.player_wearing_weapon,sjk.player_wear_bag]







print("\n"*3)
print("-"*30)
