from copy import deepcopy


def is_complete(assignment, csp):
    sum_num = 0
    for lst in csp:
        sum_num += lst.count('0')
    # print sum
    if len(assignment) == sum_num:
        return True
    return False


def get_domain_by_constraint(var, csp):
    row, col = var[0], var[1]
    my_set = set()
    all_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 1.check row
    for ele in csp[row]:
        my_set.add(int(ele))
    target_set = all_set - my_set

    # 2.check column
    my_set.clear()
    for ele in zip(*csp)[col]:
        my_set.add(int(ele))
    target_set = target_set - my_set

    # 3.check sub_cube
    my_set.clear()
    # 3.1 get sub_cube index of the variable
    pos = get_sub_cube_pos(row, col)  # up left corner pos of a sub cube
    # 3.2 enumerate each ele in the sub cube
    for i in xrange(3):  # sub cube has 3 rows
        for j in xrange(3):  # sub cube has 3 cols
            my_set.add(int(csp[pos[0] + i][pos[1] + j]))
    target_set = target_set - my_set

    return target_set


def get_sub_cube_pos(row, col):
    '''
    get up_left pos of a sub cube for a variable with pos(row,col)
    '''
    if 0 <= row <= 2:
        if 0 <= col <= 2:
            pos = (0, 0)
        elif 3 <= col <= 5:
            pos = (0, 3)
        else:
            pos = (0, 6)
    elif 3 <= row <= 5:
        if 0 <= col <= 2:
            pos = (3, 0)
        elif 3 <= col <= 5:
            pos = (3, 3)
        else:
            pos = (3, 6)
    else:
        if 0 <= col <= 2:
            pos = (6, 0)
        elif 3 <= col <= 5:
            pos = (6, 3)
        else:
            pos = (6, 6)
    return pos


def get_new_csp(csp, assignment):
    new_csp = deepcopy(csp)
    for key in assignment:
        new_csp[key[0]][key[1]] = str(assignment[key])
    return new_csp


def get_var_by_MRV(csp, assignment):
    """
    :param csp: the original csp
    :param assignment:  dict of currently assigned variables
    :return:position of the variable
    """
    new_csp = get_new_csp(csp, assignment)
    smallest_domain_size = float('inf')
    target_var = (None, None)
    target_domain = None
    for i in xrange(len(new_csp)):
        for j in xrange(len(new_csp[0])):
            if new_csp[i][j] == '0':
                var_domain = get_domain_by_constraint((i, j), new_csp)
                domain_size = len(var_domain)
                if domain_size < smallest_domain_size:
                    smallest_domain_size = domain_size
                    target_var, target_domain = (i, j), var_domain

    return target_var, target_domain


def ordered_domain(var, csp):
    pass


def is_consistent(value, var, csp, assignment):
    row, col = var[0], var[1]
    new_csp = get_new_csp(csp, assignment)
    # 1.if is consistent with row
    for i, ele in enumerate(new_csp[row]):
        if i is not col and int(ele) is value:
            return False

    # 2.if is consistent with column
    for j, ele in enumerate(zip(*new_csp)[col]):
        if j is not row and int(ele) is value:
            return False

    # 3.if is consistent with sub_cube
    up_left_pos = get_sub_cube_pos(row, col)
    for i in xrange(3):
        for j in xrange(3):
            cube_row = i + up_left_pos[0]
            cube_col = j + up_left_pos[1]
            if (var is not (cube_row, cube_col)) and int(new_csp[cube_row][cube_col]) is value:
                return False

    return True


def back_tracking(assignment, csp):
    if is_complete(assignment, csp):
        return assignment

    var, mrv_domain = get_var_by_MRV(csp, assignment)
    # for value in ordered_domain(var, csp):
    for value in mrv_domain:
        if is_consistent(value, var, csp, assignment):  # with MRV,only empty set would be unconsistent
            assignment[var] = value
            result = back_tracking(assignment, csp)
            if result is not False:
                return assignment
            del assignment[var]
    return False


def BTS(csp):
    return back_tracking({}, csp)


def alorithm(csp_str):
    sudoku_lst = [[] for i in range(9)]
    cnt = 0
    for i in xrange(9):
        for j in xrange(9):
            sudoku_lst[i].append(csp_str[cnt])
            cnt += 1
    print 'old one:' + '\r\n'
    for row in sudoku_lst:
        print row

    # solving by BTS
    result = BTS(sudoku_lst)
    print 'assignment' + str(result)

    # print result list
    for key in result:
        sudoku_lst[key[0]][key[1]] = str(result[key])
    print 'new one:' + '\r\n'
    for row in sudoku_lst:
        print row

    # format final sudoku list into string
    result_str = ''
    for i in xrange(len(sudoku_lst)):
        for j in xrange(len(sudoku_lst[0])):
            result_str += sudoku_lst[i][j]

    return result_str + ' ' + 'BTS' + '\n'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('csp_str', type=str, help='sudoku csp string')
    args = parser.parse_args()
    print args.csp_str
    # start_time = time.clock()
    test_string = '000000000302540000050301070000000004409006005023054790000000050700810000080060009'
    final_str = alorithm( args.csp_str)
    with open('output.txt', 'w') as f:
        f.write(final_str)
    # write result into txt file

#   LOOP TEST
#     correct_cnt, check_cnt = 0, 0
#     with open('sudokus_start.txt', 'r') as start_file:
#         for test_str in start_file:
#             result_str = alorithm(test_str)
#             with open('sudokus_finish.txt', 'r') as answer_file:
#                 check_str = answer_file.readlines()[check_cnt]
#                 if check_str == result_str:
#                     correct_cnt += 1
#                 check_cnt += 1
#             print('now correct num / all num ' + str(correct_cnt) + ' ' + str(check_cnt))
# print 'correct num of 400:' + str(correct_cnt)
# print "time:" + str(time.clock() - start_time)
