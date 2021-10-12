#segmentation_tree
#list(length == N)

INF = 2**30
N_bit = 2 ** (N - 1).bit_length()
dat = [[INF,INF]] * (2 * N_bit)
 
#index = k を位置情報付きの x に更新。節点にて同じ数字があった場合はindexが小さいほうを選択する
def update(k, x):
    k += N_bit -1
    dat[k] = [x ,k - N_bit + 1]
    while k > 0:
        k = (k - 1) // 2
        if dat[2 * k + 1][0] == dat[2 * k + 2][0]:
            dat[k] = [dat[2 * k + 1][0],min(dat[2 * k + 1][1],dat[2 * k + 2][1])]
        elif dat[2 * k + 1][0] < dat[2 * k + 2][0]:
            dat[k] = dat[2 * k + 1]
        else:
            dat[k] = dat[2 * k + 2]
 
#minValue & index of [l,r)
def query(l, r):
    L = l + N_bit
    R = r + N_bit
    score = INF
    pos = INF
    while L < R :
        if R & 1:
            R -= 1
            if score == dat[R-1][0]:
                pos = min(pos,dat[R-1][1])
            if score > dat[R-1][0]:
                score,pos = dat[R-1]
    
        if L & 1:
            if score == dat[L-1][0]:
                pos = min(pos,dat[L-1][1])
            if score > dat[L-1][0]:
                score,pos = dat[L-1]
            L += 1
        L >>= 1
        R >>= 1
    return [score,pos]
