# Integrantes
- Fernanda Kaory Saito (RM551104)
- Pedro Lucas de Andrade Nunes (RM550366)

# Pipeline de Processamento de Imagens com OpenCV

## Descrição do Projeto

Este projeto implementa um **pipeline básico de visão computacional
utilizando OpenCV em Python** para processar imagens e detectar objetos
automaticamente.

O sistema realiza uma sequência de etapas de processamento de imagem com
o objetivo de **segmentar objetos e identificar seus contornos**.

## Etapas do Processamento

### 1. Carregamento da imagem

A imagem é lida do disco utilizando OpenCV.

### 2. Conversão para escala de cinza

A imagem colorida é convertida para **escala de cinza (grayscale)**,
reduzindo a complexidade dos dados e facilitando o processamento.

### 3. Análise do histograma e métricas

São calculadas métricas como: - **Brilho médio** - **Contraste (desvio
padrão)**

Também é exibido o **histograma da imagem**, permitindo analisar a
distribuição das intensidades dos pixels.

### 4. Ajuste de brilho e contraste

Uma transformação linear é aplicada para melhorar a visibilidade das
regiões da imagem.

### 5. Equalização de histograma

A equalização redistribui os níveis de intensidade da imagem para
melhorar o contraste global.

### 6. Binarização (Threshold)

A imagem em escala de cinza é convertida em **imagem binária**,
separando objetos do fundo.

Pixels: - acima do limiar → branco (255) - abaixo do limiar → preto (0)

Também é utilizado o método **Otsu**, que calcula automaticamente o
melhor limiar de segmentação.

### 7. Operações morfológicas

Operações morfológicas são aplicadas para **remover ruídos e melhorar a
estrutura dos objetos detectados**.

Neste projeto é utilizado **Closing (Dilatação + Erosão)** para: -
fechar pequenos buracos - conectar regiões próximas - limpar falhas na
segmentação

### 8. Detecção de contornos

O algoritmo identifica os **contornos dos objetos presentes na imagem
binária**.

Cada contorno representa um possível objeto detectado.

### 9. Visualização dos objetos detectados

Os contornos e **bounding boxes (retângulos delimitadores)** são
desenhados sobre a imagem original.

------------------------------------------------------------------------

## Objetivo

O objetivo deste projeto é demonstrar conceitos fundamentais de
**Processamento Digital de Imagens**, incluindo:

-   pré-processamento de imagens
-   análise de histograma
-   segmentação por threshold
-   operações morfológicas
-   detecção de contornos

Esse tipo de pipeline é amplamente utilizado em aplicações reais como:

-   **inspeção industrial**
-   **agricultura de precisão**
-   **monitoramento e segurança**
-   **análise automatizada de imagens**
