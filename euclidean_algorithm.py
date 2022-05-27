def euclidean(A, B):
    if A == 0:
        return B
    if B == 0:
        return A
    # A = B*Q + R
    #Q = A//B
    R = A%B
    return euclidean(B, R)

print(euclidean(473827487823784778474774748488484383883838383838383898192839898597439594379, 30000012398219389128391829389123891289381298392829383838))