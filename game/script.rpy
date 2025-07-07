# You can place the script of your game in this file.

# Declare images below this line, using the image statement.

# BACKGROUNDS
image bg city park evening = "BG Park Evening.png"
image bg city park day = "BG Park Day.png"
image bg city park night = "BG Park Night.png"
image bg helga house day = "BG helga houseday.png"
image bg helga house night rain = "BG helga houserain.png"
image bg helga house evening = "BG helga houseevening.png"
image helga house night = "BG helga housenight.png"
image bg arnold house = "BG arnold house.png"
image bg city day = "BG City Day.png"
image bg city evening = "BG City Evening.png"
image bg arnold room = "BG arnold room.png"
image helga room day = "BG helga room day.png"
image helga room day rain = "BG helga room day rain.png"
image helga room evening = "BG helga room evening.png"
image helga room night = "BG helga room night.png"
image helga room night rain = "BG helga room night rain.png"
image record shack = "BG record shack.png"
image cafeteria = "BG Cafeteria.png"
image cafeteria doors = "BG Cafeteria Doors.png"
image festival night = "BG Festival Grounds Night.png"
image festival day = "BG Festival Grounds Day.png"
image festival pday = "BG Festival Grounds Perfect Night.png"
image school hallway = "BG Hallway.png"
image school = "BG school.png"
image chez paris inside = "BG Chez Paris.png"
image classroom = "BG Classroom.png"
image sky = "BG Sky.png"
image food court = "BG food court.png"
image food court night = "BG food court night.png"
image Inside House = "BG Helga Inside House.png"
image Ferris Wheel = "BG Ferris Wheel.png"
image Resturant = "BG Resturant.png"
image Resturant Rain = "BG Resturant Rain.png"
image Tunnel of Love = "BG Tunnel of Love.png"
image Tunnel of Love Night = "BG Tunnel of Love Night.png"
image start = "start.png"    

image splash one = "firstimage.png"
image splash two = "second image.png"
image opening pic = "splashscreen.png"
image main = "menu.jpg"
image maintwo = "menu2.jpg"

image slideshow:
    "menu.jpg" with dissolve
    pause 2.0
    "menu2.jpg" with dissolve
    pause 2.0
    repeat
image SPLASH: 
    "start.png" with fade
    pause 0.5
    "splashscreen.png" with dissolve
    pause 4.0
    "start.png" with fade
    pause 2.0

#CGs
image CG1 = "CG1.png"
image CG2 = "CG2.png"
image CG3 = "CG3.png"
image CG4 = "CG4.png"
image CG5 = "CG5.png"
image CG6 = "CG6.png"
image CG7 = "CG7.png"

#Arnold Expressions Go Here
image arnold simple = "Arnold 1.png"
image arnold grin = "Arnold 2.png"
image arnold frown = "Arnold 3.png"
image arnold sad smile = "Arnold 4.png"
image arnold surprise = "Arnold 5.png"
image arnold big blush = "Arnold 6.png"
image arnold small blush = "Arnold 7.png"
image arnold snarky 1 = "Arnold 8.png"
image arnold sneaky = "Arnold 9.png"
image arnold pissed = "Arnold 10.png"
image arnold laugh = "Arnold 11.png"
image arnold sad calm = "Arnold 12.png"
image arnold happy calm = "Arnold 13.png"
image arnold bored = "Arnold 14.png"
image arnold yeah = "Arnold 15.png"
image arnold calm = "Arnold 16.png"
image arnold shy = "Arnold 17.png"
image arnold flustered = "Arnold 18.png"
image arnold hehe = "Arnold 19.png"
image arnold yeah blush = "Arnold 20.png"
image arnold simple blush = "Arnold 21.png"
image arnold pissed 1 = "Arnold 74.png"
image arnold okay = "74.png"
image arnold pissed 2 = "73.png"
image arnold turn simple = "Arnold 22.png"
image arnold turn surprise = "Arnold 23.png"
image arnold turn sad = "Arnold 24.png"
image arnold turn angry = "Arnold 25.png"
image arnold turn unsure = "Arnold 26.png"
image arnold turn calm = "Arnold 27.png"
image arnold turn shy = "Arnold 28.png"
image arnold turn fluster = "Arnold 29.png"
image arnold turn shock = "Arnold 30.png"
image arnold turn okay = "Arnold 31.png"

#Phoebe Expressions
image phoebe grin = "Phoebe 1.png"
image phoebe question = "Phoebe 2.png"
image phoebe smile = "Phoebe 3.png"
image phoebe sad = "Phoebe 4.png"
image phoebe mad = "Phoebe 5.png"
image phoebe plot = "Phoebe 6.png"
image phoebe laugh = "Phoebe 7.png"
image phoebe hehe = "Phoebe 8.png"
image phoebe pissy = "Phoebe 9.png"
image phoebe blush = "Phoebe 10.png"
image phoebe big grin = "Phoebe 11.png"
image phoebe unsure = "Phoebe 12.png"
image phoebe surprise = "Phoebe 13.png"

