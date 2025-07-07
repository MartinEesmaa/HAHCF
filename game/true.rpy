label IFTHEN:
    $ GeraldSpills = False
    $ Festival = False
    $ Class = False
    $ Sorry = False
    $ Good = False
    $ PerfectDay = False
    $ Perfect_1 = False
    $ Perfect_2 = False
    $ Perfect_4 = False
    $ Perfect_5 = False
    $ True_1 = False
    $ True_2 = False
    $ True_3 = False
    $ IMGOING = False
    $ Maybe = False
    $ True_4 = False
    $ persistent.true = False
    $ persistent.ending_1 = False
    $ persistent.ending_2 = False
    $ soup = False
    $ skipped = False
    $ poem = False
    $ fight = False
    $ funny = False                   
    $ Waited = False                         
    $ imwrong = False
label OuchWrong:
    $ True_1 = True
    window show
    $ renpy.block_rollback()
    play music "Jim Lang - Back To School.mp3"
    scene bg city day with dissolve
    hslow "Whatever, I'm fine."
    h "I mumble as I try to dust the dirt off my jeans."
    show arnold sad smile
    with dissolve
    aslow "Oh, okay...are you feeling alright Helga?"
    aslow "You seem a little off..."
    hslow "Really, Football Head, do you listen?"
    hslow "I just said everything's fine, so get off my case, okay?!"
    show arnold frown
    with dissolve
    aslow "Uh, yeah sure Helga...sorry again. I'll see you when I see you I guess..."
    hide arnold frown
    with dissolve
    h "I watch as Arnold runs off ahead, the reason, of course, being me..."
    h "But it can't be helped! I can't control my wacky emotions when it comes to him...if only..."
    show phoebe smile
    with dissolve
    pslow "Anyway, it's on Saturday...can you believe it?"
    hslow "Huh? What is?"
    pslow "The Cheese Festival!"
    hslow "Are we still talking about this?" 
    show phoebe sad
    with dissolve
    pslow "Sorry Helga..."
    hslow "Ugh...whatever..."
    hslow "It's fine, I get that you're pumped..."
    hslow "But since I'm not going, remember to buy me some cheese sticks, will ya?"
    show phoebe grin
    with dissolve
    pslow "Remembering!"
    hslow "Great."
    call Ditching
    
label OuchWrong2:
    $ True_2 = True
    window show
    $ renpy.block_rollback()   
    play music "04 groove remote (abner).mp3"
    hslow "Yeah, I guess you're right...It's just so draining sitting in those classes..."
    show phoebe question
    with dissolve
    pslow "Do you feel your creative juices leaving you Helga?"
    hslow "That's one way of putting it Pheebs..."
    hslow "But no matter, I'm right behind you." 
    hide phoebe question
    with dissolve
    scene classroom
    with fade
    h "..."                                 
    h "......."
    h "The class is just as bad as I figured it would be..."
    h "This is soul sucking boredom I am dealing with."
    h "I can't help it if all my brain can do is wander and wonder..."
    h "To Arnold, my love, my muse~" 
    h "He has no idea how I regularly stare lovingly at his weird little football head..."
    if Perfect_1: 
        h "And yet..."
        h "The walk to school this morning with him was actually kind of okay.."
        h "And it wasn't even that hard, joking with him..."
        h "In a nice way, I mean."
        h "I wouldn't mind spending more mornings like this one."
        h "Mornings, noons, nights..."
        h "Even after all this time I was still crazy about him."
        h "..."
        scene sky
        with dissolve
        h "I try to look away from him and stare out the window..."
    if True_1:
        h "And yet..."
        h "I was my usual cranky self with him this morning..."
        h "And scared him off him like I always do."
        h "Could I...actually change myself though?"
        h "I mean if I really tried to be his friend...maybe more than his friend..."
        h "Was that even possible?"
        scene sky
        with dissolve
        h "I found myself looking out the window..."
    h "And then I remembered the Cheese Festival."
    h "Maybe...if I acted kinder towards Arnold...he might..."
    h "Ask me to go with him?"
    h "Hell it was worth a shot!"
    h "Anything was better than going on like this..."
    h "Arnold and I...barely even anything..."    
    stop music fadeout 2.0
    h "I had to try!"
    call FIRSTDAY
label OuchWrong3:
    window show
    play music "Jim Lang - Groove Remote (LockJaw).mp3"
    scene cafeteria doors
    with dissolve
    $ True_3 = True
    h "I queitly wait beside him, waiting for him to say something to me."
    h "The line slowly moves little by little and the waiting feels like an eternity..."
    h "Though more likely it was probably only a few minutes."
    show arnold bored                
    with dissolve
    aslow "Helga, can you pass me the tapioca?" 
    hslow "Huh? What?"
    h "Great , he finally talks and I'm not even paying attention."
    show arnold simple
    with dissolve
    aslow "Nothing serious, just wondering if you could pass the pudding?"
    h "I nod my head slowly and hand him over a cup."