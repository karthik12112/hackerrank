# Update braces if they are not in correct format either {[()]} or {}()[]
dict = {"{":"}", "[":"]", "(":")"}
def method(values):
    new_values = []
    for i in values:
        global new_list
        new_list=[]
        # print(i) #{}(][) #{[()}]
        length=len(i)
        for each in range(length):
            check(i, each)
        print("new_list {}").format(new_list) # ['back', 'back', 'front']
        new_list_front = new_list.count("front")
        new_list_back = new_list.count("back")
        if new_list_front > new_list_back:
            new_values.append(front(i, length)) #{}()[]
        else: #new_list_front > new_list_back:
            new_values.append(back(i, length)) #{[()}]
    return new_values
        

def check(i, each):
    # dict = {"{":"}", "[":"]", "(":")"}
    # i = "(}{)[]"
    #each = 0 to 6
    if i[each] in dict.keys(): # {[(
        if i[each + 1] == dict[i[each]]:
            new_list.append("front")
        # elif i[-each -1] == dict[i[each]]:
        #     new_list.append("back")
        else:
            new_list.append("back")
    else:
        pass
    # elif i[each] not in dict.keys():
    #     print("these are values {}").format(i[each])
    # else:
    #     print("something wrong")
    #     elif dict[i[each + 1]].keys() in dict and dict[i[each + 2]].keys():
    # 
    #     elif i[each + 1] != dict[i[each]] and i[each + 1] != dict[i[each]]:
    # else:
    #     pass

def front(i,length):
    print("**** front ****")
    order = []
    new_order = ""
    for each in range(length):
        if i[each] in dict.keys():
            order.append(i[each])
    if order:
        order_length = len(order)
        for numb in range(order_length):
            new_order = new_order + order[numb] + dict[order[numb]]
    return new_order


def back(i, length):
    print("**** back ****")
    order = []
    for each in range(length):
        if i[each] in dict.keys():
            order.append(i[each])
    new_order = "".join(str(x) for x in order)
    order.reverse()
    if order:
        order_length = len(order)
        for numb in order:
            new_order = new_order + dict[numb]
    return new_order

 #{[()]} #{}()[]

method(["[({)]}", "(}{)[]"])
