from meu_grafo import MeuGrafo

# Grafo da Paraíba
lista = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
g_p = MeuGrafo(lista)
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'C', 'P')
g_p.adicionaAresta('a5', 'C', 'P')
g_p.adicionaAresta('a6', 'C', 'M')
g_p.adicionaAresta('a7', 'C', 'T')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

print(g_p.vertices_nao_adjacentes())
print(g_p.ha_laco())
print(g_p.ha_paralelas())
print(g_p.eh_completo())
print(g_p.grau("C"))
print(g_p.arestas_sobre_vertice("C"))