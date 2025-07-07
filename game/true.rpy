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
    call WHEREUAT
label GROUPLUNCH:
    window show
    scene cafeteria
    with dissolve
    h "We pick up our trays and make our way into the cafeteria."
    h "I spy Gerald and Phoebe eating together so Arnold and I go over to join them."
    hslow "Hey Pheebs, Geraldo..."
    show gerald unsure 
    with dissolve
    gslow "Helga..."
    gslow "And Arnold together?"
    show gerald wtf
    with dissolve
    gslow "Now I've seen everything!"
    show gerald wtf at left
    with dissolve
    show arnold pissed at right
    with dissolve
    aslow "What's the big deal?"
    aslow "We just came over from the lunch line is all..."
    h "I think my heart might have sunk a bit with that."
    hide gerald wtf
    with dissolve
    show phoebe smile at left
    with dissolve
    pslow "Well, no matter..."
    pslow "We're all friends here, aren't we?"
    hide arnold pissed
    with dissolve 
    hide phoebe smile
    with dissolve
    h "The collected mumbles from the three of us was actually kind of funny."
    show gerald happy
    with dissolve
    gslow "Anyway Pheebs, what time should I pick you up on Saturday?"
    h "I tried not to look at Arnold as Gerald brought up the Festival in front of us..."
    h "Instead I stirred my pudding, hoping this subject wouldn't last very long."
    show gerald happy at left
    with dissolve
    show phoebe smile at right
    with dissolve
    pslow "Oh, 6:30ish should be fine...I'm really looking forward to it."
    h "Phoebe turns to me, and her smile slightly falls."
    hide gerald happy
    with dissolve
    show phoebe sad at center with dissolve
    pslow "I still think you should go Helga."
    hide phoebe sad 
    with dissolve
    show arnold surprise
    with dissolve
    aslow "Huh?"
    aslow "You're not going this year?"
    h "Oh yeah, he wasn't there to hear me say that."
    hslow "Uh, yeah I was thinking about skipping it."
    h "And I just kept stirring away..."
    hide arnold surprise
    with dissolve
    show phoebe question
    with dissolve
    pslow "Honestly..."
    show phoebe grin
    with dissolve
    pslow "We could all have a nice time together."
    pslow "Maybe as a group?"
    hslow "I dunno I just..."
    show phoebe grin at right
    with dissolve
    show arnold yeah at left
    with dissolve
    aslow "That wouldn't be so bad..."
    hslow "Huh?"
    show arnold simple
    with dissolve
    aslow "Going as a big group I mean..."
    aslow "Might be fun."
    hslow "Heh-heh..."
    h "That isn't anywhere near where I wanted him to be."
    h "A group? Like a bunch of people?"
    h "No, I wanted him to myself."
    h "But it's not like I can just come out and say that."
    hide arnold simple with dissolve
    show gerald happy at left with dissolve
    gslow "Well as long as me and Phoebe can get {i}some{/i} one on one time, it's fine with me."
    pslow "So Helga, what do you say?"
    hslow "I uh..."
    hide phoebe grin
    with dissolve
    hide gerald happy
    with dissolve
    h "I couldn't just say no."
    h "I didn't want him to think I was completely not interested."
    menu:
        h "What to do?"
        "Okay...I'll go.":
            jump Agree
        "Maybe?":
            jump Possibly

label Agree:
    window show
    $ IMGOING = True
    hslow "Uh, yeah sure...sounds like a plan."
    jump BACKTOSCHOOL
label Possibly:
    window show
    $ Maybe = True    
    hslow "I'll think about it, I promise."
    jump BACKTOSCHOOL
