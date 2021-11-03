import random

class Buscaminas():
    def __init__(self,rows,cols,bombs):
        self.rows = rows
        self.cols = cols
        self. bombs = bombs
        self.board = []
        self.show = []
        self.crear_board()

        self.crear_show()
        self.show_board()

    def crear_show(self):
        for rows in range(self.rows):
            fila = []
            for cols in range(self.cols):
                fila.append('#')
            self.show.append(fila)

    def crear_board(self):
        for rows in range(self.rows):
            fila = []
            for cols in range(self.cols):
                fila.append(' ')
            self.board.append(fila)
        self.llenar_board_bombs()
        self.llenar_board_nums()

    def llenar_board_bombs(self):
        i = 0
        while i < self.bombs:
            row = random.randint(0,self.rows-1)
            col = random.randint(0,self.cols-1)
            if self.board[row][col] == ' ':
                self.board[row][col] = 'B'
                i += 1

    def llenar_board_nums(self):
        
        for row in range(self.rows):
            for col in range(self.cols):
                i = 0
                check1 = [-1,1]
                check2 = [-1,0,1]

                if row == 0:          # si es la primer fila, no revisar la de arriba (xq no existe)
                    check1 = [1]
                elif row == self.rows-1:   # si es la ultima fila, no revisar la de abajo
                    check1 = [-1] 

                if col == 0:              # si es la primer columna, no revisar la anterior
                    check2 = [0,1]
                elif col == self.cols-1:    # si es la ultima columna, no revisar la siguiente
                    check2 = [-1,0]


                for fila in check1:     #fila anterior
                    for vecino1 in check2:    #revisa los 3 vecinos de arriba y abajo
                        #print(self.board[row+fila][col+vecino1])


                        if self.board[row+fila][col+vecino1] == 'B':
                            i += 1
                for vecino2 in check2:    #revisa los vecinos de los costados
                    if self.board[row][col+vecino2] == 'B':
                        i += 1
                if i != 0 and self.board[row][col] != 'B':
                    self.board[row][col] = str(i)
            


            #if self.board[row][col] == ' ':
            #    self.board[row][col] = 'B'
            #    i += 1

    def show_board(self):
        for fila in range(len(self.board)):
            print(self.board[fila],'      ',self.show[fila])
        
        

    def win(self):
        bombs_f = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 'B' and self.show[row][col] == 'F':
                    bombs_f += 1
        return bombs_f == self.bombs


    def lose(self):
        for row in self.show:
            if 'B' in row:
                return True
        return False

    def question(self,movs):
        mov = input('Ingrese la acción a realizar (flag o uncover): ')
        if mov not in movs:
            raise 
        row = int(input('Ingrese la coordenada de la fila deseada (comenzando en 0):' ))
        col = int(input('Ingrese la coordenada de la columna deseada (comenzando en 0):' ))
        return mov,row,col

    def play(self,mov,row,col):
        if mov == 'flag':
            self.show[row][col] = 'F'
        
        elif mov == 'uncover':
            self.show[row][col] = self.board[row][col]
        

if __name__ == '__main__':
    juego = Buscaminas(8,8,10)