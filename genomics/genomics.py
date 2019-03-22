"""
Student template code for Project 4
Student will implement five functions:

build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)
compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)


"""

import math


######################################################
# this program have four functions, will implement compute a common class
# of scoring matrix compute the alignment matrix respectively

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    build up scoring matrix table corresponding to alignment
    """
    score_matrix = dict()
    content = set(alphabet)
    content.add('-')
    print content, score_matrix
    for row in content:
        score_matrix[row] = dict()
        for col in content:
            if (row == '-') or (col == '-'):
                score_matrix[row][col] = dash_score
            elif row == col:
                score_matrix[row][col] = diag_score
            else:
                score_matrix[row][col] = off_diag_score
    return score_matrix


# alphabet = set(['A' ,'C', 'G', 'T'])
# diag_score = 5
# off_diag_score = 2
# dash_score = -4
# s_matrix = build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
# print s_matrix
# print s_matrix['A']['-']
# print

# build_scoring_matrix(set(['A', 'C', 'T', 'G']), 6, 2, -4)
# {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}
# {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': 6, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common
    alphabet with the scoring matrix scoring_matrix.

    The function computes and returns the alignment matrix for seq_x and seq_y
    global_flag indicates global or local pairwise alignment
    """
    #    mrow = len(seq_x)
    #    ncol = len(seq_y)

    dptable = [[0 for dummy_col in range(len(seq_y) + 1)] for dummy_row in range(len(seq_x) + 1)]
    dptable[0][0] = 0

    for idx1 in range(1, len(seq_x) + 1):
        dptable[idx1][0] = dptable[idx1 - 1][0] + scoring_matrix[seq_x[idx1 - 1]]['-']
        if not global_flag:
            dptable[idx1][0] = max(0, dptable[idx1][0])
    for idx2 in range(1, len(seq_y) + 1):
        dptable[0][idx2] = dptable[0][idx2 - 1] + scoring_matrix['-'][seq_y[idx2 - 1]]
        if not global_flag:
            dptable[0][idx2] = max(0, dptable[0][idx2])
    for idxx in range(1, len(seq_x) + 1):
        for idxy in range(1, len(seq_y) + 1):
            fr_diag = dptable[idxx - 1][idxy - 1] + scoring_matrix[seq_x[idxx - 1]][seq_y[idxy - 1]]
            fr_row = dptable[idxx - 1][idxy] + scoring_matrix[seq_x[idxx - 1]]['-']
            fr_col = dptable[idxx][idxy - 1] + scoring_matrix['-'][seq_y[idxy - 1]]
            dptable[idxx][idxy] = max(fr_diag, fr_row, fr_col)
            if not global_flag:
                dptable[idxx][idxy] = max(0, dptable[idxx][idxy])

    return dptable


