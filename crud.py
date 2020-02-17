import mysql.connector
import datetime
from crud import *

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='test')



def create():
   name   = ask_name()
   data   = ask_dta()
   sexo   = ask_sexo()
   altura = ask_altura()

   sql = "INSERT INTO  tb_pessoas(nme_pessoa, dta_nasc_pessoa, sex_pessoa, num_altura_pessoa) VALUES (%s, %s, %s, %s);"
   cursor = cnx.cursor()
   cursor.execute(sql, (name, data, sexo, altura))
   cnx.commit()
   cursor.close()
   input("----------------------------------------------"+ \
         "CADASTRO CONCLUIDO!\n"+ \
         "----------------------------------------------"+\
         "presione [ENTER]")


   return

def read():
    opcao = ask_int("DIGITE:\n" + \
                    "  1 - para todos os cadastros\n"+ \
                    "  2 - para procurar por nome.\n",
                    "CONTEUDO DIGITADO INVALIDO. TENTE NOVAMENTE.")
    if opcao == 1:
        sql = "SELECT * FROM tb_pessoas;"
        cursor = cnx.cursor()
        cursor.execute(sql, )

    elif opcao == 2:
        name = ask_name()
        sql = "SELECT * FROM tb_pessoas WHERE nme_pessoa LIKE CONCAT('%', %s, '%');"

        cursor = cnx.cursor()
        cursor.execute(sql, (name,))
    else:
        print("OPÇÃO INVALIDA! TENTE NOVAMENTE.")
        return read()


    for (idt, nome, data, sexo, altura) in cursor:
        print(idt, nome, data, sexo, altura)
    cursor.close()
    print("-------------------------------------------------")
    input("[Enter] para menu")


    return

def update():
   idt = ask_int("Qual a matricula para alterar? ",
                 "lembrece que a matricula é composta de números.\n"+ \
                 " Tente novamente.\n\n")

   sql    = ("SELECT * from tb_pessoas WHERE idt_pessoa=%s;")

   cursor = cnx.cursor()
   cursor.execute(sql, (idt,))
   (idt, nme, dta, sex, num_altura) = cursor.fetchone()
   cursor.close()

   nome   = ask_name("Digite o novo nome do(a) [" + nme + "]: ")
   data   = ask_dta()
   sexo   = ask_sexo()
   altura = ask_altura()

   sql = "UPDATE tb_pessoas SET nme_pessoa=%s, dta_nasc_pessoa=%s, "+ \
         "sex_pessoa=%s, num_altura_pessoa=%s WHERE idt_pessoa=%s;"
   cursor = cnx.cursor()
   cursor.execute(sql, (nome, data, sexo, altura, idt))
   cnx.commit()
   cursor.close()

   print("-------------------------------------------------")
   input("[Enter] para menu")
   return

def deletar():
    idt = ask_int("DIGITE A NUMERO DO CADASTRO: ",
                  "Só é aceito numeros inteiros.\n Tente novamente.")

    sql = ("SELECT * from tb_pessoas WHERE idt_pessoa=%s;")

    cursor = cnx.cursor()
    cursor.execute(sql, (idt,))
    (idt, nme, dta, sex, altura) = cursor.fetchone()
    cursor.close()

    print("Nome: " + nme)
    print("Matricula: ", idt)

    confirmacao = input("EXCLUIR [S/N]:")

    if confirmacao.upper() == "S":
        sql = "DELETE FROM tb_pessoas WHERE idt_pessoa=%s;"
        cursor = cnx.cursor()
        cursor.execute(sql, (idt,))
        cnx.commit()
        cursor.close()
        print("Excluido.")

    print("-------------------------------------------------")
    input("[Enter] para menu")

    return

text = True
while text:
   print("BEM VINDO AO BANCO DE DADOS!\n\n")
   try:
      menu = int(input("DÍGITE:\n  1 - para criar cadastro\n" + \
                       "  2 - para pesquisar cadastro\n" + \
                       "  3 - para alterar cadastro\n" + \
                       "  4 - para excluir cadastro\n" + \
                       "  5 - para sair.\n"))

   except(ValueError):
      print("Objeto digitado não coresponde com nenhuma opção\n"+ \
            "TENTE NOVAMENTE.")

   if menu == 1:
      create()
   elif menu == 2:
      read()
   elif menu == 3:
      update()
   elif menu == 4:
      deletar()
   elif menu == 5:
      print("FIM DO PROGRAMA.")
      cnx.close()
      text = False
   else:
      print("Objeto digitado não coresponde com nenhuma opção\n" + \
            "TENTE NOVAMENTE.")


