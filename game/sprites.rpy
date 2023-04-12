image Enemy Idle:
    block:
        "[EnemyIdle.image_dir] [EnemyIdle.frames].png"
        pause 0.15
        function  EnemyIdle.Animate
        repeat


image Enemy Run:
    block:
        "[EnemyRun.image_dir] [EnemyRun.frames].png"
        pause 0.15
        function  EnemyRun.Animate
        repeat

image Enemy Hurt:
    "Enemy Idle"
    pause 1.1
    block:
        "[EnemyHurt.image_dir] [EnemyHurt.frames].png"
        pause 0.15
        function  EnemyHurt.Animate
        repeat EnemyHurt.framesmax
    "Enemy Idle"

image Enemy Attack:
    block:
        "[EnemyAttack.image_dir] [EnemyAttack.frames].png"
        pause 0.15
        function  EnemyAttack.Animate
        repeat EnemyAttack.framesmax
    "Enemy Idle"

image Enemy Death:
    block:
        "[EnemyDeath.image_dir] [EnemyDeath.frames].png"
        pause 0.15
        function  EnemyDeath.Animate
        repeat EnemyDeath.framesmax 


image The Guy Walk:
    block:
        "[TheGuyWalk.image_dir] [TheGuyWalk.frames].png"
        pause 0.15
        function  TheGuyWalk.Animate
        repeat

       
image The Guy Idle:
    block:
        "[TheGuyIdle.image_dir] [TheGuyIdle.frames].png"
        pause 0.25
        function  TheGuyIdle.Animate
        repeat
        
image The Guy Attack:
    block:
        "[TheGuyAttack.image_dir] [TheGuyAttack.frames].png"
        pause 0.12
        function  TheGuyAttack.Animate
        repeat TheGuyAttack.framesmax
    "The Guy Idle"

image The Guy Hurt:
    "The Guy Idle"
    pause 2
    block:
        "[TheGuyHurt.image_dir] [TheGuyHurt.frames].png"
        pause 0.15
        function  TheGuyHurt.Animate
        repeat TheGuyHurt.framesmax
    "The Guy Idle"

image The Guy Death:
    block:
        "[TheGuyDeath.image_dir] [TheGuyDeath.frames].png"
        pause 0.15
        function  TheGuyDeath.Animate
        repeat TheGuyDeath.framesmax 
image GodLight = "God/BrightWhite.png"