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
    call DayTwo                                    
    
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
    call DayTwo
    
label OuchWrong5:
    window show
    stop music fadeout 3.0
    h "Yeah, going to school seems like the best choice."
    h "It's not like sleeping in is going to get me any closer to Arnold."  
    h "And I can kick my butt into gear if I think about him."
    scene start
    with dissolve
    h "..."
    h "......."
    play music "04 groove remote (abner).mp3" 
    h "It turned out I was running late, even Phoebe had gone on ahead of me."
    scene classroom
    with dissolve
    h "When I slid into my desk for my first class, I watched the door, waiting for Arnold."
    h "I was going to put my all into it today but..."
    h "He never freaking showed up!"
    scene start 
    with dissolve
    h "..."
    h "......."
    scene cafeteria
    with dissolve
    h "When lunch finally came I sat  down, feeling pretty defeated."
    h "I really was nuts...missing him like this...ugh."
    h "I'm pathetic..."
    show phoebe sad with dissolve
    pslow "Helga...you aren't eating today?"
    hslow "No money..."
    show phoebe sad at right with dissolve
    show gerald unsure at left with dissolve
    gslow "Uh, I think I can spot you..."
    hslow "No, it's fine...but, uh...you could answer a question."           
    hide phoebe sad with dissolve
    show gerald wtf at center with dissolve                                                          
    gslow "...Okay?"
    hslow "Where's the Football Head today, I uh...I didn't see him."      
    show gerald calm with dissolve
    gslow "I dunno, I texted him this morning, he said he had a cold."
    hslow "A cold?"                
    gslow "Yeah, it means he's sick."
    hslow "I know what it means...!"      
    show gerald wtf with dissolve 
    gslow "Okay, okay I was just kidding, no need to snap."
    hslow "Ugh...sorry, sorry."
    pslow "..."                 
    show gerald calm with dissolve
    gslow "Seriously?"                                       
    hslow "Seriously what?"
    gslow "You're apologizing?"
    hslow "What? I've done it before..."    
    show gerald wtf at left with dissolve
    show phoebe question at right with dissolve
    pslow "She has..."
    gslow "A guy can't make a joke anymore, huh?"
    hslow "Ugh, never mind..."
    scene start
    with dissolve
    h "..."
    h "......."
    h "The rest of the school day seemed kind of a blur..."
    h "Teachers talk about things I don't care about...students rambling amongst themselves."
    h "And of course I thought about Arnold...this whole day felt like such a waste because he hasn't here..."
    scene school
    with dissolve 
    h "That afternoon I left the school grounds alone, needing to think."
    hslow "Arnold, my love..."
    h "I said aloud after making sure the coast was clear..."
    hslow "How I miss your peaceful face when you're astray..."
    hslow "How you calm and force my heart to beat away..."
    hslow "Oh damn, I am on fire..."
    h "I pull out my pink book and write that line down before I forgot it..."
    hslow "How....I...miss..."
    hslow "..."
    hslow "....."
    play sound "Right Cross-SoundBible.com-1721311663.wav"
    scene CG39
    with dissolve
    hslow "Some things never change..."
    h "After I finished up my...business..."
    scene start
    with dissolve
    h "I quickly regained my composure."
    h "And made my way home..."
    scene bg city day
    with dissolve
    h "..."
    h "......"
    hslow "I don't like not seeing him, despite the inspiration boost..."
    hslow "...Ah?"
    hslow "What is this?"
    h "I had walked past some neighborhood deli with a two soup specials today..."
    h "And an idea suddenly struck..."
    hslow "Gerald did say he was sick today, didn't he?"
    h "This could be part of the new, nicer me..."
    h "Well, a step in the right direction at least."
    h "I rush right in a grabbed both...cause I didn't know which he'd like better..."
    h "And ran right over to the boarding house."
    scene bg arnold house
    with dissolve
    h "..."
    h "......."
    hslow "Okay Helga, just be honest...just-be-nice!"
    play sound "Helga Knocking.wav"
    h "With everything I had I started knocking on the door."
    h "It wouldn't be too bad since he probably wouldn't answer anyway..."
    aslow "Coming!"
    h "Wait...what?"
    h "And he opened the door suddenly, leaving me no time to prepare!"
    show arnold surprise with dissolve
    aslow "Helga?! What are you doing here?"
    hslow "I...uh...well...you...uh...."
    show arnold sad smile with dissolve
    aslow "...Huh?"
    hslow "Aren't you supposed to be sick or something?!?!"
    h "A part of me felt like pushing the hot soup into his hands and running far, far away."
    show arnold turn okay with dissolve
    aslow "Sick?"
    aslow "..."
    show arnold grin with dissolve
    aslow "Oh! Heh, yeah I did tell Gerald that this morning didn't I?"
    hslow "Yes....yes you did."
    show arnold simple with dissolve
    aslow "So...did you bring me something?"
    h "He motioned towards the paper bag in my hands."
    hslow "...Um...yeah?"
    hslow "But it's kind of shot to hell now that..."
    show arnold turn simple with dissolve
    h "He didn't let me finish and grabbed the bag and peered inside."
    aslow "Soup?"
    show arnold yeah with dissolve
    h "He grinned at me like...like..."
    h "Oh! I don't even know what!"
    aslow "You brought me soup?"
    hslow "Shut up! I was trying to be nice! It's your fault for not actually being sick!"
    show arnold calm with dissolve
    aslow "I'm not accusing you of anything..."
    h "He let that trail off as if he knew it was coming."
    show arnold sad smile with dissolve
    aslow "But why two?"
    hslow "*mumble* *mumble* didn't know *mumble mumble*"
    show arnold turn unsure with dissolve
    aslow "...What did you just say?"
    hslow "Ugh! I said I didn't know which one you liked so I got both!"
    show arnold surprise with dissolve
    aslow "Oh!"
    aslow "..."
    show arnold turn unsure with dissolve
    aslow "This is kinda weird..."
    hslow "You're telling me..."
    show arnold calm with dissolve
    aslow "But not in a bad way..."
    hslow "Not...in a...?"
    show arnold grin with dissolve
    aslow "You want one?"
    hslow "Huh?"
    show arnold simple with dissolve
    aslow "Well there are two so, one for me and one for you?"
    hslow "I uh...I guess but isn't there just one spoon?"
    show arnold yeah with dissolve
    aslow "Not a problem."
    h "He reached inside the bag and pulled out the white plastic utensil..."
    scene CG41
    with dissolve
    h "And with a flick it suddenly became two."
    hslow "Heh, very nice."
    h" I gave him a deliberately slow clap."
    aslow "I am a magician, after all..."
    aslow "I made you disappear once..."
    hslow "Hah! Very funny...gimme that!"
    scene bg arnold house
    with dissolve
    show arnold simple with dissolve
    h "I reached for one of the spoons and the tips of my fingers brushed against his..."
    h "It was like a shot of electricity went through my entire arm."
    h "And I slowly pulled away, feeling the heat rise to my cheeks."
    show arnold turn simple with dissolve
    aslow "So which one do want?"
    h "It was like he didn't even notice."
    hslow "Huh? Oh you pick, they're yours anyway."
    show arnold turn calm with dissolve
    aslow "Okay...I'll try this one."
    h "He picked one up out of the bag and set it aside then handed me the other one."
    show arnold grin with dissolve
    aslow "Enjoy!"
    hslow "Um, yeah same to you."
    h "I popped open the top and grinned."
    hslow "Oh, broccoli and cheddar!"
