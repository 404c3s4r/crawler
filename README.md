# Globo Scraping

#### Este é um projeto simples de web scraping desenvolvido em Python para extrair links da globo.com. Ele utiliza as bibliotecas requests e BeautifulSoup para coletar informações das páginas web e permite a coleta e filtragem de parâmetros.


### O objetivo 
Principal deste projeto é fornecer uma ferramenta de scraping para coletar links de maneira automatizada e filtrar parâmetros de URLs. Este código pode ser usado como base para projetos mais avançados ou para entender os conceitos básicos de scraping e segurança web.



## Como usar ?

Instalação das Dependências:
```bash
  pip3 install -r requirements.txt
```
Para utilizar este projeto, siga os passos abaixo:

### Execução do Scraping

Após a instalação das dependências, você pode executar o arquivo craw.py para iniciar o scraping dos links da página alvo.

Execute a ferramenta:
```bash
  python3 craw.py https://www.globo.com/
```

Demonstração de Filtragem e Testes de Parâmetros
![image](https://github.com/user-attachments/assets/3be792a5-1010-4898-931a-98c4a893f32e)



O código irá coletar os links da página alvo e exibir os parâmetros coletados no console. 


A estrutura de pastas do projeto está organizada da seguinte maneira:


```bash
Globo_Scraping/
│
├── craw.py           # Arquivo principal onde você inicia o web scraping 
│        
│
├── requirements.txt  # Arquivo que lista todas as dependências do projeto
└── README.md         # Este arquivo, contendo informações sobre o projeto e instruções de uso
```

## Technology Used:
- **Python** 
   
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/robertocoliver/)
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://medium.com/@robertocoliver)


Avisos Importantes
> Uso Responsável: Este projeto foi desenvolvido para fins educacionais e de aprendizado. Sempre respeite os termos de serviço dos sites ao realizar web scraping.
> Limitações e Restrições: O scraping de sites pode ser contra os termos de serviço de alguns sites. Verifique as políticas de uso e os limites de solicitação do site alvo antes de executar o código.