label BACKTOSCHOOL:
    window show
    if Maybe:
        show phoebe question with dissolve
        pslow "Well, I suppose that's better than a no."
        hslow "Trust me, you're lucky I'm considering it."
        h "Oh my god, what was the matter with me?"
        hide phoebe question with dissolve
        show arnold yeah with dissolve
        aslow "Hmm...well I'll go if you go."
        hslow "What?"
        h "It didn't make a difference, the bell rang for the next class and off he went."
        show arnold surprise with dissolve
        aslow "Sorry, I gotta go...my class is upstairs, I'll see ya guys later!"
        hide arnold surprise with dissolve
    else: 
        show phoebe grin
        with dissolve
        pslow "That's great Helga, I'm so glad you changed your mind."
        hide phoebe grin
        with dissolve
        show arnold yeah
        with dissolve
        aslow "Yeah me too..."
        hslow "Really Arnold...?"
        hslow "Uh, I mean...well yeah, you know it doesn't sound like a complete waste of time this way."
        hslow "And I've got nothing better to do this Saturday."
        show arnold turn unsure at left
        with dissolve
        aslow "Right...."
        show gerald wtf at right
        with dissolve
        gslow "Yeah..."
        hide arnold turn unsure with dissolve
        hide gerald wtf with dissolve
        show phoebe question with dissolve
        pslow "Helga?"
        h "Phoebe whispers to me, trying to be private."
        hslow "Yeah?"
        pslow "You're rambling..."
        hslow "Oh...thanks Pheebs."
        hide phoebe question with dissolve
        h "I turn away from the table, trying to hide my red cheeks."
        show arnold yeah at center
        with dissolve 
        aslow "..."
        aslow "Well...I guess since Helga's going now I might go too..."
        hslow "What?"
        h "It didn't make a difference, the bell rang for the next class and off he went."
        show arnold surprise with dissolve
        aslow "Sorry, I gotta go...my class is upstairs, I'll see ya guys later!"
        hide arnold surprise with dissolve
        jump quickchat
label quickchat:
    window show
    hslow "Wait!"
    hslow "That's not something you just leave hanging, Hair Boy!"
    show gerald wtf at left with dissolve
    show phoebe question at right with dissolve
    gslow "..."
    pslow "..."
    hslow "..."
    gslow "Helga...are you okay?"
    pslow "She's perfectly fine."
    hslow "Yeah, I'm freaking fantastic."
    gslow "Right...well I'm off."
    hide gerald wtf
    with dissolve
    hide phoebe question with dissolve
    h "I look away as he gives Phoebe a peck on her cheek."
    hslow "Ugh..."
    show phoebe sad at center with dissolve
    pslow "Helga?"
    h "I slam my head down on the table..."
    hslow "I waaaaaaaaant that."
    show phoebe unsure with dissolve
    pslow "Oh dear...."
    hslow "With that stupidly perfect Football Head!"
    h "By now most of the cafeteria was empty"
    pslow "I know Helga, I know."
    hslow "Ugh..."
    h "I groan again, feeling utterly defeated."
    hslow "There is no way this is going to end well..."
    show phoebe question
    with dissolve
    pslow "Huh?"
    hslow "Oh, it's nothing."
    pslow "...All right Helga. Well let's go, we're going to be late."
    hslow "Whatever."
    pslow "Oh Helga..."
    hide phoebe question
    $ True_4 = True
    jump afterschool

label Nope:
    window show
    hslow "Well duh, Football Head...where else would I be?"    
    show arnold grin
    with dissolve
    aslow "Haha, yeah okay Helga..."
    aslow "I'll see ya..."
    hide arnold grin with dissolve
    h "I watched him go and tried not to breath out a heavy sigh..."
    hslow "~~~sigh~~~"
    h "I guess I would have to try harder tomorrow..."                                   
    
label Saved:
    window show
    hslow "Maybe you will, maybe you won't..."    
    show arnold sneaky 
    with dissolve
    aslow "What you're just not gonna show up tomorrow?"
    hslow "Would you be worried?"
    show arnold  yeah with dissolve
    aslow "Maybe I will, maybe I won't."
    hslow "Oh, using my own words against me, huh?"
    aslow "I learn from the best."               
    hslow "Obviously."
    show arnold grin 
    with dissolve
    aslow "Haha, okay, okay, enough...I'll see you tomorrow."
    hslow "If you say so..."
    hide arnold grin with dissolve
    h "I watched him go and my heart swelled just a bit..."
    h "Maybe I can do this after all..."
    $ Good = True
    