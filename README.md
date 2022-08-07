# **Documentação API - ZSSN**
Documentação para utilizar a API da ZSSN(Rede Social de Sobrevivência Zumbi)

## **Sobrevivente**
Representa os usuários da API da ZSSN


* **GET /sobreviventes/**
Exibe uma lista com todos os usuários do sistema


* **GET /sobreviventes/detail/:idSobrevivente/**
Lista os dados de um determinado sobrevivente

    Reponse:
    ```
    {
      "id": 13,
      "nome": "Santos",
      "idade": 20,
      "sexo": "m",
      "latitude": 1292,
      "longitude": 1291,
      "estaInfectado": false,
      "countAlertInfected": 0
    }
    ```
    
    Reponse com erro:
     ```
    {
      "message": "Sobrevivente não encontrado"
    }
    ```   

* **POST /sobreviventes/create/**
Cadastra um novo sobrevivente no sistema junto com os itens declarados

    Request:
    ```
        {
            "nome": "Rubem Eslley",
            "idade": 20,
            "sexo": "m",
            "latitude": 5.037178,
            "longitude": 42.792717,
            "inventario": [
                {
                    "id": 4,
                    "quantidade": 2

                },
                {
                    "id": 2,
                    "quantidade": 2
                }
            ]
        }
    ```


* **PUT /sobreviventes/update/:idSobrevivente/localization/**
Atualizada latitude e longitude do sobrevivente

    Request:
    ```
    {
        "latitude": 5.045261,
        "longitude": 42.789111
    }
    ```
    Response:
    ```
    {
      "message": "Localização Atualizada"
    }
    ```

* **DELETE /sobreviventes/delete/:idSobrevivente/**
Delete sobrevivente do sistema

    Reponse:
    ```
    {
      "message": "Sobrevivente Deletado"
    }
    ```

* **PUT  /sobreviventes/:idSobrevivente1/contaminacao/:idSobrevivente2/**
O sobrevivente com idSobrevivente1 relata a contaminação do sobrevivente com idSobrevivente2

    Reponse:
    ```
    {
      "message": "O alerta de infecção foi recebido"
    }
    ```
    
* **GET /sobreviventes/relatorios/**
Fornece dados de relatório

    Response:
    ```
    {
      "total_sobreviventes": 5,
      "infectados": "0.4%",
      "nao_infectados": "0.6%",
      "media_agua": "3.0 por sobrevivente",
      "media_alimentacao": "3.0 por sobrevivente",
      "media_medicacao": "0 por sobrevivente",
      "media_municao": "6.0 por sobrevivente",
      "pontos_perdidos": [
        {
          "id": 10,
          "nome": "Rubem",
          "estaInfectado": true,
          "pontos_perdidos": 20
        },
        {
          "id": 11,
          "nome": "Eslley",
          "estaInfectado": true,
          "pontos_perdidos": 16
        }
      ]
    }
    ```
## **Inventário**
Representa todos os recursos que os sobreviventes possuem

* **GET /inventarios/**
Exibe uma lista com os inventários dos sobreviventes



* **GET /inventarios/sobrevivente/:idSobrevivente/**
Lista todos os recursos que um determinado sobrevivente possui

    Response:
    ```
    {
        "sobreviventeId": "13",
        "sobrevivente": "Santos",
        "itens": [
            {
                "item": {
                    "id": 1,
                    "nome": "agua",
                    "pontos": 4
                },
                "quantidade": 3
            },
            {
                "item": {
                    "id": 2,
                    "nome": "alimentacao",
                    "pontos": 3
                },
                "quantidade": 3
            },
            {
                "item": {
                    "id": 4,
                    "nome": "municao",
                    "pontos": 1
                },
                "quantidade": 6
            }
        ]
    }
    ```
    
    Response com erro:
    ```
    {
        "message": 'Não é possível acessar inventário, sobrevivente infectado'
    }
    ```
    
    
## **Item**
Representa os recursos que os sobreviventes podem possuir


* **GET /itens/**
Exibe uma lista com todos os recursos cadastrado no sistema da ZSSN

    Response:
    ```
    [
      {
        "id": 1,
        "nome": "agua",
        "pontos": 4
      },
      {
        "id": 2,
        "nome": "alimentacao",
        "pontos": 3
      },
      {
        "id": 3,
        "nome": "medicacao",
        "pontos": 2
      },
      {
        "id": 4,
        "nome": "municao",
        "pontos": 1
      }
    ]
    ```

* **POST /itens/create/**
Adiciona um novo recurso no sistema

    Request:
    ```
    {
        "nome": "ferramenta",
        "pontos": "3"
    }
    ```
    Response:
    ```
    {
      "id": 5,
      "nome": "ferramenta",
      "pontos": 3
    }
    ```
## **Comércio**
Representa as operações de troca de itens que podem ser realizadas pelos sobreviventes


* **POST /comercio/**
Transfere os itens informados para cada sobrevivente

    Request:
    ```
    {
        "sobrevivente1": 
        {
            "sobrevivente": 14,
            "itens": [
                {
                    "id": 2,
                    "quantidade": 1,
                    "pontos": 3
                },
                {
                    "id": 4,
                    "quantidade": 1,
                    "pontos": 1
                }
            ]
        },
        "sobrevivente2":
        {
            "sobrevivente": 12,
            "itens": [
                {
                    "id": 1,
                    "quantidade": 1,
                    "pontos": 4
                }
            ]
        }
    }
    ```
    Response:
    ```
    {
      "message": "Troca realizada com sucesso"
    }
    ```
    
    Response com erro:
    ```
    {
      "message": "Item oferecido não está no inventário do sobrevivente"
    }
    ```