label DASOUP:
    window show    
    h "For a moment we both sat in silence eating our soups..."
    h "On Arnold's stoop..."
    h "Me on one step, Arnold a few steps higher..."
    h "When he suddenly decided to sit next to me."
    show arnold turn simple with dissolve
    aslow "Let me try yours?"
    hslow "What?"
    show arnold simple with dissolve
    aslow "Yours looks good, can't I try some?"
    hslow "You have your own Football Head!"
    h "I dug my spoon into the creamy cheddar and stirred it..."
    hslow "So good, I guess you're gonna have to wait for the festival."
    show arnold sneaky with dissolve
    aslow "Not if you'd give me some I won't."
    menu:
        h "..."
        "Fine.":
            jump nopicture
        "No way!":
            jump picture
label nopicture:
    window show
    $ renpy.block_rollback()
    hslow "Criminy, you're such a baby...here!"
    h "I handed the cup to him and crossed my arms over my chest."
    show arnold grin with dissolve
    h "And he gladly took it, a winning smile spread across his face."
    h "...And that made it worth it, so, so worth it."
    show arnold calm with dissolve
    aslow "It's good, thanks."
    hslow "Yeah I know it was..."
    hslow "Now give it back!" 
    h "I snatched the soup from him and placed it off to the side, out of his reach."
    hslow "Maybe you should have checked under the lids before picking, huh?"
    show arnold sad smile with dissolve
    aslow "Yeah, I know...my fault."
    hslow "Damn straight."
    show arnold turn unsure with dissolve
    aslow "I'll just eat my vegetable soup over here..."
    h "Ugh, he looked so cute and pathetic..."
    hslow "...Here, we can switch."
    show arnold simple with dissolve
    aslow "Really?"
    hslow "Yeah, only cause your face is making me sick."
    aslow "..."
    show arnold frown with dissolve
    aslow "...Well, that's not a very good reason."
    hslow "...You're right...I'm sorry."
    show arnold turn unsure with dissolve
    aslow "Really?"
    hslow "Yes, really. Criminy, why does everybody doubt my sincerity!"
    show arnold turn sad with dissolve
    aslow "Because you're not so nice all the time."
    h "Those were truthful words if I ever heard them..."
    hslow "Yeah I know."
    aslow "..."
    show arnold calm with dissolve
    aslow "But you have good sides too...."
    h "And suddenly that truth stung just a little less..."
    jump friends
        
