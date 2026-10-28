# Calendário de Paradas Andritz

Calendário das paradas gerais (PG) de 2026 e 2027 num gráfico de Gantt, com uma linha por fábrica e uma barra por PG. Mostra quais paradas acontecem ao mesmo tempo e quantas estão rodando em cada dia. As paradas que já passaram ficam em cinza.

**Abrir:** <https://calendario-pgs.github.io/calendario-paradas/>, ou o arquivo `Calendario_PGs.html`, que funciona sem internet.

## Arquivos

- `Calendario_PGs.html`: o app, num arquivo só. É gerado pelo build; não edite à mão.
- `_dev/app_template.html`: o código-fonte. As datas ficam no bloco `CALS`, no topo do `<script>`.
- `_dev/build.py`: gera o `Calendario_PGs.html` (Python, só biblioteca padrão): `python _dev/build.py`.
- `index.html`: redireciona para o app (endereço do GitHub Pages).

## Atualizar

1. Edite `_dev/app_template.html`.
2. Rode `python _dev/build.py`.
3. Faça o commit e o push. O GitHub Pages publica sozinho em cerca de 1 minuto.