#Gerald Expressions
image gerald wtf = "Gerald 1.png"
image gerald sad = "Gerald 2.png"
image gerald happy = "Gerald 3.png"
image gerald pissed = "Gerald 4.png"
image gerald unsure = "Gerald 5.png"
image gerald calm = "Gerald 6.png"

#Lila Expressions
image lila ticked = "Lila 1.png"
image lila sympathy = "Lila 2.png"
image lila sad = "Lila 3.png"
image lila glad = "Lila 4.png"
image lila grin = "Lila 5.png"
image lila big blush = "Lila 6.png"
image lila shy = "Lila 7.png"
image lila pissed = "Lila 8.png"

#Day Images Go Here
image day one = "dayone1.png"
image day one2 = "dayone2.png"
image day one3 = "dayone3.png"
init:
# Declare characters used by this game.
# Slow text.
    $ hslow = Character("Helga",
                        color="#F9B7FF",
                        what_slow_cps=30,
                        font="RONDALO_.TTF")
                        
    $ pslow = Character('Phoebe', color="#F9B7FF", what_slow_cps=24, font="RONDALO_.TTF", size= 29)
    $ aslow = Character('Arnold', color="#F9B7FF", what_slow_cps=24, font="RONDALO_.TTF", size= 29)
    $ gslow = Character('Gerald', color="#F9B7FF", what_slow_cps=24, font="RONDALO_.TTF", size= 29)
    $ lslow = Character('Lila', color="#F9B7FF", what_slow_cps=24, font="RONDALO_.TTF", size= 29)
    $ h = Character(None, what_slow_cps=24, what_italic=True)
# The game starts here.
label splashscreen:
    scene black
    with fade
    $ renpy.pause(0.5, hard=True)
   
    show opening pic
    with dissolve
    $ renpy.pause(5.0, hard=True)
    
    scene black
    with dissolve
    $ renpy.pause(1.0, hard=True)
    return
