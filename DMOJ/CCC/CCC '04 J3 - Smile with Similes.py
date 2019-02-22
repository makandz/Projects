adj_ = int(input())
nouns_ = int(input())
adj = [0 for n in range(adj_)]
nouns = [0 for n in range(nouns_)]

for b in range(adj_):
    adj[b] = input()

for a in range(nouns_):
    nouns[a] = input()
    
for a in range(nouns_):
    for b in range(adj_):
        print(adj[b] + " as " + nouns[a])