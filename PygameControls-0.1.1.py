try:
    import pygame
except ImportError:
    raise Exception('Error: No pygame installed!')
pygame.init()
pygame.font.init()
pygame.mixer.init()
class Input:
    def __init__(self,fnt,bc,tc,pX,pY,w,h,mchr):
        self.font = fnt
        self.bgColor = bc
        self.textColor = tc
        self.posX = pX
        self.posY = pY
        self.buffer = ''
        self.width = w
        self.height = h
        self.write = False
        self.maxchars = mchr
        self.chars = 0
    def show(self,scr):
        pygame.draw.rect(scr,self.bgColor,(self.posX,self.posY,self.width,self.height))
        self.text = self.font.render(self.buffer,True,self.textColor)
        scr.blit(self.text,(self.posX+2,self.posY+4))
    def get_text(self):
        return self.buffer
    def key_event(self,evt):
        if evt.type==pygame.KEYDOWN:
            if self.write==True and self.chars<self.maxchars:
                self.buffer = self.buffer + chr(evt.key)
            if self.write==True and evt.key==pygame.K_BACKSPACE:
                self.buffer = self.buffer[:-2]
                self.chars = self.chars - 2
    def click_event(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
                self.write = True
            else:
                self.write = False
class TitledInput:
    def __init__(self,fnt,bc,tc,pX,pY,w,h,mchr,inf):
        self.font = fnt
        self.bgColor = bc
        self.textColor = tc
        self.posX = pX
        self.posY = pY
        self.buffer = ''
        self.width = w
        self.height = h
        self.write = False
        self.maxchars = mchr
        self.info_text = inf
        self.chars = 0
    def show(self,scr):
        self.info = self.font.render(self.info_text,True,self.textColor)
        pygame.draw.rect(scr,self.bgColor,(self.posX,self.posY,self.width,self.height))
        self.text = self.font.render(self.buffer,True,self.textColor)
        scr.blit(self.info,(self.posX,self.posY-35))
        scr.blit(self.text,(self.posX+2,self.posY+4))
    def get_text(self):
        return self.buffer
    def key_event(self,evt):
        if evt.type==pygame.KEYDOWN:
            if self.write==True and self.chars<self.maxchars:
                if not evt.key==pygame.K_RETURN:
                    self.buffer = self.buffer + chr(evt.key)
                    self.chars = self.chars + 1
            if self.write==True and evt.key==pygame.K_BACKSPACE:
                 self.buffer = self.buffer[:-2]
                 self.chars = self.chars - 2
    def click_event(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
                self.write = True
            else:
                self.write = False
class Button:
    def __init__(self,img,pX,pY,w,h):
        self.image = pygame.image.load(img)
        self.posX = pX
        self.posY = pY
        self.width = w
        self.height = h
    def show(self,scr):
        scr.blit(self.image,(self.posX,self.posY))
    def clicked(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
                return True
        else:
            return False
class OnMouseButton:
    def __init__(self,img,onmouseimg,pX,pY,w,h):
        self.image = pygame.image.load(img)
        self.onMouseImage = pygame.image.load(onmouseimg)
        self.posX = pX
        self.posY = pY
        self.mode = 'NoMouse'
        self.width = w
        self.height = h
    def show(self,scr):
        if self.mode=='NoMouse':
            scr.blit(self.image,(self.posX,self.posY))
        if self.mode=='OnMouse':
            scr.blit(self.onMouseImage,(self.posX,self.posY))
    def on_mouse(self,mousepos):
        if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
            self.mode = 'OnMouse'
        else:
            self.mode = 'NoMouse'
    def clicked(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
                return True
        else:
            return False
class Square:
    def __init__(self,v,pX,pY,w,h,c):
        self.visible = v
        self.posX = pX
        self.posY = pY
        self.width = w
        self.height = h
        self.color = c
    def show(self,scr):
        if self.visible==True:
            pygame.draw.rect(scr,self.color,(self.posX,self.posY,self.width,self.height))
        else:
            raise Exception('Cannot show invisible object or undefined value given!')
    def clicked(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
                return True
        else:
            return False
    def on_mouse(self,mousepos):
        if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
            return True
        else:
            return False
class MultiInput:
    def __init__(self,fnt,bc,tc,pX,pY,w,h,mchr,ml):
        self.font = fnt
        self.bgColor = bc
        self.textColor = tc
        self.posX = pX
        self.posY = pY
        self.width = w
        self.height = h
        self.buffer = ''
        self.write = False
        self.maxchars = mchr
        self.maxlines = ml
        self.chars = 0
        self.lines = 1
        self.charsInLine = 0
    def show(self,scr):
        pygame.draw.rect(scr,self.bgColor,(self.posX,self.posY,self.width,self.height))
        self.text = self.font.render(self.buffer,True,self.textColor)
        scr.blit(self.text,(self.posX+2,self.posY+4))
    def get_text(self):
        return self.buffer
    def get_chars(self):
        return self.chars
    def get_lines(self):
        return self.lines
    def key_event(self,evt):
        if evt.type==pygame.KEYDOWN:
            if self.write==True:
                if evt.key==pygame.K_BACKSPACE:
                    self.buffer = self.buffer[:-1]
                if evt.key==pygame.K_RETURN and self.lines<self.maxlines:
                    self.buffer = self.buffer + '\n'
                    self.lines = self.lines + 1
                    self.charsInLine = 0
                    self.lines = self.lines + 1
                if evt.key!=pygame.K_RETURN and evt.key!=pygame.K_BACKSPACE and self.charsInLine<self.maxchars:
                    self.buffer = self.buffer + chr(evt.key)
                    self.chars = self.chars + 1
                    self.charsInLine = self.charsInLine + 1
    def click_event(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX and mousepos[0]<=self.posX+self.width and mousepos[1]>=self.posY and mousepos[1]<=self.posY+self.height:
                self.write = True
            else:
                self.write = False
class GroupBox:
    def __init__(self,t,pX,pY,w,h,fnt):
        self.title = t
        self.posX = pX
        self.posY = pY
        self.width = w
        self.height = h
        self.font = fnt
    def show(self,scr):
        self.text = self.font.render(self.title,True,(255,255,255))
        scr.blit(self.text,(self.posX,self.posY))
        pygame.draw.rect(scr,(255,255,255),(self.posX,self.posY+self.height,self.width,2))
class PopupMenu:
    '''def __init__(self,it,sq,fnt,w,h):
        self.items = it
        self.square = sq
        self.onScreen = False
        self.font = fnt
        self.data = ''
        self.lastpos = 0
        self.width = w
        self.height = h
    def click_event(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if evt.button==3 and self.onScreen==False and mousepos[0]>=self.square.posX and mousepos[0]<=self.square.posX+self.square.width and mousepos[1]>=self.square.posY and mousepos[1]<=self.square.posY+self.square.height:
                self.onScreen = True
                self.lastpos = mousepos
            if self.onScreen==True:
                self.onScreen = False
    def set_data(self):
        for x in self.items:
            self.data = self.data + x + '\n'
    def show(self,scr):
        if self.onScreen==True:
            pygame.draw.rect(scr,(70,70,70),(self.lastpos[0],self.lastpos[1],self.width,self.height))
            self.text = self.font.render(self.data,True,(0,0,0))
            scr.blit(self.text,(self.lastpos[0]+2,self.lastpos[0]+4))'''
    #PopupMenu has been tempodary disabled because it isn't work
    pass
class MusicBox:
    def __init__(self,p,pX,pY):
        self.path = p
        self.posX = pX
        self.posY = pY
        self.playing = False
    def change_file(self,p):
        self.path = p
    def show(self,scr):
        pygame.draw.rect(scr,(255,255,255),(self.posX,self.posY,100,50))
        pygame.draw.rect(scr,(80,80,80),(self.posX,self.posY,50,50))
        pygame.draw.rect(scr,(0,255,0),(self.posX+10,self.posY+10,30,30))
        pygame.draw.rect(scr,(80,80,80),(self.posX+62,self.posY,50,50))
        pygame.draw.rect(scr,(255,0,0),(self.posX+72,self.posY+10,30,30))
    def click_event(self,evt,mousepos):
        if evt.type==pygame.MOUSEBUTTONDOWN:
            if mousepos[0]>=self.posX+2 and mousepos[0]<=self.posX+52 and mousepos[1]>=self.posY+2 and mousepos[1]<=self.posY+52:
                pygame.mixer.music.load(self.path)
                pygame.mixer.music.play(0)
            if mousepos[0]>=self.posX+62 and mousepos[0]<=self.posX+111 and mousepos[1]>=self.posY+2 and mousepos[1]<=self.posY+52:
                pygame.mixer.music.stop()
