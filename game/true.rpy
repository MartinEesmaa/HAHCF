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
label DAYTHREE:
    window show
    scene classroom
    with dissolve
    h "When I walked into class it felt as if my feet were made of lead."
    h "I took my seat behind him and tried to speak..."
    h "But any noise I made sounded hollow...empty..."
    h "Almost unreal."
    h "I was scared."
    h "I was always scared."
    h "And before I knew it class had ended."
    h "And Arnold rushed out without a word..."
    h "Again."
    h "..."
    h "Most of the day seemed to go the same way..."
    scene cafeteria
    with dissolve
    h "When lunch finally came around..."
    h "I had finally worked up enough nerve to apologize..."
    h "For everything."
    h "And when I stood face to face to that reality..."
    h "It seemed like a had a lot of explaining to do."
    h "But when I took a glance around the room..."
    h "I couldn't find him anywhere."
    show phoebe smile
    with dissolve
    pslow "Helga, do you wanna sit over there?"
    h "I can barely even hear her."
    hide phoebe smile
    with dissolve
    h "My eyes scanned the cafeteria, once...twice...but I still couldn't find him."
    h "And it felt like someone was squeezing my heart in their hand."
    h "..."
    h "I almost feel like a zombie as I sit down next to Phoebe at the table."
    h "She made polite Phoebe-like chit chat while I try my best to answer..."
    h "And I try to eat..."
    h "But it all kind of feels hopeless now."
    h "I..."
    h "It felt like, if it had been before I would have come up with some type of incredible scheme to get my way..."
    h "But this time I didn't know what to do..."
    h "I had come so, so far...and now..."
    h "Why was everything crashing in on itself?"
    h "Why did this always have to happen to me?"
    h "Can't something ever go right?"
    h "Ever?!"
    show phoebe question
    with dissolve
    pslow "And so like I was saying..."
    hslow "Huh?"
    show phoebe sad 
    with dissolve
    pslow "Helga...you weren't listening at all, were you?"
    hslow "I...uh, no Phoebe I'm sorry..."
    play music "04 groove remote (abner).mp3"
    pslow "Helga..."
    pslow "What's wrong?"
    pslow "You've been acting rather strange since this morning."
    h "I just shrug my shoulders."
    hslow "It's...it's probably nothing."
    hslow "I guess I'm over thinking it...or something..."
    show phoebe question
    with dissolve
    pslow "Over thinking?"
    pslow "What are you over thinking Helga?"
    h "I let out a long, defeated sigh."
    hslow "Why Arnold isn't here..."
    show phoebe sad
    with dissolve
    pslow "Oh Helga, you can't possibly think he's avoiding you."
    pslow "You said things were going well between you two only yesterday."
    hslow "I know what I said."
    hslow "But something happened after that and..."
    show phoebe question
    with dissolve
    pslow "And?"
    hslow "Arnold and I got into a fight..."
    pslow "..."
    pslow "You get into fights all the time..."
    h "I tried to glare but my eyes must have looked too sad to be convincing..."
    h "Because Phoebe saw right through it."
    show phoebe sad with dissolve
    pslow "...How bad was it?"
    hslow "Bad."
    pslow "Oh no..."
    hslow "At first he caught me spying on him and Lila."
    show phoebe question
    with dissolve
    pslow "He was with Lila?"
    h "I nodded my head."
    hslow "She said they were on a date..."
    hslow "So anything I told him was in jealousy...obviously."
    hslow "I mean I've been trying so hard..."
    hslow "And all she has to do is swing her braid around and all the boys just wanna jump her bones!"
    hslow "Ugh..."
    show phoebe sad with dissolve
    h "I pulled at my pigtails until they fell out, my hair falling to my back in two swoops."
    h "I didn't even care anymore.."
    hslow "I think you're right Phoebe.."
    show phoebe question with dissolve
    pslow "What?"
    h "She sounded unsure, so I tried to explain myself."
    hslow "Maybe I should just stop obsessing over him..."
    hslow "Maybe I'll be happier if I just move on, find someone new..."
    hslow "If anyone will take me that is."
    pslow "..."
    show phoebe sad with dissolve
    pslow "I think I was wrong, Helga."
    hslow "...What?"
    pslow "Do you know what I'd do if you'd ask me to stop thinking about Gerald?"
    hslow "...No."
    pslow "Well, I'd be pretty upset. I love him."
    hslow "So?"
    pslow "Don't you love Arnold, too?"
    hslow "You...you know that I do."
    pslow "So I was wrong Helga..."
    show phoebe smile with dissolve
    pslow "You don't just try and forget someone you love until...well, until the very end."
    pslow "And quite frankly, I still think you can keep going!"
    h "I was sure my eyes had gotten wide hearing Phoebe's words of encouragement."
    hslow "Wow...thanks Pheebs."
    show phoebe grin with dissolve
    pslow "No problem. What are best friends for?"
    hslow "Heh, yeah, you're right."
    show phoebe question with dissolve
    pslow "..."
    pslow "So Helga...what are you going to do?"
    hslow "...I know I should keep going..."
    hslow "No, I want to keep going... I want to apologize."
    show phoebe smile with dissolve
    pslow "Right, of course."
    h "I shook my head."
    hslow "But he's already with Lila, what's the point?"
    show phoebe question with dissolve
    pslow "Did he say he was with Lila?"
    hslow "Well...no."
    pslow "I don't think you can do anything until you talk to him."
    pslow "Sitting around here moping is only going to make YOU worse."
    h "Her words stung, but I knew they were the truth."
    h "I had a feeling she even saw me flinch."
    hslow "You're too smart Pheebs."
    show phoebe laugh with dissolve
    pslow "Ehehe~ I know."
