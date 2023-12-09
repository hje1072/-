import pygame as pg
import time
import random

# [index] - 0 ~ 3: 블록 상태 / 4: ID(색을 결정) / 5: 크기

#여기부터 1-omino

O_1MINO = (
    (1, 0,
     0, 0),   # 상태: 기본
    
    (1, 0,
     0, 0),  # 상태: 회전 * 1
    
    (1, 0,
     0, 0),   # 상태: 회전 * 2
    
    (1, 0,
     0, 0),   # 상태: 회전 * 3
    
    1,  # ID: 1
    
    2   # 크기: 2 * 2
)
#여기까지 1-omino


#여기부터 2-omino

I_2MINO = (
    (2, 0,
     2, 0),   # 상태: 기본
    
    (2, 2,
     0, 0),  # 상태: 회전 * 1
    
    (0, 2,
     0, 2),   # 상태: 회전 * 2
    
    (0, 0,
     2, 2),   # 상태: 회전 * 3
    
    2,  # ID: 2
    
    2   # 크기: 2 * 2
)

#여기까지 2-omino



#여기부터 3-omino

L_3MINO = (
    (3, 0,
     3, 3),   # 상태: 기본
    
    (3, 3,
     0, 3),  # 상태: 회전 * 1
    
    (0, 3,
     3, 3),   # 상태: 회전 * 2
    
    (3, 3,
     3, 0),   # 상태: 회전 * 3
    
    3,  # ID: 3
    
    2   # 크기: 2 * 2
)

I_3MINO = (
    (0, 4, 0,
     0, 4, 0,
     0, 4, 0),   # 상태: 기본
    
    (0, 0, 0,
     4, 4, 4,
     0, 0, 0),   # 상태: 회전 * 1
    
    (0, 4, 0,
     0, 4, 0,
     0, 4, 0),   # 상태: 회전 * 2
    
    (0, 0, 0,
     4, 4, 4,
     0, 0, 0),   # 상태: 회전 * 3
    
    4,  # ID
    
    3   # 크기: 3 * 3
)

#여기까지 3-omino


#여기부터 4-omino
L_TETROMINO = (
    (0, 1, 0,
     0, 1, 0,
     0, 1, 1),   # 상태: 기본
    
    (0, 0, 0,
     1, 1, 1,
     1, 0, 0),   # 상태: 회전 * 1
    
    (1, 1, 0,
     0, 1, 0,
     0, 1, 0),   # 상태: 회전 * 2
    
    (0, 0, 1,
     1, 1, 1,
     0, 0, 0),   # 상태: 회전 * 3
    
    1,  # ID
    
    3   # 크기: 3 * 3
)

J_TETROMINO = (
    (0, 2, 0,
     0, 2, 0,
     2, 2, 0),   # 상태: 기본
    
    (2, 0, 0,
     2, 2, 2,
     0, 0, 0),   # 상태: 회전 * 1
    
    (0, 2, 2,
     0, 2, 0,
     0, 2, 0),   # 상태: 회전 * 2
    
    (0, 0, 0,
     2, 2, 2,
     0, 0, 2),   # 상태: 회전 * 3
    
    2,  # ID: 2
    
    3   # 크기: 3 * 3
)

T_TETROMINO = (
    (0, 0, 0,
     3, 3, 3,
     0, 3, 0),   # 상태: 기본
    
    (0, 3, 0,
     3, 3, 0,
     0, 3, 0),   # 상태: 회전 * 1
    
    (0, 3, 0,
     3, 3, 3,
     0, 0, 0),   # 상태: 회전 * 2
    
    (0, 3, 0,
     0, 3, 3,
     0, 3, 0),   # 상태: 회전 * 3
    
    3,  # ID: 3
    
    3   # 크기: 3 * 3
)

