import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafo de segunda opção
        self.gf = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.gf.adicionaAresta('a1', 'A', 'B')
        self.gf.adicionaAresta('a2', 'A', 'G')
        self.gf.adicionaAresta('a3', 'A', 'J')
        self.gf.adicionaAresta('a4', 'G', 'K')
        self.gf.adicionaAresta('a5', 'J', 'K')
        self.gf.adicionaAresta('a6', 'G', 'J')
        self.gf.adicionaAresta('a7', 'I', 'J')
        self.gf.adicionaAresta('a8', 'G', 'I')
        self.gf.adicionaAresta('a9', 'G', 'H')
        self.gf.adicionaAresta('a10', 'F', 'H')
        self.gf.adicionaAresta('a11', 'B', 'F')
        self.gf.adicionaAresta('a12', 'B', 'G')
        self.gf.adicionaAresta('a13', 'B', 'C')
        self.gf.adicionaAresta('a14', 'C', 'D')
        self.gf.adicionaAresta('a15', 'D', 'E')
        self.gf.adicionaAresta('a16', 'B', 'D')
        self.gf.adicionaAresta('a17', 'B', 'E')

        #Grafo não conexo
        self.g2 = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'])
        self.g2.adicionaAresta('1','A','B')
        self.g2.adicionaAresta('2','B','A')
        self.g2.adicionaAresta('3','A','B')
        self.g2.adicionaAresta('4','B','B')

        self.g2.adicionaAresta('5','C','D')
        self.g2.adicionaAresta('6','D','C')
        self.g2.adicionaAresta('7','C','D')
        self.g2.adicionaAresta('8','D','D')
        self.g2.adicionaAresta('9','E','F')
        self.g2.adicionaAresta('10','F','G')
        self.g2.adicionaAresta('11','G','E')
        self.g2.adicionaAresta('12','F','H')
        self.g2.adicionaAresta('13','G','I')
        self.g2.adicionaAresta('14','E','I')
        self.g2.adicionaAresta('15','J','K')
        self.g2.adicionaAresta('16','K','L')
        self.g2.adicionaAresta('17','M','L')
        self.g2.adicionaAresta('18','M','N')
        self.g2.adicionaAresta('19','O','N')
        self.g2.adicionaAresta('20','O','P')
        self.g2.adicionaAresta('21','Q','P')
        self.g2.adicionaAresta('22','Q','R')
        self.g2.adicionaAresta('23','S','R')
        self.g2.adicionaAresta('24','S','J')

        #grafo K5
        self.k5 = MeuGrafo(['A','B','C','D','E'])
        self.k5.adicionaAresta('1','A','B')
        self.k5.adicionaAresta('5','A','C')
        self.k5.adicionaAresta('6','A','D')
        self.k5.adicionaAresta('7','A','E')
        self.k5.adicionaAresta('2','B','C')
        self.k5.adicionaAresta('8','B','D')
        self.k5.adicionaAresta('9','B','E')
        self.k5.adicionaAresta('3','C','D')
        self.k5.adicionaAresta('10','C','E')
        self.k5.adicionaAresta('4','D','E')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-J', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M'])

        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-J', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E',
                          'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J', 'T-E', 'T-P',
                          'Z-J', 'Z-C', 'Z-E',
                          'Z-P', 'Z-M'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)
	
    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))

    def test_dfs(self):
        self.assertEqual(list(self.g_p.dfs('C').A),['a1', 'a2', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('E').A),['a2', 'a1', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('J').A),['a1', 'a2', 'a4', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('M').A),['a7', 'a1', 'a2', 'a4', 'a6', 'a9'])
        self.assertEqual(list(self.g_p.dfs('P').A),['a4', 'a1', 'a2', 'a6', 'a8', 'a9'])
        self.assertEqual(list(self.g_p.dfs('T').A),['a6', 'a1', 'a2', 'a4', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.dfs('Z').A),['a9', 'a6', 'a1', 'a2', 'a4', 'a7'])

        self.assertEqual(list(self.g_p_sem_paralelas.dfs('C').A),['a1', 'a2', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('E').A),['a2', 'a1', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('J').A),['a1', 'a2', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('M').A),['a5', 'a1', 'a2', 'a3', 'a4', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('P').A),['a3', 'a1', 'a2', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('T').A),['a4', 'a1', 'a2', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('Z').A),['a7', 'a4', 'a1', 'a2', 'a3', 'a5'])

        self.assertEqual(list(self.gf.dfs('A').A),['a1', 'a11', 'a10', 'a9', 'a4', 'a5', 'a7', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.gf.dfs('B').A),['a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.gf.dfs('C').A),['a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a16', 'a15'])
        self.assertEqual(list(self.gf.dfs('D').A),['a14', 'a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a17'])
        self.assertEqual(list(self.gf.dfs('E').A),['a15', 'a14', 'a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10'])
        self.assertEqual(list(self.gf.dfs('F').A),['a10', 'a9', 'a2', 'a1', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.gf.dfs('G').A),['a2', 'a1', 'a11', 'a10', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.gf.dfs('H').A),['a9', 'a2', 'a1', 'a11', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.gf.dfs('I').A),['a7', 'a3', 'a1', 'a11', 'a10', 'a9', 'a4', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.gf.dfs('J').A),['a3', 'a1', 'a11', 'a10', 'a9', 'a4', 'a8', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.gf.dfs('K').A),['a4', 'a2', 'a1', 'a11', 'a10', 'a13', 'a14', 'a15', 'a3', 'a7'])
        
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_bfs(self):
        self.assertEqual(list(self.g_p.bfs('C').A),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('E').A),['a2', 'a1', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('J').A),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('M').A),['a7', 'a8', 'a1', 'a2', 'a4', 'a9'])
        self.assertEqual(list(self.g_p.bfs('P').A),['a4', 'a1', 'a2', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('T').A),['a6', 'a8', 'a9', 'a1', 'a2', 'a4'])
        self.assertEqual(list(self.g_p.bfs('Z').A),['a9', 'a6', 'a8', 'a1', 'a2', 'a4'])

        self.assertEqual(list(self.gf.bfs('A').A),['a1', 'a2', 'a3', 'a11', 'a13', 'a16', 'a17', 'a10', 'a4', 'a8'])
        self.assertEqual(list(self.gf.bfs('B').A),['a1', 'a11', 'a12', 'a13', 'a16', 'a17', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.gf.bfs('C').A),['a13', 'a14', 'a1', 'a11', 'a12', 'a17', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.gf.bfs('D').A),['a14', 'a15', 'a16', 'a1', 'a11', 'a12', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.gf.bfs('E').A),['a15', 'a17', 'a14', 'a1', 'a11', 'a12', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.gf.bfs('F').A),['a10', 'a11', 'a9', 'a2', 'a4', 'a6', 'a8', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.gf.bfs('G').A),['a2', 'a4', 'a6', 'a8', 'a9', 'a12', 'a11', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.gf.bfs('H').A),['a9', 'a10', 'a2', 'a4', 'a6', 'a8', 'a12', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.gf.bfs('I').A),['a7', 'a8', 'a3', 'a5', 'a1', 'a11', 'a13', 'a16', 'a17', 'a10'])
        self.assertEqual(list(self.gf.bfs('J').A),['a3', 'a5', 'a6', 'a7', 'a1', 'a11', 'a13', 'a16', 'a17', 'a10'])
        self.assertEqual(list(self.gf.bfs('K').A),['a4', 'a5', 'a2', 'a8', 'a9', 'a12', 'a11', 'a13', 'a16', 'a17'])

        self.assertEqual(list(self.g_l1.bfs('A').A),['a2'])
        self.assertEqual(list(self.g_l2.bfs('A').A),['a1'])
        self.assertEqual(list(self.g_l3.bfs('C').A),['a1'])
        self.assertEqual(list(self.g_l4.bfs('D').A),[])
        self.assertEqual(list(self.g_l5.bfs('C').A),['a1'])

        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')
            self.gf.arestas_sobre_vertice('Z')

    def test_ciclo(self):
        self.assertEqual(list(self.g_p.ha_ciclo()),['C', 'a2', 'E', 'a3', 'C'])
        
        self.assertEqual(list(self.g_p_sem_paralelas.ha_ciclo()),['M', 'a5', 'C', 'a4', 'T', 'a6', 'M'])
        
        self.assertEqual(list(self.gf.ha_ciclo()),['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a2', 'A'])
        
        self.assertEqual(self.g_d.ha_ciclo(),False)

        self.assertEqual(list(self.g2.ha_ciclo()),['A', '1', 'B', '2', 'A'])

        self.assertEqual(list(self.k5.ha_ciclo()),['A', '1', 'B', '2', 'C', '5', 'A'])


    def test_caminho(self):
        self.assertEqual(list(self.g_p.caminho(1)),['J', 'a1', 'C'])
        self.assertEqual(list(self.g_p.caminho(2)),['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(list(self.g_p.caminho(3)),['J', 'a1', 'C', 'a6', 'T', 'a8', 'M'])
        self.assertEqual(list(self.g_p.caminho(4)),['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'])
        
        self.assertEqual(list(self.gf.caminho(1)),['A', 'a1', 'B'])
        self.assertEqual(list(self.gf.caminho(2)),['A', 'a1', 'B', 'a11', 'F'])
        self.assertEqual(list(self.gf.caminho(3)),['A', 'a1', 'B', 'a11', 'F', 'a10', 'H'])
        self.assertEqual(list(self.gf.caminho(4)),['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G'])
        self.assertEqual(list(self.gf.caminho(5)),['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a4', 'K'])
        self.assertEqual(list(self.gf.caminho(6)),['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a4', 'K', 'a5', 'J'])
        self.assertEqual(list(self.gf.caminho(7)),['A', 'a1', 'B', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a4', 'K', 'a5', 'J', 'a7', 'I'])
        self.assertEqual(list(self.gf.caminho(8)),['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B', 'a13', 'C', 'a14', 'D'])
        self.assertEqual(list(self.gf.caminho(9)),['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B', 'a13', 'C', 'a14', 'D', 'a15', 'E'])
        
        self.assertEqual(list(self.g_d.caminho(1)),['A', 'asd', 'B'])
        
        self.assertEqual(list(self.g2.caminho(1)),['A', '1', 'B'])
        self.assertEqual(list(self.g2.caminho(2)),['E', '9', 'F', '10', 'G'])
        self.assertEqual(list(self.g2.caminho(3)),['E', '9', 'F', '10', 'G', '13', 'I'])
        self.assertEqual(list(self.g2.caminho(4)),['E', '14', 'I', '13', 'G', '10', 'F', '12', 'H'])
        self.assertEqual(list(self.g2.caminho(5)),['J', '15', 'K', '16', 'L', '17', 'M', '18', 'N', '19', 'O'])
        self.assertEqual(list(self.g2.caminho(6)),['J', '15', 'K', '16', 'L', '17', 'M', '18', 'N', '19', 'O', '20', 'P'])
        self.assertEqual(list(self.g2.caminho(7)),['J', '15', 'K', '16', 'L', '17', 'M', '18', 'N', '19', 'O', '20', 'P', '21', 'Q'])
        self.assertEqual(list(self.g2.caminho(8)),['J', '15', 'K', '16', 'L', '17', 'M', '18', 'N', '19', 'O', '20', 'P', '21', 'Q', '22', 'R'])
        self.assertEqual(list(self.g2.caminho(9)),['J', '15', 'K', '16', 'L', '17', 'M', '18', 'N', '19', 'O', '20', 'P', '21', 'Q', '22', 'R', '23', 'S'])

        self.assertEqual(list(self.k5.caminho(1)),['A', '1', 'B'])
        self.assertEqual(list(self.k5.caminho(2)),['A', '1', 'B', '2', 'C'])
        self.assertEqual(list(self.k5.caminho(3)),['A', '1', 'B', '2', 'C', '3', 'D'])
        self.assertEqual(list(self.k5.caminho(4)),['A', '1', 'B', '2', 'C', '3', 'D', '4', 'E'])

        with self.assertRaises(BaseException):
            self.g_p.caminho(0)
            self.g_p.caminho(5)

    def test_conexo(self):
        self.assertEqual(self.g_p.conexo(), True)

        self.assertEqual(self.g_p_sem_paralelas.conexo(), True)

        self.assertEqual(self.gf.conexo(), True)

        self.assertEqual(self.g_d.conexo(), False)

        self.assertEqual(self.g2.conexo(), False)

        self.assertEqual(self.k5.conexo(), True)

if __name__ == '__main__':
    unittest.main()