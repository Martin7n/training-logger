with open("C:/Users/M/Desktop/1.csv", encoding="utf-8") as f:
    for i in range(20):
        print(i, repr(f.readline()))