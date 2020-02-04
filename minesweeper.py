class Game:
    g_board = [];
    p_board = [];
    n = 6;
    
    def init_board(self, b):
        for i in range(self.n):
            tmp = [];
            for j in range(self.n):
                tmp.append('▓');
            b.append(tmp);

    def place_bombs(self):
        #todo randomize
        self.g_board[0][1] = 'X'
        self.g_board[1][3] = 'X'
        self.g_board[3][1] = 'X'
        self.g_board[3][4] = 'X'

    def p_input(self):
        print('\nPlease enter guess: ', end='');
        ret = input().split(',');
        ret[0] = int(ret[0]);
        ret[1] = int(ret[1]);
        return ret


    def print_board(self, b):
        for i in range(self.n):
            for j in range(self.n):
                print(b[i][j], end='');
            print();

    def print_boards(self):
        self.print_board(self.g_board);
        print();
        self.print_board(self.p_board);


    def __init__(self):
        self.init_board(self.g_board);
        self.init_board(self.p_board);
        self.place_bombs();
        self.game_loop();

    def is_hit(self, guess):
        return self.g_board[guess[0]][guess[1]] == 'X'
    
    def find_adj(self, guess):
        count = 0;
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                curr = (guess[0] + i, guess[1] + j);
                if not self.oob(curr):
                    if self.is_hit(curr):
                        count += 1;

        if count == 0:
            return '_';
        else:
            return str(count);


    def oob(self, coord):
        if coord[0] < 0 or coord[0] > (self.n-1):
            return True;
        if coord[1] < 0 or coord[1] > (self.n-1):
            return True;
        return False;

    def won(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.p_board[i][j] == '▓' and self.g_board[i][j] != 'X':
                    return False;
        return True;

    def expand(self, guess):
        stop = False;
        for i in range(self.n):
            for j in range(-i, i+1):
                for k in range(-i, i+1):
                    curr = (guess[0] + j, guess[1] + k)
                    if not self.oob(curr):
                        if self.is_hit(curr):
                            stop = True
                        else:
                            self.p_board[curr[0]][curr[1]] = self.find_adj(curr);
            if stop == True:
                break;


    def check_guess(self, guess):
        if self.is_hit(guess):
            return True;
        self.expand(guess);

    def game_loop(self):
        while(True):
            #self.print_boards();
            self.print_board(self.p_board);
            guess = self.p_input();
            if self.check_guess(guess):
                print("Game over!");
                return;
            if self.won():
                self.print_board(self.p_board);
                print("You win!");
                return;


g = Game();
