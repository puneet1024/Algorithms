def nge(li):
    st = []
    st.append(li[0])
    for i in range(1,len(li)-1):
        while len(st)>0 and li[i] > st[-1] :
            print(str(st[-1]) + " -> " + str(li[i]))
            st.pop()
        st.append(li[i])


nge([5,3,2,10,7,1,4,12,6])