Z_TETROMINO = (
    (4, 4, 0,
     0, 4, 4,
     0, 0, 0),   # 상태: 기본
    
    (0, 0, 4,
     0, 4, 4,
     0, 4, 0),   # 상태: 회전 * 1
    
    (0, 0, 0,
     4, 4, 0,
     0, 4, 4),   # 상태: 회전 * 2
    
    (0, 4, 0,
     4, 4, 0,
     4, 0, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

S_TETROMINO = (
    (0, 5, 5,
     5, 5, 0,
     0, 0, 0),   # 상태: 기본
    
    (0, 5, 0,
     0, 5, 5,
     0, 0, 5),   # 상태: 회전 * 1
    
    (0, 0, 0,
     0, 5, 5,
     5, 5, 0),   # 상태: 회전 * 2
    
    (5, 0, 0,
     5, 5, 0,
     0, 5, 0),   # 상태: 회전 * 3
    
    5,  # ID: 5
    
    3   # 크기: 3 * 3
)

O_TETROMINO = (
    (6, 6,
     6, 6),   # 상태: 기본
    
    (6, 6,
     6, 6),   # 상태: 회전 * 1
    
    (6, 6,
     6, 6),   # 상태: 회전 * 2
    
    (6, 6,
     6, 6),   # 상태: 회전 * 3
    
    6,  # ID: 6
    
    2   # 크기: 2 * 2
)

I_TETROMINO = (
    (0, 7, 0, 0,
     0, 7, 0, 0,
     0, 7, 0, 0,
     0, 7, 0, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     7, 7, 7, 7,
     0, 0, 0, 0,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 0, 7, 0,
     0, 0, 7, 0,
     0, 0, 7, 0,
     0, 0, 7, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     0, 0, 0, 0,
     7, 7, 7, 7,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    7,  # ID: 7
    
    4   # 크기: 4 * 4
)

#여기까지 4-omino


#여기부터 5-omino

F1_5OMINO = (
    (0, 4, 4,
     4, 4, 0,
     0, 4, 0),   # 상태: 기본
    
    (0, 4, 0,
     4, 4, 4,
     0, 0, 4),   # 상태: 회전 * 1
    
    (0, 4, 0,
     0, 4, 4,
     4, 4, 0),   # 상태: 회전 * 2
    
    (4, 0, 0,
     4, 4, 4,
     0, 4, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

F2_5OMINO = (
    (4, 4, 0,
     0, 4, 4,
     0, 4, 0),   # 상태: 기본
    
    (0, 4, 0,
     4, 4, 4,
     4, 0, 0),   # 상태: 회전 * 1
    
    (0, 4, 0,
     4, 4, 0,
     0, 4, 4),   # 상태: 회전 * 2
    
    (0, 0, 4,
     4, 4, 4,
     0, 4, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

I_5OMINO = (
    (0, 0, 4, 0, 0,
     0, 0, 4, 0, 0,
     0, 0, 4, 0, 0,
     0, 0, 4, 0, 0,
     0, 0, 4, 0, 0),   # 상태: 기본
    
    (0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     4, 4, 4, 4, 4,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 0, 4, 0, 0,
     0, 0, 4, 0, 0,
     0, 0, 4, 0, 0,
     0, 0, 4, 0, 0,
     0, 0, 4, 0, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     4, 4, 4, 4, 4,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    5   # 크기: 5 * 5
)

L1_5OMINO = (
    (0, 4, 0, 0,
     0, 4, 0, 0,
     0, 4, 0, 0,
     0, 4, 4, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     4, 4, 4, 4,
     4, 0, 0, 0,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 4, 4, 0,
     0, 0, 4, 0,
     0, 0, 4, 0,
     0, 0, 4, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     0, 0, 0, 4,
     4, 4, 4, 4,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    4   # 크기: 4 * 4
)

L2_5OMINO = (
    (0, 0, 4, 0,
     0, 0, 4, 0,
     0, 0, 4, 0,
     0, 4, 4, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     4, 0, 0, 0,
     4, 4, 4, 4,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 4, 4, 0,
     0, 4, 0, 0,
     0, 4, 0, 0,
     0, 4, 0, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     4, 4, 4, 4,
     0, 0, 0, 4,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    4   # 크기: 4 * 4
)

N1_5OMINO = (
    (0, 0, 4, 0,
     0, 4, 4, 0,
     0, 4, 0, 0,
     0, 4, 0, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     4, 4, 4, 0,
     0, 0, 4, 4,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 0, 4, 0,
     0, 0, 4, 0,
     0, 4, 4, 0,
     0, 4, 0, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     4, 4, 0, 0,
     0, 4, 4, 4,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    4   # 크기: 4 * 4
)

N2_5OMINO = (
    (0, 4, 0, 0,
     0, 4, 4, 0,
     0, 0, 4, 0,
     0, 0, 4, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     0, 0, 4, 4,
     4, 4, 4, 0,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 4, 0, 0,
     0, 4, 0, 0,
     0, 4, 4, 0,
     0, 0, 4, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     0, 4, 4, 4,
     4, 4, 0, 0,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    4   # 크기: 4 * 4
)

P1_5OMINO = (
    (4, 4, 0,
     4, 4, 0,
     4, 0, 0),   # 상태: 기본
    
    (4, 4, 4,
     0, 4, 4,
     0, 0, 0),   # 상태: 회전 * 1
    
    (0, 0, 4,
     0, 4, 4,
     0, 4, 4),   # 상태: 회전 * 2
    
    (0, 0, 0,
     4, 4, 0,
     4, 4, 4),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

P2_5OMINO = (
    (0, 4, 4,
     0, 4, 4,
     0, 0, 4),   # 상태: 기본
    
    (4, 4, 4,
     4, 4, 0,
     0, 0, 0),   # 상태: 회전 * 1
    
    (4, 0, 0,
     4, 4, 0,
     4, 4, 0),   # 상태: 회전 * 2
    
    (0, 0, 0,
     0, 4, 4,
     4, 4, 4),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

T_5OMINO = (
    (4, 4, 4,
     0, 4, 0,
     0, 4, 0),   # 상태: 기본
    
    (0, 0, 4,
     4, 4, 4,
     0, 0, 4),   # 상태: 회전 * 1
    
    (0, 4, 0,
     0, 4, 0,
     4, 4, 4),   # 상태: 회전 * 2
    
    (4, 0, 0,
     4, 4, 4,
     4, 0, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

U_5OMINO = (
    (0, 0, 0,
     4, 0, 4,
     4, 4, 4),   # 상태: 기본
    
    (0, 4, 4,
     0, 0, 4,
     0, 4, 4),   # 상태: 회전 * 1
    
    (4, 4, 4,
     4, 0, 4,
     0, 0, 0),   # 상태: 회전 * 2
    
    (4, 4, 0,
     4, 0, 0,
     4, 4, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

V_5OMINO = (
    (4, 0, 0,
     4, 0, 0,
     4, 4, 4),   # 상태: 기본
    
    (0, 0, 4,
     0, 0, 4,
     4, 4, 4),   # 상태: 회전 * 1
    
    (4, 4, 4,
     0, 0, 4,
     0, 0, 4),   # 상태: 회전 * 2
    
    (4, 4, 4,
     4, 0, 0,
     4, 0, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

W_5OMINO = (
    (4, 0, 0,
     4, 4, 0,
     0, 4, 4),   # 상태: 기본
    
    (0, 0, 4,
     0, 4, 4,
     4, 4, 0),   # 상태: 회전 * 1
    
    (4, 4, 0,
     0, 4, 4,
     0, 0, 4),   # 상태: 회전 * 2
    
    (0, 4, 4,
     4, 4, 0,
     4, 0, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

X_5OMINO = (
    (0, 4, 0,
     4, 4, 4,
     0, 4, 0),   # 상태: 기본
    
    (0, 4, 0,
     4, 4, 4,
     0, 4, 0),   # 상태: 회전 * 1
    
    (0, 4, 0,
     4, 4, 4,
     0, 4, 0),   # 상태: 회전 * 2
    
    (0, 4, 0,
     4, 4, 4,
     0, 4, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

Y1_5OMINO = (
    (0, 4, 0, 0,
     0, 4, 0, 0,
     0, 4, 4, 0,
     0, 4, 0, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     4, 4, 4, 4,
     0, 4, 0, 0,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 0, 4, 0,
     0, 4, 4, 0,
     0, 0, 4, 0,
     0, 0, 4, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     0, 0, 4, 0,
     4, 4, 4, 4,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    4   # 크기: 4 * 4
)

Y2_5OMINO = (
    (0, 0, 4, 0,
     0, 0, 4, 0,
     0, 4, 4, 0,
     0, 0, 4, 0),   # 상태: 기본
    
    (0, 0, 0, 0,
     0, 4, 0, 0,
     4, 4, 4, 4,
     0, 0, 0, 0),   # 상태: 회전 * 1
    
    (0, 4, 0, 0,
     0, 4, 4, 0,
     0, 4, 0, 0,
     0, 4, 0, 0),   # 상태: 회전 * 2
    
    (0, 0, 0, 0,
     4, 4, 4, 4,
     0, 0, 4, 0,
     0, 0, 0, 0),    # 상태: 회전 * 3
    
    4,  # ID: 4
    
    4   # 크기: 4 * 4
)

Z1_5OMINO = (
    (4, 4, 0,
     0, 4, 0,
     0, 4, 4),   # 상태: 기본
    
    (0, 0, 4,
     4, 4, 4,
     4, 0, 0),   # 상태: 회전 * 1
    
    (4, 4, 0,
     0, 4, 0,
     0, 4, 4),   # 상태: 회전 * 2
    
    (0, 0, 4,
     4, 4, 4,
     4, 0, 0),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

Z2_5OMINO = (
    (0, 4, 4,
     0, 4, 0,
     4, 4, 0),   # 상태: 기본
    
    (4, 0, 0,
     4, 4, 4,
     0, 0, 4),   # 상태: 회전 * 1
    
    (0, 4, 4,
     0, 4, 0,
     4, 4, 0),   # 상태: 회전 * 2
    
    (4, 0, 0,
     4, 4, 4,
     0, 0, 4),   # 상태: 회전 * 3
    
    4,  # ID: 4
    
    3   # 크기: 3 * 3
)

#여기까지 5-omino

class Tetromino:
    def __init__(self):
        self.turnCount = 0                              # 테트로미노 회전 횟수
        self.turn = self.turnCount % 4                  # 테트로미노 회전 상태

        #단계에 맞는 블록 생성하기
        self.type = random.choice(TETROMINO_BLOCK[level-1])      # 테트로미노 선택 ,#HACK 여기 바꾸자.

        
        self.form = self.type[self.turn]                # 테트로미노 형태(회전수 반영)
        self.id = self.type[4]                          # 테르로미노 ID (색상 결정)
        self.size = self.type[5]                        # 테트로미노 크기 (3 * 3 or 4 * 4)
        self.color = TETROMINO_COLOR[self.id - 1]       # 테트로미노 색상
        self.xpos = random.randint(3, 9 - self.size)    # 테트로미노 x 좌표
        self.ypos = 1 - self.size                       # 테트로미노 y 좌표
        
    def draw(self):
        for i in range(len(self.form)):
            xpos = i % self.size
            ypos = i // self.size
            element = self.form[i]
            if element != 0:
                rect_x = 40 + (self.xpos + xpos) * 40
                rect_y = 40 + (self.ypos + ypos) * 40
                pg.draw.rect(GAME_SCREEN, self.color, (rect_x, rect_y, 39, 39))
    
    def update(self):
        overlap = overlap_check(self, self.turn, self.xpos, self.ypos + 1)
        if overlap == True:
            for i in range(len(self.form)):
                xpos = i % self.size
                ypos = i // self.size
                if 0 <= self.xpos + xpos <= 10 and -1 <= self.ypos + ypos <= 17:
                    form = self.form[ypos * self.size + xpos]
                    if form != 0:
                        FIELD[self.ypos + ypos][self.xpos + xpos] = form
            new_tetromino()

# 다음 테트로미노를 결정하는 함수
def new_tetromino():
    global TETROMINO_NOW, TETROMINO_NEXT
    if TETROMINO_NEXT != None:
        TETROMINO_NOW = TETROMINO_NEXT
    TETROMINO_NEXT = Tetromino()

# 이동 후 벽 또는 다른 테트로미노 블록과 겹치는지 확인하는 함수
def overlap_check(tetromino, turn, xpos, ypos):
    form = tetromino.type[turn]
    for i in range(len(tetromino.form)):
        c = i % tetromino.size
        r = i // tetromino.size
        if 0 <= xpos + c < WALL_COL and 0 <= ypos + r < WALL_ROW:
            if form[r * tetromino.size + c] != 0 and FIELD[ypos + r][xpos + c] != 0:
                return True
    return False

# 테트로미노 하강 계산
def tetromino_descent():
    global time_count
    time_count += 1
    if time_count == TIME_INTERVAL:    
        overlap = overlap_check(TETROMINO_NOW, TETROMINO_NOW.turn, TETROMINO_NOW.xpos, TETROMINO_NOW.ypos + 1)
        if overlap == False:
            TETROMINO_NOW.ypos += 1
        TETROMINO_NOW.update()
        time_count = 0

# 줄이 완성되면 점수 증가 & 완성된 줄 지우기
def score_up():
    global score, exp, level
    compacted_row = 0
    row_check = 16
    while row_check >= 0:
        is_compactied = all(FIELD[row_check])
        if is_compactied:
            compacted_row += 1
            del(FIELD[row_check])
            FIELD.insert(0, [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9])
        else:
            row_check -= 1

    #점수 갱신 겸, 점수에 따른 레벨 분류
    if compacted_row > 0:
        score += (2 ** compacted_row) * 100
        if exp <= score and level < 5 :
            exp *= 2
            level += 1
        

# 게임 화면 그리기
def draw_background():
    GAME_SCREEN.fill((0, 0, 0))
    # 격자 무늬 그리기
    for row in range(GRID_ROW):
        for col in range(GRID_COL):
            pg.draw.rect(GAME_SCREEN, (255, 255, 255), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    # 필드 벽 그리기
    for r in range(1, WALL_ROW + 1):
        for c in range(1, WALL_COL + 1):
            if c == 1 or c == 12 or (r == 18 and c in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)):
                pg.draw.rect(GAME_SCREEN, (125, 125, 125), (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # 필드 내부 블록 그리기
    for ypos in range(WALL_ROW):
        for xpos in range(WALL_COL):
            field_element = FIELD[ypos][xpos]
            if field_element != 0 and field_element != 9 and ypos != WALL_ROW - 1:
                pg.draw.rect(GAME_SCREEN, TETROMINO_COLOR[field_element - 1], (xpos * 40 + 40, ypos * 40 + 40, 39, 39))

# 다음 테트로미노 미리보기(게임 화면 우측 상단)
def next_tetromino_preview():
    for i in range(len(TETROMINO_NEXT.form)):
        xpos = i % TETROMINO_NEXT.size
        ypos = i // TETROMINO_NEXT.size
        element = TETROMINO_NEXT.form[i]
        if element != 0:
            preview_x = 640 + xpos * 40
            preview_y = 100 + ypos * 40
            pg.draw.rect(GAME_SCREEN, TETROMINO_NEXT.color, (preview_x, preview_y, 39, 39))

# 우측 하단 점수 그리기
#   + 현 단계가 몇단계인지 표시해주기
def draw_score():

    #점
    score_txt_1 = FONT_40.render('SCORE:', True, (255, 255, 255))
    score_txt_2 = FONT_40.render(str(score), True, (255, 255, 255))
    GAME_SCREEN.blit(score_txt_1, (600, 660))
    GAME_SCREEN.blit(score_txt_2, (600, 700))


    #현단계
    level_txt_1 = FONT_40.render('LEVEL:', True, (92, 255, 209))

    if level == 5 : level_txt_2 = FONT_40.render('FINAL', True, (255, 0, 0))
    else : level_txt_2 = FONT_40.render(str(level), True, (92, 255, 209))
        
    GAME_SCREEN.blit(level_txt_1, (600, 560))
    GAME_SCREEN.blit(level_txt_2, (600, 600))
    

# 게임 종료 여부 확인
def calc_game_over():
    global ENDING_SCREEN
    game_over_check = 0
    for element in FIELD[0]:
        if element != 0 and element != 9: # 0: 빈 공간, 9: 벽
            game_over_check += 1
    if game_over_check > 0:
        ENDING_SCREEN = True

# 게임 시작 화면 그리기
def draw_intro():
    GAME_SCREEN.fill((0, 0, 0))
    game_name_txt = FONT_72.render("N - o ris", True, (255, 255, 255))
    copyright_display_txt = FONT_40.render("origin : bada1350,  ROM Hack : hje1072", True, (255, 255, 0))
    how_to_play_txt_1 = FONT_40.render("[조작 방법]", True, (255, 255, 255))
    how_to_play_txt_2 = FONT_40.render("이동 - 방향키(왼쪽/오른쪽/아래)", True, (255, 255, 255))
    how_to_play_txt_3 = FONT_40.render("테트로미노 회전 - 스페이스 바", True, (255, 255, 255))
    how_to_play_txt_4 = FONT_40.render("게임 종료 - q", True, (255, 255, 255))
    game_start_txt = FONT_40.render("PRESS ANY KEY TO START", True, (255, 255, 255))
    
    GAME_SCREEN.blit(game_name_txt, (50, 150))
    GAME_SCREEN.blit(copyright_display_txt, (50, 230))
    GAME_SCREEN.blit(how_to_play_txt_1, (50, 380))
    GAME_SCREEN.blit(how_to_play_txt_2, (50, 440))
    GAME_SCREEN.blit(how_to_play_txt_3, (50, 500))
    GAME_SCREEN.blit(how_to_play_txt_4, (50, 560))
    GAME_SCREEN.blit(game_start_txt, (160, 720))

# 게임 결과 화면 그리기
def draw_ending():
    GAME_SCREEN.fill((0, 0, 0))
    game_score_txt_1 = FONT_104.render("SCORE", True, (255, 255, 0))
    game_score_txt_2 = FONT_104.render(str(score), True, (255, 255, 255))
    game_end_txt = FONT_40.render("PRESS <Q> TO QUIT", True, (255, 255, 255))
    
    GAME_SCREEN.blit(game_score_txt_1, (230, 250))
    GAME_SCREEN.blit(game_score_txt_2, (230, 380))
    GAME_SCREEN.blit(game_end_txt, (220, 720))
    

WIDTH = 800
HEIGHT = 800


TETROMINO_BLOCK = [
    [O_1MINO], #1레벨
    [I_2MINO], #2레벨
    [L_3MINO, I_3MINO], #3레벨
    [L_TETROMINO, J_TETROMINO, T_TETROMINO, Z_TETROMINO, S_TETROMINO, O_TETROMINO, I_TETROMINO], #4레벨
    [F1_5OMINO, F2_5OMINO, I_5OMINO, L1_5OMINO, L2_5OMINO, N1_5OMINO, N2_5OMINO, P1_5OMINO, P2_5OMINO, T_5OMINO, U_5OMINO, V_5OMINO, W_5OMINO, X_5OMINO, Y1_5OMINO, Y2_5OMINO, Z1_5OMINO, Z2_5OMINO] #5레벨    
    ]



#다양한 색깔.
TETROMINO_COLOR = [(255, 128, 0), (0, 0, 255), (128, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 128, 255)]


CELL_SIZE = 40      # 필드를 구성하는 셀의 크기
WALL_ROW = 18       # 필드 행의 개수
WALL_COL = 12       # 필드 열의 개수
GRID_ROW = 20       # 격자 무늬 행의 개수
GRID_COL = 14       # 격자 무늬 열의 개수
TIME_INTERVAL = 10  # 테트로미노 하강 간격

time_count = 0      # 테트로미노 하강 속도 조절. tetromino_descent() 함수 참고
score = 0

#점수에 따라 갱신됨
level = 1
exp = 200


#블록 이동 딜레이
#블록 키보드로 이동시킬 때 너무 급격한 변화를 막아주기 위해 약간의 딜레이를 넣어주었음 
delay_time = 0

TETROMINO_NOW = Tetromino()
TETROMINO_NEXT = Tetromino()

GAME_INTRO = True
GAME_RUNNING = True
ENDING_SCREEN = False

# 게임 필드 각각의 셀에 ID 부여 - 0: 빈 공간, 1 ~ 7: 테트로미노, 9: 벽
FIELD = []
for y in range(WALL_ROW):
    if y != WALL_ROW - 1:
        field_list = []
        for x in range(WALL_COL):
            if x == 0 or x == 11:
                field_list.append(9)
            else:
                field_list.append(0)
    else:
        field_list = []
        for x in range(WALL_COL):
            field_list.append(9)
    FIELD.append(field_list)

pg.init()
pg.display.set_caption('N-ORIS')
GAME_SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.key.set_repeat(50, 200)

FONT_40 = pg.font.Font("nanum-gothic/NanumGothic.ttf", 40)
FONT_72 = pg.font.Font("nanum-gothic/NanumGothic.ttf", 72)
FONT_104 = pg.font.Font("nanum-gothic/NanumGothic.ttf", 104)

# 메인 게임 루프
GAME_RUNNING = True
while GAME_RUNNING:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME_RUNNING = False
        elif event.type == pg.KEYDOWN:
            GAME_INTRO = False
            # q를 눌러 게임 종료
            if event.key == pg.K_q:
                GAME_RUNNING = False
            # 스페이스 바를 눌러 블록 회전
            elif event.key == pg.K_SPACE:
                overlap = overlap_check(TETROMINO_NOW, (TETROMINO_NOW.turnCount + 1) % 4, TETROMINO_NOW.xpos, TETROMINO_NOW.ypos)

                #스페이스바 꾹누르고 있으면 너무 빠르게 회전해서 막아주기.
                if time.time() - delay_time < 0.1 : pass
                elif overlap == False:
                    TETROMINO_NOW.turnCount += 1
                    TETROMINO_NOW.turn = TETROMINO_NOW.turnCount % 4
                    TETROMINO_NOW.form = TETROMINO_NOW.form = TETROMINO_NOW.type[TETROMINO_NOW.turn]

                    #회전 딜레이 확인용
                    delay_time = time.time()
                    
                    
            # 방향키 아래 버튼을 눌러 테트로미노 블록 하강 이동
            elif event.key == pg.K_DOWN:
                overlap = overlap_check(TETROMINO_NOW, TETROMINO_NOW.turn, TETROMINO_NOW.xpos, TETROMINO_NOW.ypos + 1)
                
                if time.time() - delay_time < 0.1 : pass
                elif overlap == False:
                    TETROMINO_NOW.ypos += 1

                    #회전 딜레이 확인용
                    delay_time = time.time()

                    
            # 방향키 왼쪽 버튼을 눌러 테트로미노 블록 왼쪽 이동
            elif event.key == pg.K_LEFT:
                overlap = overlap_check(TETROMINO_NOW, TETROMINO_NOW.turn, TETROMINO_NOW.xpos - 1, TETROMINO_NOW.ypos)
                
                if time.time() - delay_time < 0.1 : pass
                elif overlap == False:
                    TETROMINO_NOW.xpos -= 1

                    #회전 딜레이 확인용
                    delay_time = time.time()

                    
            # 방향키 오른쪽 버튼을 눌러 테트로미노 블록 오른쪽 이동
            elif event.key == pg.K_RIGHT:
                overlap = overlap_check(TETROMINO_NOW, TETROMINO_NOW.turn, TETROMINO_NOW.xpos + 1, TETROMINO_NOW.ypos)
                
                if time.time() - delay_time < 0.1 : pass
                elif overlap == False:
                    TETROMINO_NOW.xpos += 1

                    #회전 딜레이 확인용
                    delay_time = time.time()
            else:
                pass
        else:
            pass
    
    if ENDING_SCREEN == False:
        if GAME_INTRO == True:
            draw_intro()
        else:
            # 게임 종료 여부 확인
            calc_game_over()
            
            # 배경 그리기
            draw_background()

            # 테트로미노 그리기
            TETROMINO_NOW.draw()
            
            # 다음 테트로미노 미리보기
            next_tetromino_preview()
            
            # 오브젝트 계산
            tetromino_descent()
            score_up()
            draw_score()
    else:
        draw_ending()

    # 화면 업데이트 및 업데이트 간격 설정
    pg.display.update()
    time.sleep(0.03)
pg.quit()
