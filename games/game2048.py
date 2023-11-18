import pygame

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    '-1': (200, 200, 200),
    '2': (130, 177, 255),
    '4': (68, 138, 255),
    '8': (41, 121, 255),
    '16': (41, 98, 255),
    '32': (167, 255, 235),
    '64': (100, 255, 218),
    '128': (29, 233, 182),
    '256': (0, 191, 165),
    '512': (132, 255, 255),
    '1024': (24, 255, 255),
    '2048': (0, 229, 255),
}

board= [[-1, 2, -1, -1],
         [-1, -1, -1, -1],
         [-1, -1, -1, -1],
         [-1, -1, -1, -1]]

#화면 관련 설정
size = (500, 500)
screen = pygame.display.set_mode(size)

def initScreen():
    screen.fill(colors['white'])
    pygame.display.update()

def addNewBlock():
    canSet = False

    while !canSet:
        randomX = random.randint(0,3)
        randomY = random.randint(0,3)

        if board[randomX][randomY] == -1:
            canSet = True

    board[randomX][randomY]  = 2 if random.randint(1, 10) < 10 else 4


#게임 진행 flag 변수
isGameRunning = True

def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
                return

                def setEventListener():
                    global isGameRunning
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_q:
                                isGameRunning = False
                            elif event == pygame.K_DOWN:
                                print("아래")
                            elif event == pygame.K_UP:
                                print("위")
                            elif event == pygame.K_RIGHT:
                                print("오른쪽")
                            elif event == pygame.K_LEFT:
                                print("왼쪽")

def drawDisplay():
    global screen

    baseX = 35
    baseY = 35
    blockHeight = 100
    blockWidth = 100
    margin = 10

    for i in range(4):
        for j in range(4):
            x = (blockWidth + margin) * j + baseX
            y = (blockWidth + margin) * i + baseY
            data = str(board[i][j])
            if data == '-1':
               pygame.draw.rect(screen, colors[data], [x, y, blockHeight, blockWidth], 2)
            else:
             pygame.draw.rect(screen, colors[data], [x, y, blockHeight, blockWidth], 2)

        pygame.display.flip()


def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")

    while isGameRunning:
        setEventListener()
        drawDisplay()

    pygame.quit()

run2048()
