N = int(input())
for i in range(N):
    st = input()
    index = st.find('кот')
    if index != -1:
        print(i + 1, index + 1)
