import pygame
from pygame.locals import *
import sys

# pygame初期化
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))    # サイズを指定して画面を作成
pygame.display.set_caption("QUARTO")    # タイトル文字を指定
font = pygame.font.Font(None, 60)               # フォントの設定(60px)

# メイン関数
def main():
    # 表示更新ループ
    while True:
        SURFACE.fill((180,180,180))          # 背景
        title = font.render("QUARTO", True, (0, 0, 100))
        SURFACE.blit(title, [100, 130])    # 文字列の位置を指定
        pygame.display.update()            # 画面更新
        # イベントを処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了（画面を閉じる）
                sys.exit()          # プログラムの終了

if __name__ == '__main__':
    main()