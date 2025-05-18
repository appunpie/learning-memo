H, W = map(int, input().split())
get_tree = int(input())
#print(H, W, get_tree)

#上下の外壁を準備する
y = []
for _ in range(W + max(H, W) * 2):
    y.append(0)
#左右の外壁を準備する
x = []
for _ in range(W):
    x.append(0)
#北に外壁を設置
tree_map = []
for _ in range(max(H, W)):
    tree_map.append(y)
#print(tree_map)
#東西に外壁を設置
for _ in range(H):
    a = list(map(int, input().split()))
    horizon = x + a + x
    tree_map.append(horizon)
#print(tree_map)
#南に外壁を設置
for _ in range(max(H, W)):
    tree_map.append(y)
#print(tree_map)
#一番北西の位置から順に合計値をmax_donguriにぶち込み、都度比較・更新していく
#東と南の方向について調べれば、ok
max_donguri = -1  #初期位置は紛らわしくないように-1とする
for h in range(max(H, W), max(H, W) + H):
    for w in range(max(H, W), max(H, W) + H):
        h_donguri_sum = 0  #一列の合計
        w_donguri_sum = 0  #一列の合計
        for n in range(get_tree):
            h_donguri_sum += tree_map[h][w + n]
            w_donguri_sum += tree_map[h + n][w]
        if h_donguri_sum >= w_donguri_sum:
            if h_donguri_sum > max_donguri:
                max_donguri = h_donguri_sum
        else:
            if w_donguri_sum > max_donguri:
                max_donguri = w_donguri_sum
print(max_donguri)






