# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



##define e = Character("Eileen")

# The game starts here.
label start:

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
       

        
    

    while player.hp > 0:

        #Player Turn
        $randomchance = Dice()
        $rollvalue = randomchance.roll("d4")
        menu OneVersusOne:
            "Attack":
                $player.Attack("d4", enemy)
                show The Guy Walk:
                    ease 1 pos (1075, 0)
                    "The Guy Attack"
                    pause 1
                    ease 1 pos(0,0)
                pause 1
                "You did [player.damage] damage to [enemy.name]!"
                if enemy.hp == 0:
                    return
            "Defend":
                $player.Defend("d4")
                "You are defending for [player.Defense] damage"
        # Enemy Turn
        show The Guy Walk:
            easein 0.2  pos(0,0)
        if randomchance.roll("d4") < 2:
            $enemy.Defend("d4")
            "Enemy is defending for [enemy.Defense] damage"       
        else:
            $enemy.Attack("d4", player)
            show Enemy Run:
                ease 0.75 pos (-1075, 0)
                "Enemy Attack"
                pause 1.5
                ease 1.5 pos(0,0)
            "You got hit for [enemy.damage] damage??"
    "Damn...."        


    # show eileen happy

    ## These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label camera_playerattack:
    camera:
        perspective True
    return
