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
    
    # 1. Carregar imagem 
    img = carregar_imagem("puppy.png") 
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
    exibir_imagem(img_caixas_bonus, "Bounding Boxes Filtrados")
    
