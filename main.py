def word_count():
    opcao = 1
    while opcao == 1:
        file_name = input("Digite o nome do livro: ")
        try:
            with open(file_name+'.txt') as book:
                book = len(book.readlines())
                print(" O Livro pesquisado contem aproximadamente "+str(book)+" Palavras\n")

        except FileNotFoundError:
            print("Livro não encontrado!\n")
        opcao = int(input("1 - Para Pesquisar novamente: \n2 - Para encerrar o programa: "))

word_count()
