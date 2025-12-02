import matplotlib.animation as animation
import matplotlib.pyplot as plt


def visualizador_simples(array):
    estados = []

    def insertion_sort(array):
        n = len(array)
        for i in range(n - 1):
            j = i + 1
            while array[j] < array[j - 1] and j > 0:
                array[j], array[j - 1] = array[j - 1], array[j]
                estados.append(array.copy())
                j = j - 1

    arr_copia = array.copy()
    insertion_sort(arr_copia)

    # Configuração do gráfico
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(range(len(array)), array, color="lightblue")
    ax.set_title("Insertion Sort Algorithm")

    def animar(frame):
        if frame < len(estados):
            arr_estado = estados[frame]

            # Apenas atualiza as alturas das barras
            for k, bar in enumerate(bars):
                bar.set_height(arr_estado[k])

            for txt in ax.texts:
                txt.remove()

            for k, valor in enumerate(arr_estado):
                ax.text(
                    k,
                    valor + 0.5,
                    str(valor),
                    ha="center",
                    va="bottom",
                    fontweight="bold",
                )
        return bars

    # Cria animação
    anim = animation.FuncAnimation(
        fig, animar, frames=len(estados), interval=10, repeat=False, blit=True
    )
    plt.show()


# TESTE
if __name__ == "__main__":
    array_teste = [
        33,
        201,
        89,
        242,
        142,
        199,
        12,
        54,
        161,
        177,
        23,
        212,
        112,
        155,
        188,
        74,
        2,
        44,
        222,
        64,
        92,
        239,
        108,
    ]
    visualizador_simples(array_teste)