label start:
    
     scene start
     with fade
     stop music fadeout 2.0
     scene black 
     with fade
     $ renpy.pause(0.5, hard=True)
    
     show splash one 
     with dissolve
     $ renpy.pause(2.0, hard=True)
    
     scene black 
     with fade
     $ renpy.pause(0.5, hard=True)
     
     show splash two
     with dissolve
     $ renpy.pause(2.0, hard=True)
     
     scene black 
     with fade
     $ renpy.pause(0.5, hard=True)
     scene start
     with fade
     window show
     with dissolve 
    
     $ GeraldSpills = False
     $ Festival = False
     $ Class = False
     $ Sorry = False
     $ Good = False
     $ PerfectDay = False
     $ Perfect_1 = False
     $ Perfect_2 = False
     $ Perfect_3 = False
     $ Perfect_4 = False
     $ Perfect_5 = False
     $ True_1 = False
     $ True_2 = False
     $ True_3 = False
     $ True_4 = False
     $ soup = False
     $ skipped = False
     $ poem = False
     $ fight = False
     $ funny = False
     $ almost = False
     $ IMGOING = False
     $ Maybe = False
     $ Waited = False
     $ imwrong = False
     play music "Jim Lang - Operation Ruthless End.mp3"    
     h "So, let's just start off by saying Cheese Festivals never, ever worked out in my favor..."
     scene CG1
     with dissolve
     h "I can remember..."
     h "There were two of them when I was nine-years-old and both of them ended up with me..."
     h "Well, how do they put it..."
     scene CG2
     with dissolve
     h "Forever alone." 
     h "And now..."
     h "It was that time of year again."  
     scene CG3
     with dissolve
     h "Hillwood was going to have another one."
     h "And I wasn't looking forward to it."
     h "Because I knew it would be filled with people who were happier than me."
     h "They would be having a good time, laughing...enjoying their lives."
     h "Their loves..."
     h "And the one thing that made me truly happy..."
     h "Well it made me so miserable every time the Festival came to town."
     h "I hate that."
     stop music fadeout 3.0
     scene start
     with dissolve
     h "It really pisses me off..."
     h "..."
     h "......"
     play music "Jim Lang - Home Wit Jerome.mp3"
     h "This all began on a morning pretty much exactly like any other."
     h "It started with me wondering if I should bother to tell my mother I was leaving for school."
     scene bg helga house day
     with dissolve
     hslow "Not that you can hear me passed out on the kitchen table... Criminy!"
     hslow "Oh, morning Pheebs..."
     show phoebe smile
     with dissolve
     h "Phoebe's my best friend."
     h "And a damn good assistant."
     h "But of course she's mostly my friend."
     pslow "Good morning Helga, how are you today?"
     hslow "Oh you know, same ol', same ol'..."
     h "I was lying..."
     h "I was much worse."
     show phoebe grin
     with dissolve
     pslow "That's good to hear!"
     hslow "Jeez, feeling perky, Phoebe?" 
     show phoebe hehe
     with dissolve
     pslow "Of course! Since the Cheese Festival is only a few days away now and..."
     h "Phoebe's grinning like an idiot, talking about that damn Festival."
     h "I can't even imagine myself having a good time."
     h "So I snap at her..."
     h "I just can't help myself."
     hslow "Blah, blah, blah..."
     hslow "That stupid festival never changes."
     hslow "It's the same damn carnival every year."
     hslow "Big freaking deal..."
     h "I continue to mumble quiet profanities under my breath."
     show phoebe question
     with dissolve
     h "Ever since a few years back, whenever they started dating, Phoebe and her boyfriend Gerald were like the \"it\" couple."
     h "He was cool, and she was smart and they just worked out perfectly...I guess..."
     h "..."
     h "I'll never, ever tell her I'm {i}slightly{/i} jealous."
     pslow "Why so down Helga? Don't you find the fair fun anymore?"
     hslow "Phoebe, how can you not remember..."
     h "Then again, why would she? She always ended up not feeling like a miserable failure by the end of it."
     h "Unlike me..."
     hslow "Never mind, I'm just being negative...or whatever."
     h "Negative? Hah. That's a word for it."
     show phoebe sad
     with dissolve
     pslow "If you say so." 
     hslow "I do say so!"
     hslow "And while we're on the topic of the Festival..."
     pslow "Yes?"
     hslow "There's no way I'm going this year."
     h "Phoebe frowns deeper..."
     pslow "But why not Helga?"
     pslow "Even if you've had a bad time before..."
     show phoebe question
     with dissolve
     h "I cut her off before she can go on."
     hslow "Give it a break Phoebe, criminy..."
     hslow "Why do you even care?"
     show phoebe sad
     with dissolve
     pslow "It's just..."
     h "She shakes her head, like she's clearing her thoughts. She seems ready to give me some type of lecture."
     pslow "It seems to me..."
     pslow "Maybe if you tried to focus on something other than...uh..."
     show phoebe unsure
     with dissolve
     pslow "...You-know-who..."
     show phoebe smile
     with dissolve
     pslow "You might be able to enjoy yourself more..." 
     h "I nod my head slowly, taking it all in."
     h "Just kidding."
     h "I had heard this all before, multiple times in fact."
     hslow "..."
     hide phoebe smile
     with dissolve
     scene bg city day
     with dissolve
     h "Even if I sat her down to explain the insanity of my emotions..."
     h "She just couldn't understand how hard that was for me, to put him aside."
     h "She would never understand how most of the time he felt like the only good part in my whole life..."
     h "The light in my otherwise bleak existence."
     h "But at the very same time, that damn Football Head could ruin me with a smile..."
     h "Especially if that smile was aimed at someone other than me."
     h "And almost always, it was."
     hslow "You don't get it."
     pslow "What?"
     hslow "It's not that easy..."
     show phoebe sad
     with dissolve
     pslow "Helga..."
     hslow "Ugh, don't pity me Phoebe."
     show phoebe sad
     with dissolve
     h "My warning didn't matter, she gives me a pitiful look anyway."
     hslow "I'm used to it now."
     hslow "I know..."
     stop music
     scene CG4
     play sound "Right Cross-SoundBible.com-1721311663.wav"
     with hpunch
     h "CRASH!!"
     play sound "Helga Interrupts.mp3"
     scene CG5 with dissolve
     hslow "Arnold!"
     window show
     aslow "Helga!"
     scene CG6 with dissolve
     aslow "We've got to stop bumping into each other like this! Haha!"
     scene CG7 with dissolve
     menu:
        hslow "Uh...well..."

        "Got that right!":
         
        
            jump GoodGoing
            
        "No, it's fine.":
         
        
            call OuchWrong

