from meu_grafo import MeuGrafo

# Grafo da Paraíba
lista = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
g_p = MeuGrafo(lista)
g_p.adicionaAresta('a0', 'C', 'C')
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'C', 'P')
g_p.adicionaAresta('a5', 'C', 'P')
g_p.adicionaAresta('a6', 'C', 'M')
g_p.adicionaAresta('a7', 'C', 'T')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')
g_p.adicionaAresta('a10', 'Z', 'Z')

print("J ->",list(g_p.bfs("J").A))
print("C ->",list(g_p.bfs("C").A))
print("E ->",list(g_p.bfs("E").A))
print("P ->",list(g_p.bfs("P").A))
print("M ->",list(g_p.bfs("M").A))
print("T ->",list(g_p.bfs("T").A))
print("Z ->",list(g_p.bfs("Z").A))

#J -> ['a1', 'a2', 'a4', 'a6', 'a7', 'a9']
#C -> ['a1', 'a2', 'a4', 'a6', 'a7', 'a9']
#E -> ['a2', 'a1', 'a4', 'a6', 'a7', 'a9']
#P -> ['a4', 'a1', 'a2', 'a6', 'a7', 'a9']
#M -> ['a6', 'a8', 'a1', 'a2', 'a4', 'a9']
#T -> ['a7', 'a8', 'a9', 'a1', 'a2', 'a4']
#Z -> ['a9', 'a7', 'a8', 'a1', 'a2', 'a4']

g_nd = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
g_nd.adicionaAresta('a1', 'A', 'B')
g_nd.adicionaAresta('a2', 'A', 'G')
g_nd.adicionaAresta('a3', 'A', 'J')
g_nd.adicionaAresta('a4', 'G', 'K')
g_nd.adicionaAresta('a5', 'J', 'K')
g_nd.adicionaAresta('a6', 'G', 'J')
g_nd.adicionaAresta('a7', 'I', 'J')
g_nd.adicionaAresta('a8', 'G', 'I')
g_nd.adicionaAresta('a9', 'G', 'H')
g_nd.adicionaAresta('a10', 'F', 'H')
g_nd.adicionaAresta('a11', 'B', 'F')
g_nd.adicionaAresta('a12', 'B', 'G')
g_nd.adicionaAresta('a13', 'B', 'C')
g_nd.adicionaAresta('a14', 'C', 'D')
g_nd.adicionaAresta('a15', 'D', 'E')
g_nd.adicionaAresta('a16', 'B', 'D')
g_nd.adicionaAresta('a17', 'B', 'E')

print(list(g_nd.bfs("A").A))
print(list(g_nd.bfs("B").A))
print(list(g_nd.bfs("C").A))
print(list(g_nd.bfs("D").A))
print(list(g_nd.bfs("E").A))
print(list(g_nd.bfs("F").A))
print(list(g_nd.bfs("G").A))
print(list(g_nd.bfs("H").A))
print(list(g_nd.bfs("I").A))
print(list(g_nd.bfs("J").A))
print(list(g_nd.bfs("K").A))
#A -> ['a1', 'a2', 'a3', 'a11', 'a13', 'a16', 'a17', 'a10', 'a4', 'a8']
#B -> ['a1', 'a11', 'a12', 'a13', 'a16', 'a17', 'a3', 'a4', 'a8', 'a9']
#C -> ['a13', 'a14', 'a1', 'a11', 'a12', 'a17', 'a3', 'a4', 'a8', 'a9']
#D -> ['a14', 'a15', 'a16', 'a1', 'a11', 'a12', 'a3', 'a4', 'a8', 'a9']
#E -> ['a15', 'a17', 'a14', 'a1', 'a11', 'a12', 'a3', 'a4', 'a8', 'a9']
#F -> ['a10', 'a11', 'a9', 'a2', 'a4', 'a6', 'a8', 'a13', 'a16', 'a17']
#G -> ['a2', 'a4', 'a6', 'a8', 'a9', 'a12', 'a11', 'a13', 'a16', 'a17']
#H -> ['a9', 'a10', 'a2', 'a4', 'a6', 'a8', 'a12', 'a13', 'a16', 'a17']
#I -> ['a7', 'a8', 'a3', 'a5', 'a1', 'a11', 'a13', 'a16', 'a17', 'a10']
#J -> ['a3', 'a5', 'a6', 'a7', 'a1', 'a11', 'a13', 'a16', 'a17', 'a10']
#K -> ['a4', 'a5', 'a2', 'a8', 'a9', 'a12', 'a11', 'a13', 'a16', 'a17']

g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'A')
g_l1.adicionaAresta('a2', 'A', 'B')
g_l1.adicionaAresta('a3', 'A', 'A')

g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l2.adicionaAresta('a1', 'A', 'B')
g_l2.adicionaAresta('a2', 'B', 'B')
g_l2.adicionaAresta('a3', 'B', 'A')

g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l3.adicionaAresta('a1', 'C', 'A')
g_l3.adicionaAresta('a2', 'C', 'C')
g_l3.adicionaAresta('a3', 'D', 'D')
g_l3.adicionaAresta('a4', 'D', 'D')

g_l4 = MeuGrafo(['D'])
g_l4.adicionaAresta('a1', 'D', 'D')

g_l5 = MeuGrafo(['C', 'D'])
g_l5.adicionaAresta('a1', 'D', 'C')
g_l5.adicionaAresta('a2', 'C', 'C')

print(list(g_l2.bfs("B").A))
print(list(g_l2.dfs("B").A))