import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
import numpy as np

from termopar.units import *
from termopar.instruments import Sensor, AmpOp, ADC, Filter, Temperature
from termopar.stat_test import ChiSquare

app = dash.Dash(__name__, external_stylesheets=["https://use.fontawesome.com/releases/v5.15.4/css/all.css"])

app.layout = html.Div([
    html.Div([
    html.Div([
        html.Div([
            html.I(className='fas fa-desktop', style={'color': 'var(--accent)', 'marginRight': '10px'}),
            html.Span("Dashboard de Simulação", style={'fontSize': '28px', 'fontWeight': '600', 'letterSpacing': '-0.5px'})
        ], style={'flexGrow': '1', 'textAlign': 'center'}),
        html.Button(
            html.I(className='fas fa-moon', id='theme-icon'),
            id='theme-toggle-btn',
            style={'background': 'transparent', 'border': 'none', 'color': 'var(--accent)', 'fontSize': '24px', 'cursor': 'pointer'}
        )
    ], className='header-bar'),
    
    html.Div([
        # Menu Vertical (Sidebar)
        html.Div([
            html.Button(html.I(className="fas fa-chevron-left", style={"color":"var(--accent)"}), id="toggle-sidebar-btn", className='card', style={'fontSize': '20px', 'border': 'none', 'cursor': 'pointer', 'marginBottom': '20px', 'padding': '10px 15px', 'float': 'right'}),
            html.Div([
                html.Details([
                html.Summary([html.I(className="fas fa-thermometer-half", style={"color": "var(--accent)", "marginRight": "8px"}), "Sensor (Sinal e Ruído)"], style={'fontWeight': '600', 'cursor': 'pointer', 'fontSize': '17px'}),
                html.Label("Temperatura Real (°C)"),
                dcc.Slider(0, 1000, 50, value=650, id='T-input'),
                
                html.Label("Ruído Branco (mV)"),
                dcc.Slider(0, 20, 1, value=2, id='white-noise-input'),
                
                html.Div([
                    dcc.Checklist(
                        options=[{'label': ' Adicionar ruído da rede (60Hz)', 'value': 'add_noise'}],
                        value=['add_noise'],
                        id='network-noise-check'
                    ),
                    html.Small("Referente à rede elétrica de 60Hz da fábrica.", style={'color': 'var(--text-muted)', 'display': 'block', 'marginTop': '5px'})
                ], style={'marginTop': '15px', 'marginBottom': '10px'}),
                
                html.Label("Ruído da Rede (Amp) (mV)"),
                dcc.Slider(0, 20, 1, value=5, id='amp-noise-input'),
                
                html.Div([
                    dcc.Checklist(
                        options=[{'label': ' Adicionar ruído 2º Harm. (120Hz)', 'value': 'add_harm'}],
                        value=[],
                        id='harm-noise-check'
                    ),
                    html.Small("Chaveamento de retificadores trifásicos dos fornos.", style={'color': 'var(--text-muted)', 'display': 'block', 'marginTop': '5px'})
                ], style={'marginTop': '15px', 'marginBottom': '10px'}),
                
                html.Label("Ruído 120Hz (Amp) (mV)"),
                dcc.Slider(0, 20, 1, value=3, id='amp-harm-input'),
                
                html.Div([
                    dcc.Checklist(
                        options=[{'label': ' Adicionar deriva térmica (0.05Hz)', 'value': 'add_drift'}],
                        value=[],
                        id='drift-noise-check'
                    ),
                    html.Small("Aquecimento do circuito ao longo do tempo.", style={'color': 'var(--text-muted)', 'display': 'block', 'marginTop': '5px'})
                ], style={'marginTop': '15px', 'marginBottom': '10px'}),
                
                html.Label("Deriva Térmica (Amp) (mV)"),
                dcc.Slider(0, 50, 1, value=10, id='amp-drift-input'),
            ]),
            
            html.Details([
                html.Summary([html.I(className="fas fa-wave-square", style={"color": "var(--accent)", "marginRight": "8px"}), "Amplificador de Instrumentação"], style={'fontWeight': '600', 'cursor': 'pointer', 'fontSize': '17px'}),
                html.Label("Ganho (A_V)"),
                dcc.Slider(1, 500, 10, value=100, id='gain-input'),
                
                html.Label("Offset (mV)"),
                dcc.Slider(0, 50, 1, value=15, id='offset-input'),
            ]),
            
            html.Details([
                html.Summary([html.I(className="fas fa-microchip", style={"color": "var(--accent)", "marginRight": "8px"}), "ADC"], style={'fontWeight': '600', 'cursor': 'pointer', 'fontSize': '17px'}),
                html.Label("Resolução (bits)"),
                dcc.Slider(4, 24, 1, value=10, id='bits-input'),
                
                html.Label("Frequência de Amostragem (Hz)"),
                dcc.Slider(100, 5000, 100, value=1000, id='fs-adc-input'),
            ]),
            
            html.Details([
                html.Summary([html.I(className="fas fa-filter", style={"color": "var(--accent)", "marginRight": "8px"}), "Filtro Digital"], style={'fontWeight': '600', 'cursor': 'pointer', 'fontSize': '17px'}),
                html.Label("Frequência de Corte (Hz)"),
                dcc.Slider(10, 500, 10, value=60, id='f-cut-input'),
                
                html.Label("Ordem do Filtro"),
                dcc.Slider(1, 10, 1, value=5, id='order-input'),
            ]),
            
            html.Details([
                html.Summary([html.I(className="fas fa-chart-bar", style={"color": "var(--accent)", "marginRight": "8px"}), "Teste Qui-Quadrado"], style={'fontWeight': '600', 'cursor': 'pointer', 'fontSize': '17px'}),
                html.Label("Lim. Inf. (xmin)"),
                dcc.Slider(-1.0, 0, 0.01, value=-0.1, id='xmin-input'),
                
                html.Label("Lim. Sup. (xmax)"),
                dcc.Slider(0, 1.0, 0.01, value=0.1, id='xmax-input'),
                
                html.Label("Nº de Bins"),
                dcc.Slider(10, 100, 5, value=50, id='bins-input'),
                
                html.Label("Janela de Média"),
                dcc.Slider(50, 1000, 50, value=200, id='mean-window-input'),
            ]),
                
            ], id="sidebar-content")
        ], id="sidebar-container", style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px', 'backgroundColor': 'var(--bg-sidebar)', 'height': '100vh', 'overflowY': 'auto', 'transition': 'width 0.3s'}),
        
        # Área Principal (Gráficos)
        html.Div([
            html.Div([
                dcc.Graph(id='amp-graph'),
            ], style={'width': '100%', 'marginBottom': '20px'}),
            html.Div([
                html.Div([
                    dcc.Graph(id='chi2-graph'),
                ], style={'flex': '1'}),
                html.Div(id='results-box', style={'width': '300px', 'padding': '20px', 'backgroundColor': 'var(--bg-card)', 'borderRadius': '10px', 'border': '1px solid var(--border-accent)', 'marginLeft': '20px', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center'}),
            ], style={'display': 'flex', 'alignItems': 'center', 'width': '100%'}),
        ], id="main-area", style={'width': '75%', 'display': 'inline-block', 'verticalAlign': 'top', 'transition': 'width 0.3s', 'padding': '30px'})
    ], style={'display': 'flex', 'backgroundColor': 'var(--bg-main)'})
    ], id='theme-wrapper', className='theme-light')
])

@app.callback(
    Output('amp-graph', 'figure'),
    Output('chi2-graph', 'figure'),
    Output('results-box', 'children'),
    Input('T-input', 'value'),
    Input('white-noise-input', 'value'),
    Input('amp-noise-input', 'value'),
    Input('network-noise-check', 'value'),
    Input('harm-noise-check', 'value'),
    Input('amp-harm-input', 'value'),
    Input('drift-noise-check', 'value'),
    Input('amp-drift-input', 'value'),
    Input('gain-input', 'value'),
    Input('offset-input', 'value'),
    Input('bits-input', 'value'),
    Input('fs-adc-input', 'value'),
    Input('f-cut-input', 'value'),
    Input('order-input', 'value'),
    Input('xmin-input', 'value'),
    Input('xmax-input', 'value'),
    Input('bins-input', 'value'),
    Input('mean-window-input', 'value'),
    Input('theme-wrapper', 'className')
)
def update_dashboard(T,
                     white_noise_mV,
                     amp_noise_mV,
                     network_noise_check,
                     harm_noise_check,
                     amp_harm_mV,
                     drift_noise_check,
                     amp_drift_mV,
                     gain,
                     offset_mV,
                     bits,
                     fs_adc,
                     f_cut,
                     order,
                     xmin,
                     xmax,
                     bins,
                     mean_window,
                     theme_class
                    ):
    # Setup params
    max_time_s = 1 * second
    fs_real_world = 5 * kHz
    t = np.arange(0, max_time_s, 1/fs_real_world)
    
    sens_termopar = 29.1 * mV / 700
    
    f_noise = 60
    if not network_noise_check or 'add_noise' not in network_noise_check:
        amp_noise_mV = 0
        
    if not harm_noise_check or 'add_harm' not in harm_noise_check:
        amp_harm_mV = 0
        
    if not drift_noise_check or 'add_drift' not in drift_noise_check:
        amp_drift_mV = 0
        
    sensor = Sensor(
        white_noise_V = white_noise_mV * mV, 
        amp_noise_V = amp_noise_mV * mV, 
        f_noise_Hz = f_noise * Hz, 
        sens_termopar = sens_termopar,
        amp_harm_V = amp_harm_mV * mV,
        amp_drift_V = amp_drift_mV * mV
    )
    amp = AmpOp(gain, v_offset=offset_mV * mV)
    adc = ADC(bits, fs_adc * Hz, fs_real_world)
    low_band = Filter(fs_adc * Hz, f_cut * Hz, order)
    temp = Temperature(sens_termopar, A_V=gain, v_offset=offset_mV * mV)
    
    # Run Simulation
    np.random.seed(42) # Mantém o ruído determinístico para uma mesma configuração
    t_out, v_out = sensor.run(t, T)
        
    v_amp = amp.run(v_out)
    n, v_digit = adc.run(t_out, v_amp)
    v_digit_filtered = low_band.run(v_digit)
    T_digit = temp.run(v_digit_filtered)
    
    # Plot 1: Amp Output and ADC Digits (Sinal após saída do amplificador)
    fig_amp = go.Figure()
    fig_amp.add_trace(go.Scatter(x=t_out, y=v_amp, mode='lines', name='Saída do Amplificador (Analógico)'))
    fig_amp.add_trace(go.Scatter(x=n, y=v_digit, mode='lines+markers', name='Saída do ADC (Digital)', marker=dict(size=4)))
    fig_amp.add_trace(go.Scatter(x=n, y=v_digit_filtered, mode='lines', name='Sinal Digital Filtrado', line=dict(width=2)))
    fig_amp.update_layout(title="Sinal após o Amplificador e ADC", xaxis_title="Tempo (s)", yaxis_title="Tensão (V)", template='plotly_dark' if theme_class == 'theme-dark' else 'plotly_white', plot_bgcolor='#1f2833' if theme_class == 'theme-dark' else '#ffffff', paper_bgcolor='#121212' if theme_class == 'theme-dark' else '#f9f9f9', uirevision='constant', legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

    # Plot 3: Filtered & Reconstructed Temperature
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(x=n, y=T_digit, mode='lines', name='Temperatura Reconstruída (Filtro+ADC)', line=dict(color='green')))
    fig_temp.add_hline(y=T, line_dash="dash", line_color="red", annotation_text="Temperatura Real")
    fig_temp.update_layout(title="Temperatura Reconstruída vs Temperatura Real", xaxis_title="Tempo (s)", yaxis_title="Temperatura (°C)", template='plotly_dark' if theme_class == 'theme-dark' else 'plotly_white', plot_bgcolor='#1f2833' if theme_class == 'theme-dark' else '#ffffff', paper_bgcolor='#121212' if theme_class == 'theme-dark' else '#f9f9f9', uirevision='constant')
    
    # ChiSquare Test (ligando de volta aos sliders para ajustar dinamicamente o zoom/range)
    chi2_test = ChiSquare(xmin=xmin, xmax=xmax, num_bins=bins, mean_window=mean_window)
    chi2_val, dof, chi2_out = chi2_test.run(v_digit_filtered[5::])
    
    fig_chi2 = go.Figure()
    bin_centers = chi2_out['hist']['bin_centers']
    density_obs = chi2_out['hist']['density_obs']
    bin_edges = chi2_out['hist']['bin_edges']
    bin_sizes = chi2_out['hist']['bin_sizes']
    x_fit = chi2_out['fit']['x']
    density_expected = chi2_out['fit']['density_expected']
    params = chi2_out['fit']['params']
    
    # Criando coordenadas no formato "escada" (stairs) para o histograma
    x_stairs, y_stairs = [bin_edges[0]], [0]
    for i in range(len(density_obs)):
        x_stairs.extend([bin_edges[i], bin_edges[i+1]])
        y_stairs.extend([density_obs[i], density_obs[i]])
    x_stairs.append(bin_edges[-1])
    y_stairs.append(0)
    
    fig_chi2.add_trace(go.Scatter(x=x_stairs, y=y_stairs, mode='lines', name='Densidade Obs.', line=dict(color='var(--accent)' if theme_class == 'theme-dark' else 'blue', width=3), fill=None))
    fig_chi2.add_trace(go.Scatter(x=x_fit, y=density_expected, mode='lines', name='Curva Ajustada', line=dict(color='red', width=3)))
    
    # Add mean and variance vertical lines
    mean_val = 0 # O resíduo sempre tem média matemática igual a zero!
    variance_val = np.var(v_digit_filtered[-mean_window:])
    std_val = np.sqrt(variance_val)
    fig_chi2.add_vline(x=mean_val, line_width=2, line_dash="dash", line_color="red", annotation_text=f"μ = {mean_val:.2f}")
    fig_chi2.add_vline(x=mean_val - std_val, line_width=2, line_dash="dash", line_color="black")
    fig_chi2.add_vline(x=mean_val + std_val, line_width=2, line_dash="dash", line_color="black")
    
    fig_chi2.update_layout(
        title=f"Densidade observada (k={bins}), χ²={chi2_val:.2f}",
        xaxis_title="Resíduo (°C)", yaxis_title="Densidade", 
        template='plotly_dark' if theme_class == 'theme-dark' else 'plotly_white', 
        plot_bgcolor='#1f2833' if theme_class == 'theme-dark' else '#ffffff', 
        paper_bgcolor='#121212' if theme_class == 'theme-dark' else '#f9f9f9', 
        uirevision='constant', 
        barmode='overlay', 
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    from scipy.stats import chi2
    p_value = chi2.sf(chi2_val, dof)
    chi2_status = "Aprovado ✅" if p_value > 0.05 else "Rejeitado ❌"
    
    mean_temp_reconstructed = np.mean(T_digit[-mean_window:])
    
    color_status = "#4caf50" if p_value > 0.05 else "#f44336"
    
    results_box = html.Div([
        html.H3("Resultados da Simulação", style={'textAlign': 'center', 'color': 'var(--accent)', 'marginBottom': '20px'}),
        html.Div([
            html.Strong("Temperatura Média Calculada: ", style={'fontSize': '18px'}),
            html.Span(f"{mean_temp_reconstructed:.2f} °C", style={'fontSize': '22px', 'fontWeight': 'bold', 'color': 'var(--text-main)'})
        ], style={'marginBottom': '20px'}),
        html.Div([
            html.Strong("Teste Qui-Quadrado: ", style={'fontSize': '18px'}),
            html.Span(chi2_status, style={'fontSize': '22px', 'fontWeight': 'bold', 'color': color_status})
        ]),
        html.P(f"(p-valor: {p_value:.4f}, limite 0.05)", style={'color': 'var(--text-muted)', 'marginTop': '5px'})
    ], style={'color': 'var(--text-main)'})
    
    return fig_amp, fig_chi2, results_box


@app.callback(
    Output('sidebar-container', 'style'),
    Output('main-area', 'style'),
    Output('sidebar-content', 'style'),
    Output('toggle-sidebar-btn', 'children'),
    Input('toggle-sidebar-btn', 'n_clicks'),
    State('sidebar-container', 'style'),
    State('main-area', 'style'),
    prevent_initial_call=True
)
def toggle_sidebar(n_clicks, sidebar_style, main_style):
    if n_clicks % 2 == 1:
        # Collapsed
        sidebar_style['width'] = '4%'
        main_style['width'] = '96%'
        return sidebar_style, main_style, {'display': 'none'}, html.I(className="fas fa-chevron-right", style={"color":"var(--accent)"})
    else:
        # Expanded
        sidebar_style['width'] = '25%'
        main_style['width'] = '75%'
        return sidebar_style, main_style, {'display': 'block'}, html.I(className="fas fa-chevron-left", style={"color":"var(--accent)"})


@app.callback(
    Output('theme-wrapper', 'className'),
    Output('theme-icon', 'className'),
    Input('theme-toggle-btn', 'n_clicks'),
    State('theme-wrapper', 'className'),
    prevent_initial_call=True
)
def toggle_theme(n_clicks, current_theme):
    if current_theme == 'theme-light':
        return 'theme-dark', 'fas fa-sun'
    return 'theme-light', 'fas fa-moon'

if __name__ == '__main__':
    app.run(debug=True)
