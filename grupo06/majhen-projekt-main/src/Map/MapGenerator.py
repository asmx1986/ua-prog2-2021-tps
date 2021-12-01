class Map:
    def __init__(self, length, width):
        self._map = self.make_map(length, width)
        self._list = self.blank_space_list(length, width)

    def blank_space_list(self, length, width):
        _list = []
        blank = []

        for _ in range(0, width):
            blank.append(" ")
        for _ in range(0, length):
            blank2 = blank[:]
            _list.append(blank2)
        return _list

    def row(self, width, coordinate):
        k = 0
        line = ""
        for _ in range(0, width):
            line = line + "| {"+f"self._list[{coordinate}][{k}]"+"} "

            k = k+1
        line = line + "|"
        
        return line

    def s_row(self, length):
        line = ""
        for _ in range(0, length):
            line = line + "+---"
        line = line + "+"

        return line

    def make_map(self, length, width):
        big_line = ""

        for y_coordinate in range(0, length):
            big_line = big_line + self.s_row(width) + "\\n"
            big_line = big_line + self.row(width, y_coordinate) + "\\n"

        big_line = big_line + self.s_row(width)
        return big_line

    def assign_event(self, x, y, concurrency):
        self._list[x][y] = concurrency

    def assign_value(self, y, x, value):
        self._list[y][x] = value

    def print_map(self):
        exec("print(f'" + self._map + "')")
