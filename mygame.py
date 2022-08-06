from random import sample



#generate 3 loc random
def genereta_all():
    
    l=sample([i for i in range(25)], k=3)
    # loc_x, loc_w, loc_d = l
    return l
                

#assign random locations to items : player , wind door and dragon
def createBoard(user):
    locs = genereta_all()
    data = {
        "user": user,
        "loc_x": locs[0],       #player
        "loc_w": locs[1],       #win door
        "loc_d": locs[2],       #dragon
        "win": False,
        "loss": False
    }
    
    
    return data



#check if player win or loss
def check_win(player, win_door, dragon):
    
    win = False
    loss= False
    
    if player==win_door:
        win = True
    
    if player==dragon:
        loss = True
    
    
    return (win, loss)



#move player
def moveX(instance, new):
    
    
    if new["move"]=="up":
        if (t:=instance.loc_x - 5) >= 0:
            new_loc = t
            
        else:
            new_loc=instance.loc_x
    
    if new["move"]=="down":
        if (t:=instance.loc_x + 5) < 25:
            new_loc = t
            
        else:
            new_loc=instance.loc_x
    
    if new["move"]=="left":
        if instance.loc_x%5!=0:
            new_loc = instance.loc_x-1
        else:
            new_loc=instance.loc_x

    
    if new["move"]=="right":
        if (instance.loc_x+1)%5!=0:
            new_loc = instance.loc_x+1
            
        else:
            new_loc=instance.loc_x
    
    win, loss = check_win(new_loc, instance.loc_w, instance.loc_d)
    
    data = {
            "id": instance.id,
            "loc_x": new_loc,
            "loc_w": instance.loc_w,
            "loc_d": instance.loc_d,
            "user": instance.user,
            "win": win,
            "loss": loss,
                }
    
    
    return data




def setup():
    
    
    
    
    pass

