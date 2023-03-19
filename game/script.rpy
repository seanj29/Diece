# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default usingRandBag = False

##define e = Character("Eileen")

# The game starts here.
label start:
    $player.hp = player.max_hp
    $enemy.hp = enemy.max_hp

    camera:
        perspective True
         

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg:
        pos (-207, -108) zpos 0.0
        zoom 4.41 
    show far-trees:
        pos (-207, -108) zpos 0.0 xzoom 1.0 
        zoom 4.41
        crop (0.0, 0.0, 1.0, 1.0)
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        #block:  
            
        #   linear 3.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(198.0, 0.0, 81.0)*RotateMatrix(0.0, 0.0, 0.0)
        #  linear 3.0   matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        # repeat 
        
    show mid-trees:
        pos (-207, -108) zpos 0.0 xzoom 1.0 
        zoom 4.41 
        crop (0.0, 0.0, 1.0, 1.0)
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        #linear 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(198.0, 0.0, 81.0)*RotateMatrix(0.0, 0.0, 0.0)  
    show close-trees:
        pos (-207, -108) zpos 0.0 xzoom 1.0 
        zoom 4.41 
        crop (0.0, 0.0, 1.0, 1.0) 



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    show screen hp_bars_1v1
    
 
    
    show Enemy Idle:
        subpixel True
        anchor (-1224, -54) 
        zoom 10.2 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)



    show The Guy Idle:
        subpixel True
        anchor (-225, -500) ypos 0 zpos 0.0 
        zoom 6
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
       

        
    

    while player.hp > 0 and enemy.hp > 0:

     
        
        
        menu OneVersusOne:
            "Attack":
                $player.state = "Attacking"
                $player.Target(enemy)
                $enemy.Target(player)
                $enemy.takeTurn()
                call Rolling 
                # Conditions for who's turn is first, Defenders always have priority                 
                if enemy.state == "Defending":
                    "[enemy.name] is defending for [enemy.Defense] damage"
                    call camreset
                    call player_attack
                    call camreset
                    if enemy.hp == 0:
                        "You win!"
                        return     
                else:
                    if player.initiative > enemy.initiative:
                        call player_attack
                        call camreset
                        if enemy.hp == 0:
                            "You win!"
                            return     
                        call enemy_attack
                        call camreset
                        if player.hp == 0:
                            "Damn...."
                            return
                    else:
                        call enemy_attack
                        call camreset
                        if player.hp == 0:
                            "Damn...."
                            return
                        call player_attack   
                        call camreset
                        if enemy.hp == 0:
                            "You win!"
                            return  
                        
             


            "Defend":
                # Same as above but this time Player is defending so also has prio
                $player.state = "Defending"
                $player.Target(enemy)
                $enemy.Target(player)
                $enemy.takeTurn()
                call Rolling
                if enemy.state == "Defending":
                    if player.initiative > enemy.initiative:
                        "You are defending for [player.Defense] damage"
                        "[enemy.name] is defending for [enemy.Defense] damage"
                    else:
                        "[enemy.name] is defending for [enemy.Defense] damage"
                        "You are defending for [player.Defense] damage"
                else:
                    "You are defending for [player.Defense] damage" 
                    call enemy_attack
                    call camreset  
                    if player.hp == 0:
                            "Damn...."
                            return  
         


    # show eileen happy

    ## These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
return


label player_attack:
    camera:
        perspective True

    show The Guy Walk:
        ease 1 pos (1075, 0)
        "The Guy Attack"
        pause 1
        ease 1 pos(0,0)
        pause 1  
    
    "You rolled [result] and did [player.damage] damage to [player.target.name]!"
return

label enemy_attack:
    $enemy.Attack("d4")
    camera:
        perspective True
        
    show Enemy Run:
        ease 0.75 pos (-1075, 0)
        "Enemy Attack"
        pause 1.5
        ease 1.5 pos(0,0)
        pause 1
 
    "You got hit for [enemy.damage] damage??"
return

label camreset:

    show Enemy Idle:
        easein 0.2  pos(0,0)



    show The Guy Idle:
        easein 0.2  pos(0,0)
       
return


label Rolling:
    menu:
        "D4":
            $result = player.roll("d4")
        "D6":
            $result = player.roll("d6")
        "D8":
            $result = player.roll("d8")
        "D10":
            $result = player.roll("d10")
        "D12":
            $result = player.roll("d12")
        "D20":
            $result = player.roll("d20") 
return result
    



