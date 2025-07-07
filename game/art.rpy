init:
    # Position the navigation on the right side of the screen.
    $ style.gallery_nav_frame.xpos = 800 - 10
    $ style.gallery_nav_frame.xanchor = 1.0
    $ style.gallery_nav_frame.ypos = 12
    # Add the gallery to the main menu.
    $ config.main_menu.insert(2, ('Gallery', "gallery", "True"))
# The entry point to the gallery code.
label gallery:
    python hide:

        # Construct a new gallery object.
        g = Gallery()

        # The image used for locked buttons.
        g.locked_button = "locked.png"

        # The background of a locked image.
        g.locked_background = "lockedbg.jpg"

        # Frames added over unlocked buttons, in hover and idle states.
        g.hover_border = "hover.png"
        g.idle_border = "idle.png"

        # An images used as the background of the various gallery pages.
        g.background = "GBACK.jpg"

        # Lay out the gallery images on the screen.
        # These settings lay images out 3 across and 4 down.
        # The upper left corner of the gird is at xpos 10, ypos 20.
        # They expect button images to be 155x112 in size.
        g.grid_layout((3, 4), (10, 12), (160, 124))

        # Show the background page.
        g.page("Special Events")
       

        # Our first button is a picture of the beach.
        g.button("thumb_CG1.png")
        g.unlock_image("CG1")
        g.unlock_image("CG2")
        g.button("thumb_CG3.png")
        g.unlock_image("CG3")
        g.button("thumb_CG4.png")
        g.unlock_image("CG4")
        g.button("thumb_CG5.png")
        g.unlock_image("CG5")
        g.unlock_image("CG6")
        g.unlock_image("CG7")
        #
        # These show images, if they have been unlocked. The image name must
        # have been defined using an image statement.
        


        # Now, show the gallery.
        g.show()
jump main_menu_screen
