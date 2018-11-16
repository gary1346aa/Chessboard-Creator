import cv2
import numpy as np

def draw_chessboard(N, M, length, dpi ,border):
    
    dots = int(length * dpi/2.54)
    boarder = int(border * dpi/2.54)
    img = np.tile(255, ((N + 1)*dots + 2*boarder, (M + 1)*dots + 2*boarder, 3))
    
    for i in range((N + 1)*dots):
        for j in range((M + 1)*dots):
            if (i//dots + j//dots) % 2:
                img[i + boarder][j + boarder].fill(0)

    cv2.imwrite(f'Chessboard {n}x{m}_{l}cm_{dpi}dpi.jpg',img)
    

if __name__ == '__main__':
    
    print("Please enter your chessboard parameters: ")
    print("N x M for corner size")
    print("length(cm) for each square")
    print("DPI for printing")
    print("Boarder(cm) length\n\n")
    
    n = int(input("input N: "))
    m = int(input("input M: "))
    l = [float(x) for x in input("length(s) : ").split()]
    dpi = int(input("DPI    : "))
    boarder = float(input("Boarder length : "))
    
    for length in l:
        draw_chessboard(n, m, length, dpi, boarder)
        
    