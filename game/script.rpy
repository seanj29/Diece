# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default usingRandBag = False

define g = Character("???")

# The game starts here.
label start:
    scene black
    play music "sounds/Alone in the Chamber.ogg"
    "....."
    "......."
    show GodLight at center with dissolve
    show GodLight:
        animation
        anchor (-170, -190)
        block:
            easein 2 pos (0, 0)
            easein 2 pos (0, -100)
            repeat
        


    "*Crash*"
    g "Who's there?"
    g "Ah. it's just you"
    g "Well, are you not going to play?" 

    menu begin:
        "Go Play"("Start the Game"):
            play sound "sounds/ConfirmBtnMain.ogg"
            call fight from _call_fight
        "Ask more questions"("Help and Basic Controls"):
            "Use arrow keys or mouse movement to pick menu options"
            "If you roll the highest amount on a dice, that dice then Explodes, and causes the next dice up in value to be rolled"
            "If one player Defends, they will always move first."
            call begin 
        "No thank you"("Quits the game"):
            g "I'm saddened....."
            return
return


label fight:
    $player.initialize()
    $enemy.initialize()
    play music "sounds/Dark Dragon.ogg"

    camera:
        perspective True
         


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
    
    with dissolve


    
    show screen hp_bars_1v1 
    
     

    show The Guy Idle:
        subpixel True 
        anchor (-225, -500) ypos 0 zpos 0.0 
        zoom 6
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show Enemy Idle:
        subpixel True
        anchor (-1224, -54) 
        zoom 10.2 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)

    with pixellate

       

    if player.initiative >= enemy.initiative:
        "You have a higher initiative, so your moves have priority!" 
    else:
        "[enemy.name] has a higher initiative, so their moves have priority!"  

        

    

    while player.hp > 0 and enemy.hp > 0:
     
        
        
        menu OneVersusOne:
            "Attack":
                $player.state = "Attacking"
                $player.Target(enemy)
                $enemy.Target(player)
                $enemy.takeTurn()
                call Rolling from _call_Rolling 
                # Conditions for who's turn is first, Defenders always have priority                 
                if enemy.state == "Defending":
                    call enemy_defending from _call_enemy_defending
                    call camreset from _call_camreset
                    call player_attack(result) from _call_player_attack
                    call camreset from _call_camreset_1
                    if enemy.hp == 0:
                        call enemy_death from _call_enemy_death
                        return     
                else:
                    if player.initiative >= enemy.initiative:
                        call player_attack(result) from _call_player_attack_1
                        call camreset from _call_camreset_2
                        if enemy.hp == 0:
                            call enemy_death from _call_enemy_death_1
                            return     
                        call enemy_attack from _call_enemy_attack
                        call camreset from _call_camreset_3
                        if player.hp == 0:
                            call player_death from _call_player_death
                            return
                    else:
                        call enemy_attack from _call_enemy_attack_1
                        call camreset from _call_camreset_4
                        if player.hp == 0:
                            call player_death from _call_player_death_1
                            return
                        call player_attack(result) from _call_player_attack_2   
                        call camreset from _call_camreset_5
                        if enemy.hp == 0:
                            call enemy_death from _call_enemy_death_2
                            return  
                        
             


            "Defend":
                # Same as above but this time Player is defending so also has prio
                $player.state = "Defending"
                $player.Target(enemy)
                $enemy.Target(player)
                $enemy.takeTurn()
                call Rolling from _call_Rolling_1
                if enemy.state == "Defending":
                    if player.initiative >= enemy.initiative:
                        call player_defending(result) from _call_player_defending
                        call enemy_defending from _call_enemy_defending_1
                    else:
                        call enemy_defending from _call_enemy_defending_2
                        call player_defending(result) from _call_player_defending_1
                else:
                    call player_defending(result) from _call_player_defending_2
                    call enemy_attack from _call_enemy_attack_2
                    call camreset from _call_camreset_6  
                    if player.hp == 0:
                            call player_death from _call_player_death_2
                            return  
            
            "Special" if player.state != "Special":

                call Special from _call_Special
                


         


    # This ends the game.
return


label player_attack(DiceToRoll):
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
    $No = player.Attack(DiceToRoll)
    "You rolled a [No] and did [player.damage] damage to [player.target.name]!"
return

label enemy_attack:
    $enemy.Attack("d10")
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
    camera:
        easein_cubic 0.1 pos(0,0) zpos 0 rotate 0
    show Enemy Death:
        pause 3.5 alpha 0.0 

    "You win!"
return

label player_death:
    camera:
        easein_cubic 0.1 pos(0,0) zpos 0 rotate 0
    show The Guy Death:
        pause 1.5 alpha 0.0 

    "Damn...."
return

label camreset:
    camera:
        easein_cubic 0.1 pos(0,0) zpos 0 rotate 0
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
    "[enemy.name] is defending for [enemy.Defense] damage"


return

label player_defending(DiceToRoll):
    show The Guy Idle:
        easein 0.25 matrixcolor BrightnessMatrix(0.3)
    $No = player.Defend(DiceToRoll)    
    "You rolled a [No] and are defending for [player.Defense] damage" 

return

label Rolling:
    menu:
        "D4"if player.DiceisEnabled["d4"]:
            $result = "d4"
        "D6"if player.DiceisEnabled["d6"]:
            $result = "d6"
        "D8"if player.DiceisEnabled["d8"]:
            $result = "d8"
        "D10" if player.DiceisEnabled["d10"]:
            $result = "d10"
        "D12" if player.DiceisEnabled["d12"]:
            $result = "d12"
        "D20" if player.DiceisEnabled["d20"]:
            $result = "d20" 
return result

label Special:
    menu:
        "Explode"(f"Costs {player.SpecialMPCosts['Explode']} MP") if player.mp >= player.SpecialMPCosts["Explode"]:
            $player.state = "Special"
            $player.Special("Explode")
        "Double Down"(f"Costs {player.SpecialMPCosts['Double Down']} MP") if player.mp >= player.SpecialMPCosts["Double Down"]:
            $player.state = "Special"
            $player.Special("Double Down")
        "Enable Dice":
            call enable_dice from _call_enable_dice
            $player.Special("Enable Dice", dicetoenable)
        "Back":
            return
        
return

label enable_dice:

    menu:
        "D4"(f"Costs {player.EnableCost['d4']} MP") if player.mp >= player.EnableCost["d4"] and not player.DiceisEnabled["d4"]: 
            $dicetoenable = "d4"
        "D6"(f"Costs {player.EnableCost['d6']} MP")  if player.mp >= player.EnableCost["d6"] and not player.DiceisEnabled["d6"]: 
            $dicetoenable = "d6"
        "D8"(f"Costs {player.EnableCost['d8']} MP") if player.mp >= player.EnableCost["d8"] and not player.DiceisEnabled["d8"]: 
            $dicetoenable  = "d8"
        "D10"(f"Costs {player.EnableCost['d10']} MP") if player.mp >= player.EnableCost["d10"] and not player.DiceisEnabled["d10"]:
            $dicetoenable = "d10"
        "D12"(f"Costs {player.EnableCost['d12']} MP") if player.mp >= player.EnableCost["d12"] and not player.DiceisEnabled["d12"]:
            $dicetoenable  = "d12"
        "D20"(f"Costs {player.EnableCost['d20']} MP") if player.mp >= player.EnableCost["d20"] and not player.DiceisEnabled["d20"]:
            $dicetoenable  = "d20"
return dicetoenable