label GoodGoing:
    $ Perfect_1 = True
    $ renpy.block_rollback()
    play music "Jim Lang - Back To School.mp3"
    hslow "Got that right, Football Head, one of these days I might actually hurt you!"
    h "Whew~"
    scene bg city day with dissolve
    show arnold sad smile
    with dissolve
    aslow "Right Helga, whatever you say."
    show arnold turn unsure
    with dissolve
    aslow "Well anyway..."
    h "He looks around, kind of nervously."
    aslow "Do you mind if I walk with you guys the rest of the way?"
    show arnold turn unsure at left
    with dissolve 
    show phoebe question at right
    with dissolve 
    pslow "I've no issue with that..."
    pslow "Helga?"
    h "Remain calm...calm...calm..."
    hslow "Whatever floats your boat."
    h "Why is my heart pounding like this?"
    h "Why does he do this to me?!"
    show arnold simple 
    with dissolve
    aslow "Cool, thanks."
    h "..."
    h "......"
    show phoebe grin
    with dissolve
    pslow "So Arnold..."
    h "Phoebe's voice breaks through the silence."
    h "Thank God."
    pslow "Plan to do anything fun this weekend?"
    show arnold sad smile
    with dissolve
    aslow "Oh, wow..."
    aslow "Phoebe are you asking me to the Cheese Festival?" 
    aslow "I really don't think Gerald will be happy about that..."
    show phoebe surprise
    with dissolve
    pslow "Goodness!"
    pslow "By no means was I implying that...I mean...no!"
    h "Phoebe looks as if her head is about to explode."
    show arnold laugh
    with dissolve
    aslow "Haha, calm down I'm only teasing..."
    show arnold turn unsure
    with dissolve
    aslow "To be honest, I don't know if I'm going this year."
    h "He gives an uneasy shrug of his shoulders."
    aslow "They haven't been all that great for me in the past."
    show phoebe question
    with dissolve
    hslow "I know that feeling..."
    h "...!"
    h "I didn't mean to say that out loud!"
    hide phoebe question
    with dissolve
    show arnold surprise at center
    with dissolve
    aslow "Really Helga?"
    hslow "What?"
    h "Why did he have the hear me?"
    h "Why?"
    show arnold frown
    with dissolve
    aslow "You haven't had a good time with the Festivals either?"
    hslow "I didn't say that..."
    show arnold turn unsure
    with dissolve
    aslow "No, you did, you just said..."
    hslow "It doesn't matter what I said, hey look!"
    h "I point out the looming, big, brown building."
    scene school
    with dissolve
    hslow "It's the school!"
    show arnold turn unsure at left
    with dissolve
    show phoebe grin at right
    with dissolve
    pslow "Anyway the festival..."
    h "Phoebe tries to pull his attention away from me..."
    h "I suppose my showing him where the school was...wasn't good enough."
    pslow "It's on Saturday. Can you believe it?"
    show arnold turn surprise
    with dissolve
    aslow "Wow, only three more days?"
    hslow "Whoopee~"
    h "..."
    h "That they decide to ignore."
    show arnold turn angry
    with dissolve
    h "Suddenly Arnold turns towards the school."
    aslow "Ugh..."
    aslow "I gotta rush...my class is all the way on the other side of the building."
    show arnold simple
    with dissolve
    aslow "Well, I'll see you guys later!"
    hide arnold simple
    with dissolve
    show phoebe smile at center
    with dissolve
    h "There walks the love of my life..."
    h "Completely oblivious as always."
label Ditching:  
    scene school
    with dissolve
    h "..."
    h "......"
    h "As we get closer to the entrance of the school, I notice I start to slow down..."
    hslow "I really don't wanna be here right now..."
    h "I stop completely, finding a stone on the sidewalk more interesting then moving on."
    hslow "Phoebe, I think I'm just gonna skip class..."
    stop music fadeout 3.0
    show phoebe sad
    with dissolve
    pslow "Helga that's not wise..."
    menu:
        hslow "I know but..."

        "Okay, you're right...":
        
            call OuchWrong2
            
        "I'll be back later.":
        
            jump GoodGoing2

label GoodGoing2:
    $ Perfect_5 = True
    $ renpy.block_rollback()
    hslow "I promise I'll be back before the afternoon classes start..."
    play music "Jim Lang - Thinkin' It Over.mp3"
    hslow "I just gotta..."
    h "I want to give her a valid excuse, something better than...than..."
    hslow "Think or something..."
    h "Better than that."
    pslow "Well, okay. I'll take notes for you."
    hslow "Thanks..." 
    h "It's all I could think to say."
    pslow "Bye-bye."
    hide phoebe sad
    with dissolve
    h "I turn and leave without a word and, somehow, after a long while of aimlessly walking..."
    scene festival day
    with dissolve
    h "I end up at the festival grounds."
    h "The whole place looks like some type of horror movie in the making."
    h "It was completely abandoned...I guess the guys who were suppose to set it up were on break."
    h "I took a look around anyway..."
    h "The only thing this place brought up in me was bad memories."
    h "It was like I could see every unsuccessful scheme flash before my eyes."
    hslow "Ugh, my plans never go right!"
    h "I felt like the best thing to do at this point was to fall down, maybe curl up and sleep."
    h "Was there even a point to evil plans and plots anymore?"
    h "Even if I ruined Arnold's time, he always ended up kind of, sort of happy in the end."
    h "That beautiful, damn-it-all, always looking on the bright side attitude."
    stop music fadeout 3.0
    h "And that's when it hit me...I should get to him before he even has a chance to ask someone else."
    play music "Jim Lang - Helga Confession Blowout.mp3"
    h "I should just get him to bring me!"
    hslow "That's it!" 
    h "The real question though, was how..."
    h "It's obvious that by now, after all these years, Arnold isn't exactly used to a nice, ask-this-girl-out-right-now, type of personality from me..."
    h "But I could try, couldn't I? To be just a little nicer to him, a little kinder..."
    h "It wasn't that much of a stretch."
    h "Could he be swayed?"
    h "Could I...his one true love...finally win his heart?!"
    h "This would have to be handled delicately, any wrong choice could completely botch things up."
    h "Without another thought I turn around and head back towards the school..."
    h "This time I was going to be successful! I was sure of it..."
    hslow "Hegla G. Pataki, Saturday night is gonna be your night ol' girl!" 
