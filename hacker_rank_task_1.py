class Paint:

    def __init__(self, row, col, arr):
        self.ROW = row
        self.COL = col
        self.arr = arr

    def visit(self, i, j, visited):
        ele = self.arr[i][j]
        for k in range(i,self.ROW):
            for l in range(j, self.COL):
               if self.arr[k][l]==ele:
                   visited[k][l]=True
                   v=l
                   if l>0 and self.arr[k][l-1]==ele and not visited[k][l-1]:
                       self.visit(k, l-1, visited)
                   if k>0 and self.arr[k-1][l]==ele and not visited[k-1][l]:
                       self.visit(k-1, l, visited)
               elif l>=v:
                   break
    # 2D matrix
    def count_cells(self):
        # Make an array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

        # Initialize count as 0 and travese
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell value false then not visited yet
                # then visit
                if visited[i][j] == False:
                    # Visit all cells in the array
                    self.visit(i, j, visited)
                    print(visited)
                    count += 1

        return count


# arr = ["aabba", "aabba", "aaacb"]
# arr = ['aaaba', 'ababa', 'aaaca']
arr = ['aaaaa', 'aaaaa', 'aaaaa']

row = len(arr)
col = len(arr[0])

p = Paint(row, col, arr)

# print (p.count_cells())


def convertTo2dArray(picture):
    arr = []
    for p in picture:
        arr.append([s for s in p])

    return arr


def visited2dArray(arr):
    visited = []
    for i in range(len(arr)):
        visited.append([False for j in range(len(arr[i]))])

    return visited


def DFS(pic, visited, i, j, h, w):
    visited[i][j] = True
    i_ = [i + 1, i - 1, i, i]
    # i for vertical
    j_ = [j, j, j + 1, j - 1]
    # j for horizontal
    for ind in range(4):
        if 0 <= i_[ind] < h and 0 <= j_[ind] < w:
            if not visited[i_[ind]][j_[ind]] and pic[i_[ind]][j_[ind]] == pic[i][j]:
                DFS(pic, visited, i_[ind], j_[ind], h, w)


def strokesRequired(picture):
    # Write your code here
    pic = convertTo2dArray(picture)
    # print(pic)
    h = len(pic)
    w = len(pic[0])
    visited = visited2dArray(pic)
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                DFS(pic, visited, i, j, h, w)
                count += 1
    return count


# print(strokesRequired(['aabba', 'aabba', 'aaacb']))
# print(strokesRequired(['aaaba', 'aaaaa', 'aaaca']))
print(strokesRequired(['aaaaa', 'aaaaa', 'aaaaa']))




