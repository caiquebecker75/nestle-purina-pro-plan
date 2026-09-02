# Pro Plan Science System · Nestlé Purina × 75 LAB

Apresentação comercial em HTML (10 telas) da proposta estratégica da 75 LAB para o
ponto natural de Pro Plan no piloto Dog's Day (Pinheiros, Vila Olímpia, Granja Julieta).

## Como usar
- Abra `index.html` no navegador (ou sirva a pasta com qualquer servidor estático).
- Navegação: setas / espaço / PageUp-PageDown, `Home`/`End`, `M` abre o índice, swipe no mobile.
- Exportar PDF: `Cmd+P` (há estilo de impressão, uma tela por página).

## Fotos e renders
- `assets/vt/` · 20 fotos da visita técnica (31/08/2026), 10 por loja, usadas no mosaico da tela 3 (com lightbox).
- `assets/render-01/02/03.jpg` · renders de estúdio do sistema (frontal e duas perspectivas).
- `assets/render-amb-01..07.jpg` · renders ambientados (corredor, troca de testeira, gaveta de cartuchos, navegação, ponta de gôndola, abastecimento, trilhos reguláveis).
- `assets/render-tower-01..03.jpg` · torre giratória 360° (formato flagship); `assets/render-wall-01.jpg` · módulo vertical compacto.
- Tela 6: cada pilar mostra o render que o ilustra. Tela 7: galeria de 7 renders com lightbox para os 14. Tela 8: Compact = módulo vertical (`render-compact.jpg`), Core = sistema na gôndola (`render-core.jpg`), Flagship = torre 360° (`render-flagship.jpg`).

## Versão em arquivo único
`python3 build-standalone.py` gera `proplan-science-system-standalone.html` com todas as imagens embutidas.

## Marca
- Identidade Purina Pro Plan: preto `#0B0B0C`, vermelho Purina `#E4002B`, branco/prata, xadrez.
- O lockup "PURINA / PRO PLAN" é tipográfico com o xadrez em SVG. Substitua pelo logo oficial
  (`assets/proplan-logo.svg`) quando o brand guide chegar.
- 75 LAB: wordmarks em `assets/75lab-wordmark-*.png`.

## Fonte do conteúdo
`Estrategia_Nestle_Purina_Pro_Plan_75LAB.docx` (01/09/2026) e visita técnica de 31/08/2026.