label picture:
    window show
    $ renpy.block_rollback()
    hslow "No way, this is all mine Arnoldo..."
    show arnold sad smile with dissolve
    h "I stuck my spoon in my mouth and ran it over my tongue."
    h "Then I dug it back in for another helping..."
    hslow "So jealous of my cheddar goodness, aren't you?"
    h "But just as I lifted my serving out..."
    scene CG42
    with dissolve
    h "He grabbed my hand and stuck the spoon into his own mouth..."
    h "..."
    h "But it had just been in my mouth..."
    h "What just happened?"
    h "Slowly he pulled my hand, gripped tightly on the spoon, away from his lips."
    scene bg arnold house
    with dissolve
    show arnold yeah with dissolve
    aslow "I knew it was good."
    hslow "I-I-I...."
    show arnold sneaky with dissolve
    aslow "If you would have shared that wouldn't have happened."
    hslow "That was in my mouth!"
    show arnold bored with dissolve
    aslow "We've chewed the same piece of gum before and that's much worse."
    hslow "Well, yeah...but...!"
    hslow "I....Okay, you got me there."
    show arnold sneaky with dissolve
    h "He gave me a nearly devilish look and licked the spoon clean."
    h "Then he took his own spoon, going for another helping."
    h "I forgot Arnold could be like that..."
    show arnold yeah with dissolve
    aslow "I'm glad we worked this out."
    hslow "It's just..."
    aslow "Hmm?"
    hslow "You like getting a rise outta me, don't ya Hair Boy?"
    show arnold simple with dissolve
    aslow "I have no idea what you're talking about."
    h "Though his voice was serious I could see the smile that played on his lips."
    h "He liked teasing me?!"
    h "...Well, I did like teasing him too but that's not my point!"
    h "Did he know...?"
    h "No, he doesn't know anything!"
    h "Nothing!"