label Ohwhy:    
    window show
    $ renpy.block_rollback()  
    $ Waited = True
    hslow "So...I'll talk to him as soon as I see him..."
    scene start 
    with dissolve
    h "..."
    h "..."
    h "The crappy thing was, I didn't see him the entire rest of the day."
    h "And even though I did want to..."
    h "Even though I knew I should keep fighting until the end..."
    h "It felt like it was all over."
    call FAIRGROUNDS 
label NO:
    window show
    $ renpy.block_rollback()             
    $ imwrong = True
    play music "Jim Lang - Helga and Arnold Make Up.mp3"
    hslow "It's nothing...really, I'm okay."
    if fight:
        scene CG43
        with dissolve
        hslow "It was just a lot..."
        h "Arnold takes a seat beside me."
        h "His body goes somewhat slack, as if all that tense pressure from before has faded away."
        aslow "A lot of what?"
        h "He finally asks, his voice slightly quiet."
        hslow "A lot of everything..."
    hslow "I guess..."
    aslow "..."                                                               
    hslow "It's just...I've been trying so hard..."
    hslow "And...I feel like it's for nothing!"
    aslow "...Trying hard? What for?"
    hslow "To be nicer...? I dunno..."
    if fight:
        hslow "As bad as I can be at trying..."
    hslow "It's just..."
    aslow "..."
    h "My words felt lost...but I had to keep going."
    hslow "I don't hate you."
    h "I felt like I really needed to say that."
    scene CG44
    with dissolve
    aslow "...I know."
    hslow "Yeah?"
    scene festival day
    with dissolve
    if fight:
        show arnold sad smile with dissolve
        aslow "Even if you made it hard for me to wanna try..."
    show arnold yeah with dissolve  
    aslow "I want to be your friend."
    hslow "..."
    aslow "..."
    show arnold turn sad
    with dissolve
    aslow "No...wait..."
    h "What is he..."
    show arnold frown
    with dissolve
    aslow "I'm sorry."
    h "That I wasn't expecting."
    hslow "What?"
    h "I sound too...weak."
    hslow "Wh-Why the hell are you sorry..."
    h "Why do I do this to myself?"
    show arnold sad smile
    with dissolve
    aslow "I didn't talk to you today...pretty much ignored you."
    aslow "That was because..."
    show arnold turn sad
    with dissolve
    aslow "I thought that was what you wanted."
    h "Why would I ever want that ever?"
    aslow "Cause when you ran off yesterday..."
    if poem:
        aslow "I figured I did something...wrong."
        h "My heart has surely stopped."
        show arnold frown
        with dissolve
        aslow "And I should have asked if you were okay when I saw you this morning..."
        aslow "I was wrong and..."
        hslow "No..."
        show arnold turn sad
        with dissolve
        aslow "What?"
        hslow "I..."
        h "My voice is almost like a whisper..."
        h "I can't get it any louder..."
        hslow "I left because of me, not you....not you."
        show arnold sad smile
        with dissolve
        hslow "I thought...you weren't talking to me today because..."
        hslow "Because I scared you off or...or something and..."
        hslow "And...the way you just accepted it right then..."
        hslow "That part of me I always hide, I..."
        hslow "I wasn't prepared for that."
        hslow "But rejection?"
        hslow "That's easier to expect."
        hslow "But..."
        hslow "But you praised me Arnold..."
        show arnold calm
        with dissolve
        hslow "You surprised me...and elated me...and scared me."
        hslow "It was... it was a lot to handle all at once."
        show arnold sad smile
        with dissolve
        aslow "Helga...did you really think I'd laugh at you for opening up to me?"
        aslow "Do I seem like that kind of person to you?"
        hslow "..."
        h "...He was right...of course he wasn't."
        hslow "No, but still..."
        show arnold calm
        with dissolve
        aslow "Actually I was glad you did it."
        aslow "I don't know how many times I have to tell you..."
        show arnold yeah
        with dissolve
        aslow "I've always known there was apart of you that you hid from everybody else..."
        aslow "That you weren't so cold...or mean..."
        aslow "And when you gave me your poem..."
        show arnold simple blush
        with dissolve
        aslow "Well, it was kind of like you gave me the key."
        hslow "Hah...how corny."
        show arnold turn shy
        with dissolve
        aslow "Yeah, but it's the truth Helga."
        show arnold yeah
        with dissolve
        aslow "And I'm no liar."
        hslow "I know..."
        show arnold calm
        with dissolve
        aslow "Okay..."
        aslow "..."
        hslow "..."
        show arnold sad smile with dissolve
        aslow "So why did you run off?"
        hslow "I...uh...saw you with Lila..."
        show arnold okay with dissolve
        aslow "And?"
        hslow "And you guys seemed really close..."
    else:
        show arnold sad smile with dissolve
        aslow "When I slammed the door on you..."
        h "He seems almost ashamed of himself...but there was no reason for it."
        show arnold turn sad with dissolve
        aslow "It felt like...I should just give up."
        hslow "Oh..."
        show arnold frown with dissolve
        aslow "I mean, why was I trying so hard when all you ever do is snap back at me?"
        aslow "I knew you were trying to be better though, but I got frustrated...."
        aslow "So I'm sorry."
        hslow "You're sorry?"
        hslow "But...it was my fault."
        hslow "Really, Arnold, you don't have to be the better person all the time."
        show arnold turn sad with dissolve
        aslow "I know but..."
        hslow "No."
        h "He gave me a questioning look."
        hslow "Let me be a better person...at least once."
        hslow "..."
        hslow "Arnold, I'm sorry for...everything."
        h "And I meant it."
        show arnold turn unsure with dissolve
        aslow "Everything?"
        hslow "Yes...everything. Every time I was mean for no reason, for bullying you, and hurting you..."
        hslow "And for yesterday...cause I was..."
        show arnold sad smile with dissolve
        aslow "What?"
        h "I felt my cheeks grow warm."
        hslow "I was jealous, okay?"
        h "He seemed honestly surprised."
        show arnold turn surprise with dissolve
        aslow "Jealous over Lila...and me?"
        hslow "Yeah, yeah...be shocked or whatever."
    hslow "I didn't know you guys were dating so..."        
    show arnold surprise with dissolve      
    stop music
    aslow "Wait, wait, what?"
    if poem:
        hslow "She said she liked seeing you happy..."
    else:
        hslow "Yesterday...Lila said she had a nice time on your date."
    show arnold sad smile with dissolve                       
    play music "Jim Lang - Helga's True Love.mp3"                                
    aslow "That doesn't mean we're together Helga..."      
    hslow "You...aren't?"
    aslow "Yeah, I haven't liked Lila like that in a while."
    h "I felt completely stunned."
    hslow "Oh."
    aslow "..."
    show arnold turn shock with dissolve
    aslow "Wait a minute..."
    h "Suddenly he looked away, almost as if he was shy."
    show arnold turn shy with dissolve
    aslow "You...like me, right?"
    h "Oh my god, I was such an idiot."
    hslow "What?! Who said that?! I didn't say that!"
    show arnold turn okay with dissolve
    aslow "..."
    hslow "..."
    hslow "But I don't hate you."
    h "It felt like it needed to be repeated."
    aslow "Well..."
    show arnold simple blush with dissolve
    aslow "As long as you don't hate me..."                                 