label FIRSTDAY:    
    window hide dissolve
    stop music fadeout 1.0
    scene start 
    with fade
label FIRSTTITLE:    
    scene black 
    $ renpy.pause(0.5, hard=True)
    with fade
    
    show day one
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show day one2
    with dissolve 
    $ renpy.pause(3.0, hard=True)
    
    scene black 
    with dissolve
    $ renpy.pause(0.2, hard=True)
    scene cafeteria doors
    with fade
    window show
    if Perfect_5:
        h "I somehow make it back just in time for lunch and catch Arnold standing on line for food..."
    if True_2:
        h "Lunch came quicker than I expected it too..."
        h "And I catch Arnold on the food line."
    h "Without really thinking on it..."    
    h "I casually cut the person standing behind him and take his spot."
    menu:
        h "But what do I do?..."

        "Say something to him...":
        
            jump GoodGoing3
            
        "Wait to be greeted...":
        
            call OuchWrong3
            
label GoodGoing3:
    $ Perfect_2 = True
    $ renpy.block_rollback()
    play music "Jim Lang - Groove Remote (LockJaw).mp3"
    hslow "Hey Arnoldo, how's it hanging?"
    show arnold grin
    with dissolve
    aslow "Oh, hey Helga..."
    show arnold calm
    with dissolve
label WHEREUAT:    
    if Perfect_5:
        aslow "I didn't see you in class..."
        hslow "Nope, I skipped."
        aslow "Oh yeah? Any reason?"
        hslow "I just needed some time to think is all..."
        h "That excuse seems to be working for me today."
        hslow "Nothing to worry your handsome Football Head about..."
        show arnold turn okay
        with dissolve
        h "...!"
        h "Did I really say that out loud and the world didn't explode?"
        aslow "..."
        aslow "......."
        h "Why isn't he saying anything!?"
        aslow "..."
        show arnold yeah
        with dissolve
        aslow "Well that's good, you were missed."
        h "He must think that I'm trying to tease him."
        h "I'm not sure if that's a good thing or a bad thing."
        h "..."
        hslow "Oh was I now? Did you miss me Arnold?"
        show arnold sneaky
        with dissolve
        aslow "Yeah, I missed you kicking the back of my chair, Helga..."
        aslow "I've learned I can't live without it..."
        h "Is this flirting...or is he making fun of me?"
        h "Or is it both.......?"
        hslow "Good to know, I'll kick it extra hard tomorrow."
        hslow "Just for you!"
        h "Heh. I can do it too!"
        show arnold yeah
        with dissolve
        aslow "Great, hah, it's a date." 
    if True_2:
        aslow "How's your day so far?"
        hslow "You ask me like you weren't there for some of it..."
        show arnold sad smile
        with dissolve
        aslow "Haha, yeah, that's true."
        aslow "I'm gonna take a wild guess here and say, \"boring\"?"
        hslow "Ding-ding-ding...you win a prize."
        h "My voice is rather sarcastic...but he keeps smiling at me."
        show arnold sneaky
        with dissolve
        aslow "Yeah? Anything good?"
        hslow "Uh..."
        h "I grab a cookie from the desert tray and pay the lunch lady what I owe her."
        hslow "Enjoy."
        show arnold surprise
        with dissolve
        aslow "Seriously?"
        hslow "You should honored by my kindness..."
        aslow "Oh, trust me I am."        
    hide arnold surprise
    with dissolve
    if True_3:
        call GROUPLUNCH
