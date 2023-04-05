# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default usingRandBag = False

##define e = Character("Eileen")

# The game starts here.
label start:
    $player.initialize()
    $enemy.initialize()

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
                    call enemy_defending
                    "[enemy.name] is defending for [enemy.Defense] damage"
                    call camreset
                    call player_attack
                    call camreset
                    if enemy.hp == 0:
                        call enemy_death
                        return     
                else:
                    if player.initiative > enemy.initiative:
                        call player_attack
                        call camreset
                        if enemy.hp == 0:
                            call enemy_death
                            return     
                        call enemy_attack
                        call camreset
                        if player.hp == 0:
                            call player_death
                            return
                    else:
                        call enemy_attack
                        call camreset
                        if player.hp == 0:
                            call player_death
                            return
                        call player_attack   
                        call camreset
                        if enemy.hp == 0:
                            call enemy_death
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
                        call player_defending
                        "You rolled [result] and are defending for [player.Defense] damage"
                        call enemy_defending
                        "[enemy.name] is defending for [enemy.Defense] damage"
                    else:
                        call enemy_defending
                        "[enemy.name] is defending for [enemy.Defense] damage"
                        call player_defending
                        "You rolled [result] and are defending for [player.Defense] damage"
                else:
                    call player_defending
                    "You rolled [result] and are defending for [player.Defense] damage" 
                    call enemy_attack
                    call camreset  
                    if player.hp == 0:
                            call player_death
                            return  
            
            #TODO #5 Add Special Options
            "Special" if player.state != "Special":

                call Special
                


         


    # show eileen happy

    ## These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
return


label player_attack:
    camera:
        pause 0.1
        easeout_elastic 0.6 pos (432, 0) zpos -603.0 rotate 3.0 
        pause 1.2
        easein_cubic 0.6 pos(0,0) zpos 0 rotate 0


 



    show The Guy Walk:
        ease 1 pos (1075, 0)
        "The Guy Attack"
        pause 1
        ease 1 pos(0,0)
        pause 1 

    show Enemy Hurt 
    
    "You rolled [result] and did [player.damage] damage to [player.target.name]!"
return

label enemy_attack:
    $enemy.Attack("d4")
    camera:
        pause 0.1
        easeout_elastic 0.8 pos (-432, 0) zpos -603.0 rotate -3.0 
        pause 1.5
        easein_cubic 0.6 pos(0,0) zpos 0 rotate 0
    

        
    show Enemy Run:
        ease 0.75 pos (-1075, 0)
        "Enemy Attack"
        pause 1.5
        ease 1.5 pos(0,0)
        pause 1

    show The Guy Hurt
    "You got hit for [enemy.damage] damage??"
return

label enemy_death:
    camera at reset
    show Enemy Death:
        pause 3.5 alpha 0.0 

    "You win!"
return

label player_death:
    camera at reset
    show The Guy Death:
        pause 1.5 alpha 0.0 

    "Damn...."
return

label camreset:
    camera at reset
    if enemy.Defense == 0:
        show Enemy Idle:
            matrixcolor BrightnessMatrix(0.0)
            easein 0.2  pos(0,0)
    else:
        show Enemy Idle:
            matrixcolor BrightnessMatrix(0.3)
            easein 0.2  pos(0,0)


    if player.Defense == 0:
        show The Guy Idle:
            matrixcolor BrightnessMatrix(0.0)
            easein 0.2  pos(0,0)
    else:
        show The Guy Idle:
            matrixcolor BrightnessMatrix(0.3)
            easein 0.2  pos(0,0)

    

       
return

label enemy_defending:
    show Enemy Idle:
        easein 0.25 matrixcolor BrightnessMatrix(0.3)

return

label player_defending:
    show The Guy Idle:
        easein 0.25 matrixcolor BrightnessMatrix(0.3)

return

label Rolling:
    menu:
        "D4"if player.DiceisEnabled["d4"]:
            $result = player.roll("d4")
        "D6"if player.DiceisEnabled["d6"]:
            $result = player.roll("d6")
        "D8"if player.DiceisEnabled["d8"]:
            $result = player.roll("d8")
        "D10" if player.DiceisEnabled["d10"]:
            $result = player.roll("d10")
        "D12" if player.DiceisEnabled["d12"]:
            $result = player.roll("d12")
        "D20" if player.DiceisEnabled["d20"]:
            $result = player.roll("d20") 
return result

label Special:
    menu:
        "Explode"("Costs 4 MP") if player.mp > 4:
            $player.state = "Special"
            $player.Special("Explode")
        "Double Down"("Costs 8 MP") if player.mp > 8:
            $player.state = "Special"
            $player.Special("Double Down")
        "Enable Dice":
            call enable_dice
            $player.Special("Enable Dice", dicetoenable)
        "Back":
            return
        
return

label enable_dice:

    menu:
        "D4"("Costs 4 MP") if player.mp >= 4 and not player.DiceisEnabled["d4"]: 
            $dicetoenable = "d4"
        "D6"("Costs 6 MP")  if player.mp >= 6 and not player.DiceisEnabled["d6"]: 
            $dicetoenable = "d6"
        "D8"("Costs 8 MP") if player.mp >= 8 and not player.DiceisEnabled["d8"]: 
            $dicetoenable  = "d8"
        "D10"("Costs 10 MP") if player.mp >= 10 and not player.DiceisEnabled["d10"]:
            $dicetoenable = "d10"
        "D12"("Costs 12 MP") if player.mp >= 12 and not player.DiceisEnabled["d12"]:
            $dicetoenable  = "d12"
        "D20"("Costs 20 MP") if player.mp >= 20 and not player.DiceisEnabled["d20"]:
            $dicetoenable  = "d20"
return dicetoenable