label TRUEASK:    
    window show
    h "It looked as if his little Football Head was coming up with a plan."
    if IMGOING:
        show arnold calm with dissolve
        aslow "You're still going to the Festival tomorrow, right?"
        hslow "Yeah, I guess so."
    elif Maybe:
        show arnold calm with dissolve
        aslow "Have you made up you're mind about going to the Festival?"
        hslow "Why...do you ask?"
    else:
        show arnold calm with dissolve
        aslow "About the Festival tomorrow..."
    show arnold yeah with dissolve    
    aslow "Well, why don't I pick you up and we can meet Gerald and Phoebe there?"
    hslow "...Like...a double date or something?"
    aslow "Yeah."
    hslow "..."
    aslow "...."
    hslow "Okay."
    show arnold grin with dissolve
    aslow "Great. I'll see you tomorrow at seven then, okay?"
    hslow "Uh, yeah, okay!"                    
    h "He gave a quick wave and then off he went."
    hide arnold grin with dissolve
    h "..."
    h "So I was going on a date with Arnold."
    h "It seems like things actually did go my way."
    if fight:     
        stop music
        lslow "So have you made up?"
        hslow "What?"
        h "I turn around and catch Lila standing behind me, smiling."
        show lila glad with dissolve
        h "I could have socked her right then and there."
        hslow "Yeah, we made up...no thanks to you."
        lslow "..." 
        show lila grin with dissolve            
        play music "Jim Lang - Groove Remote (LockJaw).mp3"
        lslow "Thank goodness!"                    
        hslow "Um...what?"
        show lila sympathy with dissolve
        lslow "I was so worried, just ever so worried!"
        hslow "Wait, I'm confused..."
        hslow "Don't you like Arnold too?"
        show lila glad with dissolve
        lslow "Why of course not, Helga."
        lslow "He's a dear friend, just like you are."
        hslow "...I still don't get it."
        show lila sympathy with dissolve
        lslow "It's quite simple, actually."
        hslow "It doesn't seem like it is."
        show lila shy with dissolve
        lslow "I just felt like you needed a little bit of a push..."
        lslow "You're the type of person who does well under some pressure I believe..."
        lslow "Rather than..."
        hslow "WAIT ONE MINUTE!"
        hslow "Just how sick are you, thinking making us fight would...?"
        show lila sad with dissolve
        lslow "It's not that I wanted you to fight...I just felt like..."
        lslow "Maybe if you were a bit more honest with him..."
        hslow "...Fine, I get that."
        hslow "But how is this any of your business?"
        show lila glad with dissolve
        lslow "Contrary to what you might think Helga..."
        lslow "I do considering myself your friend."
        h "For a moment I was speechless."
        hslow "..."
        show lila grin with dissolve
        lslow "Well, now you and Arnold are one step closer together."
        lslow "I feel like it was a plan well accomplished!"
        h "She seemed rather proud of herself."
        hslow "I don't really know what to say?"
        show lila sympathy with dissolve
        lslow "You don't have to say anything..."
        show lila glad with dissolve
        lslow "Though, it was quite hard being so mean spirited."
        h "I smile despite myself."
        hslow "It gets easier with practice."
        show lila grin with dissolve
        lslow "Ehehehe~ I'll have to take you're word for it."
        h "There was beat of silence..."
        show lila glad with dissolve
        lslow "So he's taking you to the Cheese Festival?"
        hslow "Huh? Oh yeah..."
        lslow "What are you going to wear?"
        h "My eyes got wide..."
        hslow "I have no idea."
        h "Lila laughed."
        show lila grin with dissolve
        lslow "I'm ever so sure we'll find something..."
        hide lila grin with dissolve
        h "She rushed behind me and pushed my back, out of the fair grounds..."
        h "To who knows where..."
        hslow "..."
        hslow "This is gonna be one weird friendship I know it."         
        stop music fadeout 3.0
        scene start
        with dissolve
        call HOMEAGAIN
    else:
        call HOMEAGAIN
