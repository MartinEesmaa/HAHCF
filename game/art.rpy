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
        g.page("Special Events One")
       

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
        g.button("thumb_CG7.png")
        g.unlock_image("CG9")
        g.unlock_image("CG10")
        g.button("thumb_CG6.png")
        g.unlock_image("CG8")
        g.button("thumb_CG8.png")
        g.unlock_image("CG11")
        g.button("thumb_CG9.png")
        g.unlock_image("CG12")
        g.unlock_image("CG13")
        g.unlock_image("CG14")
        g.unlock_image("CG15")
        g.button("thumb_CG13.png")
        g.unlock_image("CG23")
        g.button("thumb_CG10.png")
        g.unlock_image("CG16")
        g.unlock_image("CG17")
        g.unlock_image("CG18")
        g.unlock_image("CG19")
        g.button("thumb_CG11.png")
        g.unlock_image("CG20")
        g.button("thumb_CG14.png")
        g.unlock_image("CG24")
        #
        # These show images, if they have been unlocked. The image name must
        # have been defined using an image statement.
        
        g.page("Special Events Two")
        g.button("thumb_CG16.png")
        g.unlock_image("CG26")
        g.button("thumb_CG15.png")
        g.unlock_image("CG25")
        g.button("thumb_CG17.png")
        g.unlock_image("CG27")
        g.button("thumb_CG18.png")
        g.unlock_image("CG28")
        g.unlock_image("CG29")
        g.button("thumb_CG19.png")
        g.unlock_image("CG32")
        g.unlock_image("CG31")
        g.unlock_image("CG33")
        g.unlock_image("CG34")
        g.button("thumb_CG20.png")
        g.unlock_image("CG35")
        g.unlock_image("CG36")
        g.button("thumb_CG21.png")
        g.unlock_image("CG37")
        g.button("thumb_CG23.png")
        g.unlock_image("CG38")
        g.button("thumb_CG22.png")
        g.unlock_image("CG39")
        g.button("thumb_CG24.png")
        g.unlock_image("CG40")
        g.button("thumb_CG25.png")
        g.unlock_image("CG41")
        g.button("thumb_CG26.png")
        g.unlock_image("CG42")
        
        g.page("Special Events Three")
        g.button("thumb_CG28.png")
        g.unlock_image("CG45")
        g.button("thumb_CG27.png")
        g.unlock_image("CG43")
        g.unlock_image("CG44")
        g.button("thumb_CG29.png")
        g.unlock_image("CG46")
        g.button("thumb_CG33.png")
        g.unlock_image("CG51")


        # Now, show the gallery.
        g.show()
jump main_menu_screen
