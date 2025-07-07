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