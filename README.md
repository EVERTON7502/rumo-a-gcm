# Rumo à GCM Salvador

App de estudos para o concurso da **Guarda Civil Municipal de Salvador** (Edital nº 02/2026, banca FGV). Prova objetiva em **17/01/2027, das 8h às 12h30**.

Funciona no navegador do computador (layout principal) e do celular, pode ser instalado como aplicativo e abre sem internet depois da primeira visita.

## Funcionalidades

- **Hoje**: "Sua próxima ação", contagem regressiva até a prova, tempo estudado hoje e nos últimos 7 dias, sequência de dias, progresso da semana e do plano, gráfico dos últimos 7 dias, mapa de constância de 28 dias e progresso por matéria.
- **2 matérias por dia**, cada uma com seus assuntos e etapas (aula de 20 min com aviso de pausa a cada 6 min, pausa, resumo em PDF, **questões FGV em todo bloco**, erros e flashcards). Você começa por qualquer uma. Depois das 2, aparece um **bônus opcional**, que adianta o plano sem criar pendência.
- **Cronômetro livre**: conta para cima, sem tempo fixo (os minutos são só sugestão), com Iniciar, Pausar/Retomar e Parar e concluir. Tudo é gravado a cada etapa; fechar a página não perde o que foi feito.
- **Revisões 1, 7 e 30 dias** depois de cada assunto, e **Caderno de erros**.
- **Plano** de 11 semanas (de terça, 03/11/2026, até a prova em 17/01/2027).
- **Matérias**: as 8 matérias e os 130 assuntos do edital, cada um com PDF e flashcards.
- **Aulas deste assunto**: 180 vídeos do YouTube escolhidos e conferidos, um para cada parte do assunto (ex.: Penal 1 = "Conceito de Direito Penal" + "Fontes do Direito Penal"), com título, professor e duração. O botão "Aula" abre direto o primeiro vídeo. Lista em tools/aulas.json.
- **O que o edital pede** em cada assunto: o texto do edital dividido em pontos, com caixinha para marcar o que já estudou, busca de aula de cada ponto e link "Ler a lei" quando o ponto cita uma lei. Use esta lista para conferir se a aula cobriu tudo.
- **Como a FGV cobra**: padrões de 237 questões de 4 provas da FGV (GCM Salvador 2019, Polícia Civil PR 2026, Câmara de Fortaleza 2023, Bombeiros AM 2021) em cada matéria e assunto, na aba Edital e na etapa Aula. Detalhes em PADROES_FGV.md.
- **Minhas anotações** em cada assunto (na aba Matérias, no bloco em andamento e nas revisões). Salvam sozinhas enquanto você digita e entram no código de backup.
- **Questões**: 69 questões da prova oficial GCM Salvador 2019 (FGV) com gabarito oficial; 39 questões autorais ficam marcadas e só aparecem se você escolher. As questões são apoio e não contam para concluir os estudos.
- **Simulados no plano**: mini simulado de 30 questões aos domingos a partir da semana 3 e simulados completos de 70 questões em 03/01 e 10/01/2027.
- **Simulados**: aleatório, modelo do edital (70 questões, resultado por Módulo com a meta 14/21/35) e a prova de 2019 completa em 4 horas.
- **Edital e prova**: quadro de matérias, regra de aprovação, etapas, TAF, avaliação psicológica, dia da prova, desempate, curso de formação, cronograma, requisitos e link oficial.
- Tema escuro (padrão) e claro, tutorial de 3 passos na primeira visita, seção "Como usar".

## Instalar no celular ou no computador

- **Android (Chrome)**: abra o site, toque no menu ⋮ e em **Instalar app** (ou "Adicionar à tela inicial").
- **iPhone (Safari)**: toque em **Compartilhar** e em **Adicionar à Tela de Início**.
- **Computador (Chrome ou Edge)**: clique no ícone de instalar na barra de endereço.

## Sincronizar notebook e celular

Na aba **Hoje**, abra **Sincronizar notebook e celular** e siga os 3 passos uma vez em cada aparelho:

1. **Criar chave no GitHub** (permissão só "gist", sem expiração) e copie a chave `ghp_…`.
2. Cole no campo e toque em **Conectar**.

O progresso fica num gist **privado** da sua conta do GitHub (`rumo-a-gcm-progresso.json`, não apague). Cada mudança é enviada sozinha alguns segundos depois, e o que foi feito em outro aparelho chega quando o app abre ou volta para a tela. Os aparelhos são **juntados**, nunca sobrescritos: blocos, revisões, erros, anotações (vale a mais nova) e tempo estudado (soma dos aparelhos).

## Backup e restauração do progresso

O progresso fica **só no navegador de cada aparelho** (localStorage, chave `gcm2`). Ele não vai sozinho de um aparelho para outro nem de um endereço para outro.

1. Na aba **Hoje**, no fim da página, abra **Backup do progresso** e toque em **Gerar e copiar código** (começa com `GCMBKP1:`).
2. Guarde o código (Notas, e-mail ou mensagem para você mesmo).
3. No outro aparelho ou endereço, cole o código no mesmo campo e toque em **Restaurar deste código**.

Faça backup de vez em quando. Limpar os dados do navegador apaga o progresso daquele aparelho.

## Como atualizar o site

1. Edite os arquivos e aumente `VERSION` em `sw.js` (ex.: `v1.0.1`).
2. `git commit` e `git push` na branch `main`. O GitHub Pages publica em 1 ou 2 minutos.
3. Ao abrir o app, aparece "Nova versão disponível"; toque em **Atualizar**.

Os ícones são gerados com `python tools/gerar_icones.py` (precisa do Pillow).

## Estrutura

```
index.html            app completo (HTML, CSS e JS num arquivo só)
manifest.webmanifest  dados de instalação (PWA)
sw.js                 service worker (offline, cache-first)
icons/                ícones 192, 512, maskable, apple-touch-icon e favicon
fonts/                Inter e Plus Jakarta Sans (woff2, licença OFL)
CONFERENCIA_EDITAL.md conferência item por item do edital com o app
tools/                script dos ícones
```

## Avisos

- As questões de 2019 são da **FGV** (prova oficial da GCM Salvador 2019) e estão aqui **só para estudo pessoal**. Os direitos são da banca.
- Este app não tem vínculo com a Prefeitura de Salvador nem com a FGV. Confira sempre o edital e os comunicados na página oficial: https://conhecimento.fgv.br/concursos/pmsguarda2026
