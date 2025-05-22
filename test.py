H, W = map(int, input().split())
print(H, W)

#外壁を含めた全体図を作る
kingdom_map = []

#北の外壁を設置
sn_wall = []
for _ in range(W + 2):
    sn_wall.append(".")
kingdom_map.append(sn_wall)

#東西の外壁を設置
ew_wall = ["."]

#国内エリアを描写
for _ in range(H):
    coloum = list(input())
    coloum_sum = ew_wall + coloum + ew_wall
    kingdom_map.append(coloum_sum)

#南の外壁を設置
kingdom_map.append(sn_wall)
print(kingdom_map)

#順番に湖を探していき、その座標をリストに格納していく
#狙い：いきなり二重for文で湖を見つけながら、再帰処理をしてもいいが、
#重い処理が重なりすぎてしまうため、ランタイムエラーが発生すると思う
h_lake = []  #湖の縦座標
w_lake = []  #湖の横座標
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if kingdom_map[i][j] == "#":
            h_lake.append(i)
            w_lake.append(j)

#ショッピングモールを建てたところから上下左右に湖があるかどうかを調べ、
#一か所ピックアップして、そこから湖を見つけてはその座標を控えていく幅優先探索を取る
for h, w in zip(h_lake, w_lake):
    pos = []  #スタート位置と移動回数を設定
    kingdom_map[h][w] = "."  #探索済みとして湖を陸地に変換
    if kingdom_map[h][w + 1] == "#":  #右に探索
        pos.append([h, w + 1, 0])
    elif kingdom_map[h + 1][w] == "#":  #下に探索
        pos.append([h + 1, w, 0])
    elif kingdom_map[h][w - 1] == "#":  #左に探索
        pos.append([h, w - 1, 0])
    elif kingdom_map[h - 1][w] == "#":  #上に探索
        pos.append([h - 1, w, 0])
    print(pos)


        
    while len(pos) > 0:
        y, x, moves_num = pos.pop(0)
        
        kingdom_map[y][x] = "."  #探索済みとして湖を陸地に変換
        if kingdom_map[y][x + 1] == "#":  #右に探索
            pos.append([y, x + 1, moves_num + 1])
        elif kingdom_map[y + 1][x] == "#":  #下に探索
            pos.append([y + 1, x, moves_num + 1])
        elif kingdom_map[y][x - 1] == "#":  #左に探索
            pos.append([y, x - 1, moves_num + 1])
        elif kingdom_map[y - 1][x] == "#":  #上に探索
            pos.append([y - 1, x, moves_num + 1])
    print(moves_num)

        
        




    