data = []
lenths = []
sum_len = 0
#把 reviews.txt 讀進來
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
#把各留言長度加進 清單lenths
for comment in data:
    lenths.append(len(comment))
#將各留言長度加總
for lenth in lenths:
    sum_len += lenth
#印出留言平均長度
print('留言的平均長度是:', sum_len / len(data))