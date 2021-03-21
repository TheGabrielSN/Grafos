from meu_grafo import MeuGrafo

# Grafo da Paraíba
lista = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
g_p = MeuGrafo(lista)
#g_p.adicionaAresta('a0', 'C', 'C')
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

#print(g_p.ha_ciclo())
#print(g_p.caminho(1))
#print(g_p.caminho(2))
#print(g_p.caminho(3))
#print(g_p.caminho(4))
#print(g_p.conexo())

#-----------------------------------------------------------------------------#

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

#print(g_nd.ha_ciclo())
#print(g_nd.caminho(1))
#print(g_nd.caminho(2))
#print(g_nd.caminho(3))
#print(g_nd.caminho(4))
#print(g_nd.caminho(5))
#print(g_nd.caminho(6))
#print(g_nd.caminho(7))
#print(g_nd.caminho(8))
#print(g_nd.caminho(9))
#print(g_nd.conexo())

g2 = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'])
g2.adicionaAresta('1','A','B')
g2.adicionaAresta('2','B','A')
g2.adicionaAresta('3','A','B')
g2.adicionaAresta('4','B','B')

g2.adicionaAresta('5','C','D')
g2.adicionaAresta('6','D','C')
g2.adicionaAresta('7','C','D')
g2.adicionaAresta('8','D','D')

g2.adicionaAresta('9','E','F')
g2.adicionaAresta('10','F','G')
g2.adicionaAresta('11','G','E')
g2.adicionaAresta('12','F','H')
g2.adicionaAresta('13','G','I')
g2.adicionaAresta('14','E','I')

g2.adicionaAresta('15','J','K')
g2.adicionaAresta('16','K','L')
g2.adicionaAresta('17','M','L')
g2.adicionaAresta('18','M','N')
g2.adicionaAresta('19','O','N')
g2.adicionaAresta('20','O','P')
g2.adicionaAresta('21','Q','P')
g2.adicionaAresta('22','Q','R')
g2.adicionaAresta('23','S','R')
g2.adicionaAresta('24','S','J')

#
#print("CONEXO:",g2.conexo())
#print("CICLO:",g2.ha_ciclo())
#for i in range(1,15):
#    try:
#        print(f"CAMINHO {i} : {g2.caminho(i)}")
#    except Exception as e:
#        print(e)

k5 = MeuGrafo(['A','B','C','D','E'])
k5.adicionaAresta('1','A','B')
k5.adicionaAresta('5','A','C')
k5.adicionaAresta('6','A','D')
k5.adicionaAresta('7','A','E')
k5.adicionaAresta('2','B','C')
k5.adicionaAresta('8','B','D')
k5.adicionaAresta('9','B','E')
k5.adicionaAresta('3','C','D')
k5.adicionaAresta('10','C','E')
k5.adicionaAresta('4','D','E')

#print("CONEXO,k5.conexo()")
#print("CICLO:",k5.ha_ciclo())
#for i in range(1,10):
#    try:
#        print(f"CAMINHO {i} : {k5.caminho(i)}")
#    except Exception as e:
#        print(e)
#