label friends:  
    window show
    hslow "..."
    hslow "So...are we like...friends now?"
    show arnold surprise with dissolve
    aslow "Huh?"
    hslow "What? I uh, well...it just seems like it ya know..."
    hslow "So...I...."
    show arnold turn sad with dissolve
    h "He frowned and my heart fell..."
    aslow "We were friends before this...weren't we?"
    h "Were we?"
    h "If he thought so then I sure as hell wasn't going to disagree...."
    hslow "I guess, I just thought I...bugged you."
    show arnold okay with dissolve
    aslow "You do bug me."
    hslow "..."
    hslow "I'm going home now..."
    show arnold turn unsure with dissolve
    aslow "No, no wait..."
    h "He grabbed my arm and I sat back down."
    show arnold calm with dissolve
    aslow "It's not like I mean that in a bad way..."
    hslow "How could that possibly mean anything else?"
    show arnold turn unsure with dissolve
    aslow "Uh, it's like this..."
    aslow "..."
    hslow "..."
    h "Was he really being serious right now?" 
    aslow "..."
    hslow "Would you say something already! Criminy!"
    show arnold surprise with dissolve
    aslow "Ah! Sorry, sorry..."
    show arnold sad smile with dissolve
    aslow "It's just..."
    aslow "I kinda wanna figure you out."
    hslow "What's to figure out? I'm me..."
    aslow "Yeah, I know that."
    hslow "Hey, watch your tone, bucko."
    show arnold turn unsure with dissolve
    aslow "Heh, well what I mean is..."
    aslow "You know, like I said...I know you're hiding something from me..."
    hslow "...?"
    show arnold calm with dissolve
    aslow "And it bugs me cause I wanna know what it is..."
    hslow "Who would have thought you'd find me so...mysterious."
    h "He takes another spoonful of soup, MY soup, and nodded his head."
    show arnold yeah with dissolve
    aslow "I bet you're actually the sweetest girl in the world..."
    hslow "In your dreams!"
    aslow "...Yep."
    hslow "...Wait, what?"
    if skipped:
        show arnold turn calm with dissolve
        aslow "I didn't say a word."
        hslow "Lies, I heard you!"
        h "He shook his head."
        show arnold calm with dissolve
        aslow "I'm going in now, I'll see you later."
    else:
        show arnold calm with dissolve
        aslow "It's nothing, thanks for the soup Helga."
    hide arnold calm with dissolve
    h "He waved  his hand and walked back into he boarding house, leaving me alone on the stoop."
    h "He didn't just admit to dreaming about me, did he?"
    h "DID HE?!"
    $ soup = True
    h "..."
    h "...."
    call School
label Backtoschool:
    window show
    $ renpy.block_rollback()
    hslow "I...uh..."
    hslow "I have no idea."
    show arnold pissed 2 with dissolve
    aslow "..."
    aslow "Yeah?"
    h "He shot me a rather serious glance before I gave in..."
