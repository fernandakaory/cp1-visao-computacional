from leitura_conversao import (
    carregar_imagem,
    converter_cinza,
    exibir_imagem,
    plotar_histograma,
    ajustar_brilho_contraste,
    equalizar_imagem,
    calcular_metricas,
    aplicar_threshold,
    aplicar_otsu,
    aplicar_morfologia,
    encontrar_contornos,
    filtrar_contornos, 
    desenhar_contornos,
    desenhar_caixas_limite
)


if __name__ == "__main__":
    
    # 1. Carregar imagem (use imagem sem direitos autorais)
    img = carregar_imagem("sample.jpg") 
    print("Dimensões imagem colorida:", img.shape)

    # 2. Converter para cinza
    cinza = converter_cinza(img)
    print("Dimensões imagem cinza:", cinza.shape)
    exibir_imagem(cinza, "Imagem Original (Cinza)")
    plotar_histograma(cinza)

    brilho, contraste = calcular_metricas(cinza)
    print("\n--- MÉTRICAS ORIGINAIS ---")
    print("Brilho médio:", brilho)
    print("Contraste (desvio padrão):", contraste)

    # 3. Ajustar brilho e contraste
    img_ajustada = ajustar_brilho_contraste(cinza, alpha=1.3, beta=30)
    exibir_imagem(img_ajustada, "Brilho e Contraste Ajustados")
    plotar_histograma(img_ajustada)

    brilho_ajustado, contraste_ajustado = calcular_metricas(img_ajustada)
    print("\n--- MÉTRICAS APÓS AJUSTES ---")
    print("Brilho médio:", brilho_ajustado)
    print("Contraste (desvio padrão):", contraste_ajustado)

    # 4. Equalizar histograma
    img_equalizada = equalizar_imagem(img_ajustada)
    exibir_imagem(img_equalizada, "Imagem Equalizada")
    plotar_histograma(img_equalizada)

    brilho_eq, contraste_eq = calcular_metricas(img_equalizada)
    print("\n--- MÉTRICAS APÓS EQUALIZAÇÃO ---")
    print("Brilho médio:", brilho_eq)
    print("Contraste (desvio padrão):", contraste_eq)

    # 5.1 Threshold manual
    img_thr_manual = aplicar_threshold(cinza)
    exibir_imagem(img_thr_manual, "Threshold Manual")
    plotar_histograma(img_thr_manual, "Threshold Manual")
   
    # 5.2. Threshold Otsu 
    img_thr_otsu = aplicar_otsu(cinza)
    exibir_imagem(img_thr_otsu, "Threshold Otsu")
    plotar_histograma(img_thr_otsu, "Threshold Otsu")

    # 6. Morfologia
    img_limpa = aplicar_morfologia(img_thr_otsu)
    exibir_imagem(img_limpa, "Imagem Após Morfologia")
    plotar_histograma(img_limpa, "Imagem Após Morfologia")

    # 7. Detecção de Contornos
    contornos = encontrar_contornos(img_limpa)
    print("Quantidade de objetos detectados:", len(contornos))

    # 8. Desenho dos Contornos
    img_contornos = desenhar_contornos(img, contornos)
    exibir_imagem(img_contornos, "Contornos Detectados")

    # 9. Desenho de bounding boxes
    img_caixas = desenhar_caixas_limite(img, contornos)
    exibir_imagem(img_caixas, "Bounding Boxes")

    # 10. Filtro por Área
    contornos_filtrados = filtrar_contornos(contornos, area_minima=500)
    print("Quantidade de objetos detectados (filtrados):", len(contornos_filtrados))

    img_contornos_bonus = desenhar_contornos(img, contornos_filtrados)
    exibir_imagem(img_contornos_bonus, "Contornos Filtrados")

    img_caixas_bonus = desenhar_caixas_limite(img, contornos_filtrados)
    exibir_imagem(img_caixas_bonus, "Caixas Delimitadoras")
    

"""
RESPOSTAS ÀS PERGUNTAS CONCEITUAIS (Checkpoint Aula 4):

1 - Por que a conversão para escala de cinza é importante?
    A conversão para cinza é importante porque simplifica a representação da imagem. Inicialmente, a imagem lida é colorida e é retornada como um np.array de 3 dimensões (altura, largura, canais). Ao transformarmos uma imagem colorida para uma escala de cinza, estamos reduzindo a dimensionalidade desta, pois antes a imagem que possuía três canais de cor (BGR) passa a ter apenas um, representado por um único valor de cinza. Assim, a imagem que antes possuía três dimensões (altura, largura e canais) passa a ter apenas duas dimensões (altura e largura), já que não há mais separação entre canais de cor. Essa transformação economiza memória, acelera o processamento e facilita a aplicação de técnicas como detecção de bordas, segmentação e thresholding.

2 - O que o histograma revela sobre a imagem
    O histograma revela distribuição dos níveis de intensidade dos picels (intensidade x frequência)
    No eixo X é representada a intensidade dos pixels que variam entre 0 a 255 e no eixo Y é indicada a quantidade de pixels que possuem aquele valor. Utilizar o histograma é útil para identificar diversos comportamentos da imagem:

    - Se a imagem está muito escura, a maioria dos pixels estará
    concentrada em valores baixos.

    - Se a imagem está muito clara, os pixels estarão concentrados
    em valores altos.

    - Se a imagem tem bom contraste, os valores estarão bem
    distribuídos ao longo do intervalo.

    - Se a imagem tem baixo contraste, os valores estarão
    concentrados em uma faixa pequena.

    Assim, é possível entender melhor que ajustem precisam ser feitos

3 -Por que aplicar morfologia antes de detectar contornos?
    Aplicar a morfologia antes do passo de detecção de contornos é importante para melhorar a qualidade da imagem. Após a binarização da imagem (threshold), normalmente aparecem pequenos ruídos e imperfeições na segmentação.

    No código utilizamos MORPH_CLOSE, uma função do OpenCV que realiza duas etapas. Primeiro ela dilata a imagem (expande o branco) e depois a erode (encolhe o branco).

    O resultado é o fechamento de buracos dentro dos objetos e a conexão de partes que deveriam estar juntas. Dessa forma, a imagem e os objetos ficam mais consistentes, reduzindo ruídos e facilitando a detecção correta dos contornos.

4. Em qual cenário real esse sistema poderia ser aplicado?
    Esse tipo de pipeline pode ser aplicado em diversos cenários nos quais o objetivo é detectar objetos automaticamente em imagens. Por exemplo, na inspeção industrial, sistemas de visão computacional podem ser utilizados em linhas de produção para detectar peças, contar objetos ou identificar defeitos em produtos. Dessa forma, uma câmera pode analisar as imagens capturadas e verificar se os componentes estão presentes ou se há falhas nas embalagens.

    Na agricultura, esse tipo de sistema também pode ser utilizado para identificar frutas, contar plantas ou detectar pragas em imagens capturadas por drones ou câmeras no campo, auxiliando no monitoramento das plantações.

    Além disso, pode ser aplicado em segurança e monitoramento, permitindo detectar pessoas ou objetos em imagens de câmeras de vigilância e auxiliando na análise automática das imagens capturadas.
"""