label FOUNDYOU:
    window show
    h "Why is he here?"      
    h "How do we always end up finding each other..."
    h "Always?"
    h "..."
    h "Was he...looking for me?"
    show arnold frown with dissolve
    h "When I turn and look at him my heart quickens..."
    hslow "Football Head..."
    h "And I can't control my mouth."                           
    hslow "What are you doing following me around all the time?!"
    hslow "I've already got one stalker, I don't need another one..."
    hslow "Especially if it's you."
    hslow "So just go."
    show arnold turn angry with dissolve
    aslow "..."                                      
    aslow "So you're still acting this way, huh?"
    hslow "Acting like what?"
    hslow "A completely...what was it again?"
    show arnold turn sad with dissolve
    aslow "..."
    hslow "That's right...a completely {i}horrible{/i} person."
    hslow "Guess that's just me."
    aslow "..."
    hslow "Gonna say something Football Head?"
    show arnold turn angry with dissolve
    aslow "It was like you weren't even listening yesterday..."
    hslow "Oh no, no...I heard every single freaking word!"
    h "I felt a shudder of pain mix with anger rush through my whole being."
    h "It was getting hard to stand."
    show arnold pissed with dissolve
    aslow "Then can't you understand I'm trying here?"
    hslow "So am I! And it's like..."
    with vpunch 
    hslow "!!!"
    h "For a minute I got dizzy...I had to grab on to something to keep straight."
    h "..."
    h "It was like Arnold completely forgot we were even fighting..."
    show arnold frown with dissolve
    aslow "Take it easy..."
    h "Strong hands grab onto my shoulders and lead me towards a bench."
    h "The world started to even out again..."
    show arnold turn sad with dissolve
    aslow "Are you...okay now?"
    call NO
        
label TRUEPATH:
    window show
    $ funny = True
    hslow "Well, I gotta say...you do look a little funny."
    h "I tried to stifle a laugh...and Arnold blushed."
    show arn turn sad with dissolve
    aslow "Aw, ya see...I knew it!"
    show arn simple with dissolve
    aslow "I'm gonna go home and change real quick..."
    hslow "But wait, Arnold...the rain?"
    show arn grin with dissolve
    aslow "Oh right!"
    h "He stops and smiles."
    aslow "The rain's already letting up, so they say the Festival's still a go..."
    aslow "Apparently they covered everything with tarps just in time..."
    hslow "Seriously?"
    aslow "Yeah, so I'll go change and you get ready."
    hslow "Right, okay!"
    hide arn grin with dissolve
    h "So it looked like this wasn't a lost hope after all!"
    call TRUEPATHEND_1
    
label TRUEPATHEND:
    window show
    scene start
    with dissolve                        
    play music "02 groove remote.mp3"
    h "When I woke up the next morning I was thrilled."
    h "In just..."
    h "I glance at my alarm clock..."
    h "Eight hours my love would come here looking for me..."
    h "Ready to take me to the Festival!"
    h "I made a move towards my window and threw open my curtains..."
    scene helga room day
    with dissolve
    h "Nothing was going to ruin my day!"
    h "Sure, it was a double date...but it was better than nothing!"
    h "..."
    h "...."
    h "The only down side..."
    h "I had no idea what to do with myself..."
    if fight:
        h "I got up out of bed and moved towards my closet, pulling out the outfit I had bought the day before..."
    else:
        h "I got up out of bed and walked towards my closet."
        h "I fanned through my clothes until I found something rather okay to wear tonight..."
        
    hslow "Well, that's something done...at least."
    h "After another minute of lost thought..."
    h "I sit down at my vanity..."                
    h "And stare at my face."
    h "Of course, I just got up so I didn't exactly look my best..."
    h "But I was more curious as to what I should do with it tonight."
    h "I opened the drawer and pulled out the various make-up kits I had..."
    h "And uh, barely ever wore."
    hslow "Ugh, I used to be better at this..."
    h "..."
    h "After a minute of being completely frozen I got up."
    hslow "Shower first..."
    h "Other things...later...much later."