label Walk:
    window show
    $ renpy.block_rollback()
    hslow "Okay, okay, you're right...let's go to class."
    show arnold sad smile with dissolve
    aslow "You don't have to sound so defeated about it."
    hslow "I just...I really hate class."
    hslow "I don't even know how I'm gonna make it in college....I'll barely ever go I know it...."
    show arnold turn unsure with dissolve
    aslow "College?...That's right around the corner isn't it."
    hslow "Yeah..."
    h "I gave Arnold a side-ways glance as he walked..."
    h "When I went off to college..."
    h "I wouldn't get to see him anymore..."
    h "It felt as if a knife had been plunged into my heart."
    h "As much as I wanted to get away from my family..."
    h "I didn't want to leave Arnold behind...at all."
    h "Why didn't I think of this before?"
    show arnold okay with dissolve
    aslow "Are you...gonna stay in state?"
    hslow "Hah! Like Big Bob's gonna dish out the cash so I can go to an outta state school..."
    hslow "I'm not Olga."
    show arnold turn calm with dissolve
    aslow "Same here..."
    hslow "..."
    show arnold sad smile with dissolve
    aslow "Well, not quite the same but I only applied to in state schools too..."
    hslow "Yeah?"
    show arnold frown with dissolve
    aslow "I don't wanna put too much strain on my grandparents finances, ya know?"
    aslow "They're telling me not to worry about it but...staying close to home seems to be the best option."
    h "For some reason I let out a sigh of relief..."
    h "Lucky for me he didn't pick up on it though."
    scene school
    with dissolve
    hslow "And here we are... Our lovely little hell on Earth."
    show arnold sneaky with dissolve
    aslow "Okay, stop exaggerating..."
    hslow "Exaggerating? I'm dead serious Football Head..."
    show arnold calm with dissolve
    aslow "Right, right..."
    scene start
    with dissolve
    h "He didn't leave me any room for argument as he pushed me through the front doors..."
    h "And straight into the office for a late slip."
    h "It wasn't any fun at all..."
    scene school hallway
    with dissolve
    hslow "See, coming to school ruined any chance of a good day."
    show arnold calm with dissolve
    aslow "Yeah, yeah I know..."
    h "I froze as I looked down the hallway..."
    h "I needed to walk in a different direction from him..."
    hslow "So, I guess I'll see you?"
    show arnold surprise with dissolve
    aslow "Ah!...Um...."
    hslow "What the heck was that?"
    show arnold turn shy with dissolve
    aslow "Nothing, nothing..."
    aslow "Yeah, I'll see ya."
    hide arnold turn shy with dissolve
    h "With a short wave he walked off towards his class and I watched him go..."
    h "I thought...maybe..."
    h "If he turned around I was doing something right..."
    h "Turn around Arnold..."
    h "Turn around..."
    h "..."
    show arnold calm with dissolve
    h "And he did."
    h "He even smiled at me...."
    h "And I did the same."
    scene start
    with dissolve
    h "..."
    h "....."
    h "Most of my daydreams that afternoon were filled with Arnold..."
    h "As usual..."
    h "But I felt they were tinted with just a little bit more hope than normal..."
    scene school
    with dissolve
    h "..."
    show phoebe smile with dissolve
    h "When school ended I greeted Phoebe with a smile..."
    h "I was sure I took her by surprise considering how down I've been as of late."
    hslow "Hey there Pheebs, ready to go?"
    show phoebe grin with dissolve
    pslow "Goodness, you've certainly cheered up..."
    pslow "Could that possibly be because you got some extra sleep this morning?"
    hslow "Well, that's part of it..."
    scene start
    with dissolve
    h "I then proceed to explain everything that had happened the last day and a half..."
    h "Explain how I was seriously ready to tell Arnold my feelings..."
    h "Well..."
    h "So long as he made the first move."
    scene bg helga house day
    with dissolve
    hslow "So how do you think I'm doing Pheebs? Any advice?"
    show phoebe question with dissolve
    pslow "Well..."
    hslow "What give it to me... I can take it."
    pslow "I'm not really sure what to tell you..."
    hslow "Really?"
    hslow "I was hoping for a little Phoebe insight..."
    pslow "The only thing I can think of is..."
    show phoebe unsure with dissolve
    pslow "Go with your gut?"
    hslow "..."
    hslow "I feel like that's how I've been doing it all along."
    hslow "And my gut doesn't always  know best..."
    show phoebe sad with dissolve
    pslow "Right..."
    hslow "But I'm gonna keep going."
    hslow "Something tells me I may actually have a chance."
    show phoebe smile with dissolve
    pslow "Good for you Helga."
    hslow "Yeah. Thanks Pheebs."
    show phoebe grin with dissolve
    pslow "No problem!"
    scene start
    with dissolve
    h "After that, I headed back home..."
    h "For some reason...I was kind of tired."
