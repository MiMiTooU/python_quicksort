def q_sort(int_list):
    left=[]
    right=[]
    for i in range(1,len(int_list)):
        if int_list[i]>=int_list[0]:
           right.append(int_list[i])
        else:
           left.append(int_list[i])
    if len(left)==0:
        left.append(int_list[0])
        if len(right)>1:
            right=sort_a(right)
    elif len(right)==0 and len(left)==1:
        right.append(int_list[0])
        if len(left)>1:
            left=sort_a(left)
    elif len(left)==1 and len(right)==1:
        left.append(int_list[0])
    elif len(left)==1 and len(right)!=1:
        right=sort_a(right)
        left.append(int_list[0])
    elif len(left)!=1 and len (right)==1:
        left=sort_a(left)
        left.append(int_list[0])
    else:
        left=sort_a(left)
        right=sort_a(right)
        left.append(int_list[0])
    return left+right