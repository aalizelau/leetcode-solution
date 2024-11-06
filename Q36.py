class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #creates a list of 9 empty sets
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        #extract num in board 
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == ".":
                    continue 
                # check for duplicate in row
                if num in rows[row]:
                    return False
                rows[row].add(num)
                #check for duplicate in column
                if num in columns[column]:
                    return False
                columns[column].add(num)
                #check for duplicate sub-boxes 
                box_id = row//3 *3 + column//3
                if num in boxes[box_id]:
                    return False
                boxes[box_id].add(num)
        return True

            
        