import numpy as np

def regular_polygon_Relo(n: int = 3,
                         center: np.ndarray = np.array([0, 0]),
                         r: float = 1,
                         N: int = 100) -> np.ndarray:
    """Возвращает матрицу координат точек границы правильного многоугольника Рело.

    Arguments:
        n: количество вершин (нечетное, >2)
        center: центр фигуры (np.array([x, y]))
        r: ширина (радиус дуг)
        N: число точек на одну сторону

    Returns:
        np.ndarray формы (n*N, 2)
    """

    # --- проверки (как требует задание) ---
    assert isinstance(n, int), 'n должно быть целым'
    assert n > 2, 'n должно быть больше 2'
    assert n % 2 == 1, 'n должно быть нечетным'
    assert isinstance(center, np.ndarray), 'center должен быть numpy массивом'
    assert center.shape == (2,), 'center должен быть размера (2,)'
    assert r > 0, 'r должно быть положительным'
    assert isinstance(N, int), 'N должно быть целым'
    assert N > 0, 'N должно быть положительным'

    # --- формулы из задания 4.2 ---
    l = 2 * r * np.sin(np.pi / (2 * n))
    R = l / (2 * np.sin(np.pi / n))

    # --- вершины правильного n-угольника ---
    t = np.arange(0, 2 * np.pi, 2 * np.pi / n)
    vertices = center + R * np.transpose([np.cos(t), np.sin(t)])

    # --- параметры дуг ---
    alpha = 2 * np.pi / n
    beta = np.pi / n
    angle = np.linspace(-beta, beta, N)

    # --- построение всех сторон ---
    list_sides = [
        vertices[i] + r * np.transpose([
            np.cos(np.pi + i * alpha + angle),
            np.sin(np.pi + i * alpha + angle)
        ])
        for i in range(n)
    ]

    sides = np.concatenate(list_sides)
    return sides