label callonme:    
    scene start
    with dissolve
    h "..."
    h "......."
    scene helga room evening
    with dissolve
    h "I spent most of the day trying to find things to take off my mind about the evening..."
    h "Watching TV, trying to write, read..."
    h "But most of it was in vain and in the end I was still nervous as hell."
    h "At least the sun had come out sometime during the day..."
    h "I mean, sure, Phoebe was going to be there...but it still felt like so much more than just a usual hang out."
    h "And Arnold was going to be here any minute now."
    h "Only minutes?!"
    h "Sitting on the edge of my bed I tapped my foot nervously before finally getting up."
    scene Inside House
    with dissolve
    h "Holding on to the railing for dear life, I made my way downstairs and sat on the first step, watching the door."
    h "Even if he was late I wasn't going to snipe or be rude..."
    h "Well, at least I was going to try."
    h "Pulling my phone out of my bag, I watched as 6:59 became 7:00..." 
    stop music fadeout 3.0
    h "And my eyes flashed to the door..."
    h "...Nothing...."
    h "......Nothing...."
    h ".........Nothing..."
    h "And then finally..."
    play sound "Arnold Knock.wav"
    h "A knock on the door."
    h "Moving faster then I thought I could, I throw open the door and smile at him."
    h "And he smiles right back."
    show arnold grin with dissolve                        
    play music "Jim Lang - Helga's True Love.mp3"
    aslow "You ready to go?"           
    h "Even though he told me he would be here..."
    h "I'm still surprised to see him."
    h "So instead of answering him, I simply nod my head."
    h "Wanting to do nothing that could break the fantasy."
    h "..."
    h "He steps aside and motions for me to walk out first."
    h "And I do so, hearing him close my front door for me."
    scene bg helga house evening
    with dissolve
    show arnold turn calm with dissolve
    aslow "Well it's finally here..."
    h "He mumbles this more to himself than to me..."
    h "So I give no reply."
    show arnold calm with dissolve
    aslow "Gerald told me to meet him and Phoebe by the food tables when we get there..."
    h "I silently nod my head, again."
    h "I'm afraid my big mouth is gonna screw this up for me."
    scene start
    with dissolve
    h "..."
    h "......"
    scene bg city evening
    with dissolve
    h "For a few more minutes we walk in complete silence."
    h "But then, Arnold suddenly stops me."
    show arnold sad smile with dissolve              
    stop music
    aslow "Is there any reason you're being so quiet?"
    aslow "It's...not really like you."
    hslow "Quiet?"
    h "I don't know what to say without sound like a complete moron."
    h "So instead...I just deny it."
    hslow "I'm not being quiet, I'm just like I always am, Arnoldo really!"
    show arnold calm with dissolve
    aslow "Yeah?"
    hslow "Yeah!"
    show arnold sneaky with dissolve       
    play music "04 groove remote (abner).mp3"
    aslow "Cause that was the first thing you've said to me all night."
    hslow "Ah...um..."
    h "Damn it, he got me."
    hslow "Okay...fine...it's just..."
    show arnold simple with dissolve
    aslow "..."
    aslow "Just what?"
    hslow "I don't wanna say anything that's gonna...ya know...screw this up."
    aslow "..."
    show arnold laugh with dissolve
    aslow "Hahaha~"
    h "So he laughs at me?"
    h "Does he want me to punch him in the face or something?"
    h "So I bite the inside of my cheek to keep from boiling over."
    hslow "Ya know, I was trying to be honest...thanks for that."
    show arnold grin with dissolve
    aslow "That's not why I'm laughing..."
    hslow "Uh-huh, yeah sure."
    show arnold calm with dissolve
    aslow "No really..."
    h "Finally, he's able to stifle his chuckles..."
    show arnold yeah with dissolve
    aslow "I asked, you to come with me didn't I?"
    aslow "You, as in Helga. Not some quiet pod person who's gonna stand next to me the whole night in silence."
    aslow "If you're gonna yell at me, I can take it."
    show arnold turn calm with dissolve
    aslow "I have all this time, now shouldn't make it any different."
    h "I look away from him for a moment."
    hslow "But I..."
    hslow "Ugh, I want it to be different, okay?"
    show arnold turn simple with dissolve
    aslow "..."
    h "It looks as if Arnold is thinking something over."
    h "But then he nods his head."
    show arnold yeah with dissolve
    aslow "Trust me, Helga."
    hslow "What?"
    aslow "It already is different."
    h "Arnold continues on his way to the Festival...but..."
    hide arnold yeah with dissolve
    h "I'm not exactly sure what to make of that."
    h "But I follow behind him...thinking I guess I could act a bit more..."
    h "Like me."        
    stop music fadeout 3.0