label FIGHT:
    window show
    h "..."
    h "......."
    scene helga room evening
    with dissolve
    h "Somehow...between then and now..."
    h "I wound up taking a rather long nap."
    h "And when I got up it was nearly sunset."
    h "..."
    h "Weird as it was..."
    h "I find myself filled with energy."
    h "Well, more antsy than energetic really."
    h "And I wanted to see Arnold..."
    h "Sad thing was I had NO reason..."
    h "I couldn't just walk over and ask him to..."
    h "What?"
    h "Hang out or something?"
    hslow "Could I?"
    h "I threw the blanket off my legs and swung my feet to the floor..."
    h "I mean...I did kind of hang out with him today already but..."
    hslow "Forget this, I'm just gonna go for it..."
    h "I grabbed my ear-buds and iPhone and devised a plan of action."
    h "Something like, I was just strolling by, wanna go for a walk?"
    h "Simple, to the point..."
    h "And if he said no I would be crushed."
    h "But I could take it!"
    h "So after cleaning myself up..."
    scene start
    with dissolve
    h "Off I went."
    h "..."
    h "......."
    scene bg city evening
    with dissolve
    h "My heart had been a fast paced drum the entire walk."
    h "I even tried singing aloud to the songs that played into my ears..."
    h "But all that gave me was strange looks."
    h "And when I saw the boarding house come into view..."
    h "My heart froze in my chest."
    h "And not because of nerves."
    scene bg arnold house
    with dissolve
    show lila glad with dissolve       
    play music "jim_lang_-_sid___stink.mp3"
    lslow "Oh my, I did so enjoy those cheese burgers."       
    lslow "And those sundaes were quite tasty."
    show lila glad at right  with dissolve
    show arnold calm at left with dissolve
    aslow "Yeah, definitely."
    h "Almost like I was an animal suddenly afraid..."
    h "I ducked into the alley and waited...and watched."
    show lila sympathy with dissolve
    lslow "You know, you were missed in class today."
    show arnold yeah with dissolve
    aslow "Oh yeah?"
    lslow "Why yes, just ever so much."
    show lila big blush with dissolve
    lslow "Whatever were you possibly doing?"
    h "She giggled and I felt like throwing up."
    show arnold turn unsure with dissolve
    aslow "I was with someone."
    h "I had forgotten how to breathe."
    show lila sad with dissolve
    lslow "Oh..."
    h "She looked so disappointed."
    h "I couldn't help the wicked grin that spread across my face."
    show lila glad with dissolve
    lslow "Who?"
    h "He smiled and looked away."
    show arnold turn shy with dissolve
    aslow "You probably won't believe me."
    show lila sympathy with dissolve
    lslow "Goodness Arnold, I'm sure I will."
    show arnold simple blush with dissolve
    aslow "Uh, I hung out with Helga today."
    show lila sympathy with dissolve
    lslow "Really?"
    lslow "Well that sounds lovely."
    h "Even I could tell she was lying."
    h "But Arnold didn't seem to notice..."
    h "The moron."
    show arnold yeah with dissolve
    aslow "You know it's like I've always said..."
    aslow "When she puts down that front she always has up..."
    aslow "I really like..."
    show lila glad with dissolve
    lslow "That aside..."
    h "I could have killed her."
    h "Was he just going to confess he liked me?"
    h "I mean...even if it was only as friend it was something."
    h "A little glimmer of hope."
    show lila shy with dissolve
    lslow "I had a wonderful time on our date."
    h "Suddenly I had felt like the world had broken into pieces."
    show arnold turn surprise with dissolve
    aslow "..."
    h "She leaned in and brushed her lips against his cheek before walking off..."
    h "But not before..."
    show lila glad with dissolve
    lslow "Oh!"
    lslow "Arnold, you should probably let Helga know she doesn't need to hide in the alley anymore."
    show lila grin with dissolve
    lslow "No need to be so silly!"
    show arnold pissed 2 with dissolve
    aslow "What?"
    h "He quickly turned to face me...and didn't look all that happy."
    h "Damn..."
    show lila glad with dissolve
    lslow "Ta-ta for now, Arnold."
    show lila sympathy with dissolve
    lslow "Helga."
    hide lila sympathy with dissolve
    show arnold pissed 2 at center with dissolve
    h "For a minute I didn't know what to do..."
    h "Maybe if I got as close to the wall as I could, I'd just disappear into it..."
    h "No, that wasn't going to happen."
    hslow "Heh...I just didn't want to, uh interrupt you two!"
    h "What was the point of trying to save face now?"
    h "He was already dating Lila."
    show arnold pissed with dissolve
    aslow "Yeah, well hiding and eavesdropping isn't exactly what I'd call polite either."
    hslow "I wasn't eavesdropping!"
    hslow "I was watching..."
    aslow "That doesn't make it any better."
    hslow "Fine! Look, I'm sorry, didn't mean to ruin the end of your date!"
    show arnold surprise with dissolve
    aslow "Date?"
    hslow "What are you acting dumb for, Arnold?"
    hslow "I saw her kiss you..."
    show arnold turn unsure with dissolve
    aslow "No, that was just..."
    show arnold turn angry with dissolve
    aslow "Wait... Why am I explaining myself to you?"
    h "Yeah...why was he?"
    hslow "How the hell should I know?"
    hslow "You feel guilty for it?"
    show arnold pissed with dissolve
    aslow "What?!"
    h "I didn't even know what I was saying anymore."
    h "I was jealous..."
    h "We may have been friends now...but I wanted more."
    h "And he just..."
    h "Did not."
    show arnold turn angry with dissolve
    aslow "I...don't know how I feel."
    hslow "Excuse me?"
    h "He looked away, his expression...troubled?"
    show arnold turn sad with dissolve
    aslow "I don't know what to think anymore..."
    aslow "About you...about me...everything!"
    show arnold turn angry with dissolve
    aslow "It's driving me crazy..."
    show arnold pissed 2 with dissolve
    aslow "You are driving me crazy!"
    hslow "So basically, you're mad at me for being nicer to you?"
    hslow "Is that it?"
    hslow "Cause it's easier being a bitch, let me tell you!"
    show arnold pissed with dissolve
    aslow "No! Damn it! That isn't what I'm saying at all!"
    h "I let out a small gasp, unused to the way he was speaking to me..."
    h "But I didn't back down....No..."
    h "I think I just got worse."
    hslow "Then what the hell are you saying, you idiot?"
    hslow "Do you honestly think I can understand this nonsense you're spewing all over me?!"
    hslow "Quit beating around it and just tell me."
    scene CG45
    with dissolve
    aslow "Like you can talk!"
    hslow "What?"
    aslow "Nice one minute, and than a completely horrible person the next!"
    h "That one hurt."
    aslow "Why do you do that?"
    aslow "Why can't you just be honest!?"
    aslow "Why can't you, for even {i}one day{/i}, be the person you really are?"   
    stop music
    hslow "Because I'm scared!"
    h "I covered my mouth, as if I could catch the words before they flew away."
    scene bg arnold house
    with dissolve
    show arnold frown with dissolve
    h "And suddenly...Arnold wasn't so angry anymore."      
    play music "Jim Lang - Operation Ruthless End.mp3"
    aslow "What are you scared of?"                                     
    hslow "I..."
    hslow "I...should go..."
    h "There was too much said...I didn't know what to do..."
    show arnold pissed 2 with dissolve
    aslow "Fine."
    h "His voice was like ice."
    aslow "All I wanted to do was be your friend..."
    aslow "And you're making that impossible."
    hide arnold pissed 2 with dissolve
    play sound "door-9-close.wav"
    h "Without another word he slammed his front door behind, going inside."
    h "And I nearly collapsed on the sidewalk..."
    h "I felt like crawling into a hole and dying."
    h "Never had Arnold and I fought that badly..."
    h "Never."                             
    stop music fadeout 2.0
    $ fight = True
    call BLOCK
