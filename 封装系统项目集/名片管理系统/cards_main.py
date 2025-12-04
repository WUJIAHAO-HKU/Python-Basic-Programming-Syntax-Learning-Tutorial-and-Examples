import cards_tools
#无限循环：由用户决定什么时候退出循环
while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()
    # 使用 in 针对 列表 判断，避免使用 or 拼接复杂的逻辑条件
    # 没有使用 int 转换用户输入，可以避免 一旦用户输入的不是数字，导致程序运行出错
    action_str = input("请选择希望执行的操作")
    print("你选择的操作是[%s]"%action_str)
    # 针对名片的操作
    if action_str in ["1","2","3"]:
        #新增名片
        if action_str == "1":
            cards_tools.new_card()
        #显示全部
        elif action_str == "2":
            cards_tools.show_all()
        #查询名片
        elif action_str == "3":
            cards_tools.search_card()
        pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("你输入的不正确")
