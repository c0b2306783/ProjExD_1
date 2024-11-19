import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #ウインドウの左上のタイトル設定
    screen = pg.display.set_mode((800, 600)) #ウインドウのサイズを設定(横, 縦)
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像をパスを指定して読み込む
    fbg_img = pg.transform.flip(bg_img, True, False)
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)

    kt_rct = kt_img.get_rect() #Surfaceからrect(四角形)を抽出
    kt_rct.center = 200, 300 #rectを使った初期座標の設定(画像を移動させる場合はこっち)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        diff_x = 0
        diff_y = 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            diff_y -= 1
            #kt_rct.move_ip(0, -1) #moveip 特定のキーが押されている間(True)、縦or横に移動させる (横,　縦)
        
        if key_lst[pg.K_DOWN]:
            #kt_rct.move_ip(0, +1)
            diff_y += 1
        
        if key_lst[pg.K_RIGHT]:
            ##kt_rct.move_ip(+2, 0)
            diff_x += 2
        
        if key_lst[pg.K_LEFT]:
            ##kt_rct.move_ip(-1, 0)
            diff_x -= 1
        else:
            ##kt_rct.move_ip(-1, 0) #キーが押されていない場合
            diff_x -= 1

        kt_rct.move_ip((diff_x, diff_y))

        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0]) #自身に別のSurdaceを貼り付ける
        screen.blit(fbg_img, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(fbg_img, [x+4800, 0])
        screen.blit(kt_img, kt_rct)

        pg.display.update()

        tmr += 1
        #print(tmr)   
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()