# 📊 Exploração de Poços no Brasil: Evolução ao Longo dos Anos

## Autor: Paulo Roberto  
**Data:** Março de 2025  

### 📝 Descrição do Projeto  
Este projeto utiliza a biblioteca `Bar Chart Race` para gerar gráficos de corrida de barras animados, mostrando a evolução dos poços perfurados nas bacias sedimentares brasileiras ao longo dos anos.  

A visualização interativa ajuda a identificar:  
- Quais bacias receberam maior atenção ao longo do tempo  
- Quais se destacaram e estão associadas às maiores reservas de óleo e gás  

---

## 📁 **Arquivos Utilizados**  
- **Notebook:** `bar_chart_pocos.ipynb`  
- **Base de Dados:** `Tabela_pocos_2025_Março_16.csv`  

---

## 🛠️ **Bibliotecas Necessárias**  
Para rodar o notebook, você precisará das seguintes bibliotecas:  

```bash
pip install pandas matplotlib bar_chart_race
```

Ou instale direto com o arquivo `requirements.txt`:  

```bash
pip install -r requirements.txt
```

---

## 📌 **Principais Etapas do Notebook**

1. **Importação das Bibliotecas**  
   ```python
   import pandas as pd
   import bar_chart_race as bcr
   import matplotlib.pyplot as plt
   from IPython.display import HTML
   ```

2. **Leitura da Base de Dados**  
   ```python
   df_pocos = pd.read_csv('Tabela_pocos_2025_Março_16.csv', sep=';', encoding='latin1')
   ```

3. **Tratamento e Exploração dos Dados**  
   - Limpeza dos dados  
   - Agrupamento por bacias sedimentares  
   - Preparação dos dados para o gráfico animado  

4. **Criação do Gráfico de Corrida de Barras**  
   ```python
   bcr.bar_chart_race(
       df=df_pocos,
       filename='evolucao_pocos.mp4',
       title='Evolução dos Poços Perfurados no Brasil (Ano a Ano)'
   )
   ```

---

## 🎥 **Resultado Final**  
O notebook gera um vídeo `evolucao_pocos.mp4` que mostra dinamicamente quais bacias ganharam mais destaque ao longo dos anos.  


![Evolução dos Poços](pocos.gif)
