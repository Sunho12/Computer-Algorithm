INF = int (1e9+7)

def floyd_warshall(dist,length):
    pred = [[-1]* length for _ in range(length)]
    for r in range(length):
        for p in range(length):
            for q in range(length):
                if dist[p][q] > dist[p][r] + dist[r][q]:
                    dist[p][q] = dist[p][r] + dist[r][q]
                    pred[p][q] = r
    print_dist(dist, pred, length)

def print_dist(dist, pred, length):
    for p in range(length):
      for q in range(length):
        if p != q and dist[p][q] != INF:
            path = [q]
            while pred[p][path[-1]] != -1:
                path.append(pred[p][path[-1]])
            path.append(p)
            path.reverse()
            #print(f"shortest path from {p} to {q}: {path}")
        
        if p==1 and q==3:
            print(f"shortest path from {p} to {q}: {path}")
        if p==0 and q==2:
            print(f"shortest path from {p} to {q}: {path}")
#test code
W = [[0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0]]
floyd_warshall(W,len(W[0])) 