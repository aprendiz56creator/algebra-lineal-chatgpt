import plotly.graph_objects as go
import numpy as np

# Generar datos
z_vals = np.linspace(-5, 5, 100)
w_vals = np.linspace(-3, 3, 10)  # Valores fijos de w para animación

fig = go.Figure()

for w in w_vals:
    x = 42 - 8*z_vals + 4*w
    y = 8 - 2*z_vals - 12*w
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z_vals,
        mode='lines',
        name=f'w = {w:.1f}'
    ))

fig.update_layout(
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    ),
    title='Soluciones para distintos valores de w'
)
fig.show()