try:
  from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
  from bibgrafo.grafo_exceptions import *
  import itertools
  import operator
except Exception as e:
  print(e)

class MeuGrafo(GrafoListaAdjacencia):
    
    def __init__(self, master):
        super().__init__(master)
        self.lista_vertices = []
        
  
    def criarlistavertices(self, dfs=False):
        """
        Gera a lista com os valores dos vertices.
        """
        if self.lista_vertices == []:
            for key in self.A:
                if dfs:
                    self.lista_vertices.append([self.A[key].getV1(), self.A[key].getV2(), key])
                else:
                    self.lista_vertices.append([self.A[key].getV1(), self.A[key].getV2()])

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        self.criarlistavertices()
        lista_VNA = []
        for subset in itertools.permutations(self.N, 2):
            if (list(subset) in self.lista_vertices) == False and (list(subset)[::-1] in self.lista_vertices) == False:
                lista_VNA.append(f"{subset[0]}-{subset[1]}")

        return lista_VNA

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        self.criarlistavertices()
        for key in self.A:
            if self.A[key].getV1() == self.A[key].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        self.criarlistavertices()
        grau = 0
        for i in self.lista_vertices:
            if i[0] == V and i[1] == V:
                grau += 2
            elif i[0] == V or i[1] == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        self.criarlistavertices()
        for i in range(len(self.lista_vertices)):
            if self.lista_vertices[i] in self.lista_vertices[i+1::]:
                return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        self.criarlistavertices()
        lista_ASV = []
        for key in self.A:
            if V == self.A[key].getV1():
                lista_ASV.append(key)
            if V == self.A[key].getV2():
                lista_ASV.append(key)
        
        return lista_ASV

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        self.criarlistavertices()
        listacontagem = [0] * len(self.N)
        lista = self.N
        for i in range(len(lista)):
            for c in self.lista_vertices:
                listacontagem[i] += (c.count(lista[i]))
        if self.ha_laco() == False and self.ha_paralelas() == False and all(map(operator.eq, listacontagem, [len(lista) - 1] * (len(lista) - 1))):
            return True
        return False

    def dfs(self, V='',**kwargs):
        '''
        Provê uma árvore (um grafo) que contém apenas as arestas do dfs
        :param V: O vértice a de onde se inicia o caminho
        :return: Um grafo do tipo árvore
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        try:
            self.acdfs = kwargs["dfs"]
        except:
            self.acdfs = True
        
        if self.acdfs == True:
            self._arvoredfs = MeuGrafo(self.N)
            self.arestas_dfs = []
            self.acdfs = False

        self.criarlistavertices(dfs=True)
        for i in range(len(self.lista_vertices)):
            if (V in self.lista_vertices[i]):
                aresta = self.lista_vertices[i]
                if((aresta[0] not in self.arestas_dfs) or (aresta[1] not in self.arestas_dfs))\
                and (self.lista_vertices[i][0] != self.lista_vertices[i][1]):
                    self._arvoredfs.adicionaAresta(aresta[2], aresta[0], aresta[1])
                    self.arestas_dfs.append(aresta[0])
                    self.arestas_dfs.append(aresta[1])
                    self.dfs(aresta[1] if aresta[1]!= V else aresta[0],**{"dfs":False})
    
        return self._arvoredfs