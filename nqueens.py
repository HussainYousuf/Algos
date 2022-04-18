def main(rows=[None]*4, cur_row=0):
    if(cur_row >= len(rows)):
        print(rows)
    else:
        for col in range(len(rows)):
            legal = True
            for row in range(cur_row):
                if(rows[row] == col or rows[row] == col - cur_row + row or rows[row] == col + cur_row - row):
                    legal = False
                    break
            if(legal):
                rows[cur_row] = col
                main(rows, cur_row + 1)


main()
