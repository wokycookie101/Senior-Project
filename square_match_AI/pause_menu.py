import pygame

class PauseMenu:
    def __init__(self, screen_size):
        self.resume_button=pygame.Rect(screen_size//2-100,screen_size//2-20,200,40)
        self.quit_button=pygame.Rect(screen_size//2-100,screen_size//2+40,200,40)

    def draw(self,screen,font,screen_size):
        overlay=pygame.Surface((screen_size,screen_size+100))
        overlay.set_alpha(180); overlay.fill((50,50,50))
        screen.blit(overlay,(0,0))
        title=font.render("Paused",True,(255,255,255))
        screen.blit(title,(screen_size//2-50,screen_size//2-80))
        pygame.draw.rect(screen,(200,200,0),self.resume_button)
        screen.blit(font.render("Resume",True,(0,0,0)),(self.resume_button.x+60,self.resume_button.y+8))
        pygame.draw.rect(screen,(200,0,0),self.quit_button)
        screen.blit(font.render("Quit",True,(255,255,255)),(self.quit_button.x+70,self.quit_button.y+8))