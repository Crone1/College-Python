import sys


class Boggle(object):

    board_size = 4

    def __init__(self, file):
        '''Boggle board class constructor

        :param file: Path to the dictionary file
        :return: None'''

        self.size = Boggle.board_size
        self.board = [[' '] * self.size for _ in range(self.size)]
        self.adjacency = self.build_adjacency()
        self.words, self.prefixes = self.load_dictionary(file)

        # Points per word of given length
        points = {3: 1,
                  5: 2,
                  6: 3,
                  7: 5,
                  8: 11}

        self.points = [0 for _ in range(self.size**2)]
        #print (len(self.points))
        for i in range(len(self.points)):

            if i in points:
                #print (i)
                self.points[i] = points[i]

            else:
                #print ('l = ' + str(i))
                #print (self.points[i-1])
                self.points[i] = self.points[i - 1]

    def adjacent(self, pos):
        '''Finds all adjacent positions for a given position on the board

        :param pos: A 2-tuple giving row and column of a position
        :return: A list of positions adjacent to the given position'''

        row, col = pos
        adj = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                new_row = row + i
                new_col = col + j

                if 0 <= new_row < self.size and 0 <= new_col < self.size and not (i == j == 0):
                    adj.append((new_row, new_col))

        return adj

    def build_adjacency(self):
        '''Builds the adjacency lookup for each position on the board

        :return: A dictionary of adjacent positions for each position on the board'''

        adjacency = dict()
        for row in range(0, self.size):

            for col in range(0, self.size):
                adjacency[(row, col)] = self.adjacent((row, col))

        return adjacency

    def load_dictionary(self, file):
        '''Loads a dictionary file into Boggle object's word list

        :param name: Path to the dictionary file
        :return: None'''

        prefixes = set()
        with open(file, 'r') as f:

            lines = [line.strip().upper() for line in f.readlines()]

            words = set(word for word in lines if len(word) > 2)

            for line in lines:
                for i in range(len(line)):
                    prefixes.add(line[:i])

        return words, prefixes

    def get_letter(self, pos):
        '''Gets the letter at a given position

        :param pos: A 2-tuple giving row and column location of a position
        :return: A letter at the given position'''

        return self.board[pos[0]][pos[1]]

    def set_board(self, letters):
        '''Sets the letters on the board

        :param letters: A string giving the letters, row by row
        :return: None'''

        for row in range(self.size):
            index = row * self.size
            row_letters = letters[index:index + self.size]

            for col, letter in enumerate(row_letters):
                self.board[row][col] = letter

    def find_words(self):
        '''Finds all words on the board

        :return: A set of words found on the board'''

        words = set()
        for row in range(self.size):

            for col in range(self.size):
                words |= self.find_words_pos((row, col))

        return words

    def find_words_pos(self, pos):
        '''Finds words starting at a given position on the board

        :param pos: A 2-tuple giving row and column on the board
        :return: A set of words starting at the given position'''

        stack = [(n, [pos], self.get_letter(pos)) for n in self.adjacency[pos]]
        words = set()

        while stack:
            curr, path, chars = stack.pop()
            curr_char = self.get_letter(curr)
            curr_chars = chars + curr_char

            # Check if path forms a word
            if curr_chars in self.words:
                words.add(curr_chars)

            # Check if path forms the prefix of a word
            if curr_chars in self.prefixes:
                # Get adjacent positions
                curr_adj = self.adjacency[curr]

                # Check if adjacent positions have already been visited
                stack.extend([(n, path + [curr], curr_chars)
                              for n in curr_adj if n not in path])

        return words

    def score(self):
        score = 0
        words = self.find_words()

        for word in words:
            score += self.points[len(word)]

        return score


if __name__ == '__main__':
    b = Boggle(sys.argv[2])
    with open(sys.argv[1]) as f:

        for line in f.readlines():
            b.set_board(line.strip().upper())
            # print(b.find_words())
            print('Possible points: {}'.format(b.score()))
