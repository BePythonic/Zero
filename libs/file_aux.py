# -*- coding: utf-8 -*-
# @author Eduardo

class FileAux:
	def __init__(self, nome_arq, lin=0, busca=''):
		'''(FileAux, str, str -> None)'''
		self.nome_arq = nome_arq
		self.busca = busca		# trecho a partir do qual começar a leitura
		self.cont_lin = lin-1 	# linha atual
		self.num_linhas = 0		# número de linhas (não-vazias) do arquivo
		self.cont_pal = 0		# índice da palavra atual da linha atual
		self.num_pal = 0		# número de palavras de uma dada linha
		self.qtde_palavras = 0 	# total de palavras do arquivo
		self.linhas = list() 	# lista com as linhas não vazias do arquivo
		self.getArquivo()
		self.setLinhaInicial()
		self.setQtdePalavras()

	def getArquivo(self):
		'''(FileAux -> None)'''
		arq = open(self.nome_arq, 'r', encoding="utf8")
		for linha in arq:
			if linha != "":
				self.linhas.append(linha)
		arq.close()
		self.num_linhas = len(self.linhas)

	def setLinhaInicial(self):
		'''(FileAux -> None)'''
		if self.cont_lin < 0:
			self.cont_lin = 0
		if self.busca != '':
			linha = ""
			while self.busca not in linha:
				linha = self.linhas[self.cont_lin]
				self.cont_lin += 1

	def getLinha(self):
		'''(FileAux, bool -> str)'''
		linha = ""
		if self.cont_lin < self.num_linhas:
			linha = self.linhas[self.cont_lin]
		return linha

	def getPalavra(self):
		'''(FileAux -> str)'''
		palavra, linha = "", []
		if self.cont_pal == 0:
			while len(linha) == 0 and self.cont_lin < self.num_linhas:
				linha = self.getLinha().split()
				if len(linha) == 0:
					self.cont_lin += 1
			self.num_pal = len(linha)
		else:
			linha = self.getLinha().split()
		if self.cont_pal < self.num_pal:
			palavra = linha[self.cont_pal]
			self.cont_pal += 1
		elif self.cont_pal == self.num_pal:
			self.cont_pal = 0
			self.cont_lin += 1 # acacabaram as palavras da linha
		if self.cont_lin >= self.num_linhas and palavra == "":
			palavra = None
		return palavra

	def setQtdePalavras(self):
		'''(FileAux -> None)'''
		for i in range(self.cont_lin, self.num_linhas):
			linha = self.linhas[i]
			if len(linha) > 0:
				self.qtde_palavras += len(linha.split())
