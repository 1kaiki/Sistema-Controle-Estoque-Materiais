# Sistema de Controle de Estoque de Materiais

Sistema em Python, executado no terminal, para controlar o estoque de materiais: cadastro, entradas e saídas, edição, busca e um relatório com o valor total do estoque e alertas de estoque baixo.

> Projeto final da disciplina de Programação para Engenharia do curso de Engenharia de Software, UNISATC.

## Funcionalidades

- **Cadastrar material** com nome, categoria, quantidade, preço e unidade de medida, sem permitir nomes repetidos
- **Listar** todos os materiais cadastrados
- **Buscar** um material pelo nome (sem diferenciar maiúsculas e minúsculas)
- **Registrar entrada e saída** de estoque, com validação para a saída não passar do saldo disponível
- **Atualizar** preço, nome, quantidade ou categoria de um material
- **Remover** um material do estoque
- **Relatório do estoque** com o total de materiais, o valor total em estoque (quantidade × preço) e alertas para materiais com menos de 10 unidades

Todos os campos são validados: nome obrigatório, quantidade e preço não podem ser negativos.

## Exemplo de uso

```
=============MENU PRINCIPAL=============
1 - Cadastrar material
2 - Listar materiais
3 - Buscar material
4 - Editar estoque
5 - Relatório do estoque
0 - Sair
Digite qual opção você deseja:
```

Menu de edição do estoque:

```
-----------MENU EDITAR ESTOQUE------------
1 - Registrar entrada de estoque
2 - Registrar saída de estoque
3 - Atualizar o material
4 - Remover material
0 - Sair
```

## Tecnologias

- Python 3.10 ou mais novo (usa `match`/`case`)
- Listas e dicionários para guardar os materiais em memória

## Como rodar

Pré-requisito: Python 3.10 ou mais novo instalado.

```bash
git clone https://github.com/1kaiki/Sistema-Controle-Estoque-Materiais.git
cd Sistema-Controle-Estoque-Materiais
python main.py
```

Os dados ficam em memória enquanto o programa está aberto e são perdidos ao sair.

## Autor

Kaiki Mariano
