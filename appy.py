# tpcuanti2

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulador de Sinestesia Visual-Auditiva")
st.write("Experimenta cómo una persona con sinestesia podría 'ver' sonidos como colores o patrones visuales.")

st.sidebar.header("Configuración del sonido")

note = st.sidebar.selectbox("Selecciona una nota musical", ["C", "D", "E", "F", "G", "A", "B"])
frequency = st.sidebar.slider("Frecuencia del sonido (Hz)", 20, 2000, 440)

def sound_to_color(frequency):
    # Escalar la frecuencia para obtener valores en un rango de color visible
    normalized_freq = (frequency - 20) / (2000 - 20)  # Normaliza entre 0 y 1
    red = np.sin(normalized_freq * np.pi) * 255
    green = np.sin(normalized_freq * np.pi / 2) * 255
    blue = np.cos(normalized_freq * np.pi) * 255
    return (int(red), int(green), int(blue))

def generate_visualization(color):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_facecolor(np.array(color) / 255)  # Configura el color de fondo
    ax.text(0.5, 0.5, '🎵', fontsize=120, ha='center', va='center', color='white')
    plt.axis('off')
    return fig

color = sound_to_color(frequency)
st.write(f"Color generado: {color}")
fig = generate_visualization(color)
st.pyplot(fig)
pattern = st.sidebar.selectbox("Selecciona un patrón visual", ["Onda", "Círculo", "Mosaico"])

def generate_pattern_visualization(pattern, color):
    fig, ax = plt.subplots(figsize=(4, 4))
    if pattern == "Onda":
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x * frequency / 100) * 100
        ax.plot(x, y, color=np.array(color) / 255, linewidth=4)
    elif pattern == "Círculo":
        circle = plt.Circle((0.5, 0.5), 0.3, color=np.array(color) / 255)
        ax.add_patch(circle)
    elif pattern == "Mosaico":
        for i in range(10):
            for j in range(10):
                square_color = np.array(color) / 255 * (i + j) / 20
                square = plt.Rectangle((i * 0.1, j * 0.1), 0.1, 0.1, color=square_color)
                ax.add_patch(square)
    plt.axis('off')
    return fig

fig = generate_pattern_visualization(pattern, color)
st.pyplot(fig)
