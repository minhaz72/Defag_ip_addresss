def Defag_ip_address(address): 
    newadd=  " "
    split_add= address.split(" , ")
    separate='[, ]'
    newadd= separate.join(split_add)
    return newadd 
if __name__ == '__main__': 
    add= input('enter your ip address : ')
    print(Defag_ip_address(add))
    