label CORRECT:    
    scene cafeteria 
    with dissolve
    h "We pick up our trays and walk into the cafeteria..."
    h "On a typical day, this is when we'd walk our separate ways, to sit with our own cliques."
    h "But..."
    show arnold turn okay
    with dissolve
    h "Is Arnold hesitating?"
    show arnold turn shy
    with dissolve
    aslow "Looks like Gerald and Phoebe are eating together today..."
    hslow "Yeah looks like it..."
    h "This wasn't unusual. They ate together often enough..."
    h "So why was Arnold suddenly making such a big deal of it?"
    show arnold yeah blush 
    with dissolve
    aslow "..."
    aslow "You wanna grab a table over there or something?" 
    h "He motions vaguely with his shoulder to a table off in the back."
    h "For a moment, I'm speechless." 
    h "How do I respond to this?"
    h "This is what I wanted, isn't it?"
    h "I can't screw this up!"
    hslow "Sure, that sounds..."
    hslow "..."
    h "Say something you moron, use your words! You're good at words!!"
    hslow "Super..."
    show arnold simple
    with dissolve
    h "God, I can't believe I just said that..."
    hide arnold simple
    with dissolve
    h "Luckily, Arnold just nodded at my verbal nonsense...{i}SUPER{/i}... And made his way to a table near the windows."
    h "..."
    h "At first I thought things were going to be awkward and quiet between us..."
    show arnold calm 
    with dissolve
    h "But Arnold started talking with me so easily, it felt like we had been alone like this all the time."
    h "And for a moment I thought that this might really work out for me, just this once..."
    h "That was until she showed up."
    show arnold yeah 
    with dissolve
    aslow "Oh, hey Lila."
    show arnold yeah at left
    with dissolve
    show lila grin at right
    with dissolve
    lslow "Hello Arnold! Oh, and it seems you're eating with Helga today? I think that's ever so sweet!"
    hslow "Well it was..."
    h "I couldn't help the pout that made its way to my face."
    show arnold pissed
    with dissolve
    aslow "Come on Helga, don't be rude..."
    show lila sympathy
    with dissolve
    hslow "Who's being rude? You're used to me by now, aren't you Liiiiiila?" 
    show lila grin
    with dissolve
    lslow "Why, of course Helga! We're like old friends!" 
    hslow "Heh...riiiiiiight."
    aslow "Anyway..."
    h "I could hear a slight gruffness in his voice."
    h "It was a familiar tone, currently, and usually meant for me."
    show arnold simple
    with dissolve
    aslow "Why don't you join us?"
    show lila big blush
    with dissolve
    lslow "That sounds ever so nice Arnold, thank you..."
    h "I don't even let her finish as I make a move to stand up, picking up my tray as I do so."
    hslow "You know, I'm not feeling so hungry anymore..."
    h "I turn towards the garbage and dump the remainders of my lunch in."
    hide lila sad 
    with dissolve
    show arnold frown at center
    with dissolve
    hslow "I'll see you in class Arnold."
    aslow "Huh? Helga wait..."
    hide arnold frown
    with dissolve
    hide lila sad
    with dissolve
    aslow "Helga!"
    h "I hear him call out to me again but I ignore him."
    h "Even if he didn't have those types of feelings for her anymore..."
    h "Even if there was the smallest chance he maybe, possibly, could have feelings for me..."
    h "The fact that he asked her to sit with us..."
    stop music fadeout 3.0
    h "Well it made me want to pull my hair out!"
    scene school hallway
    with dissolve
    h "..."
    h "......"
    h "Yet the further away I walk from the cafeteria the more I realize being a bitch to Arnold's friends isn't going to get me on his good side..."
    h "I stop for a minute and lean against the wall."
    h "What were my choices here?"
    menu: 
        h "I could either..."
           
        "Go and apologize...":
        
            jump Apologize
            
        "Find him later...":
        
            jump GoodGoing5
label Apologize:
    $ renpy.block_rollback()
    h "As I turn to go back I see Arnold making his way towards me..."
    play music "Jim Lang - Helga and Arnold Make Up.mp3"
    hslow "Arnold?"
    show arnold frown
    with dissolve
    aslow "Helga, there you are..."
    h "He seems slightly out of breath, like he had been running."
    h "But the trek here from the cafeteria isn't that much..."
    h "Could he have been worried?"
    aslow "Why'd you leave? We were having lunch together..."
    show arnold turn unsure
    with dissolve
    aslow "Weren't we?"
    hslow "Yeah, we were and I was coming back to say..."
    hslow "...To say..."
    hslow "I'm sorry...!"
    h "I let the words fly out, truthful to the core."
    show arnold surprise
    with dissolve
    aslow "Then why did you...?"
    hslow "It's just you asked Lila to sit with us...a-and we don't get along and..."
    jump Continue    
