import cv2
"""
Biblioteca OpenCV para processamento de imagens.
Trabalha com arrays NumPy.
"""

import matplotlib.pyplot as plt
"""
Matplotlib para visualização de imagens e histogramas.
"""

def carregar_imagem(caminho: str):
    """
    Carrega imagem escolhida.
    
    Args:
        caminho (str): Caminho da imagem.
    
    Returns:
        np.ndarray: Imagem BGR ou None se falhar.
    
    Raises:
        ValueError: Se imagem não encontrada.
    """
    imagem = cv2.imread(caminho)
    if imagem is None:
        raise ValueError("Imagem não encontrada.")
    return imagem

def converter_cinza(imagem):
    """
    Converte imagem BGR para escala de cinza.
    
    Args:
        imagem (np.ndarray): Imagem colorida.
    
    Returns:
        np.ndarray: Imagem em tons de cinza.
    """
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

def exibir_imagem(imagem, titulo="Imagem"):
    """
    Exibe imagem usando Matplotlib.
    
    Args:
        imagem (np.ndarray): Imagem a exibir.
        titulo (str): Título da figura.
    """
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis("off")
    plt.show()

def plotar_histograma(imagem, titulo="Histograma de Intensidade"):
    """
    Plota histograma de intensidades.
    
    Args:
        imagem (np.ndarray): Imagem em cinza.
        titulo (str): Título do gráfico.
    """
    plt.hist(imagem.ravel(), bins=256, range=[0, 256])
    plt.title(titulo)
    plt.xlabel("Intensidade")
    plt.ylabel("Quantidade de Pixels")
    plt.show()

def ajustar_brilho_contraste(imagem, alpha=1.0, beta=0):
    """
    Ajusta brilho e contraste.
    
    Args:
        imagem (np.ndarray): Imagem de entrada.
        alpha (float): Fator de contraste.
        beta (float): Offset de brilho.
    
    Returns:
        np.ndarray: Imagem ajustada.
    """
    return cv2.convertScaleAbs(imagem, alpha=alpha, beta=beta)

def equalizar_imagem(imagem):
    """
    Equaliza histograma para melhorar contraste.
    
    Args:
        imagem (np.ndarray): Imagem em cinza.
    
    Returns:
        np.ndarray: Imagem equalizada.
    """
    return cv2.equalizeHist(imagem)

def calcular_metricas(imagem):
    """
    Calcula brilho e contraste.
    
    Args:
        imagem (np.ndarray): Imagem em cinza.
    
    Returns:
        tuple: (média, desvio padrão).
    """
    brilho = imagem.mean()
    contraste = imagem.std()
    return brilho, contraste 

def aplicar_threshold(imagem, threshold=127):  
    """
    Aplica threshold(limiar) manual.
    
    Args:
        imagem (np.ndarray): Imagem em cinza.
        threshold (int): Valor de threshold.
    
    Returns:
        imagem_binaria (np.ndarray): Imagem binária.
    """
    _, imagem_binaria = cv2.threshold(imagem, threshold, 255, cv2.THRESH_BINARY)
    return imagem_binaria

def aplicar_otsu(imagem):
    """
    Aplica threshold Otsu automático.
    
    Args:
        imagem (np.ndarray): Imagem em cinza.
    
    Returns:
        imagem_binaria (np.ndarray): Imagem binária.
    """
    _, imagem_binaria = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return imagem_binaria

def aplicar_morfologia(imagem_binaria):
    """
    Aplica operação morfológica de fechamento.
    
    Args:
        imagem_binary (np.ndarray): Imagem binária.
    
    Returns:
        np.ndarray: Imagem limpa.
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imagem_limpa = cv2.morphologyEx(imagem_binaria, cv2.MORPH_CLOSE, kernel)
    return imagem_limpa

def encontrar_contornos(imagem_binaria):
    """
    Detecta contornos externos.
    
    Args:
        imagem_binary (np.ndarray): Imagem binária.
    
    Returns:
        list: Lista de contornos.
    """
    contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contornos

def desenhar_contornos(imagem, contornos):
    """
    Desenha contornos na imagem.
    
    Args:
        imagem (np.ndarray): Imagem original.
        contornos (list): Contornos detectados.
    
    Returns:
        np.ndarray: Imagem com contornos.
    """
    imagem_copiada = imagem.copy()
    cv2.drawContours(imagem_copiada, contornos, -1, (0, 255, 0), 2)
    return imagem_copiada

def desenhar_caixas_limite(imagem, contornos):
    """
    Desenha caixas delimitadoras nos contornos.
    
    Args:
        imagem (np.ndarray): Imagem original.
        contornos (list): Contornos detectados.
    
    Returns:
        imagem_copiada (np.ndarray): Imagem com caixas.
    """
    imagem_copiada = imagem.copy()
    for contorno in contornos:
        x, y, l, a = cv2.boundingRect(contorno)
        cv2.rectangle(imagem_copiada, (x, y), (x + l, y + a), (0, 255, 0), 2)
    return imagem_copiada

# Função de filtro para área mínima de contornos
def filtrar_contornos(contornos, area_minima=100):
    """
    Filtra contornos por área mínima (remove ruído).
    
    Args:
        contornos (list): Lista de contornos.
        area_minima (int): Área mínima em pixels.
    
    Returns:
        list: Contornos filtrados.
    """
    return [c for c in contornos if cv2.contourArea(c) > area_minima]