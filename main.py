# -*- coding: utf-8 -*-
"""
@author: Walter Jhameson Xavier Pereira
@e-mail: walterjxp@gmail.com
@read.me: Esse código foi escrito usando conceitos de Programação Orientada a Objetos (POO).
"""
#Importando a biblioteca do Sistema para Evitar que o usuário digite um número negativo
import sys

#Criando a classe Aluno e seus métodos

class Aluno(object):
    def __init__(self, nome, sexo):
        self.nome, self.sexo, self.notas = nome, sexo, []

    def append_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return (sum(self.notas) / len(self.notas))

    def situacao_aluno(self):
        media = self.media()
        for valor, situacao in (7, "Aprovado"), (4, "Exame"):
            if media >= valor:
                return situacao
        else:
            return "Reprovado"

def main():
    print("~-"*40)
    print("Bem-vindo ao Sistema de Gerenciamento de Notas de Alunos")
    print("IFSP-Campus Sertãozinho")
    print("~-"*40)
    classe_inicial = []
    while True:
        print()
        print(f'Você possui {len(classe_inicial)} aluno(s) cadastrados até agora')
        novo_aluno = input('Você deseja adicionar um novo aluno (s/n) ?\n')
        if novo_aluno[0].lower() != 's':
            break
        nome_aluno = input('Digite o nome completo do Aluno:\n')
        sexo_aluno = input('Sexo: (M/F)\n')
        classe_inicial.append(Aluno(nome_aluno, sexo_aluno))
        print('Aluno:', nome_aluno)
        print('~-'*10)
        
        for prova in range(1, 4):
            print(f'Digite a Nota da AP{prova}')
            score = float(input(':'))
            if (score < 0) or (score > 10):
                print(f'{score} não é uma nota válida.\n Por favor, digite uma nota entre 0 e 10.')
                sys.exit("Nota inválida. Execute o Script novamente!")
            classe_inicial[-1].append_nota(score) 

    print_report(classe_inicial)

def print_report(classe_inicial):
    print("~-"*40)
    print(' '*20 + 'Relatório do Sistema')
    print("~-"*40)
    print(f'Total de Alunos cadastrados: {len(classe_inicial)}')
    print()
    
    #total
    q_aprovado = 0
    q_exame = 0
    q_reprovado = 0
    
    #por sexo
    m_aprovado = 0
    f_aprovado = 0
    
    m_exame = 0
    f_exame = 0
    
    m_reprovado = 0
    f_reprovado = 0
    
    
    for estudante in sorted(classe_inicial, key=lambda s: s.nome):
        if estudante.situacao_aluno().lower() == 'aprovado':
            q_aprovado +=1
            
            if estudante.sexo.lower() == 'm':
                m_aprovado +=1
            elif estudante.sexo.lower() == 'f':
                f_aprovado +=1
                
        elif estudante.situacao_aluno().lower() == 'exame':
            q_exame+=1
            
            if estudante.sexo.lower() == 'm':
                m_exame +=1
            elif estudante.sexo.lower() == 'f':
                f_exame +=1
        else:
            q_reprovado+=1
            
            if estudante.sexo.lower() == 'm':
                m_reprovado +=1
            elif estudante.sexo.lower() == 'f':
                f_reprovado +=1
            
            
    print("~-"*40)
    print("Percentagens:")
    print(f'Quatidade de alunos aprovados: {round(q_aprovado*100/len(classe_inicial), 2)} %')
    print(f'Quatidade de alunos de exame: {round(q_exame*100/len(classe_inicial), 2)} %')
    print(f'Quatidade de alunos reprovados: {round(q_reprovado*100/len(classe_inicial), 2)} %')
    print()
    print("~-"*40)
    print("Valores Absolutos:")
    print(f'Quantidade de pessoas do sexo feminino aprovadas: {f_aprovado}')
    print(f'Quantidade de pessoas do sexo masculino aprovadas: {m_aprovado}')
    print(f'Quantidade de pessoas do sexo feminino de exame: {f_exame}')
    print(f'Quantidade de pessoas do sexo masculino de exame: {m_exame}')
    print(f'Quantidade de pessoas do sexo feminino reprovadas: {f_reprovado}')
    print(f'Quantidade de pessoas do sexo masculino reprovadas: {m_reprovado}')
    print()

main()