label GoodGoing5:
    $ renpy.block_rollback()
    h "It's probably best if I wait to talk to him..."
    h "Lila might still be there and..."
    aslow "Helga!"
    play music "Jim Lang - Helga and Arnold Make Up.mp3"
    show arnold frown
    with dissolve
    hslow "A-Arnold!"
    h "I felt my heart race up into my throat."
    hslow "Criminy, Football Head, why you always sneaking up on me?"
    hslow "Wait, wait..."
    hslow "What are you doing here?"    
    show arnold turn unsure
    with dissolve
    aslow "We were having lunch together, weren't we?"
    hslow "Yeah...and then you invited Lila..."
    aslow "That was bad?"
    hslow "Well she and I...we don't really get along and..."
label Continue:
    show arnold sad smile
    with dissolve
    aslow "But Helga...you and I...we don't get along either..."
    hslow "I know, but you're different Arnold!" 
    hslow "~gasp~"
    h "I cover my mouth with my hand as if I could capture my words."
    h "The motion was a little too late..."
    h "I let go a little more then I intended."
    show arnold turn shy
    with dissolve
    aslow "Really...I am?"
    hslow "..."
    hslow "........"
    aslow "Helga?"
    hslow  "Yes..."
    h "Can I just leave it at that?"
    aslow "Yes, what?"
    h "No, apparently not."
    hslow "Yes, really...for cripes sake..."
    aslow "..."
    show arnold turn sad
    with dissolve
    aslow "But why?"
    aslow "..."
    aslow "Why am I..."
    h "It was like it was hard for him to finish it."
    hslow "Ugh..."
    h "It isn't as if I could just come out and say..."
    h "{i}Because you are the light of my life, my love, my heart, my soul...the essence of my eternal bliss.{/i}"
    h "That would be a little much."
    hslow "I...I can't tell you!"
    h "Yeah, that works."
    show arnold surprise
    with dissolve
    aslow "But..."
    hslow "...Yet... I can't tell you yet..."
    h "There would come a day I would admit my deepest secret to the holder of my heart."
    scene CG9
    with dissolve
    aslow "......."
    aslow ".........."
    hslow "What?...!"
    aslow "I feel..."
    scene CG10
    with dissolve
    aslow "Sorry...It's just a bad case of déjà vu."
    hslow "Huh? Déjà vu?"
    aslow "It's-it's nothing, really. I probably just imagined it." 
    hslow "Well okay...but..."
    aslow "Hmm?"
    hslow "Do you get it Football Head?"
    scene school hallway
    with dissolve
    show arnold turn unsure
    with dissolve
    aslow "I guess..."
    aslow "So you will tell me..."
    aslow "Not now...but?"
    hslow "One day...just - not - now!"
    show arnold yeah 
    with dissolve
    aslow "Okay, okay I get it!" 
    play sound "School Bell.wav"
    h "*RIIIIIIIIIING*"
    menu:
        h "Oh damn the bell..."
        "I'll try to stall him.":
            jump stall
        "I'll joke around...":   
            jump joke
label stall:
    $ renpy.block_rollback()
    hslow "Wow, class just snuck up on us huh?"
    show arnold sad smile
    with dissolve
    aslow "Yeah, too bad...I was kind of..."
    gslow "Hey Arnold! Let's go man, we're gonna be late!"
    h "What? Kind of what?"
    show arnold sneaky
    with dissolve
    aslow "Alright I hear you!"
    h "Arnold turns and looks at me again..."
    show arnold yeah
    with dissolve
    aslow "You going my way Helga?"
    h "With his shoulder he motions towards the hallway behind him."
    hslow "Well, looks it looks that way, doesn't it?"
    aslow "Great, I'll walk ya to class."
    hslow "Fine with me, Arnoldo..."
    aslow "Heh..."
    jump continueon
label joke:
    $ renpy.block_rollback()
    hslow "Great, with all that talking we've run out of time to eat Arnoldo!" 
    show arnold calm
    with dissolve
    aslow "Hah, right Helga, it's all my fault."
    hslow "Damn straight!"
    h "I start to move down the hall, grabbing Arnold's shirt sleeve as I do so."
    hslow "Come on, you can walk me to class as atonement for your crimes, haha!"
    show arnold yeah
    with dissolve   
label continueon:    
    aslow "Should I carry your books too?"
    stop music fadeout 3.0
    hslow "Jeez, don't get too mushy Arnold..."
    h "One step at a time or I might die!" 
    hide arnold yeah
    with dissolve
