def print_queue(c_buff, front, back):
    #print(c_buff, front, back)
    return_q = []
    if back < front:
        for n in c_buff[front:]:
            return_q.append(n)
        for n in c_buff[:back]:
            return_q.append(n)
            
    elif back > front:
        
        for n in c_buff[front:back]:
           return_q.append(n)

    return return_q