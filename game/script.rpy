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
image bg city evening = "BG Park Evening.png"
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

#Day Images Go Here
image day one = "dayone1.png"
image day one2 = "dayone2.png"
image day one3 = "dayone3.png"
init:
# Declare characters used by this game.
# Slow text.
    $ hslow = Character("Helga", color="#83C3FF", what_slow_cps=30)
    $ pslow = Character("Phoebe", color="#83C3FF", what_slow_cps=24)                       
    $ aslow = Character('Arnold', color="#83C3FF", what_slow_cps=24)
    $ h = Character(None, what_slow_cps=24)
# The game starts here.
label splashscreen:
    scene black
    with fade
    $ renpy.pause(0.5, hard=True)
   
    show opening pic
    with dissolve
    play sound "OPENINGSONG.wav"
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
    
     $ GeraldSpills = False
     $ Good = False
     play music "Jim Lang - Operation Ruthless End.mp3"
     h "So, let's just start off by saying Cheese Festivals never, ever worked out in my favor..."
     h "I can remember..."
     h "There were two of them when I was nine-years-old and both of them ended up with me..."
     h "Well, how do they put it..."
     h "Forever alone." 
     h "And now..."
     h "It was that time of year again."  
     h "Hillwood was going to have another one."
     h "And I wasn't looking forward to it."
     h "Because I knew it would be filled with people who were happier than me."
     h "They would be having a good time, laughing...enjoying their lives."
     h "Their loves..."
     h "And the one thing that made me truly happy..."
     h "Well it made me so miserable every time the Festival came to town."
     h "I hate that."
     stop music fadeout 3.0
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
     play sound "Right Cross-SoundBible.com-1721311663.wav"
     with hpunch
     h "CRASH!!"
     hslow "Arnold!"
     window show
     aslow "Helga!"
     aslow "We've got to stop bumping into each other like this! Haha!"
     hslow "Uh...well..."
label GoodGoing:
    $ GeraldSpills = True
    hslow "Got that right, Football Head, one of these days I might actually hurt you!"
    h "Whew~"
    scene bg city day
    show arnold sad smile
    aslow "Right Helga, whatever you say."
    show arnold turn unsure
    aslow "Well anyway..."
    h "He looks around, kind of nervously."
    aslow "Do you mind if I walk with you guys the rest of the way?"
    show arnold turn unsure at left
    show phoebe question at right
    pslow "I've no issue with that..."
    pslow "Helga?"
    h "Remain calm...calm...calm..."
    hslow "Whatever floats your boat."
    h "Why is my heart pounding like this?"
    h "Why does he do this to me?!"
    show arnold simple 
    aslow "Cool, thanks."
    h "..."
    h "......"
    show phoebe grin
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
    show arnold frown
    with dissolve
    aslow "You haven't had a good time with the Festivals either?"
    hslow "I didn't say that..."
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
    h "{i}I arrive at City Park and walk towards my tree.{/i}"
    h "{i}Yes, it was my tree...I took claim of it years ago even if nobody knew it...{/i}"
    h "{i}I had carved dozen of things in its bark and yet somehow found an excuse to chisel it away afterwards.{/i}"
    h "{i}I was always, even at this very moment, so terribly frightened of my love for...{/i}"
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