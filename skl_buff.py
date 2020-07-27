#buff作用函数
def xuezhou(user_name,user_sx):

    print(user_name+"感到胸口一阵炙热，好似被火烧一般疼痛，头晕目眩忽而喷出一口鲜血，似乎想要摔倒")
    user_sx["血量"]-=1.2*user_sx["防御力"]
    back_message=[user_sx["血量"]]
    return back_message
def diyuwumen(user_name,user_sx):

    print(user_name+"双目失明，一口鲜血喷出")
    user_sx["血量"]-=999*user_sx["防御力"]
    back_message=[user_sx["血量"]]
    return back_message