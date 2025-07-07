init -50 python:

    style.create('gallery_nav_frame', 'frame')
    style.create('gallery_nav_vbox', 'vbox')
    style.create('gallery_nav_button', 'button')
    style.create('gallery_nav_button_text', 'button_text')

    style.gallery_nav_button.size_group = "gallery_nav_button"
    store.gallery_transition = dissolve 
    class GalleryGridLayout(object):
        def __init__(self, gridsize, upperleft, offsets):
            self.gridsize = gridsize
            self.upperleft = upperleft
            self.offsets = offsets

        def __call__(self, imagenum, image_count):

            cols, rows = self.gridsize
            ulx, uly = self.upperleft
            ox, oy = self.offsets

            return dict(
                xpos = ulx + (imagenum % cols) * ox,
                ypos = uly + (imagenum // cols) * oy,
                )
           
    class GalleryAllPriorCondition(object):

        def check(self, all_prior):
            return all_prior
    
    class GalleryArbitraryCondition(object):
        def __init__(self, condition):
            self.condition = condition

        def check(self, all_prior):
            return eval(self.condition)
                    
    class GalleryUnlockCondition(object):
        def __init__(self, images):
            self.images = images
            
        def check(self, all_prior):
            for i in self.images:
                if tuple(i.split()) not in persistent._seen_images:
                    return False

            return True
            
            
    class GalleryImage(object):
        def __init__(self, gallery, images, displayable):
            self.gallery = gallery
            self.images = images or [ ]
            self.displayable = displayable
            self.conditions = [ ]

        def check_unlock(self, all_prior):
            for i in self.conditions:
                if not i.check(all_prior):
                    return False

            return True
        
        def show_locked(self, image_num, image_count):
            renpy.transition(self.gallery.transition)
            self.gallery.locked_image(image_num, image_count)

            ui.saybehavior()
            ui.interact()
            
        def show(self, image_num, image_count):
            renpy.transition(self.gallery.transition)

            renpy.scene()

            for i in self.images:
                renpy.show(i)

            if self.displayable:
                ui.add(self.displayable)

            ui.saybehavior()
            ui.interact()

            
                    
    class GalleryButton(object):
        def __init__(self, gallery, idle, hover, insensitive, properties):
            self.gallery = gallery
            self.idle = idle
            self.hover = hover
            self.insensitive = insensitive
            self.properties = properties
            self.images  = [ ]
            self.conditions = [ ]
            
        def check_unlock(self):
            for i in self.conditions:
                if not i.check(True):
                    return False
            
            for i in self.images:
                if i.check_unlock(False):
                    return True

            return False
            
        def render(self, i, pos):
            props = pos.copy()
            props.update(self.properties)

            if not self.check_unlock():
                insensitive = self.insensitive or self.gallery.locked_button
                if insensitive is not None:
                    ui.image(insensitive, **props)
                    return

            if self.hover:
                ui.imagebutton(self.idle,
                               self.hover,
                               clicked=ui.returns(("button", i)),
                               **props)
            
            else:
                ui.image(self.idle, **props)
                ui.imagebutton(self.gallery.idle_border,
                               self.gallery.hover_border,
                               clicked=ui.returns(("button", i)),
                               **props)

        def show(self):

            all_prior = True

            for i, img in enumerate(self.images):
                if img.check_unlock(all_prior):
                    img.show(i, len(self.images))
                else:
                    img.show_locked(i, len(self.images))
                    all_prior = False
                
                
    class GalleryPage(object):

        def __init__(self, gallery, name, background):
            self.gallery = gallery
            self.name = name
            self.background = background
            self.buttons = [ ]

            
    class Gallery(object):

        transition = dissolve
        
        locked_button = None
        locked_background = "#000"
                
        hover_border = None
        idle_border = None

        background = None
        
        
        def __init__(self):
            self.pages = [ ]

            self.page_ = None
            self.button_ = None
            self.image_ = None
            self.unlockable = None
            
        def page(self, name, background=None):

            self.page_ = GalleryPage(self, name, background)
            self.pages.append(self.page_)

        def button(self, idle, hover=None, locked=None, **properties):
            self.button_ = GalleryButton(self, idle, hover, locked, properties)
            self.page_.buttons.append(self.button_)
            self.unlockable = self.button_
            
        def image(self, *images):
            self.image_ = GalleryImage(self, images, None)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_

        def display(self, displayable):
            self.image_ = GalleryImage(self, [ ], displayable)
            self.button_.images.append(self.image_)
            self.unlockable = self.image_
            
        def unlock(self, *images):
            self.unlockable.conditions.append(GalleryUnlockCondition(images))

        def condition(self, condition):
            self.unlockable.conditions.append(GalleryArbitraryCondition(condition))

        def allprior(self):
            self.unlockable.conditions.append(GalleryAllPriorCondition())
    
        def unlock_image(self, *images):
            self.image(*images)
            self.unlock(*images)

        def navigation(self, page_name, page_num, pages):

            ui.frame(style='gallery_nav_frame')
            ui.vbox(style='gallery_nav_vbox')

            for i, p in enumerate(self.pages):
                layout.button(p.name,
                              "gallery_nav",
                              selected=(i == page_num),
                              clicked=ui.returns(("page", i)))

            ui.null(height=22)
            layout.button("Return", "gallery_nav", clicked=ui.returns(("return", 0)))

            ui.close()


        def grid_layout(self, gridsize, upperleft, offsets):
            self.layout = GalleryGridLayout(gridsize, upperleft, offsets)

        def layout(self, i, n):
            return { }

        def locked_image(self, num, total):
            ui.add(self.locked_background)
            ui.text(_("Image %d of %d is locked.") % (num + 1, total), xalign=0.5, yalign=0.5)
            
        def show(self, page=0):

            
            while True:
                renpy.transition(self.transition)
                store.gallery_transition = Dissolve 

                p = self.pages[page]
                
                bg = p.background or self.background
                if bg is not None:
                    renpy.scene()
                    ui.add(bg)

                self.navigation(p.name, page, len(self.pages))
                    
                for i, b in enumerate(p.buttons):
                    pos = self.layout(i, len(p.buttons))
                    b.render(i, pos)

                cmd, arg = ui.interact(suppress_overlay=True, suppress_underlay=True)

                if cmd == "return":
                    return

                elif cmd == "page":
                    page = arg
                    continue

                elif cmd == "button":
                    p.buttons[arg].show()
                    continue
