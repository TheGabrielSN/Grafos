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
        
  
    def __criarlistavertices(self, dfs=False, bfs=False):
        """
        Gera a lista com os valores dos vertices.
        """
        self.lista_vertices = []
        for key in self.A:
            if dfs or bfs: #[V0,V1,A]
                self.lista_vertices.append([self.A[key].getV1(), self.A[key].getV2(), key])
            else: #[V0,V1]
                self.lista_vertices.append([self.A[key].getV1(), self.A[key].getV2()])

    #---------- Roteiro 1 ----------#

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        self.__criarlistavertices()
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
        self.__criarlistavertices()
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
        self.__criarlistavertices()
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
        self.__criarlistavertices()
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

        self.__criarlistavertices()
        lista_ASV = []
        for key in self.A:
            if V == self.A[key].getV1():
                lista_ASV.append(key)
            if (V == self.A[key].getV2()) and (self.A[key].getV1()!=self.A[key].getV2()):
                lista_ASV.append(key)
        
        return lista_ASV

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        self.__criarlistavertices()
        listacontagem = [0] * len(self.N)
        lista = self.N
        for i in range(len(lista)):
            for c in self.lista_vertices:
                listacontagem[i] += (c.count(lista[i]))
        if self.ha_laco() == False and self.ha_paralelas() == False and all(map(operator.eq, listacontagem, [len(lista) - 1] * (len(lista) - 1))):
            return True
        return False

    #---------- Roteiro 2 ----------#

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

        self.__criarlistavertices(dfs=True)
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

    #---------- Roteiro 3 ----------#

    def bfs(self, V='',**kwargs):
        '''
        Provê uma árvore (um grafo) que contém apenas as arestas do dfs
        :param V: O vértice a de onde se inicia o caminho
        :return: Um grafo do tipo árvore
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        try:
            self.acbfs = kwargs["bfs"]
        except:
            self.acbfs = True
        
        if self.acbfs == True:
            self._arvorebfs = MeuGrafo(self.N)
            self.arestas_bfs = []
            self.acbfs = False
            self.asv = []

        asv = self.arestas_sobre_vertice(V)

        self.__criarlistavertices(bfs=True)
        for i in range(len(self.lista_vertices)):
            if (self.lista_vertices[i][2] in asv)\
                and ((self.lista_vertices[i][0] not in self.arestas_bfs)\
                or (self.lista_vertices[i][1] not in self.arestas_bfs))\
                and (self.lista_vertices[i][0] != self.lista_vertices[i][1]):
                self._arvorebfs.adicionaAresta(self.lista_vertices[i][2], self.lista_vertices[i][0], self.lista_vertices[i][1])
                self.arestas_bfs.append(self.lista_vertices[i][0])
                self.arestas_bfs.append(self.lista_vertices[i][1])
        
        for i in range(len(self.lista_vertices)):
            if(self.lista_vertices[i][2] in asv) and (self.__verificar(**{"arvore":self._arvorebfs}) == False) and self.lista_vertices[i][2] not in self.asv:
                self.asv.append(self.lista_vertices[i][2])
                self.bfs(self.lista_vertices[i][1] if self.lista_vertices[i][1]!= V else self.lista_vertices[i][0],**{"bfs":False})

        return self._arvorebfs
        
    def __verificar(self,**kwargs):
        _aux = []
        kwargs["arvore"].__criarlistavertices()
        for i in kwargs["arvore"].lista_vertices:
            if (i[0] in _aux) == False:
                _aux.append(i[0])
            if (i[1] in _aux) == False:
                _aux.append(i[1])
        if len(_aux) == len(kwargs["arvore"].N):
            return True
        return False

    #---------- Roteiro 4 ----------#

    def ha_ciclo(self):
        """
        Verifica a existencia de ciclo no grafo
        :return: False ou Uma lista com o caminho do ciclo
        """
        ciclo = list()
        for v in self.N:
            ciclo = self.__laco(v)
            if(ciclo!=False):
                return [ciclo[1][0],ciclo[0],ciclo[1][1]]
            ciclo = self.__dfs_ciclo(v)
            if(ciclo != []):
                aux = []
                for i in range(0,len(ciclo),2):
                    if i==0:
                        aux.append(ciclo[i+1][0])
                        aux.append(ciclo[i])
                        aux.append(ciclo[i+1][1])
                    else:
                        aux.append(ciclo[i])
                        aux.append(ciclo[i+1][1] if aux[-2] != ciclo[i+1][1] else ciclo[i+1][0])
                contc = contt = 0
                for i in range(1,len(ciclo),2):
                    if(ciclo[i][0] in aux):
                        contc+=1
                    if(ciclo[i][1] in aux):
                        contc+=1
                    contt+=2
                if aux[0]==aux[-1] and contc==contt:
                    return aux

        return False

    def __laco(self, V):
        """
        Verifica a existencia de laços no vertice
        :param V: Vertice a ser analizado
        :return: bool referente a existencia de laços
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        """
        if V not in self.N:
            raise VerticeInvalidoException
        self.__criarlistavertices(dfs=True)
        for aresta in self.lista_vertices:
            if(V in aresta) and (aresta[0]==aresta[1]):
                return [aresta[2],[aresta[0],aresta[1]]]
        return False

    def __dfs_ciclo(self, V='',**kwargs):
        '''
        Provê uma lista com as arestas do ciclo
        :param V: O vértice a de onde se inicia o caminho 
        :return: Uma lista de arestas
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        try:
            self.acdfs = kwargs["dfs"]
        except:
            self.acdfs = True
        
        if self.acdfs == True:
            self.arestas_cilo = []
            self.acdfs = False

        self.__criarlistavertices(dfs=True)
        for i in range(len(self.lista_vertices)):
            self.__criarlistavertices(dfs=True)
            if (V in self.lista_vertices[i]):
                aresta = self.lista_vertices[i]
                if(([aresta[0],aresta[1]] not in self.arestas_cilo) or (not (aresta[2] in self.arestas_cilo)))\
                and (len(self.arestas_sobre_vertice(aresta[0]))>1 and len(self.arestas_sobre_vertice(aresta[1]))>1)\
                and (self.lista_vertices[i][0] != self.lista_vertices[i][1]):
                    if self.arestas_cilo != []:
                        if((self.arestas_cilo[-1][0]==self.arestas_cilo[1][0]) or (self.arestas_cilo[-1][1]==self.arestas_cilo[1][0]))\
                        and len(self.arestas_cilo)>3:
                            return self.arestas_cilo
                    try:
                        self.arestas_cilo.append(aresta[2])
                    except Exception as e:
                        pass
                    self.arestas_cilo.append([aresta[0], aresta[1]])
                    if(self.arestas_cilo.count([aresta[0],aresta[1]])>=2):
                        return self.arestas_cilo
                    else:
                        _value = self.__dfs_ciclo(aresta[1] if aresta[1]!= V else aresta[0],**{"dfs":False})
                        if(len(_value)==4):
                            return _value
                else:
                    self.__criarlistavertices(dfs=True)
        return self.arestas_cilo

    def caminho(self, n):
        '''
        Provê uma lista com o caminho de tamanho n
        :param n: tamanho do caminho desejado
        :return: Uma lista com vertices e arestas
        :raises: PathOutTheRange se o tamanho for maior que o possível
        '''
        if not (n<0 and n>len(self.N)):
            for i in self.N:
                value = self.__dfs_caminho(i,**{"num":n})
                if value != False:
                    return self.__outC(value)

        raise "PathOutTheRange"

    def __outC(self,A):
        _lout = []
        while(len(A)>0):
            self.__criarlistavertices(dfs=True)
            for i in range(len(self.lista_vertices)):
                try:
                    if((A[0]==self.lista_vertices[i][0] and A[1]==self.lista_vertices[i][1])) or ((A[1]==self.lista_vertices[i][0] and A[0]==self.lista_vertices[i][1])):
                        if _lout==[]:
                            _lout.append(A[0])
                            _lout.append(self.lista_vertices[i][2])
                            _lout.append(A[1])
                        else:
                            _lout.append(self.lista_vertices[i][2])
                            _lout.append(A[1] if A[1]!=_lout[-2] else A[0])
                        A.pop(0)
                        A.pop(0)
                except:
                    continue
        return _lout
    
    def __paralelas(self, A):
        self.__criarlistavertices()
        if(self.lista_vertices.count(A)>1):
            return True
        return False

    def __dfs_caminho(self, V='',**kwargs):
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
        try:
            self.num = kwargs["num"]
        except:
            pass
        
        if self.acdfs == True:
            self.arestas_dfs = []
            self.acdfs = False

        self.__criarlistavertices(dfs=True)
        for i in range(len(self.lista_vertices)):
            if (V in self.lista_vertices[i]):
                aresta = self.lista_vertices[i]
                if((aresta[0] not in self.arestas_dfs) or (aresta[1] not in self.arestas_dfs))\
                and (self.lista_vertices[i][0] != self.lista_vertices[i][1]):
                    if(aresta[1] if aresta[1]!= V else aresta[0] not in self.arestas_dfs):
                        self.arestas_dfs.append(aresta[0])
                        self.arestas_dfs.append(aresta[1])
                    self.__dfs_caminho(aresta[1] if aresta[1]!= V else aresta[0],**{"dfs":False})
                    if(len(self.arestas_dfs)/2 == self.num):
                        return self.arestas_dfs
                    if(aresta[1] if aresta[1]!= V else aresta[0] in self.arestas_dfs):
                        self.arestas_dfs.pop()
                        self.arestas_dfs.pop()
        return False

    def conexo(self):
        '''
        Verifica se o grafo é conexo
        :return: Bool representando se o grafo é conexo
        '''
        listadfs = list()
        for vertice in self.N:
            dfs = self.dfs(vertice)
            l = list()
            for aresta in dfs.A:
                l.append(dfs.A[aresta].getV1())
                l.append(dfs.A[aresta].getV2())
            listadfs.append(l)
        for dfs in listadfs:
            cont = 0
            for vertice in self.N:
                if(vertice in dfs):
                    cont += 1
                else:
                    return False
        return True