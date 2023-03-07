image Enemy Idle:
    block:
        "[EnemyIdle.image_dir] [EnemyIdle.frames].png"
        pause 0.15
        function  EnemyIdle.Animate
        repeat

image The Guy Idle:
    block:
        "[TheGuyIdle.image_dir] [TheGuyIdle.frames].png"
        pause 0.25
        function  TheGuyIdle.Animate
        repeat

image Enemy Run:
    block:
        "[EnemyRun.image_dir] [EnemyRun.frames].png"
        pause 0.15
        function  EnemyRun.Animate
        repeat

image Enemy Attack:
    block:
        "[EnemyAttack.image_dir] [EnemyAttack.frames].png"
        pause 0.15
        function  EnemyAttack.Animate
        repeat EnemyAttack.framesmax    
    "Enemy Idle"

image The Guy Attack:
    block:
        "[TheGuyAttack.image_dir] [TheGuyAttack.frames].png"
        pause 0.12
        function  TheGuyAttack.Animate
        repeat TheGuyAttack.framesmax
    "The Guy Idle"

image The Guy Walk:
    block:
        "[TheGuyWalk.image_dir] [TheGuyWalk.frames].png"
        pause 0.15
        function  TheGuyWalk.Animate
        repeat
       