label Home:    
    scene start 
    with dissolve
    scene helga room evening
    h "After a much needed nap..."
    h "I get up from bed, grab my diary, and begin to write in poems, draw random doodles."
    h "And just as the sun was beginning to set over the city...."
    h "I find myself looking away from my work, out the window."
    h "My mind, as always finds Arnold...wondering what my love could be doing right at this moment..."
    h "I look over my mess of notes and drawings, then outside, back and forth..."
    h "Slowly I get up from my bed and leave my room, barely a word to Big Bob and Miriam as I slam the front door behind me."
    h "Passing the Festival grounds once again, almost like an omen or something..."
    scene bg city evening
    with dissolve
    h "I arrive at City Park and walk towards my tree."
    h "Yes, it was my tree...I took claim of it years ago even if nobody knew it..."
    h "I had carved dozen of things in its bark and yet somehow found an excuse to chisel it away afterwards."
    h "I was always, even at this very moment, so terribly frightened of my love for..."
    window show
    show arnold grin
    with dissolve
    aslow "I keep running into you today Helga!"
    show arnold simple
    aslow "Granted this time it isn't literal..."
    hslow "Arnold!..."
    hslow "Seriously Football Head...a little warning!" 
    show arnold small blush
    aslow "Heh, sorry..."
    hslow "Yeah, sure...sure, whatever." 
    if GeraldSpills:
        hslow "...Anyway..."
        hslow "I heard a funny rumor about you today, Arnoldo..."
        show arnold sad smile
        aslow "A rumor?"
        hslow "Yeah, some tall-haired birdie said you've been talking about me~"
        h "I let that trail off a little more giddily than necessary."
        show arnold big blush
        aslow "Huh?"
        hslow "Yep...so you think we had a nice chat after lunch, huh?"
        aslow "Uh...well..."
        hslow "Come on, spit it out."
        hslow "Use your big boy words."
        show arnold turn shy
        aslow "Well, yeah Helga, I did say that and I meant it too."
        h "The point of me bringing this up was to make him all flustered for once..."
        h "And yet somehow he manages to turn the tables back on me!"
        aslow "I've always known that you were a nice girl Helga..."
        aslow "I'm just kinda happy you're finally showing me."
        aslow "I like you like that." 
        hslow "..."
        hslow "Really?"
        aslow "Yeah..."
        hslow "I sorta don't know what to say..."
        show arnold surprise
        aslow "Well that's different."
        hslow "Hey, watch it!"
        show arnold grin
        aslow "I'm sorry, it's not everyday I get to be the one who does the teasing..."
        hslow "Well don't go thinking I'm ever gonna give you a chance to do it again!"
        show arnold sad smile
        aslow "Alright, alright I'll keep that in mind..."
        show arnold simple
        h "Arnold looks down at the grass and kicks something visible to him."
        aslow "So..."
        hslow "So?"
        aslow "Can I walk ya home or something?"
        hslow "Or something..."
        show arnold sad smile
        aslow "What?"
        hslow "Nothing, Arnoldo...just teasing you."
        hslow "Restoring the world to its natural order."
        show arnold sneaky
        aslow "I didn't realize joking on you was such a big deal."
        hslow "The world could have ended and it would've been all your fault."
        hslow "That's how serious it was."
        show arnold simple
        aslow "Okay Helga, whatever you say."
    else:
        hslow "So what brings you out here Arnold?"
        show arnold sad smile
        with dissolve
        aslow "Just taking a walk, I guess"
        hslow "You guess? You mean you don't know?"
        show arnold bored
        with dissolve
        aslow "Very funny Helga..."
        hslow "I know...I'm a barrel of laughs." 
        show arnold turn unsure
        with dissolve
        aslow "..."
        aslow "You know you've kind of been hot and cold with me all day, any reason?"
        hslow "I'm imbalanced? I don't know..."
        show arnold sad smile
        with dissolve
        aslow "I don't think that's the case, but I won't try to pry."
        hslow "..."
        hslow "Hmm..."
        hslow "Arnold Shortman, not trying to butt into other people's business?"
        hslow "You must be fighting every urge not to."
        show arnold sad calm
        with dissolve
        aslow "......"
        aslow "..."
        show arnold turn angry
        with dissolve
        h "He didn't say anything...just made a face like I hit the target perfectly..."
        hslow "Haha! I must know you better than you think I do!"
        show arnold yeah with dissolve
        aslow "Seems like it..."
        h "Ugh, always taking me by surpirse...always!"
        show arnold sad smile with dissolve
        aslow "It's just, right when I think you're gonna break down that wall for me..."
        aslow "You somehow put it right back up again..."
        hslow "What wall...? This is all me here Football Head."
        h "That's an awful, awful lie."
        aslow "..."
        show arnold calm with dissolve
        aslow "No, I don't think so."
        hslow "What?"
        show arnold turn calm with dissolve
        aslow "You're hiding yourself, I know it."
        hslow "Yeah, right I'm hiding myself..."
        hslow "Criminy! Are you kidding?"
        show arnold simple with dissolve
        aslow "Okay Helga, like I said, I won't press your buttons."
        h "He turns away from me, and then causally looks over his shoulder to say..."
        aslow "I'll see ya tomorrow, okay?"
        hslow "..."