label Okay:
    window show
    $ skipped = True
    $ renpy.block_rollback()
    hslow "Well, yeah I like to think I have some creative ideas..."
    show arnold calm with dissolve
    aslow "Hmm...Yeah, I can see that about you."
    hslow "Oh, I'm so glad."
    show arnold sad smile with dissolve
    aslow "Ouch."
    aslow "Your sarcasm can kill, ya know?..."
    hslow "I perfected it so much, it's reached that level?"
    hslow "I'm awesome."
    show arnold sneaky with dissolve
    aslow "I gotta learn how to turn an intended insult into a compliment too..."
    aslow "Maybe then I can learn to fight you off."
    hslow "It's a gift, you'll never know."
    show arnold yeah with dissolve
    aslow "Haha~ darn."
    h "There was a beat of silence..."
    h "Then..."
    show arnold simple with dissolve
    aslow "You hungry?"
    hslow "Huh?"
    show arnold turn simple with dissolve
    aslow "I'm starving...you want something to eat?"
    h "It was funny..."
    h "I had completely forgotten about my lack of breakfast right up until this point."
    h "And then my stomach pretty much roared."
    hslow "Guess that answers your question, doesn't it?"
    h "My voice was as snarky as ever..."
    h "By my red cheeks betrayed my bravado."
    h "He let out a quiet laugh."
    show arnold yeah with dissolve
    aslow "Come on let's talk a walk and find something..."
    hslow "Alrighty then..."
    scene start
    with dissolve
    h "..."
    h "......."
    scene bg city day
    with dissolve
    h "We wandered about the city trying to find something to eat..."
    h "And...maybe arguing about it..."
    h "Just a little bit."
    hslow "This was your idea, could you pick something already?"
    hslow "Criminy!"
    show arnold pissed 2 with dissolve
    aslow "I just don't know what I want..."
    hslow "Thank you, Captain Obvious, as if I didn't gather that by now."
    show arnold frown with dissolve
    aslow "...Right..."
    h "He slowed his pace just a bit then took a look inside a deli window."
    show arnold okay with dissolve
    aslow "Soup."
    hslow "Seriously?"
    hslow "Whatever, you finally made a choice I'm not gonna fight you on it."
    scene start
    with dissolve
    h "We entered the deli and ordered our soups..."
    h "I got cheddar and broccoli..."
    h " And Arnold ordered veggie..."
    h "..."
    scene bg city day
    with dissolve
    hslow "Where are we gonna eat these?"
    h "As I held up the bag, I could feel the contents shift inside..."
    h "I had to be a bit more careful..."
    show arnold okay with dissolve
    aslow "My house is nearby, let's just go there."
    hslow "And your grandparents are gonna be cool about you coming home in the middle of the day?"
    show arnold simple with dissolve
    aslow "I'll just tell them I had a free period and left early."
    hslow "And now I've corrupted you into lying!"
    show arnold sad smile with dissolve
    aslow "You make it sound as if you're some criminal..."
    hslow "I'm quite the {i}Hell Girl...{/i}"
    show arnold sneaky with dissolve
    aslow "...That was a terrible joke."
    hslow "Whatever, move faster I'm hungry."
    scene start 
    with dissolve
    h "..."
    h "......."
    scene bg arnold house
    with dissolve
    h "We sat down on his front stoop and pulled the soup out of the bag..."
    h "I handed him his vegetable, and took out mine as well."
    hslow "Damn."
    show arnold turn simple with dissolve
    aslow "What's wrong?"
    hslow "I think there's only one spoon."
    h "I handed him off the bag to check."
    h "He dug through it for a minute, then took the plastic utensil out of the bag."
    show arnold simple with dissolve
    aslow "Not to worry..."
    h "And with a flick it suddenly became two."
    hslow "Heh, very nice."
    h" I gave him a deliberately slow clap."
    show arnold sneaky with dissolve
    aslow "I am a magician, after all..."
    aslow "I made you disappear once..."
    hslow "Hah! Very funny...gimme that!"
    h "I reached for one of the spoons and the tips of my fingers brushed against his..."
    h "It was like a shot of electricity went through my entire arm."
    h "And I slowly pulled away, feeling the heat rise to my cheeks."
    show arnold sad smile with dissolve
    aslow "Did you just shock me?"
    h "Was that all it was?"
    hslow "Uh...yeah, sorry I guess."
    show arnold calm with dissolve
    aslow "No...no, it's fine."
    h "He took a quick glance down at his hand then shook his head."
    h "It looked as if he was trying to erase a thought or something..."
    h "But what the hell did I know?"
    show arnold grin with dissolve
    aslow "Enjoy!"
    hslow "Um, yeah same to you."
    jump DASOUP