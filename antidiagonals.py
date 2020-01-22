
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    n = max(1, n)
    return list(l[i:i + n] for i in range(0, len(l), n))

T = int(input())
if(1 <= T <= 30):
    N = int(input())
    inputlist = []
    for i in range(0,N):
        for j in range(0,N):
            val = input()
            inputlist.append(val)
    print(chunks(inputlist,N))

    # for i in range(0,N):
    #     for j in range(0,N):
    #         print(inputlist[j])
