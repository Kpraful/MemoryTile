import pygame
import game_config as gc

from pygame import display,event, image

from animal import Animal

from time import sleep

def find_index(x,y):# index each image on the screen
    row=y // gc.IMAGE_SIZE
    col=x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index


pygame.init()# intilaize all pygame input

#display

display.set_caption('My game')# naem of game window

screen = display.set_mode((512,512)) # sceeen size
# above function return screen i.e a surface obj. all the images have to be displayed on this screen i.e on surface obj

matched = image.load('other_assets/matched.jpeg')# return surface elemnt

#screen.blit(matched,(0,0))#blit display surface on other surface (0,0) to start from top left corner of screen i.e cordinates
#display.flip()# to show the updated screen

running=True
tiles=[Animal(i) for i in range (0,gc.NUM_TILES_TOTAL)]#0-15 as 15 is NUM_TILES_TOTAL
current_images=[]

while(running):#gameloop
#get fun of pygame even get you all the input of keyboard and mouse event and return it as list
    current_event = event.get()# list of keyboard and mouse event and then evnt is removed from queue

    for e in current_event:
        if e.type == pygame.QUIT:#defined in pygame
            running = False

        if e.type == pygame.KEYDOWN: #for any key is pressed
            if e.key == pygame.K_ESCAPE:# if escape is pressed it exit
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:# for changing gray to white we need mouse capture
            mouse_x, mouse_y = pygame.mouse.get_pos() #to know which image hve been clicked
            #print(mouse_x,mous_y)# to show what it does
            index= find_index(mouse_x,mouse_y)
            if index not in current_images:# to check if we already clicked on that skin
                current_images.append(index)# to show images on which we have clicked
            if len(current_images) > 2:# show only 2 images
                current_images = current_images[1:]# leaving the first element


    screen.fill((255 , 255 ,255))

    total_skipped=0

    for _, tile in enumerate(tiles):
        image_i=tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i , (tile.col * gc.IMAGE_SIZE + gc.MARGIN , tile.row*gc.IMAGE_SIZE + gc.MARGIN))# update all the 16 images on the screen
        else:
            total_skipped +=1


    display.flip()# without this no image

    if len(current_images)==2:
        idx1 ,idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.4)#400 mili second
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            current_images=[]
    if total_skipped == len(tiles):# to stop the gameloop after finishing it
        running = False

print('Goodbye')
