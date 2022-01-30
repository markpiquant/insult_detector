def censure(dict):
    """
    Entrée : {"tweet":[liste des insultes du tweet]}
    Sortie : [liste des tweets censurés]
    """
    LL=[]
    for tweet in dict.keys():
        L=[]
        for elt in dict[tweet]:
            s=""
            s+=elt[0]
            for i in range(len(elt)-1):
                s+="*"
            
            L.append(s)
        m=tweet
        for i in range(len(L)):
            m=m.replace(dict[tweet][i],L[i])
        LL.append(m)
    return LL