#
# global_flag = True
# seq_x = 'AC'
# seq_y = 'TAG'
# out = compute_alignment_matrix(seq_x, seq_y, s_matrix, global_flag)
# print "out=", out
# print

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common
    alphabet with the scoring matrix scoring_matrix.
    This function computes a global alignment of seq_x and seq_y using the
    global alignment matrix alignment_matrix.

    Start from bottom right cell and end in top left cell.

    The function returns a tuple of the form (score, align_x, align_y)
    """

    idxi, idxj = len(seq_x), len(seq_y)
    # print idxi, idxj
    score = alignment_matrix[idxi][idxj]
    align_x, align_y = '', ''
    # print "len alignment_matrix", len(alignment_matrix)

    # print "end idx", idxi, idxj, score
    while idxi and idxj:
        if alignment_matrix[idxi][idxj] == alignment_matrix[idxi - 1][idxj - 1] + scoring_matrix[seq_x[idxi - 1]][
            seq_y[idxj - 1]]:
            align_x += seq_x[idxi - 1]
            align_y += seq_y[idxj - 1]
            idxi -= 1
            idxj -= 1
            print "align_xy1", align_x, align_y
        else:
            if alignment_matrix[idxi][idxj] == alignment_matrix[idxi - 1][idxj] + scoring_matrix[seq_x[idxi - 1]]['-']:
                align_x += seq_x[idxi - 1]
                align_y += '-'
                idxi -= 1
                print "align_xy2", align_x, align_y
            else:
                align_x += '-'
                align_y += seq_y[idxj - 1]
                idxj -= 1

                print "align_xy3", align_x, align_y
        print "end idx", idxi, idxj
    while idxi:
        align_x += seq_x[idxi - 1]
        align_y += '-'
        idxi -= 1
        print "align_xy4", align_x, align_y
    while idxj:
        align_x += '-'
        align_y += seq_y[idxj - 1]
        idxj -= 1
        print "align_xy5", align_x, align_y
    align_x = align_x[::-1]
    align_y = align_y[::-1]
    return (score, align_x, align_y)


print compute_global_alignment('ACTACT', 'GGACTGCTTCTGG', {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6], [0, 1, 2, 4, 4, 6, 7, 7, 7, 7, 7, 7, 7, 7], [0, 1, 2, 4, 6, 6, 7, 9, 9, 9, 9, 9, 9, 9], [0, 1, 2, 4, 6, 8, 8, 9, 11, 11, 11, 11, 11, 11]])
#returned aligned y sequence does not include the entire original sequence: 'GGACTGCT'

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common
    alphabet with the scoring matrix scoring_matrix.
    This function computes a local alignment of seq_x and seq_y using the
    local alignment matrix alignment_matrix.

    Start from max score cell and end in any cell with 0 score.

    The function returns a tuple of the form (score, align_x, align_y)
    """
    score = float('-inf')
    align_x, align_y = '', ''
    idxi, idxj = 0, 0
    for idx in range(len(alignment_matrix)):
        for item in alignment_matrix[idx]:
            if item >= score:
                score = item
                idxi = idx
                idxj = alignment_matrix[idx].index(item)

                # print "end idx", idxi, idxj, score

    while idxi and idxj and (alignment_matrix[idxi][idxj] != 0):
        if alignment_matrix[idxi][idxj] == alignment_matrix[idxi - 1][idxj - 1] + scoring_matrix[seq_x[idxi - 1]][
            seq_y[idxj - 1]]:
            align_x += seq_x[idxi - 1]
            align_y += seq_y[idxj - 1]
            idxi -= 1
            idxj -= 1
            # print "align_xy1", align_x, align_y
        else:
            if alignment_matrix[idxi][idxj] == alignment_matrix[idxi - 1][idxj] + scoring_matrix[seq_x[idxi - 1]]['-']:
                align_x += seq_x[idxi - 1]
                align_y += '-'
                idxi -= 1
                # print "align_xy2", align_x, align_y
            else:
                align_x += '-'
                align_y += seq_y[idxj - 1]
                idxj -= 1

                # print "align_xy3", align_x, align_y
        # print "end idx", idxi, idxj
    while idxi and (alignment_matrix[idxi][0] != 0):
        align_x += seq_x[idxi - 1]
        align_y += '-'
        idxi -= 1
        # print "align_xy4", align_x, align_y
    while idxj and (alignment_matrix[0][idxj] != 0):
        align_x += '-'
        align_y += seq_y[idxj - 1]
        idxj -= 1
        # print "align_xy5", align_x, align_y
    align_x = align_x[::-1]
    align_y = align_y[::-1]
    return (score, align_x, align_y)

    print compute_local_alignment('ACTACT', 'GGACTGCTTCTGG', {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1}, 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1}, '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0}, 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1}, 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}}, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [0, 1, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6], [0, 1, 2, 4, 4, 6, 7, 7, 7, 7, 7, 7, 7, 7], [0, 1, 2, 4, 6, 6, 7, 9, 9, 9, 9, 9, 9, 9], [0, 1, 2, 4, 6, 8, 8, 9, 11, 11, 11, 11, 11, 11]])