label TRUEPATHEND_1:   
    window show
    scene start
    with dissolve
    h "..."
    h "......"
    scene food court
    with dissolve
    h "When we get to the Festival we see Gerald and Phoebe just sitting down to eat."
    h "We make our way over to them."         
    play music "Jim Lang - Home Wit Jerome.mp3"
    if funny:
        show phoebe grin with dissolve
        pslow "Oh, Helga!"
        pslow "We certainly lucked out didn't we?"
        pslow "Thank goodness they put those tents up!"
        hslow "Heh, yeah."
    else:
        show phoebe grin with dissolve
        pslow "Oh, Helga!" 
        pslow "There you are!"
    show phoebe laugh with dissolve    
    pslow "Here you go, as promised."
    h "She hands me a cheese stick which I take eagerly."
    if almost:
        h "With all the sleeping...and Arnold's sudden pick up..."
    else:
        h "I somehow, with all the busy work..."
    h "Had forgotten to eat today."
    hslow "Thanks Pheebs!"
    hide phoebe laugh with dissolve 
    show gerald happy at left with dissolve
    show arnold okay at right with dissolve 
    gslow "Arnold, man what's up?"
    aslow "Eh...nothing yet."
    gslow "I get that." 
    h "They greeted each other with their classic handshake."
    h "Some things never change."
    show gerald calm with dissolve
    gslow "So what are we doin' tonight?"
    show arnold grin with dissolve
    aslow "Haha~ I have no idea."
    hslow "That's great, I'm really excited now guys."
    hide gerald calm with dissolve 
    show arnold turn simple at center with dissolve
    aslow "Okay, give me a minute, I'll think of something."
    hslow "Well..."
    show arnold okay with dissolve
    aslow "Well what?"
    hslow "Why don't you go think about it over there..."
    hslow "And get me some nachos..."
    show arnold bored with dissolve
    hslow "..."
    aslow "..."
    hslow "Please?"
    show arnold calm at right with dissolve
    show gerald happy at left with dissolve
    aslow "Sure."
    aslow "Come on, Gerald."
    gslow "Yeah, you want anything?"
    h "He was looking to Phoebe."
    hide arnold calm with dissolve
    hide gerald happy with dissolve
    show phoebe smile with dissolve
    pslow "Nothing, thank you."
    h "I waited until they were out of listening distance before I turned to face Phoebe."
    hslow "I can't calm down!"
    hslow "Agh, I've got butterflies and everything."
    hslow "This isn't good."
    show phoebe question with dissolve
    pslow "..."
    show phoebe laugh with dissolve
    h "Phoebe was only quiet a moment before she began to laugh."
    hslow "That keeps happening to me today..."
    pslow "I'm sorry Helga, it's just..."
    show phoebe grin with dissolve
    pslow "It's normal to feel this way."
    hslow "I figured as much..."
    hslow "I just thought I'd be more ready for this when it finally happened."
    hslow "But I'm kind of pathetic."
    show phoebe smile with dissolve
    pslow "Arnold wants to be here with you..."
    pslow "Just relax."
    pslow "You'll feel better soon, okay?"
    hide phoebe smile with dissolve
    h "I nod my head and take a deep breath in..."
    h "Hoping the extra air would calm my nervous..."
    show arnold simple with dissolve
    aslow "Okay so we talked it over..."
    h "Arnold suddenly speaks, surprising me."
    h "Where did he come from?"
    show arnold yeah with dissolve                                                         
    stop music fadeout 3.0
    h "But with a smile he places my food in front of me..."
    h "And all is forgiven."        
    play music "Jim Lang - Groove Remote (LockJaw).mp3"  
    if fight:  
        h "And then..."
        hslow "Oh...it's Lila."
        hslow "I'm gonna go over and say hi."
        show arnold surprise at left with dissolve
        show phoebe question at right with dissolve
        aslow "What?"
        pslow "Certainly you're joking..."
        hide arnold surprise with dissolve
        hide phoebe question with dissolve
        show gerald wtf with dissolve
        gslow "Even I know that's not right."
        hide gerald wtf with dissolve
        hslow "...Uh, well...she's not so bad..."
        h "Still all I was getting was blank stares."
        hslow "I'll be right back."
        scene festival night
        with dissolve
        h "With a small wave I grabbed her attention and made my way over."
        show lila glad with dissolve
        lslow "Oh, hello there Helga!"
        hslow "Hey, so you came too, huh?"
        lslow "Well of course, I do so enjoy the festival!"
        hslow "Yeah, it's..."
        h "I look over my shoulder towards Arnold."
        hslow "...Not so bad."
        hslow "Do you wanna come hang with us or...?"
        show lila grin with dissolve
        lslow "Oh, as much as I would like to I'm here with someone."
        hslow "Really?"
        show lila big blush with dissolve
        lslow "Yes, eheheh~ It's a boy named George from a school downtown..."
        lslow "He's quite charming."
        hslow "Haha~ well have fun."
        show lila glad with dissolve
        lslow "You too, Helga."
        h "And off she went."
        scene food court
        with dissolve
        h "As I sat back down at our table..."
        h "The blank stares didn't fade."
        show arnold turn simple with dissolve
        aslow "Anyway..."
        h "Apparently no one was even going to ask..."
        h "It was probably better that way."
    else:    
        show arnold simple with dissolve
        aslow "So we were talking..."                                  
    aslow "Figured we start over at the game booths first..."
    if soup:
        show arnold yeah with dissolve
        h "He stole a chip from my plate..."
        h "That was a lot easier to deal with than what happened before..."      
    show arnold yeah at left with dissolve    
    show phoebe smile at right with dissolve    
    pslow "Fine with me."
    hide phoebe smile at right with dissolve
    show gerald happy at right with dissolve
    gslow "Gonna try to go for that top prize?"
    aslow "Of course, if not...why even try?"
    gslow "Let's put a little wager on this then..."
    h "I looked between the two of them..."
    h "It was like Phoebe and I weren't even here."
    show arnold turn unsure with dissolve
    aslow "A bet? I dunno..."
    gslow "Come on man, don't wimp out."
    show arnold sneaky with dissolve
    aslow "Fine, fine what are your terms?"
    gslow "Winner buys everything for the group for the rest of the night..."
    aslow "..."
    hide gerald happy with dissolve
    show arnold okay at center with dissolve
    h "He looked over at me as if I was supposed to tell him to do to."
    h "So I went with my gut..."
    hslow "I say go for it, Football Head..."
    show arnold yeah with dissolve
    h "He smiled and nodded his head."
    aslow "All right, you're on."
    scene start
    with dissolve
    h "..."
    h "......"
    scene festival night
    with dissolve
    h "I was starting to regret telling Arnold to go for that stupid bet."
    h "It was my fifth consecutive loss at the water gun target game when I finally gave up..."
    h "Some snot nose brat kept winning..."
    hslow "No more..."
    h "I walk away from the booth and look over at Arnold a few games down..."
    h "He and Gerald were immersed in a game of darts..."
    hslow "I didn't know it was going to be like this..."
    show phoebe question with dissolve
    pslow "Be like what?"
    h "Phoebe walks up beside me and pockets a little doll."
    h "Instead of answering her, I change the subject."
    hslow "Where did you get that?"
    show phoebe hehe with dissolve
    pslow "Well...I paid the vendor five dollars for it."
    hslow "...Nice."
    pslow "I couldn't help it, it's just so cute."
    hslow "Right, okay, okay."
    pslow "..."
    show phoebe question with dissolve
    pslow "So are you going to answer my question now?"
    h "I slump forward."
    hslow "This is just like every other Festival, Phoebe!"
    hslow "With us over here...and them over there."
    h "I threw my arms up in defeat and nearly collapsed on a park bench."
    h "Phoebe sat down beside me, quiet as she thought."
    show phoebe sad with dissolve
    pslow "Then we'll just go over, okay?"
    hslow "No...maybe..."
    hslow "Maybe I just got my hopes up...and this isn't as important..."
    hide phoebe sad with dissolve
    show arnold grin with dissolve     
    stop music
    aslow "Helga!" 
    h "Suddenly Arnold calls my name, running over towards us, completely pulling me from my thoughts."
    hslow "What's wrong?"
    aslow "What? Wrong? Nothing's wrong!"
    h "He laughed."                              
    play music "Jim Lang - Helga's True Love.mp3"
    h "It was then I noticed the rather large prize he had in his hands."
    show arnold sneaky with dissolve
    aslow "I got him beat by just a few points."
    show arnold grin with dissolve
    aslow "So here!"
    h "He holds it out for me, and I'm not exactly sure what he wants me to do with it."
    h "Is he...giving this to me?"
    hslow "Uh...what?"
    hide arnold grin with dissolve 
    show gerald happy at left with dissolve
    show phoebe grin at right with dissolve
    gslow "What, did you think we were gonna play that game all this time and not get you guys something?"
    h "He pulls Phoebe beside him and hands her a tiny blue snow globe."
    pslow "Oh! Thank you!"
    gslow "No problem."
    h "She examines the little novelty for a minute before slipping it inside her purse for safe keeping."
    hide gerald happy with dissolve
    hide phoebe grin with dissolve
    h "The prize that I assumed was meant for me...well..."
    h "It wasn't going to fit in my bag, that was for sure."
    scene CG46 with dissolve
    h "He held in his hands a pink rabbit with a rather large bow sitting atop its head."
    h "I stare at it for another moment before looking back up at him."
    hslow "Why...this?"
    h "I couldn't think of anything else to say."
    aslow "Well it kind of looks like you, doesn't it?"
    hslow "Uh....what?"
    h "I stare at him, as if I heard him wrong."
    h "To my stare he shyly tries to laugh it off..."
    aslow "What? Don't give me that face it does look like you."
    aslow "It's got the bow and everything."
    h "I feel a steady heat rise to my cheeks before I snatch the damn thing away."
    h "I hold it tightly to my chest and turn away from all the people smiling at me..."
    h "I couldn't take it."
    scene festival night
    with dissolve
    h "So I point towards the rides, hoping the topsy-turvy feelings of a fast ride would get off my mind..."
    h "Just how amazing Arnold is."
    h "..."
    h "......"
    h "After riding some of the bigger, faster rides with Nibbles in tow..."
    h "Yes...I named the stupid thing..."
    h "Without telling anybody of course..."
    h "Arnold suggested..."
    show arnold simple with dissolve
    aslow "I say we end the night on the Ferris Wheel."
    h "He points up to the Festival's biggest attraction, and from way down here..."
    h "It looked like the giant wheel almost touched the moon."
    hide arnold simple with dissolve
    show gerald happy at left with dissolve
    show phoebe smile at right with dissolve
    gslow "Sounds good to me."
    pslow "Very romantic."
    h "To be honest I was glad it wasn't the Tunnel of Love..."
    h "That might have been a bit too much to take."
    h "So the two love birds, so used to one another by now head for the line."
    hide gerald happy with dissolve
    hide phoebe smile with dissolve
    h "Leaving Arnold and myself alone..."
    show arnold yeah with dissolve
    aslow "Come on."
    hslow "Right."
    h "He moves towards the ride and I follow behind, finding my legs hard to move."
    hide arnold yeah with dissolve
    h "This was going to be the {i}alone time{/i} wasn't it?"
    h "Could I handle this?"
    h "..."
    scene Ferris Wheel
    with dissolve
    h "When we reach the car, Arnold enters first, and I follow..."
    h "Except..."                  
    with hpunch
    h "My stupid shoe gets caught in the door and I nearly fall in."
    h "So apparently, I can't handle this."
    h "But Arnold grabs my arms before I fall face first between the Ferris Wheel seats."
    show arnold yeah with dissolve      
    aslow "It's okay I got you."              
    hslow "Yeah, thanks."
    h "I slowly move out of his grasp and take the seat across from him, my heart racing in my chest."
    h "The door closes behind us and then the car makes a quick move, rising off the ground."
    h "For a moment we're both silence, looking out the window to the city below..."
    h "It could have been magic if I believed in things like that..."
    h "..."    
    show arnold turn unsure with dissolve
    aslow "So..."
    h "Suddenly Arnold speaks, breaking me from my thoughts."
    hslow "Huh? Uh, yeah? What's up?"
    aslow "I was going to ask if you were having a good time but..."
    hslow "No, No I am...it's just..."
    hslow "Uh..."
    show arnold sad smile with dissolve
    aslow "..."
    hslow "You make me kinda nervous, all right?"
    show arnold calm with dissolve
    aslow "Really? Why?" 
    h "{i}Why?{/i} Is he for real right now?"
    hslow "Because I..."
    h "I said it so quietly, he didn't even hear me."
    show arnold simple with dissolve
    aslow "You've been pretty okay with me over the last few days..."
    if fight:                                                                               
        aslow "Even if we did fight..."
        hslow "Yeah, don't remind me..."
    aslow "That's why I asked you out in the first place."
    hslow "B-but this isn't us just hanging out."
    show arnold turn simple with dissolve
    aslow "It's not?"
    hslow "It's a date...right?"
    h "Arnold slowly nods his head, then gives me a small smirk."
    show arnold calm with dissolve
    aslow "I don't mind taking you out more."
    aslow "If only to help you get more comfortable with me."
    h "I roll my eyes."
    hslow "That isn't funny."
    hslow "I'm trying to be serious, so don't joke with me."
    show arnold yeah with dissolve
    aslow "Who's joking?"
    aslow "I'm being completely serious too, Helga."
    h "I stare him down but he doesn't falter."
    h "So I give him a quick shrug of my shoulders."
    hslow "I dunno, I think you like to tease me almost as much as I like to tease you."
    stop music fadeout 3.0
    show arnold sneaky with dissolve
    aslow "Well that's true..."
    hslow "Hmph!"
    show arnold calm with dissolve 
    play music "Jim Lang - The Kids Finally Get It.mp3"               
    aslow "But I'm being honest."       
    h "He suddenly grabs my hand, his touch...so warm."
    show arnold yeah blush with dissolve
    aslow "I...really like you, Helga."
    aslow "I think we should be together."
    h "..."
    h "......"
    h "I blink a few times, making sure I heard him right..."
    hslow "Are you seri..."
    scene start
    with dissolve
    h "But before I can finish, Arnold leans in for a quick kiss."
    h "It must have only been a few seconds but..."
    h "This time I did believe in magic."
    h "..."
    scene CG51
    with dissolve
    h "As he pulls away I let out a quiet thank you, with out meaning too..."
    h "To which he replies an equally quiet..."
    aslow "You're welcome."                        
    h "For a moment there is nothing but the silence..."
    h "The far away sounds of the city and the Festival below..."
    h "And then..."
    h "Without a reason why..."
    h "We start to laugh..."
    hslow "..."
    aslow "..."
    aslow "Happy Cheese Festival, Helga..."
    hslow "Happy Cheese Festival, Arnold..."
    call end_true  

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
