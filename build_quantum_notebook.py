#!/usr/bin/env python3
"""Constrói o notebook Colab didático de Física Quântica, Qiskit e QML."""

from __future__ import annotations

import hashlib
import json
import textwrap
from pathlib import Path


OUTPUT = Path("trilha_quantum_ia_pesquisador_colab.ipynb")
cells: list[dict] = []


def _source(text: str) -> list[str]:
    clean = textwrap.dedent(text).strip("\n") + "\n"
    return clean.splitlines(keepends=True)


def _cell_id(kind: str, text: str, index: int) -> str:
    payload = f"{kind}:{index}:{text}".encode("utf-8")
    return hashlib.sha1(payload).hexdigest()[:12]


def md(text: str, tags: list[str] | None = None) -> None:
    idx = len(cells)
    cells.append(
        {
            "cell_type": "markdown",
            "id": _cell_id("md", text, idx),
            "metadata": {"tags": tags or []},
            "source": _source(text),
        }
    )


def code(text: str, tags: list[str] | None = None) -> None:
    idx = len(cells)
    cells.append(
        {
            "cell_type": "code",
            "execution_count": None,
            "id": _cell_id("code", text, idx),
            "metadata": {"tags": tags or []},
            "outputs": [],
            "source": _source(text),
        }
    )


md(r"""
<div style="overflow:hidden; margin:6px 0 24px 0; border:1px solid #334155; border-radius:24px; background:radial-gradient(circle at 88% 12%,rgba(34,211,238,.22),transparent 27%),radial-gradient(circle at 8% 92%,rgba(139,92,246,.25),transparent 32%),linear-gradient(135deg,#07111f 0%,#101c35 52%,#16213e 100%); box-shadow:0 14px 38px rgba(2,6,23,.28); color:#f8fafc;">
  <div style="height:5px; background:linear-gradient(90deg,#22d3ee,#8b5cf6,#f472b6);"></div>
  <div style="display:flex; flex-wrap:wrap; align-items:center; gap:28px; padding:30px;">
    <div style="position:relative; flex:0 0 164px; text-align:center;">
      <a href="https://github.com/MarceloClaro" target="_blank" rel="noopener noreferrer" title="Abrir o perfil de Marcelo Claro no GitHub">
        <img src="https://avatars.githubusercontent.com/u/58664974?v=4" alt="Foto do autor Prof. Marcelo Claro Laranjeira" width="154" height="154" style="display:block; width:154px; height:154px; object-fit:cover; margin:auto; border-radius:26px; border:3px solid rgba(255,255,255,.92); box-shadow:0 12px 28px rgba(0,0,0,.42);">
      </a>
      <div style="display:inline-block; position:relative; margin-top:-13px; padding:6px 11px; border-radius:999px; background:#22c55e; color:#052e16; font-size:11px; font-weight:900; letter-spacing:.04em; box-shadow:0 4px 10px rgba(0,0,0,.3);">AUTOR • PESQUISADOR</div>
    </div>
    <div style="flex:1 1 480px; min-width:260px;">
      <div style="font-size:12px; font-weight:800; letter-spacing:.16em; color:#67e8f9; margin-bottom:10px;">QUANTUM RESEARCH LAB • COLAB EDITION</div>
      <h1 style="font-size:34px; line-height:1.12; color:#ffffff; margin:0 0 10px 0;">Física Quântica, Computação Quântica e IA</h1>
      <div style="font-size:17px; line-height:1.5; color:#cbd5e1; margin-bottom:18px;">Do primeiro qubit a um protocolo de Quantum Machine Learning pré-registrável, auditável e orientado por evidências.</div>
      <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:20px;">
        <span style="padding:6px 10px; border:1px solid rgba(103,232,249,.35); border-radius:999px; background:rgba(8,145,178,.14); color:#cffafe; font-size:12px;">Qiskit 2.x</span>
        <span style="padding:6px 10px; border:1px solid rgba(196,181,253,.35); border-radius:999px; background:rgba(124,58,237,.14); color:#ede9fe; font-size:12px;">QML reprodutível</span>
        <span style="padding:6px 10px; border:1px solid rgba(253,164,175,.35); border-radius:999px; background:rgba(225,29,72,.12); color:#ffe4e6; font-size:12px;">SDD + TDD científico</span>
        <span style="padding:6px 10px; border:1px solid rgba(134,239,172,.35); border-radius:999px; background:rgba(22,163,74,.12); color:#dcfce7; font-size:12px;">OSF-ready</span>
      </div>
      <div style="display:flex; flex-wrap:wrap; align-items:center; gap:12px; padding:14px 16px; border:1px solid rgba(148,163,184,.25); border-radius:14px; background:rgba(15,23,42,.54);">
        <div style="flex:1 1 270px;">
          <div style="font-size:18px; font-weight:850; color:#ffffff;">Prof. Marcelo Claro Laranjeira</div>
          <div style="font-size:13px; color:#94a3b8; margin-top:3px;">Pesquisa em Inteligência Artificial, Educação e Computação Quântica</div>
        </div>
        <a href="https://github.com/MarceloClaro" target="_blank" rel="noopener noreferrer" style="display:inline-block; padding:9px 14px; border-radius:10px; background:#f8fafc; color:#0f172a; font-size:13px; font-weight:850; text-decoration:none;">GitHub ↗ @MarceloClaro</a>
      </div>
    </div>
  </div>
  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:1px; background:rgba(148,163,184,.18); border-top:1px solid rgba(148,163,184,.20);">
    <div style="padding:12px 16px; background:rgba(15,23,42,.70);"><div style="font-size:11px;color:#94a3b8;">DESENHO</div><div style="font-weight:800;">Comparativo pareado</div></div>
    <div style="padding:12px 16px; background:rgba(15,23,42,.70);"><div style="font-size:11px;color:#94a3b8;">VALIDAÇÃO</div><div style="font-weight:800;">CV aninhada 4 × 3</div></div>
    <div style="padding:12px 16px; background:rgba(15,23,42,.70);"><div style="font-size:11px;color:#94a3b8;">ESCADA</div><div style="font-weight:800;">Ideal → shots → ruído → QPU</div></div>
    <div style="padding:12px 16px; background:rgba(15,23,42,.70);"><div style="font-size:11px;color:#94a3b8;">REGRA</div><div style="font-weight:800;">Evidence Gate go/no-go</div></div>
  </div>
</div>

**Perfil e portfólio de código:** [github.com/MarceloClaro](https://github.com/MarceloClaro)  

**Edição didática:** agosto de 2026  
**Ambiente-alvo:** Google Colab • Python 3 • Qiskit 2.3 • Qiskit Aer 0.17 • Qiskit Machine Learning 0.9

> **Pergunta central:** como transformar conceitos quânticos em um experimento de IA reproduzível, comparável com métodos clássicos e cientificamente honesto?

Ao terminar esta trilha, você será capaz de:

1. explicar os princípios essenciais da física quântica sem depender de jargão;
2. representar estados com notação de Dirac, vetores e probabilidades;
3. construir circuitos, visualizar a esfera de Bloch e interpretar medições;
4. distinguir superposição, interferência, correlação e entrelaçamento;
5. simular ruído e compreender as limitações dos dispositivos NISQ;
6. explicar onde a computação quântica pode — e onde ainda não consegue — ajudar a IA;
7. comparar regressão logística, SVM clássico e kernel quântico no mesmo protocolo;
8. transformar métricas em um parecer de evidência, com próximos passos auditáveis;
9. executar validação aninhada, equivalência e análise mecanística multibase;
10. exportar resultados, protocolo, métodos e achados para um paper reproduzível.

**Não é necessário conhecimento prévio de física quântica.** Álgebra linear e Python são introduzidos conforme surgem.
""")

md(r"""
## Como usar esta trilha

Execute as células na ordem, usando **Ambiente de execução → Executar tudo** somente depois de ler os avisos opcionais.

| Rota | Módulos | Tempo aproximado | Produto |
|---|---:|---:|---|
| Leitura leiga | mapas + paradas 🧒 | 45–70 min | intuição, analogias e vocabulário |
| Essencial | 0–3 | 70–100 min | fundamentos, qubit, medição e Bell |
| Aplicada | 0–6 | 3–4 h | comparação clássica × quântica e portão de evidência |
| Pesquisa | 0–8 | 1–2 dias | CV aninhada repetida, escada de ruído, aplicações e pacote de paper |

Cada laboratório segue o ciclo:

**intuição → previsão → formalização → código → visualização → interpretação → teste → exercício.**

### Legenda pedagógica

- 🌱 **Nível 0:** intuição e linguagem simples.
- 🧒 **Explique a uma criança:** história concreta antes da fórmula.
- 🧠 **Mapa mental:** relações entre ideias, não uma lista para decorar.
- 🎓 **Graduação:** matemática e implementação.
- 🔬 **Pesquisa:** hipótese, controles, limitações e reprodutibilidade.
- ✅ **TDD:** teste automático do resultado esperado.
- ⚠️ **Onde a analogia falha:** limite obrigatório para preservar o rigor.
- 🧭 **Pare e interprete:** não avance antes de explicar o gráfico com suas palavras.

> **Regra de ouro:** um resultado quântico só é cientificamente interessante quando comparado a baselines clássicos fortes, sob o mesmo particionamento de dados e sem vazamento de informação.

### Método das três camadas

Cada conceito difícil pode ser lido em três níveis, sem contradição:

1. **Imagem concreta:** algo que uma criança consegue imaginar.
2. **Tradução científica:** o conceito correto, com símbolos quando necessário.
3. **Limite da imagem:** o ponto em que a analogia deixa de representar a física.

Não pule a terceira camada. Uma analogia é uma ponte para o conceito — não é o próprio fenômeno.
""")

md(r"""
## Mapa conceitual da trilha

| Módulo | Pergunta orientadora | Evidência produzida |
|---:|---|---|
| 0 | Como manter o experimento reproduzível? | manifesto de ambiente e sementes |
| 1 | O que torna um fenômeno quântico? | amplitudes complexas e regra de Born |
| 2 | Como programar e medir um qubit? | circuitos, Statevector, Bloch e shots |
| 3 | O que é entrelaçamento? | estado de Bell, entropia e correlações |
| 4 | Como interferência e ruído alteram resultados? | curva de interferência e modelo NISQ |
| 5 | Onde a computação quântica entra em IA? | mapa de decisão e arquitetura híbrida |
| 6 | O kernel quântico melhora este problema? | benchmark, incerteza pareada e portão de evidência |
| 7 | Como transformar o laboratório em pesquisa? | ablações, validação robusta, escada de ruído e aplicações |
| 8 | Como migrar para hardware real com responsabilidade? | Bell e âncoras de kernel opcionais em QPU |
""")

md(r"""
## SDD — contrato científico e de software

Este notebook trata o experimento como um pequeno produto científico.

### Requisitos funcionais

1. Executar em uma sessão limpa do Google Colab.
2. Gerar resultados determinísticos sempre que o simulador permitir.
3. Separar treino e teste **antes** de ajustar transformações.
4. Comparar modelos sobre as mesmas observações.
5. Produzir métricas, figuras e arquivos exportáveis.
6. Não declarar vantagem quântica a partir de uma única amostra pequena.
7. Toda analogia deve apresentar sua tradução formal e declarar onde deixa de funcionar.

### Critérios de aceitação

- estados normalizados: $\sum_i |\alpha_i|^2=1$;
- porta Hadamard em $|0\rangle$: $P(0)=P(1)=0{,}5$ no statevector ideal;
- Bell ideal: somente `00` e `11`, salvo flutuação/ruído introduzido;
- kernel: matriz aproximadamente simétrica, diagonal próxima de 1 dentro de tolerância compatível com shots e sem autovalor negativo relevante após correção PSD;
- resultados: pelo menos três modelos, métricas comparáveis e versões registradas.
- inferência: diferença pareada contra baseline pré-especificado, sem converter um único resultado em alegação de vantagem.

### Hipótese do estudo demonstrativo

> **H1:** um kernel quântico baseado em mapa de características ZZ consegue separar o conjunto sintético `make_moons` com desempenho mensurável, mas não deve ser considerado superior sem comparação multi-semente, análise de custo, controle de hiperparâmetros e teste em dados externos.

Essa formulação evita confundir **prova de conceito** com **vantagem quântica**.
""")

code(r"""
# @title 0.1 — Configuração do pesquisador {display-mode: "form"}
NOME_PESQUISADOR = "Marcelo Claro Laranjeira"  # @param {type:"string"}
PROJETO = "Fundamentos quânticos aplicados à pesquisa em IA"  # @param {type:"string"}
SEED = 42  # @param {type:"integer"}
SHOTS = 2048  # @param {type:"slider", min:256, max:8192, step:256}
MODO_RAPIDO = True  # @param {type:"boolean"}
EXECUTAR_EXPERIMENTOS_ESTENDIDOS = False  # @param {type:"boolean"}
EXECUTAR_VALIDACAO_ROBUSTA = False  # @param {type:"boolean"}
EXECUTAR_ESCADA_RUIDO = False  # @param {type:"boolean"}
EXECUTAR_SUITE_APLICACOES = False  # @param {type:"boolean"}
EXECUTAR_PAPER_AVANCADO = False  # @param {type:"boolean"}
EXECUTAR_CURVAS_APRENDIZAGEM = False  # @param {type:"boolean"}
EXECUTAR_RUIDO_ANINHADO = False  # @param {type:"boolean"}
EXECUTAR_BENCHMARK_AMPLIADO = False  # @param {type:"boolean"}
EXECUTAR_BASELINES_DEEP = False  # @param {type:"boolean"}
EXECUTAR_AQUISICAO_ATIVA = False  # @param {type:"boolean"}

print(f"Pesquisador(a): {NOME_PESQUISADOR}")
print(f"Projeto: {PROJETO}")
print(f"Semente: {SEED} | shots: {SHOTS} | modo rápido: {MODO_RAPIDO}")
print(
    "Módulos de custo elevado:",
    {
        "ablações": EXECUTAR_EXPERIMENTOS_ESTENDIDOS,
        "CV aninhada repetida": EXECUTAR_VALIDACAO_ROBUSTA,
        "ruído Aer": EXECUTAR_ESCADA_RUIDO,
        "suíte de aplicações": EXECUTAR_SUITE_APLICACOES,
        "paper avançado": EXECUTAR_PAPER_AVANCADO,
        "curvas de aprendizagem": EXECUTAR_CURVAS_APRENDIZAGEM,
        "ruído aninhado multissemente": EXECUTAR_RUIDO_ANINHADO,
        "benchmark 10+ bases": EXECUTAR_BENCHMARK_AMPLIADO,
        "CNN e embedding congelado": EXECUTAR_BASELINES_DEEP,
        "Nyström e aquisição ativa": EXECUTAR_AQUISICAO_ATIVA,
    },
)
""")

md(r"""
# Módulo 0 — Preparar o laboratório computacional

## Por que instalar poucas bibliotecas?

O material anterior misturava vários frameworks e fixava componentes de baixo nível. Isso aumenta conflitos e distrai do objetivo científico. Aqui usamos uma pilha mínima:

- **Qiskit:** circuitos, estados e informação quântica;
- **Qiskit Aer:** simulação eficiente e modelos de ruído;
- **Qiskit Machine Learning:** kernels e algoritmos híbridos;
- **scikit-learn:** baselines e métricas;
- **Matplotlib/Seaborn:** visualização.

As versões do ecossistema quântico são limitadas à mesma série menor para que APIs e resultados permaneçam reprodutíveis. Se o Colab solicitar reinício após a instalação, reinicie e volte a esta seção.
""")

code(r"""
# @title 0.2 — Instalação reproduzível (execute uma vez)
%pip install -q "qiskit[visualization]~=2.3.1" "qiskit-aer~=0.17.1" "qiskit-machine-learning~=0.9.0" "scikit-learn>=1.5,<2.0" "scikit-image>=0.24,<1" "statsmodels>=0.14,<1" "torch>=2.3,<3" "torchvision>=0.18,<1" "seaborn>=0.13,<1.0" "ipywidgets>=8,<9" "jinja2>=3.1,<4" "medmnist>=3,<4"
""")

code(r"""
# @title 0.3 — Manifesto do ambiente e semente global
import json
import os
import platform
import random
import sys
from importlib.metadata import version as versao_pacote
from datetime import datetime, timezone

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import qiskit
import qiskit_aer
import qiskit_machine_learning
import seaborn as sns
import sklearn
import skimage
import statsmodels
import medmnist

random.seed(SEED)
np.random.seed(SEED)
os.environ["PYTHONHASHSEED"] = str(SEED)

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams.update({"figure.figsize": (8, 4.8), "figure.dpi": 120})

VERSOES = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "python": sys.version.split()[0],
    "plataforma": platform.platform(),
    "numpy": np.__version__,
    "pandas": pd.__version__,
    "scikit_learn": sklearn.__version__,
    "qiskit": qiskit.__version__,
    "qiskit_aer": qiskit_aer.__version__,
    "qiskit_machine_learning": qiskit_machine_learning.__version__,
    "scikit_image": skimage.__version__,
    "statsmodels": statsmodels.__version__,
    "medmnist": medmnist.__version__,
    "torch": versao_pacote("torch"),
    "torchvision": versao_pacote("torchvision"),
    "seed": SEED,
    "shots": SHOTS,
}

display(pd.Series(VERSOES, name="valor").to_frame())

# TDD: contratos mínimos de versão usados na construção desta edição.
assert int(qiskit.__version__.split(".")[0]) == 2, "Use Qiskit 2.x."
assert qiskit_aer.__version__.startswith("0.17"), "Use Qiskit Aer 0.17.x."
assert qiskit_machine_learning.__version__.startswith("0.9"), "Use Qiskit ML 0.9.x."
print("✅ Ambiente validado.")
""")

code(r"""
# @title 0.4 — Pré-voo: orçamento lógico antes de executar
def estimar_avaliacoes_kernel(n_treino, n_teste):
    treino_unico = n_treino * (n_treino - 1) // 2
    teste_treino = n_teste * n_treino
    return treino_unico + teste_treino

ntr_previsto = 32 if MODO_RAPIDO else 64
nte_previsto = 16 if MODO_RAPIDO else 32
avaliacoes_nucleo = estimar_avaliacoes_kernel(ntr_previsto, nte_previsto)
avaliacoes_validacao_publicacao = 12 * estimar_avaliacoes_kernel(90, 30)

orcamento_prevoo = pd.DataFrame([
    {
        "etapa": "núcleo didático",
        "avaliações_lógicas": avaliacoes_nucleo,
        "shots_lógicos": avaliacoes_nucleo * SHOTS,
        "execução": "automática",
    },
    {
        "etapa": "CV aninhada 4 folds × 3 repetições",
        "avaliações_lógicas": avaliacoes_validacao_publicacao,
        "shots_lógicos": avaliacoes_validacao_publicacao * SHOTS,
        "execução": "emulação rápida de shots em statevector",
    },
    {
        "etapa": "escada com ruído Aer",
        "avaliações_lógicas": avaliacoes_nucleo,
        "shots_lógicos": avaliacoes_nucleo * SHOTS,
        "execução": "opcional e potencialmente lenta",
    },
])
display(orcamento_prevoo.style.format({
    "avaliações_lógicas": "{:,}",
    "shots_lógicos": "{:,}",
}))

assert avaliacoes_nucleo > 0
assert avaliacoes_validacao_publicacao > avaliacoes_nucleo
print("✅ Orçamento estimado antes de alocar tempo computacional.")
""")

md(r"""
## 0.5 — Congelamento do protocolo para publicação

O registro abaixo deve ser executado **antes** dos resultados. O hash detecta alterações posteriores no plano, mas não produz sozinho um carimbo temporal público. Para uma submissão científica, publique o protocolo em um repositório de pré-registro, como o [OSF Registries](https://help.osf.io/article/330-welcome-to-registrations), antes da análise confirmatória.

### Contribuição metodológica candidata

> Avaliar se a **sobrevivência da geometria do kernel** entre statevector, shots, ruído e QPU — combinada com desempenho pareado, posto efetivo e custo — pode atuar como critério reprodutível de *go/no-go* para aplicações de QML.

Esta é uma **hipótese de novidade**, não uma declaração de ineditismo. A alegação final depende de busca sistemática documentada, triagem por pares e atualização até a data de submissão.
""")

code(r"""
# @title 0.5 — Pré-registro local, hipóteses e hash do protocolo
import hashlib

PROTOCOLO_PRE_REGISTRADO = {
    "titulo_provisorio": (
        "Portões de Evidência Geométrica para Kernels Quânticos Reprodutíveis sob Ruído e Custo"
    ),
    "descricao": (
        "Estudo computacional pré-registrado que compara kernels quânticos de fidelidade "
        "com SVM-RBF em Iris Setosa–Versicolor, BreastMNIST e make_moons. O protocolo "
        "integra validação cruzada aninhada repetida, escada statevector–shots–ruído, "
        "diagnósticos geométricos, custo e portões prospectivos antes de qualquer QPU."
    ),
    "colaboradores": ["Marcelo Claro — https://osf.io/user/953q4"],
    "licenca": "CC BY 4.0 para protocolo, texto, tabelas e figuras; código sob MIT",
    "assuntos": [
        "Quantum computing", "Machine learning", "Artificial intelligence",
        "Statistics", "Reproducible research", "Biomedical imaging",
    ],
    "tags": [
        "quantum-machine-learning", "quantum-kernel", "qiskit", "nested-cross-validation",
        "noise-model", "BreastMNIST", "Iris", "make-moons", "open-science",
    ],
    "pergunta_primaria": (
        "A acurácia balanceada do kernel quântico supera o SVM-RBF sob seleção interna "
        "justa e validação cruzada externa repetida?"
    ),
    "hipotese_primaria": "H1: média pareada de ΔBAC = BAC_QML − BAC_RBF > 0",
    "hipotese_mecanistica": (
        "H2: maior sobrevivência geométrica ideal→shots→ruído está associada a menor "
        "degradação preditiva."
    ),
    "hipoteses_adicionais": [
        "H3 exploratória: regularização aparente por ruído deve replicar entre seeds e folds",
        "H4: a sobrevivência geométrica prediz delta BAC após controlar aplicação e custo",
        "H5 exploratória: o QUS prospectivo discrimina configurações aptas ao portão QPU",
        "H6: aquisição ativa ou Nyström preserva maior utilidade por shot que medição uniforme",
    ],
    "desfecho_primario": "delta_acuracia_balanceada",
    "desfechos_secundarios": [
        "delta_acuracia",
        "delta_f1",
        "alinhamento_kernel_alvo",
        "posto_efetivo_relativo",
        "erro_frobenius_relativo",
        "tempo_kernel_s",
    ],
    "modelo_referencia": "SVM-RBF",
    "validacao_externa": "4 folds estratificados × 3 repetições",
    "validacao_interna": "3 folds estratificados",
    "grade_C": [0.1, 1.0, 10.0],
    "grade_gamma_rbf": ["scale", "auto"],
    "alpha": 0.05,
    "margem_equivalencia_bac": 0.02,
    "teste_primario": "t corrigido de Nadeau-Bengio para folds dependentes",
    "analises_sensibilidade": [
        "permutação exata de sinais",
        "TOST de equivalência com erro-padrão corrigido",
        "IC corrigido de 95%",
        "Holm para desfechos secundários",
    ],
    "regra_alegacao": (
        "não usar a expressão vantagem quântica sem ganho, custo de escala, teste externo "
        "e validação em hardware"
    ),
    "osf": {
        "perguntas_hipoteses": (
            "Pergunta primária: sob seleção interna justa e validação externa repetida, "
            "o SVM com kernel quântico apresenta BAC superior ao SVM-RBF? H1: a média "
            "pareada de ΔBAC = BAC_QML − BAC_RBF é maior que zero. Pergunta mecanística: "
            "a sobrevivência geométrica ideal→shots→ruído prediz menor degradação? "
            "H2: a associação entre sobrevivência geométrica e ΔBAC é positiva. H4: essa "
            "associação permanece positiva em modelo multinível que controla aplicação e custo. "
            "H3 exploratória: um perfil de ruído selecionado apenas na validação pode atuar "
            "como regularizador; sua superioridade deve reaparecer em repetição independente. "
            "H5 exploratória: o Quantum Utility Score, calculado sem consultar o fold externo, "
            "discrimina configurações que preservam utilidade nesse fold e, futuramente, na QPU. "
            "H6: sob orçamento idêntico, Nyström orientado por leverage scores ou aquisição ativa "
            "preserva maior BAC×geometria por shot do que a medição uniforme."
        ),
        "conhecimento_previo": (
            "Antes do registro foram inspecionadas as bases públicas, executados exemplos "
            "didáticos e observados resultados-piloto usados para depuração, incluindo "
            "frequências com diferentes shots e desvio diagonal aproximado de 0,006. "
            "Nenhum desses resultados será tratado como evidência confirmatória. São também "
            "conhecidas a separabilidade elevada de Iris Setosa e a geometria curva construída "
            "de make_moons; BreastMNIST possui definição e splits publicados."
        ),
        "manejo_conhecimento_previo": (
            "Decisões decorrentes da depuração foram congeladas neste protocolo. A análise "
            "confirmatória usará execução limpa, seeds e folds registrados, e relatório de "
            "todos os perfis. Alterações posteriores serão datadas como desvio ou análise "
            "exploratória; pilotos não serão combinados com estimativas confirmatórias."
        ),
        "tipo_estudo": (
            "Estudo computacional comparativo de métodos, com dados secundários públicos e "
            "dados sintéticos; sem recrutamento, intervenção ou participantes humanos."
        ),
        "intencao_causal": (
            "Não. As estimativas são preditivas e associativas. Variações controladas de "
            "ruído estimam sensibilidade do pipeline, não efeitos causais clínicos."
        ),
        "cegueira_tratamentos": (
            "Não aplicável: não existem tratamentos experimentais nem participantes."
        ),
        "cegamento_adicional": (
            "O analista não está cego aos rótulos, necessários ao aprendizado supervisionado. "
            "O viés analítico é reduzido por código pré-especificado, teste lacrado, seleção "
            "apenas na validação, exportação integral e critérios automáticos."
        ),
        "desenho_estudo": (
            "Três aplicações principais: Iris Setosa–Versicolor, BreastMNIST e make_moons; "
            "PneumoniaMNIST constitui replicação exploratória externa de imagem. "
            "Um benchmark ampliado de pelo menos dez bases públicas/sintéticas avalia validade "
            "externa e fornece clusters suficientes para a análise hierárquica. "
            "O pré-processamento é ajustado somente no treino. A análise principal emprega "
            "CV aninhada estratificada 4×3 externamente e 3 folds internamente. Curvas de "
            "aprendizagem avaliam tamanhos pré-especificados sem reutilizar o teste. A escada "
            "compara statevector exato, amostragem finita e cinco perfis Aer. Perfil de ruído "
            "e C são escolhidos na validação; o teste é aberto uma vez. Pares-âncora em QPU "
            "dependem dos portões; classificador QPU completo é a última etapa."
        ),
        "randomizacao": (
            "Divisões estratificadas, embaralhamento de folds, simulação e transpilação usam "
            "SEED=42 e derivações determinísticas documentadas. BreastMNIST preserva primeiro "
            "os splits oficiais; apenas a subamostragem interna é estratificada por seed."
        ),
        "coleta_dados": (
            "Iris é obtida por sklearn.datasets.load_iris e filtrada para classes 0 e 1. "
            "BreastMNIST v2 e, na replicação exploratória, PneumoniaMNIST são baixados pelo "
            "pacote medmnist, size=28, com splits oficiais train, "
            "val e test; rótulo 0=maligno e 1=normal/benigno. make_moons é gerado com n=120, "
            "noise=0,18 e random_state=42. Serão preservadas versões de pacotes, hashes, seeds, "
            "matrizes, tempos e contagens lógicas. BreastMNIST é exclusivamente metodológico."
        ),
        "tamanho_amostra": (
            "Iris: 100 observações elegíveis antes das divisões. make_moons: 120 observações. "
            "BreastMNIST: população oficial de 780 imagens; no laboratório de ruído serão "
            "usadas no máximo 24 treino, 12 validação e 12 teste por custo quadrático. Na suíte "
            "multibase, o teto pré-especificado é 160 observações por base."
        ),
        "justificativa_amostra": (
            "O estudo é um benchmark mecanístico de viabilidade, não um estudo clínico de "
            "prevalência. Os tetos foram definidos antes da confirmação para conter O(n²) "
            "avaliações de kernel e shots. Incerteza será explicitada por IC e CV repetida; "
            "ausência de cálculo de poder prospectivo é limitação declarada."
        ),
        "regras_partida_parada": (
            "Iniciar a confirmação somente após registro OSF e verificação dos hashes. Parar "
            "uma execução por falha de integridade, classe ausente, split sobreposto, NaN/Inf, "
            "matriz incompatível ou custo acima do orçamento. Não parar por desempenho favorável "
            "ou desfavorável. QPU: enviar primeiro pares-âncora; avançar ao classificador completo "
            "somente se correlação ideal–QPU≥0,90, MAE≤0,10 e custo viável."
        ),
        "variaveis_manipuladas": (
            "Aplicação; regime de execução (statevector, shots, Aer ruidoso e QPU condicional); "
            "shots; probabilidades de erro de uma porta, duas portas e leitura; C do SVM; gamma "
            "do RBF; seed/fold. Perfis de ruído: controle 0/0/0; baixo 0,0005/0,005/0,01; "
            "moderado 0,001/0,01/0,02; alto-2Q 0,001/0,03/0,02; leitura-alta 0,001/0,01/0,05. "
            "O perfil confirmatório é escolhido pela média das seeds somente na validação interna."
        ),
        "variaveis_medidas": (
            "Acurácia balanceada (primária), acurácia, F1, ΔBAC pareado, alinhamento "
            "kernel–alvo, posto efetivo, erro relativo de Frobenius, sobrevivência geométrica, "
            "tempo, avaliações de circuitos, shots lógicos, correlação ideal–QPU e MAE. "
            "Diagnósticos de concentração: variância fora da diagonal, separação intra/interclasse, "
            "condição espectral, entropia e lacuna efetiva."
        ),
        "indices": (
            "ΔBAC=BAC_QML−BAC_RBF. Erro geométrico=||K_obs−K_ideal||F/||K_ideal||F. "
            "Sobrevivência=clip(1−erro geométrico,0,1). Alinhamento=<K,yyᵀ>F/(||K||F||yyᵀ||F). "
            "Posto efetivo=exp(−Σp_i log p_i), p_i=λ_i/Σλ. GO exploratório no laboratório "
            "se ΔBAC>0,02 e sobrevivência≥0,85; NO-GO se ΔBAC<−0,02; demais casos são "
            "equivalência prática ou inconclusivos."
        ),
        "modelos_estatisticos": (
            "SVC com kernel quântico pré-computado versus SVC-RBF. C∈{0,1;1;10}; "
            "gamma_RBF∈{scale,auto}; seleção interna por BAC. Inferência primária: teste t "
            "unilateral com correção de Nadeau–Bengio sobre diferenças pareadas dos folds "
            "externos. Reportar média, IC95% corrigido, dz pareado e p. Sensibilidades: permutação "
            "exata de sinais, TOST e Holm para desfechos secundários. H2 inicia com Spearman; H4 "
            "usa modelo de efeitos mistos com intercepto aleatório por aplicação e erros robustos "
            "por cluster como sensibilidade. Folds não serão tratados como replicações independentes."
        ),
        "transformacoes": (
            "Dentro de cada treino: imputação mediana, StandardScaler, PCA com dois componentes "
            "e MinMaxScaler para [0,π]. Imagens 28×28 são vetorizadas antes do pipeline. A mesma "
            "transformação ajustada no treino é aplicada à validação/teste. Kernel de treino "
            "ruidoso é simetrizado e projetado no cone PSD; a correção e a matriz bruta são reportadas."
        ),
        "criterios_inferencia": (
            "α=0,05 para H1 unilateral; IC bilateral de 95%. Superioridade requer estimativa "
            "positiva e p corrigido<0,05. Equivalência prática usa TOST com margem ±0,02 BAC. "
            "Holm controla multiplicidade secundária. Resultados que não satisfazem os critérios "
            "serão nulos/inconclusivos, sem linguagem de vantagem quântica."
        ),
        "inclusao_exclusao": (
            "Incluir observações pertencentes às classes binárias pré-especificadas e splits "
            "oficiais quando existentes. Excluir a terceira espécie de Iris; não excluir casos "
            "por dificuldade de classificação. Subamostrar estratificadamente apenas para os tetos "
            "de custo. Excluir execução, não observação, quando falhar teste de integridade; "
            "registrar motivo e rerun com a mesma seed."
        ),
        "dados_faltantes": (
            "Iris, BreastMNIST e make_moons não devem conter faltantes. A asserção será registrada. "
            "Se surgirem faltantes em dados tabulares adicionais, imputar mediana ajustada apenas no "
            "treino; não imputar rótulo. Quantidade por variável e por split será reportada."
        ),
        "outras_analises": (
            "Escada de shots; ablações de mapa e ruído; curvas de aprendizagem; baselines fortes "
            "linear, RBF, logístico, floresta, boosting e HOG para imagem; permutação de rótulos; "
            "CNN pequena, embedding congelado, calibração e curvas de decisão; benchmark 10+ bases; "
            "Nyström aleatório, leverage-score e aquisição ativa sob orçamento igual; "
            "deslocamento das entradas; concentração espectral; relação entre sobrevivência "
            "geométrica e ΔBAC; QUS em desenvolvimento; custo; matriz de novidade; pares-âncora QPU se os "
            "portões forem satisfeitos. H3, comparações não congeladas e qualquer análise clínica "
            "serão exploratórias; interpretação clínica de BreastMNIST ou PneumoniaMNIST é proibida."
        ),
        "contexto_adicional": (
            "Notebook Colab em português, Qiskit 2.x, Qiskit Aer e scikit-learn, desenvolvido "
            "por Marcelo Claro. O estudo avalia um Evidence Gate prospectivo, não reivindica "
            "ineditismo nem vantagem quântica antecipadamente. Serão publicados notebook limpo, "
            "ambiente, hashes, protocolo, resultados nulos, custos e desvios. BreastMNIST não é "
            "destinado a uso clínico."
        ),
    },
}

texto_protocolo = json.dumps(
    PROTOCOLO_PRE_REGISTRADO,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
)
HASH_PROTOCOLO = hashlib.sha256(texto_protocolo.encode("utf-8")).hexdigest()

display(pd.Series(PROTOCOLO_PRE_REGISTRADO, name="especificação").to_frame())
print("SHA-256 do protocolo:", HASH_PROTOCOLO)
print("✅ Plano confirmatório congelado localmente; registre-o externamente antes da análise final.")
""")

md(r"""
## 0.5.1 — Pacote pronto para registro no OSF

A célula seguinte materializa o plano **antes da primeira análise confirmatória**. O arquivo ZIP contém somente protocolo, manifesto e hash; resultados não entram no pré-registro. Depois do registro, cole a URL pública ou embargada no campo `OSF_REGISTRATION_URL` e preserve a data e a versão.

### Dois modos seguros

- **Preparar o registro:** deixe `OSF_REGISTRATION_URL` vazio. Mesmo que algum módulo tenha sido marcado por engano, a célula o desativará temporariamente, gerará o ZIP e continuará sem erro.
- **Executar o estudo:** depois de concluir o registro, cole a URL permanente do registro, execute novamente as células `0.1` e `0.5.1` e então ative os módulos desejados.

Uma URL de perfil, como `https://osf.io/user/...`, não libera as análises. Use a URL do **registro**, não apenas a página do projeto.

> **Ordem obrigatória:** gerar pacote → registrar no OSF → executar CV aninhada → executar suíte multibase → executar ruído → avaliar pares-âncora → somente então considerar classificador completo em QPU.
""")

code(r"""
# @title 0.5.1 — Gerar pacote de pré-registro OSF antes da análise
from pathlib import Path
import shutil
import re
from urllib.parse import urlparse
from IPython.display import Markdown, display

OSF_REGISTRATION_URL = ""  # @param {type:"string"}
DATA_CORTE_LITERATURA = "2026-08-16"

pasta_osf = Path("pre_registro_osf")
pasta_osf.mkdir(exist_ok=True)

with open(pasta_osf / "protocolo_pre_registrado.json", "w", encoding="utf-8") as f:
    json.dump(PROTOCOLO_PRE_REGISTRADO, f, ensure_ascii=False, indent=2)
(pasta_osf / "protocolo_sha256.txt").write_text(HASH_PROTOCOLO + "\n", encoding="utf-8")

osf = PROTOCOLO_PRE_REGISTRADO["osf"]
protocolo_osf_md = f'''
# Formulário OSF — conteúdo pronto para colar

## Metadados

### Título

{PROTOCOLO_PRE_REGISTRADO["titulo_provisorio"]}

### Descrição

{PROTOCOLO_PRE_REGISTRADO["descricao"]}

### Colaboradores

- [Marcelo Claro](https://osf.io/user/953q4) — autor responsável e administrador do projeto.

### Licença

{PROTOCOLO_PRE_REGISTRADO["licenca"]}. A licença dos conjuntos de dados de terceiros permanece a definida por seus mantenedores.

### Assuntos

{'; '.join(PROTOCOLO_PRE_REGISTRADO["assuntos"])}.

### Tags

{', '.join(PROTOCOLO_PRE_REGISTRADO["tags"])}.

## Visão geral

### Perguntas ou hipóteses de pesquisa

{osf["perguntas_hipoteses"]}

### Conhecimento prévio de dados ou evidências

{osf["conhecimento_previo"]}

### Explicação do conhecimento prévio e manejo de influências não intencionais

{osf["manejo_conhecimento_previo"]}

## Design de Pesquisa

### Tipo de estudo

{osf["tipo_estudo"]}

### Intenção para interpretação causal

{osf["intencao_causal"]}

### Cegueira de tratamentos experimentais

{osf["cegueira_tratamentos"]}

### Cegamento adicional durante pesquisas ou análises

{osf["cegamento_adicional"]}

### Desenho do estudo

{osf["desenho_estudo"]}

### Arquivo recomendado para o desenho

Anexar `trilha_quantum_ia_pesquisador_colab.ipynb` e `protocolo_pre_registrado.json`.

### Randomização

{osf["randomizacao"]}

## Amostragem

### Procedimentos de coleta de dados

{osf["coleta_dados"]}

### Procedimentos de coleta de dados — Upload de arquivos

Anexar `manifesto_pre_registro.json`, `requirements_lock.txt` quando gerado e a documentação das fontes. Não redistribuir imagens se a licença da fonte não permitir.

### Tamanho da amostra

{osf["tamanho_amostra"]}

### Justificativa do tamanho da amostra

{osf["justificativa_amostra"]}

### Regras de partida e parada

{osf["regras_partida_parada"]}

## Variáveis

### Variáveis manipuladas

{osf["variaveis_manipuladas"]}

### Arquivo recomendado para variáveis manipuladas

Anexar `protocolo_pre_registrado.json`; após a execução, publicar `busca_ruido_aplicacoes.csv` sem substituir o arquivo registrado.

### Variáveis medidas

{osf["variaveis_medidas"]}

### Variáveis medidas — Upload de arquivo

Anexar `dicionario_variaveis_osf.csv` gerado por este notebook.

### Índices

{osf["indices"]}

### Índices — Upload de arquivos

Anexar `dicionario_variaveis_osf.csv` e `protocolo_pre_registrado.json`.

## Plano de Análise

### Modelos estatísticos

{osf["modelos_estatisticos"]}

### Modelos estatísticos — Upload de arquivos

Anexar o notebook limpo, o hash e, se o OSF aceitar arquivo adicional, `paper_metodos.md` somente como material complementar versionado.

### Transformações

{osf["transformacoes"]}

### Critérios de inferência

{osf["criterios_inferencia"]}

### Inclusão e exclusão de dados

{osf["inclusao_exclusao"]}

### Dados faltantes

{osf["dados_faltantes"]}

### Outras análises planejadas

{osf["outras_analises"]}

## Outros

### Contexto e informações adicionais

{osf["contexto_adicional"]}

## Identificação do congelamento

**Autor responsável:** {NOME_PESQUISADOR}  
**Projeto:** {PROJETO}  
**Data de congelamento:** {DATA_CORTE_LITERATURA}  
**SHA-256:** `{HASH_PROTOCOLO}`

## Sequência e regra de progressão

1. CV aninhada repetida e inferência corrigida para folds dependentes.
2. Suíte multibase com pré-processamento ajustado exclusivamente no treino.
3. Escada statevector → shots → ruído Aer.
4. Pares-âncora na QPU somente após os itens 1–3.
5. Classificador completo na QPU somente se correlação ideal–QPU ≥ 0,90 e MAE ≤ 0,10 nos pares-âncora, além de viabilidade de custo.

## Controle de alegações

{PROTOCOLO_PRE_REGISTRADO["regra_alegacao"]}. Toda análise acrescentada após o carimbo OSF será identificada como exploratória ou como desvio justificado.
'''
(pasta_osf / "protocolo_osf.md").write_text(
    protocolo_osf_md.strip() + "\n", encoding="utf-8"
)
(pasta_osf / "formulario_osf_preenchido.md").write_text(
    protocolo_osf_md.strip() + "\n", encoding="utf-8"
)
with open(pasta_osf / "formulario_osf_campos.json", "w", encoding="utf-8") as f:
    json.dump({
        "metadados": {
            "titulo": PROTOCOLO_PRE_REGISTRADO["titulo_provisorio"],
            "descricao": PROTOCOLO_PRE_REGISTRADO["descricao"],
            "colaboradores": PROTOCOLO_PRE_REGISTRADO["colaboradores"],
            "licenca": PROTOCOLO_PRE_REGISTRADO["licenca"],
            "assuntos": PROTOCOLO_PRE_REGISTRADO["assuntos"],
            "tags": PROTOCOLO_PRE_REGISTRADO["tags"],
        },
        "campos_osf": osf,
        "hash_protocolo": HASH_PROTOCOLO,
    }, f, ensure_ascii=False, indent=2)

dicionario_osf = pd.DataFrame([
    {"variavel": "BAC", "papel": "desfecho primário", "definicao": "média do recall por classe", "escala": "0 a 1"},
    {"variavel": "delta_BAC", "papel": "contraste primário", "definicao": "BAC_QML - BAC_RBF no mesmo fold", "escala": "-1 a 1"},
    {"variavel": "erro_frobenius_relativo", "papel": "mecanismo", "definicao": "norma de K_obs-K_ideal dividida pela norma de K_ideal", "escala": "maior ou igual a 0"},
    {"variavel": "sobrevivencia_geometrica", "papel": "mecanismo", "definicao": "clip(1-erro_frobenius_relativo,0,1)", "escala": "0 a 1"},
    {"variavel": "alinhamento_kernel_alvo", "papel": "secundário", "definicao": "similaridade de Frobenius entre K e yyT", "escala": "-1 a 1"},
    {"variavel": "posto_efetivo", "papel": "secundário", "definicao": "exponencial da entropia dos autovalores normalizados", "escala": "1 a n"},
    {"variavel": "tempo_kernel_s", "papel": "custo", "definicao": "tempo de parede para avaliar matrizes", "escala": "segundos"},
    {"variavel": "shots_logicos", "papel": "custo", "definicao": "avaliações lógicas multiplicadas por shots", "escala": "inteiro"},
])
dicionario_osf.to_csv(pasta_osf / "dicionario_variaveis_osf.csv", index=False)

def url_registro_osf_valida(url):
    '''Valida a forma da URL sem realizar consulta externa ou revelar credenciais.'''
    try:
        analisada = urlparse(str(url).strip())
        caminho = analisada.path.rstrip("/")
        host_valido = analisada.scheme == "https" and analisada.hostname in {"osf.io", "www.osf.io"}
        nao_eh_perfil = not caminho.startswith("/user")
        id_curto = bool(re.fullmatch(r"/[A-Za-z0-9]{4,12}", caminho))
        rota_registro = bool(re.fullmatch(r"/registrations/[A-Za-z0-9-]{4,64}", caminho))
        return bool(host_valido and nao_eh_perfil and (id_curto or rota_registro))
    except Exception:
        return False

estado_modulos_solicitados = {
    "EXECUTAR_VALIDACAO_ROBUSTA": bool(EXECUTAR_VALIDACAO_ROBUSTA),
    "EXECUTAR_ESCADA_RUIDO": bool(EXECUTAR_ESCADA_RUIDO),
    "EXECUTAR_SUITE_APLICACOES": bool(EXECUTAR_SUITE_APLICACOES),
    "EXECUTAR_PAPER_AVANCADO": bool(EXECUTAR_PAPER_AVANCADO),
    "EXECUTAR_CURVAS_APRENDIZAGEM": bool(EXECUTAR_CURVAS_APRENDIZAGEM),
    "EXECUTAR_RUIDO_ANINHADO": bool(EXECUTAR_RUIDO_ANINHADO),
    "EXECUTAR_BENCHMARK_AMPLIADO": bool(EXECUTAR_BENCHMARK_AMPLIADO),
    "EXECUTAR_BASELINES_DEEP": bool(EXECUTAR_BASELINES_DEEP),
    "EXECUTAR_AQUISICAO_ATIVA": bool(EXECUTAR_AQUISICAO_ATIVA),
}
modulos_confirmatorios_solicitados = any(estado_modulos_solicitados.values())
URL_OSF_VALIDA = url_registro_osf_valida(OSF_REGISTRATION_URL)

if modulos_confirmatorios_solicitados and not URL_OSF_VALIDA:
    STATUS_GATE_OSF = "bloqueado_sem_excecao"
    for nome_flag in estado_modulos_solicitados:
        globals()[nome_flag] = False
elif URL_OSF_VALIDA:
    STATUS_GATE_OSF = "liberado_por_url_registro"
else:
    STATUS_GATE_OSF = "aguardando_registro"

manifesto_osf = {
    "status": "registrado_no_osf" if URL_OSF_VALIDA else "congelado_localmente",
    "status_gate_osf": STATUS_GATE_OSF,
    "url_osf_validada_sintaticamente": URL_OSF_VALIDA,
    "osf_registration_url": str(OSF_REGISTRATION_URL).strip(),
    "hash_protocolo": HASH_PROTOCOLO,
    "data_corte_literatura": DATA_CORTE_LITERATURA,
    "analises_confirmatorias_executadas_antes_deste_pacote": False,
    "modulos_solicitados_antes_do_gate": estado_modulos_solicitados,
    "acao_automatica": (
        "flags confirmatorias temporariamente desativadas; nenhuma analise iniciada"
        if STATUS_GATE_OSF == "bloqueado_sem_excecao" else "nenhuma"
    ),
    "ordem_obrigatoria": [
        "OSF", "CV aninhada", "suíte de aplicações", "ruído Aer",
        "pares-âncora QPU", "classificador completo QPU",
    ],
}
with open(pasta_osf / "manifesto_pre_registro.json", "w", encoding="utf-8") as f:
    json.dump(manifesto_osf, f, ensure_ascii=False, indent=2)

arquivo_osf_zip = shutil.make_archive("pre_registro_osf", "zip", root_dir=pasta_osf)
assert (pasta_osf / "protocolo_osf.md").exists()
assert (pasta_osf / "protocolo_pre_registrado.json").exists()
assert (pasta_osf / "formulario_osf_preenchido.md").exists()
assert (pasta_osf / "formulario_osf_campos.json").exists()
assert (pasta_osf / "dicionario_variaveis_osf.csv").exists()
assert hashlib.sha256(texto_protocolo.encode("utf-8")).hexdigest() == HASH_PROTOCOLO
print("Pacote OSF:", arquivo_osf_zip)
print("✅ Conteúdo confirmatório congelado antes dos resultados.")

if STATUS_GATE_OSF == "bloqueado_sem_excecao":
    nomes_ativos = [nome for nome, ativo in estado_modulos_solicitados.items() if ativo]
    display(Markdown(
        "### 🔒 Execução confirmatória pausada com segurança\n\n"
        "O pacote foi criado corretamente. A URL do registro ainda está vazia ou não possui "
        "o formato esperado. Os seguintes módulos foram temporariamente desativados: `" +
        "`, `".join(nomes_ativos) + "`.\n\n"
        "**Próximo passo:** envie `pre_registro_osf.zip` ao OSF, conclua o registro, copie a URL "
        "permanente, cole em `OSF_REGISTRATION_URL`, execute novamente `0.1` e `0.5.1` e reative "
        "os módulos. Nenhum resultado confirmatório foi calculado nesta passagem."
    ))
elif STATUS_GATE_OSF == "liberado_por_url_registro":
    display(Markdown(
        "### ✅ Portão OSF liberado\n\n"
        "A URL possui formato OSF válido. Preserve o comprovante e confirme manualmente que "
        "ela corresponde a um **registro concluído**, e não somente a um projeto editável."
    ))
else:
    display(Markdown(
        "### 📦 Pacote pronto para registro\n\n"
        "Nenhum módulo confirmatório foi solicitado. Registre o ZIP no OSF e volte com a URL "
        "permanente antes de ativar as análises."
    ))
""")

md(r"""
# Atlas didático — mapas mentais e analogias rigorosas

Os mapas mostram **como as ideias se conectam**. As analogias ajudam a iniciar a compreensão, mas cada uma vem acompanhada de uma tradução científica e de um aviso sobre seus limites.

> Estratégia de leitura: primeiro conte a história com palavras simples; depois aponte no mapa; por último leia a formulação matemática.
""")

code(r"""
# @title 0.6 — Galeria de mapas mentais editáveis {display-mode: "form"}
import textwrap
from matplotlib.patches import FancyBboxPatch
from IPython.display import Markdown, display

MAPA_ESCOLHIDO = "visão geral"  # @param ["visão geral", "qubit", "circuito", "QML", "escada de validade", "paper"]
MOSTRAR_TODOS_OS_MAPAS = True  # @param {type:"boolean"}

MAPAS_DIDATICOS = {
    "visão geral": {
        "centro": "Física e computação quântica",
        "ramos": {
            "Estado": ["amplitudes", "fase", "normalização"],
            "Transformação": ["portas", "interferência", "entrelaçamento"],
            "Medição": ["base", "probabilidade", "shots"],
            "Pesquisa": ["baseline", "incerteza", "reprodução"],
        },
    },
    "qubit": {
        "centro": "Qubit",
        "ramos": {
            "Base": ["|0⟩", "|1⟩", "espaço 2D"],
            "Estado": ["α|0⟩+β|1⟩", "fase", "norma 1"],
            "Geometria": ["esfera de Bloch", "polos", "equador"],
            "Leitura": ["escolha da base", "colapso", "frequências"],
        },
    },
    "circuito": {
        "centro": "Circuito quântico",
        "ramos": {
            "Preparar": ["estado inicial", "dados", "qubits"],
            "Transformar": ["H", "rotações", "CX"],
            "Executar": ["statevector", "Aer", "QPU"],
            "Observar": ["bitstrings", "contagens", "estimativas"],
        },
    },
    "QML": {
        "centro": "Kernel quântico",
        "ramos": {
            "Dados": ["split", "PCA no treino", "ângulos"],
            "Geometria": ["feature map", "fidelidade", "matriz K"],
            "Aprendizado": ["SVM", "C", "predição"],
            "Controle": ["RBF", "custo", "IC pareado"],
        },
    },
    "escada de validade": {
        "centro": "O resultado sobrevive?",
        "ramos": {
            "Ideal": ["statevector", "sem shots", "referência"],
            "Amostragem": ["shots", "flutuação", "PSD"],
            "Ruído": ["portas", "leitura", "decoerência"],
            "Hardware": ["âncoras", "go/no-go", "QPU"],
        },
    },
    "paper": {
        "centro": "Evidência publicável",
        "ramos": {
            "Antes": ["pergunta", "hipótese", "pré-registro"],
            "Desenho": ["CV aninhada", "baseline", "sem vazamento"],
            "Inferência": ["efeito", "IC", "equivalência"],
            "Transparência": ["custos", "limitações", "dados e código"],
        },
    },
}

ANALOGIAS_RIGOROSAS = {
    "estado quântico": {
        "crianca": "Uma receita que informa quanto de cada possibilidade participa do estado.",
        "formal": "Vetor complexo normalizado; em um qubit, |ψ⟩=α|0⟩+β|1⟩.",
        "limite": "Não é uma mistura material pronta nem ignorância sobre um valor já decidido.",
    },
    "amplitude e probabilidade": {
        "crianca": "Amplitude é a seta da receita; probabilidade é o tamanho da sombra dessa seta.",
        "formal": "P(i)=|αᵢ|²; amplitudes podem ter sinal e fase e, por isso, interferir.",
        "limite": "Probabilidade não guarda toda a informação contida na amplitude complexa.",
    },
    "fase": {
        "crianca": "Duas crianças pulando corda podem estar no mesmo ritmo, mas em momentos opostos.",
        "formal": "A fase relativa altera termos de interferência, embora não mude uma medição isolada em Z.",
        "limite": "Fase não é atraso de relógio clássico; é uma relação no espaço de estados.",
    },
    "shots": {
        "crianca": "Tirar muitas fotografias da mesma fonte para estimar o padrão que aparece.",
        "formal": "Repetições independentes de preparação, circuito e medição estimam probabilidades.",
        "limite": "Cada shot não revela a amplitude nem copia um estado quântico desconhecido.",
    },
    "circuito": {
        "crianca": "Uma partitura: cada símbolo diz o que fazer e a ordem muda a música.",
        "formal": "Composição ordenada de operações unitárias, seguida opcionalmente por medição.",
        "limite": "Portas quânticas não movem objetos macroscópicos; transformam amplitudes.",
    },
    "entrelaçamento": {
        "crianca": "Uma coreografia conjunta cuja descrição completa pertence à dupla, não a cada dançarino.",
        "formal": "Estado composto não separável em produto tensorial de estados locais.",
        "limite": "Não é apenas colocar uma luva em cada envelope; isso seria correlação clássica pré-definida.",
    },
    "ruído": {
        "crianca": "Uma coreografia executada num palco que treme e com uma câmera que às vezes lê errado.",
        "formal": "Canais físicos alteram o estado e erros de leitura alteram o registro clássico.",
        "limite": "Ruído quântico não é somente som ou distração; é uma transformação física modelável.",
    },
    "kernel quântico": {
        "crianca": "Uma régua especial que compara dois objetos depois de colocá-los num mapa diferente.",
        "formal": "K(x,y)=|⟨φ(x)|φ(y)⟩|²; a matriz de similaridades alimenta um SVM clássico.",
        "limite": "A régua não aprende sozinha e uma geometria mais complexa não garante melhor generalização.",
    },
    "CV aninhada": {
        "crianca": "Treinar com simulados dentro da sala e deixar a prova final em envelope lacrado.",
        "formal": "Folds internos selecionam hiperparâmetros; folds externos estimam generalização.",
        "limite": "Os folds compartilham dados e não são experimentos totalmente independentes.",
    },
    "portão de evidência": {
        "crianca": "Um semáforo científico: observar, confirmar e só depois avançar.",
        "formal": "Regra pré-especificada que integra efeito, incerteza, custo, replicação e hardware.",
        "limite": "Não produz verdade automática; organiza decisões sob critérios transparentes.",
    },
}

def desenhar_mapa_mental(nome, especificacao):
    centro = especificacao["centro"]
    ramos = especificacao["ramos"]
    posicoes = [(-3.5, 2.3), (3.5, 2.3), (-3.5, -2.3), (3.5, -2.3)]
    cores = plt.cm.Set2(np.linspace(0, 1, len(ramos)))
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(-6.2, 6.2)
    ax.set_ylim(-4.4, 4.4)
    ax.axis("off")

    caixa_centro = FancyBboxPatch(
        (-1.55, -0.60), 3.10, 1.20,
        boxstyle="round,pad=0.18,rounding_size=0.12",
        facecolor="#24292f", edgecolor="#24292f", linewidth=1.5, zorder=3,
    )
    ax.add_patch(caixa_centro)
    ax.text(0, 0, textwrap.fill(centro, 24), ha="center", va="center", color="white", weight="bold", zorder=4)

    for (titulo_ramo, itens), (x, y), cor in zip(ramos.items(), posicoes, cores):
        ax.annotate(
            "", xy=(x * 0.72, y * 0.72), xytext=(0, 0),
            arrowprops={"arrowstyle": "-|>", "lw": 2, "color": cor}, zorder=1,
        )
        caixa = FancyBboxPatch(
            (x - 1.45, y - 0.72), 2.90, 1.44,
            boxstyle="round,pad=0.16,rounding_size=0.10",
            facecolor=cor, edgecolor=cor, alpha=0.88, zorder=2,
        )
        ax.add_patch(caixa)
        texto_itens = " · ".join(itens)
        ax.text(x, y + 0.24, titulo_ramo, ha="center", va="center", weight="bold", zorder=3)
        ax.text(x, y - 0.22, textwrap.fill(texto_itens, 30), ha="center", va="center", zorder=3)

    ax.set_title(f"Mapa mental — {nome}", pad=12, weight="bold")
    plt.tight_layout()
    plt.show()

nomes_mapas = list(MAPAS_DIDATICOS) if MOSTRAR_TODOS_OS_MAPAS else [MAPA_ESCOLHIDO]
for nome_mapa in nomes_mapas:
    desenhar_mapa_mental(nome_mapa, MAPAS_DIDATICOS[nome_mapa])

assert len(MAPAS_DIDATICOS) == 6
assert all(len(mapa["ramos"]) == 4 for mapa in MAPAS_DIDATICOS.values())
assert all({"crianca", "formal", "limite"} <= set(a) for a in ANALOGIAS_RIGOROSAS.values())
print("✅ Seis mapas e dez analogias validados com tradução formal e limite explícito.")
""")

code(r"""
# @title 0.7 — Cartão de analogia: escolha um conceito {display-mode: "form"}
ANALOGIA_ESCOLHIDA = "qubit"  # @param ["qubit", "estado quântico", "amplitude e probabilidade", "fase", "shots", "circuito", "entrelaçamento", "ruído", "kernel quântico", "CV aninhada", "portão de evidência"]

# "Qubit" é apresentado pelo cartão de "estado quântico".
chave_analogia = "estado quântico" if ANALOGIA_ESCOLHIDA == "qubit" else ANALOGIA_ESCOLHIDA
cartao = ANALOGIAS_RIGOROSAS[chave_analogia]
display(Markdown(f'''
### 🧒 {ANALOGIA_ESCOLHIDA.title()}

**Conte assim:** {cartao["crianca"]}

**Tradução científica:** {cartao["formal"]}

**⚠️ Onde a comparação para de funcionar:** {cartao["limite"]}
'''))
""")

md(r"""
# Módulo 1 — O que é física quântica?

## 🌱 Uma definição operacional

A física quântica é a teoria usada para descrever matéria e radiação em escalas nas quais previsões clássicas deixam de funcionar. Ela não diz simplesmente que “tudo é possível”. Ela fornece regras matemáticas extremamente precisas para calcular **amplitudes**, **probabilidades** e **correlações**.

Quatro ideias sustentam esta trilha:

1. **Quantização:** algumas grandezas aparecem em valores discretos em determinados sistemas.
2. **Superposição:** o estado pode combinar possibilidades por amplitudes complexas.
3. **Interferência:** amplitudes podem se reforçar ou se cancelar.
4. **Medição:** o experimento produz resultados clássicos segundo probabilidades calculadas pela regra de Born.

O **entrelaçamento**, estudado no Módulo 3, surge quando o estado do conjunto não pode ser escrito como estados independentes de suas partes.

> Superposição não é “um objeto clássico escondido em dois lugares”. É uma descrição de amplitudes que prevê estatísticas de medições e padrões de interferência.
""")

md(r"""
## Do experimento à teoria

| Observação | Limite da explicação clássica | Ideia quântica associada |
|---|---|---|
| espectros atômicos em linhas | energia contínua não explica linhas discretas | níveis quantizados |
| efeito fotoelétrico | intensidade sozinha não determina ejeção | quanta de energia |
| dupla fenda com partículas individuais | trajetórias clássicas não reproduzem o padrão | amplitudes e interferência |
| correlações de Bell | modelos locais clássicos têm limites | entrelaçamento |

### Três equívocos a evitar

- **“Observar” não significa necessariamente consciência humana:** significa interação física/registro de informação.
- **Incerteza não é apenas instrumento ruim:** certos pares de observáveis têm limitação estrutural conjunta.
- **Entrelaçamento não envia mensagens mais rápidas que a luz:** as correlações não permitem comunicação superluminal controlada.
""")

md(r"""
## Bit clássico × qubit

| Aspecto | Bit | Qubit |
|---|---|---|
| estado antes da leitura | 0 ou 1 | $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$ |
| parâmetros | um valor discreto | amplitudes complexas normalizadas |
| leitura | revela 0 ou 1 | produz 0 ou 1 probabilisticamente |
| cópia arbitrária | possível | proibida para estado desconhecido pelo teorema da não clonagem |
| transformação ideal | lógica booleana | operação unitária reversível |

Para um qubit puro:

$$|\alpha|^2+|\beta|^2=1.$$

A regra de Born fornece:

$$P(0)=|\alpha|^2, \qquad P(1)=|\beta|^2.$$

As fases de $\alpha$ e $\beta$ não aparecem diretamente nessas duas probabilidades, mas tornam-se observáveis por **interferência**.
""")

md(r"""
## 🧒 Parada leiga 1 — receita, setas e corda de pular

### Estado quântico como receita

Imagine uma receita com duas possibilidades, `|0⟩` e `|1⟩`. Os coeficientes $alpha$ e $eta$ dizem **quanto cada possibilidade participa do estado**. Ao medir, não retiramos os dois ingredientes: obtemos um único resultado, com probabilidades calculadas por $|\alpha|^2$ e $|\beta|^2$.

**Tradução rigorosa:** o estado é um vetor complexo normalizado, não uma lista de probabilidades clássicas.

**⚠️ Limite:** a receita comum contém ingredientes materiais simultaneamente. A superposição descreve amplitudes e pode interferir; não é uma mistura física comum nem apenas falta de informação.

### Amplitude como seta; probabilidade como sombra

Uma seta possui comprimento e direção. O comprimento ao quadrado fornece a probabilidade; a direção representa fase. Duas setas podem produzir a mesma “sombra” probabilística em Z e ainda apontar em direções diferentes.

**Exemplo:** $|+\rangle$ e $|-\rangle$ produzem 50%–50% quando medidos em Z, mas uma porta Hadamard revela resultados opostos.

**⚠️ Limite:** a amplitude não é uma seta física no espaço da sala; ela vive num espaço vetorial complexo.

### Fase como duas crianças pulando corda

Duas crianças podem repetir o mesmo movimento, mas uma sobe quando a outra desce. A diferença de “momento do ciclo” lembra a fase relativa. Quando caminhos se reencontram, as amplitudes podem se somar ou cancelar.

**⚠️ Limite:** fase quântica não é simplesmente atraso de relógio. O que importa experimentalmente é a relação de fase entre componentes do estado.

### Experiência sem equipamento

1. Desenhe duas setas de mesmo comprimento apontando na mesma direção: a soma cresce.
2. Desenhe-as em direções opostas: a soma pode zerar.
3. Compare com ondas: crista + crista reforça; crista + vale cancela.

Esse desenho explica **interferência de amplitudes**, mas não cria uma superposição quântica real.
""")

md(r"""
## Pré-cálculo essencial: números complexos, vetores e Dirac

- $i^2=-1$.
- O conjugado de $z=a+bi$ é $z^*=a-bi$.
- O módulo ao quadrado é $|z|^2=z^*z=a^2+b^2$.
- Um **ket** $|\psi\rangle$ é um vetor coluna.
- Um **bra** $\langle\psi|$ é o conjugado transposto.
- O produto interno $\langle\phi|\psi\rangle$ mede sobreposição entre estados.

Base computacional:

$$|0\rangle=\begin{bmatrix}1\\0\end{bmatrix},\qquad
|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}.$$

Exemplo de estado com fase relativa:

$$|+i\rangle=\frac{|0\rangle+i|1\rangle}{\sqrt{2}}.$$
""")

code(r"""
# @title 1.1 — Laboratório: amplitudes complexas e regra de Born
alpha = np.sqrt(3) / 2
beta = 0.5j
psi = np.array([alpha, beta], dtype=complex)

norma = np.vdot(psi, psi).real
probabilidades = np.abs(psi) ** 2

print("Estado |ψ⟩ =", psi)
print("Norma² =", norma)
print("P(0), P(1) =", probabilidades)

fig, ax = plt.subplots(subplot_kw={"projection": "polar"}, figsize=(6, 5))
for amp, rotulo, cor in zip(psi, ["α", "β"], ["#2563eb", "#dc2626"]):
    ax.arrow(np.angle(amp), 0, 0, np.abs(amp), width=0.025, color=cor, alpha=0.85)
    ax.text(np.angle(amp), np.abs(amp) + 0.08, rotulo, color=cor, fontsize=13)
ax.set_ylim(0, 1.15)
ax.set_title("Amplitudes como vetores complexos (fasores)")
plt.show()

# TDD
assert np.isclose(norma, 1.0)
assert np.isclose(probabilidades.sum(), 1.0)
assert np.allclose(probabilidades, [0.75, 0.25])
print("✅ Estado normalizado e regra de Born verificadas.")
""")

md(r"""
### 🧭 Pare e interprete

1. Por que `beta = 0.5j` tem a mesma probabilidade de `beta = 0.5` na base computacional?
2. Em que etapa uma fase poderia alterar um resultado observável?
3. O gráfico polar mostra probabilidades ou amplitudes?

### Exercício 1

Construa o estado $|\phi\rangle=(|0\rangle-|1\rangle)/\sqrt{2}$, calcule as probabilidades e confirme a normalização. Depois compare-o com $|+\rangle=(|0\rangle+|1\rangle)/\sqrt{2}$. Eles têm as mesmas probabilidades na base computacional? São o mesmo estado?
""")

code(r"""
# @title 1.2 — Gabarito executável do Exercício 1 {display-mode: "form"}
phi = np.array([1, -1], dtype=complex) / np.sqrt(2)
plus = np.array([1, 1], dtype=complex) / np.sqrt(2)

print("Pφ =", np.abs(phi) ** 2)
print("P+ =", np.abs(plus) ** 2)
print("Sobreposição ⟨+|φ⟩ =", np.vdot(plus, phi))

assert np.isclose(np.vdot(phi, phi), 1.0)
assert np.allclose(np.abs(phi) ** 2, np.abs(plus) ** 2)
assert np.isclose(np.vdot(plus, phi), 0.0)
print("✅ Mesmas probabilidades em Z, mas estados ortogonais: a fase relativa importa.")
""", tags=["gabarito"])

md(r"""
# Módulo 2 — Do qubit ao circuito quântico

## O que é computação quântica?

Computação quântica é um modelo de processamento da informação no qual estados, transformações e medições obedecem às regras da mecânica quântica. Um algoritmo organiza **superposição, fase, interferência e entrelaçamento** para aumentar a probabilidade de respostas úteis e reduzir a de respostas indesejadas.

Ela não é simplesmente um computador clássico menor ou mais rápido. O fluxo é:

**problema → algoritmo → circuito → portas → transpilação para o dispositivo → execução → medição clássica → interpretação.**

O ganho, quando existe, vem da estrutura do algoritmo e do problema; ler o resultado continua produzindo uma quantidade clássica limitada de informação.

## Portas como transformações

Portas quânticas ideais são matrizes unitárias $U$, isto é, $U^\dagger U=I$. A unitariedade preserva a norma do estado.

$$X=\begin{bmatrix}0&1\\1&0\end{bmatrix},\qquad
H=\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix}.$$

- `X` troca $|0\rangle$ e $|1\rangle$.
- `H` transforma $|0\rangle$ em $|+\rangle$ e $|1\rangle$ em $|-\rangle$.
- `RY(θ)` realiza uma rotação controlada por um ângulo.

Para $RY(\theta)|0\rangle$:

$$|\psi\rangle=\cos(\theta/2)|0\rangle+\sin(\theta/2)|1\rangle.$$
""")

code(r"""
# @title 2.1 — Portas X e H sem biblioteca quântica
ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

estado_x = X @ ket0
estado_h = H @ ket0

print("X|0⟩ =", estado_x)
print("H|0⟩ =", estado_h)

assert np.allclose(X.conj().T @ X, np.eye(2))
assert np.allclose(H.conj().T @ H, np.eye(2))
assert np.allclose(estado_x, ket1)
assert np.allclose(np.abs(estado_h) ** 2, [0.5, 0.5])
print("✅ Unitariedade e estados esperados confirmados.")
""")

md(r"""
## Statevector, esfera de Bloch e medição

O **Statevector** guarda as amplitudes do estado ideal. Para um qubit puro, podemos representá-lo por um ponto na esfera de Bloch:

$$|\psi\rangle=\cos\left(\frac{\theta}{2}\right)|0\rangle+e^{i\varphi}\sin\left(\frac{\theta}{2}\right)|1\rangle.$$

- polo norte: $|0\rangle$;
- polo sul: $|1\rangle$;
- equador: superposições balanceadas;
- longitude: fase relativa $\varphi$.

> A esfera de Bloch representa exatamente **um qubit puro**. Ela não é uma bola dentro do processador e não representa diretamente estados gerais de muitos qubits.
""")

code(r"""
# @title 2.2 — Primeiro circuito Qiskit: Hadamard e esfera de Bloch
from IPython.display import display
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

qc_h = QuantumCircuit(1)
qc_h.h(0)
estado_h_qiskit = Statevector.from_instruction(qc_h)

display(qc_h.draw("mpl"))
print("Statevector:", estado_h_qiskit.data)
display(plot_bloch_multivector(estado_h_qiskit, title="H|0⟩ = |+⟩"))

assert np.allclose(np.abs(estado_h_qiskit.data) ** 2, [0.5, 0.5])
print("✅ Qiskit reproduziu o cálculo matricial.")
""")

code(r"""
# @title 2.3 — Laboratório interativo: rotação RY {display-mode: "form"}
THETA_GRAUS = 60  # @param {type:"slider", min:0, max:360, step:15}
theta = np.deg2rad(THETA_GRAUS)

qc_ry = QuantumCircuit(1)
qc_ry.ry(theta, 0)
estado_ry = Statevector.from_instruction(qc_ry)
probs_ry = estado_ry.probabilities()
probs_teoricas = np.array([np.cos(theta / 2) ** 2, np.sin(theta / 2) ** 2])

display(qc_ry.draw("mpl"))
display(plot_bloch_multivector(estado_ry, title=f"RY({THETA_GRAUS}°)|0⟩"))
print("Probabilidades Qiskit:", probs_ry)
print("Probabilidades teóricas:", probs_teoricas)

assert np.allclose(probs_ry, probs_teoricas)
print("✅ Rotação validada analiticamente.")
""")

md(r"""
## 🧒 Parada leiga 2 — partitura, bússola e fotografia

### Circuito = partitura de uma música

Imagine que cada linha do circuito é um instrumento e cada porta é uma instrução escrita na partitura. A ordem importa: tocar `H` e depois `X` não precisa produzir o mesmo estado que tocar `X` e depois `H`.

**🔬 Tradução científica:** um circuito representa uma composição ordenada de operações unitárias e, quando há medições, operações não unitárias. Se $U_1$ vem antes de $U_2$, o estado final ideal é $U_2U_1|\psi\rangle$.

**⚠️ Onde a analogia falha:** uma partitura comum pode ser copiada e escutada sem alterar os músicos. Medir um sistema quântico muda o estado e entrega apenas uma amostra clássica.

### Esfera de Bloch = bússola sobre um globo

O ponto na esfera funciona como uma seta de bússola: norte é $|0\rangle$, sul é $|1\rangle$, e direções no equador representam superposições balanceadas com fases diferentes.

**🔬 Tradução científica:** para um qubit puro, os ângulos $(\theta,\varphi)$ parametrizam $|\psi\rangle=\cos(\theta/2)|0\rangle+e^{i\varphi}\sin(\theta/2)|1\rangle$.

**⚠️ Onde a analogia falha:** não existe uma esfera física girando dentro do chip. Estados mistos ficam dentro da esfera; estados gerais de vários qubits não cabem em uma única esfera de Bloch.

### Atividade prática de 3 minutos

1. Desenhe um círculo com norte `0`, sul `1` e equador `50/50`.
2. Marque `H|0⟩` no equador.
3. Mude `THETA_GRAUS` na célula 2.3 para `0`, `90` e `180`.
4. Antes de executar, aponte no desenho onde espera encontrar o estado.
5. Compare previsão, esfera e probabilidades. Se divergirem, revise o ângulo de meia-rotação $\theta/2$.
""")

md(r"""
## Statevector não é o mesmo que resultado experimental

Um dispositivo real não entrega diretamente $\alpha$ e $\beta$. Ele entrega uma sequência de resultados clássicos. Cada repetição é um **shot**.

Se $P(1)=0{,}25$, então 2.048 shots produzirão algo próximo de 25% de `1`, mas não exatamente. O erro amostral típico diminui aproximadamente como $1/\sqrt{N}$.

### Antes de executar

Para `H|0⟩`, preveja:

- quais bitstrings podem aparecer;
- a frequência esperada de cada um;
- qual conjunto de shots deve oscilar mais: 128 ou 8.192?
""")

code(r"""
# @title 2.4 — Medição e convergência estatística com AerSimulator
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

simulador = AerSimulator()
qc_medida = QuantumCircuit(1, 1)
qc_medida.h(0)
qc_medida.measure(0, 0)
qc_t = transpile(qc_medida, simulador)

shots_testados = [128, 512, 2048, 8192]
linhas = []
contagens_por_shots = {}
for n_shots in shots_testados:
    resultado = simulador.run(qc_t, shots=n_shots, seed_simulator=SEED).result()
    counts = resultado.get_counts()
    contagens_por_shots[n_shots] = counts
    p1 = counts.get("1", 0) / n_shots
    linhas.append({"shots": n_shots, "P_hat(1)": p1, "erro_absoluto": abs(p1 - 0.5)})

df_shots = pd.DataFrame(linhas)
tabela_shots = df_shots.rename(columns={
    "shots": "Shots",
    "P_hat(1)": "P̂(1)",
    "erro_absoluto": "Erro absoluto",
})
display(
    tabela_shots.style
    .hide(axis="index")
    .format({"Shots": "{:,.0f}", "P̂(1)": "{:.6f}", "Erro absoluto": "{:.6f}"})
    .set_caption("Convergência da estimativa de P(1) para H|0⟩")
)

ax = df_shots.plot(x="shots", y="erro_absoluto", marker="o", logx=True, color="#7c3aed")
ax.set_title("Erro amostral observado para H|0⟩")
ax.set_ylabel("|P̂(1) − 0,5|")
plt.show()

# `plot_histogram` interpreta um dicionário como uma única execução. Para quatro
# execuções, fornecemos uma lista com quatro dicionários e quatro legendas.
dados_histograma = [contagens_por_shots[n] for n in shots_testados]
legendas_histograma = [f"{n:,} shots".replace(",", ".") for n in shots_testados]
cores_histograma = ["#94a3b8", "#60a5fa", "#2563eb", "#1e3a8a"]

assert len(dados_histograma) == len(legendas_histograma) == len(cores_histograma)
display(plot_histogram(
    dados_histograma,
    legend=legendas_histograma,
    color=cores_histograma,
    bar_labels=False,
    title="Distribuições para diferentes números de shots",
))

assert set().union(*(set(c) for c in contagens_por_shots.values())) <= {"0", "1"}
assert abs(df_shots.iloc[-1]["P_hat(1)"] - 0.5) < 0.05
print("✅ Medição e convergência estatística verificadas.")
""")

md(r"""
### 🧒 Shots = refazer a mesma fotografia muitas vezes

Uma fotografia mostra apenas um resultado. Para descobrir o padrão de uma fonte que produz `0` e `1`, repetimos **preparar → executar → medir** muitas vezes e contamos as fotografias.

**🔬 Tradução científica:** se cada shot é aproximadamente independente e tem probabilidade $p$ de produzir `1`, então $\hat p=n_1/N$ tem erro-padrão $\sqrt{p(1-p)/N}$. No pior caso, $p=0{,}5$, o erro-padrão é $1/(2\sqrt{N})$.

**⚠️ Onde a analogia falha:** lançar uma moeda clássica ilustra somente **amostragem finita**. A moeda não explica amplitudes complexas, fase, interferência, contextualidade ou colapso da medição. Não diga que “o qubit é uma moeda girando”.
""")

code(r"""
# @title 2.4.1 — Laboratório leigo: moeda explica shots, não superposição
rng_shots = np.random.default_rng(SEED)
repeticoes_laboratorio = 200
linhas_moeda = []

for n_shots in shots_testados:
    estimativas = rng_shots.binomial(n_shots, 0.5, size=repeticoes_laboratorio) / n_shots
    linhas_moeda.append({
        "shots": n_shots,
        "erro_medio_absoluto": float(np.mean(np.abs(estimativas - 0.5))),
        "desvio_estimativas": float(np.std(estimativas, ddof=1)),
        "escala_1_sobre_raiz_N": 0.5 / np.sqrt(n_shots),
    })

df_moeda_shots = pd.DataFrame(linhas_moeda)
display(
    df_moeda_shots.style.hide(axis="index").format({
        "shots": "{:,.0f}",
        "erro_medio_absoluto": "{:.4f}",
        "desvio_estimativas": "{:.4f}",
        "escala_1_sobre_raiz_N": "{:.4f}",
    }).set_caption("Experimento clássico para entender apenas a incerteza de shots")
)

plt.loglog(
    df_moeda_shots["shots"],
    df_moeda_shots["desvio_estimativas"],
    "o-",
    label="desvio observado em 200 repetições",
)
plt.loglog(
    df_moeda_shots["shots"],
    df_moeda_shots["escala_1_sobre_raiz_N"],
    "--",
    label=r"teoria: $1/(2\sqrt{N})$",
)
plt.xlabel("shots N")
plt.ylabel("incerteza de P̂(1)")
plt.title("Mais shots estreitam a estimativa")
plt.legend()
plt.show()

razao_final_inicial = (
    df_moeda_shots.iloc[-1]["desvio_estimativas"]
    / df_moeda_shots.iloc[0]["desvio_estimativas"]
)
razao_teorica = np.sqrt(shots_testados[0] / shots_testados[-1])
assert np.isclose(razao_final_inicial, razao_teorica, rtol=0.35)
assert (df_moeda_shots["desvio_estimativas"].diff().dropna() < 0).all()
print("⚠️ A moeda modela a contagem binomial; não modela superposição quântica.")
print("✅ Escala estatística 1/√N observada dentro da tolerância Monte Carlo.")
""")

md(r"""
### Exercício 2 — previsão antes do código

1. Escolha `THETA_GRAUS = 120` na célula 2.3.
2. Calcule manualmente $P(0)$ e $P(1)$.
3. Crie uma cópia do circuito, adicione medição e execute com 4.096 shots.
4. Compare frequência observada e probabilidade teórica.
5. Explique a diferença sem usar a palavra “erro” de forma vaga: é erro de implementação, erro amostral ou ruído físico?
""")

code(r"""
# @title 2.5 — Gabarito executável do Exercício 2
theta_ex2 = np.deg2rad(120)
qc_ex2 = QuantumCircuit(1, 1)
qc_ex2.ry(theta_ex2, 0)
qc_ex2.measure(0, 0)

counts_ex2 = simulador.run(
    transpile(qc_ex2, simulador), shots=4096, seed_simulator=SEED
).result().get_counts()

p_teorica_1 = np.sin(theta_ex2 / 2) ** 2
p_observada_1 = counts_ex2.get("1", 0) / 4096
print("P(1) teórica:", p_teorica_1)
print("P̂(1) observada:", p_observada_1)
print("Diferença amostral:", p_observada_1 - p_teorica_1)

assert abs(p_observada_1 - p_teorica_1) < 0.04
print("✅ A discrepância é compatível com amostragem finita do simulador ideal.")
""", tags=["gabarito"])

md(r"""
# Módulo 3 — Muitos qubits e entrelaçamento

## Produto tensorial

Dois qubits vivem em um espaço de dimensão $2^2=4$:

$$|\psi\rangle=\alpha_{00}|00\rangle+\alpha_{01}|01\rangle+\alpha_{10}|10\rangle+\alpha_{11}|11\rangle.$$

Um estado produto pode ser escrito como $|a\rangle\otimes|b\rangle$. Um estado entrelaçado não pode.

O estado de Bell:

$$|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt{2}}$$

é criado aplicando `H` ao primeiro qubit e depois `CX` do primeiro para o segundo.

### O aparente paradoxo

Cada qubit isolado parece maximamente aleatório; o par, porém, apresenta correlação perfeita na mesma base. A informação relevante está nas **correlações**, não em um qubit individual.
""")

md(r"""
## 🧒 Parada leiga 3 — uma coreografia compartilhada

Pense em dois dançarinos treinados para responder juntos quando o diretor escolhe como observá-los. Individualmente, cada resposta parece imprevisível; quando comparamos os pares, aparece uma estrutura que pertence à **coreografia conjunta**.

**🔬 Tradução científica:** no estado $|\Phi^+\rangle$, o estado reduzido de cada qubit é $I/2$, mas o sistema bipartido é puro e não separável. Na base Z, aparecem `00` e `11`; em bases compatíveis adicionais, as correlações revelam coerências que uma mistura clássica não possui.

**⚠️ Onde a analogia falha:** os qubits não recebem instruções instantâneas um do outro e o entrelaçamento não permite enviar mensagens mais rápido que a luz. “Duas luvas em envelopes” explicam correlação clássica pré-combinada, mas não reproduzem todas as estatísticas multibase nem violações de desigualdades de Bell.

### Experiência prática: envelopes e o ponto em que ela quebra

1. Coloque dois cartões iguais (`0,0` ou `1,1`) em envelopes separados, escolhendo o par ao acaso.
2. Abra os dois: cada envelope sozinho parece aleatório, e os pares sempre combinam.
3. Isso imita a distribuição de Bell **somente na base Z**.
4. Agora pergunte como os cartões responderiam se cada lado pudesse escolher entre diferentes bases de medição.
5. Cartões com respostas locais pré-escritas obedecem a limites de Bell; estados quânticos podem produzir correlações que ultrapassam esses limites.

> **Regra de rigor:** correlação perfeita em uma única base não demonstra entrelaçamento. Para uma alegação experimental, use testemunha de entrelaçamento, tomografia ou teste de Bell compatível com o desenho e reporte hipóteses e lacunas experimentais.
""")

code(r"""
# @title 3.1 — Estado de Bell: circuito, statevector e subsistemas
from qiskit.quantum_info import entropy, partial_trace

qc_bell_estado = QuantumCircuit(2)
qc_bell_estado.h(0)
qc_bell_estado.cx(0, 1)
bell_sv = Statevector.from_instruction(qc_bell_estado)

display(qc_bell_estado.draw("mpl"))
print("Amplitudes [|00⟩, |01⟩, |10⟩, |11⟩]:")
print(bell_sv.data)

rho_q0 = partial_trace(bell_sv, [1])
rho_q1 = partial_trace(bell_sv, [0])
entropia_q0 = entropy(rho_q0, base=2)

print("\nEstado reduzido do q0:\n", rho_q0.data)
print("Estado reduzido do q1:\n", rho_q1.data)
print("Entropia de emaranhamento S(q0) =", entropia_q0, "bit")

assert np.allclose(np.abs(bell_sv.data) ** 2, [0.5, 0.0, 0.0, 0.5])
assert np.allclose(rho_q0.data, np.eye(2) / 2)
assert np.isclose(entropia_q0, 1.0)
print("✅ Bell ideal e entropia máxima verificados.")
""")

code(r"""
# @title 3.2 — Medindo correlações de Bell
qc_bell_medida = qc_bell_estado.copy()
qc_bell_medida.measure_all()
qc_bell_t = transpile(qc_bell_medida, simulador)
counts_bell = simulador.run(
    qc_bell_t, shots=SHOTS, seed_simulator=SEED
).result().get_counts()

display(plot_histogram(counts_bell, title="Medições do estado de Bell"))

shots_observados = sum(counts_bell.values())
correlacionados = counts_bell.get("00", 0) + counts_bell.get("11", 0)
taxa_correlacao = correlacionados / shots_observados
print("Taxa de resultados iguais:", taxa_correlacao)

assert set(counts_bell) <= {"00", "11"}
assert taxa_correlacao == 1.0
print("✅ No simulador ideal, todos os pares são correlacionados.")
""")

md(r"""
### 🧭 Pare e interprete

- Por que o primeiro qubit, visto sozinho, tem matriz de densidade $I/2$?
- Por que “50% de `00` e 50% de `11`” não equivale automaticamente a uma mistura clássica? Qual experimento em outra base ajudaria a distingui-las?
- O que a entropia $S=1$ mede neste estado puro bipartido?

### Exercício 3 — estado GHZ

Crie $|GHZ\rangle=(|000\rangle+|111\rangle)/\sqrt{2}$ com três qubits, meça-o e escreva testes para impedir bitstrings inesperadas.
""")

code(r"""
# @title 3.3 — Gabarito executável: GHZ de três qubits
qc_ghz = QuantumCircuit(3)
qc_ghz.h(0)
qc_ghz.cx(0, 1)
qc_ghz.cx(1, 2)
ghz_sv = Statevector.from_instruction(qc_ghz)

qc_ghz_m = qc_ghz.copy()
qc_ghz_m.measure_all()
counts_ghz = simulador.run(
    transpile(qc_ghz_m, simulador), shots=SHOTS, seed_simulator=SEED
).result().get_counts()

display(qc_ghz.draw("mpl"))
display(plot_histogram(counts_ghz, title="Estado GHZ"))

assert np.count_nonzero(np.abs(ghz_sv.data) > 1e-12) == 2
assert set(counts_ghz) <= {"000", "111"}
print("✅ GHZ preparado e medido corretamente.")
""", tags=["gabarito"])

md(r"""
# Módulo 4 — Interferência, ruído e era NISQ

## Interferência: o recurso antes do algoritmo

Considere `H → P(φ) → H`. A primeira Hadamard cria caminhos de amplitude; a porta de fase altera a relação entre eles; a segunda Hadamard recombina os caminhos.

$$P(0)=\cos^2(\varphi/2), \qquad P(1)=\sin^2(\varphi/2).$$

Isso mostra por que fase é fisicamente relevante mesmo quando não aparece diretamente na primeira medição em Z.
""")

code(r"""
# @title 4.1 — Varredura de fase e padrão de interferência
fases = np.linspace(0, 2 * np.pi, 101)
p0_simulado = []

for fase in fases:
    circuito = QuantumCircuit(1)
    circuito.h(0)
    circuito.p(fase, 0)
    circuito.h(0)
    p0_simulado.append(Statevector.from_instruction(circuito).probabilities()[0])

p0_simulado = np.array(p0_simulado)
p0_teorico = np.cos(fases / 2) ** 2

plt.plot(fases, p0_simulado, label="Statevector", lw=2)
plt.plot(fases, p0_teorico, "--", label="cos²(φ/2)")
plt.xlabel("fase φ (rad)")
plt.ylabel("P(0)")
plt.title("Interferência de amplitudes")
plt.legend()
plt.show()

assert np.max(np.abs(p0_simulado - p0_teorico)) < 1e-10
print("✅ Curva de interferência validada.")
""")

md(r"""
## 🧒 Parada leiga 4 — ondas que se ajudam ou se apagam

Jogue duas pedrinhas em uma bacia. Em alguns pontos, as ondas chegam juntas e ficam maiores; em outros, uma crista encontra um vale e elas se reduzem. A fase decide **como os caminhos se recombinam**.

**🔬 Tradução científica:** amplitudes complexas somam antes do módulo quadrado. Para caminhos com amplitudes $a$ e $b$, a probabilidade contém o termo de interferência $2\operatorname{Re}(a^*b)$, que pode ser positivo ou negativo.

**⚠️ Onde a analogia falha:** a função de onda não é, em geral, uma ondinha material na água. A água é um campo clássico contínuo; amplitudes quânticas vivem no espaço de estados e a medição obedece à regra de Born.

### Brincadeira verificável

Use a célula 4.1 como uma “mesa de ondas”: marque antes de executar os ângulos $0$, $\pi/2$, $\pi$ e $2\pi$. Calcule $P(0)=\cos^2(\varphi/2)$ e verifique se os máximos e mínimos previstos aparecem. A analogia só é aceita se a equação também acertar os dados.
""")

md(r"""
## O que muda em hardware real?

Dispositivos atuais são frequentemente descritos como **NISQ**: escala intermediária e presença de ruído. Fontes comuns:

- relaxação de energia ($T_1$);
- perda de fase ($T_2$);
- erro de portas de um e dois qubits;
- erro de leitura;
- crosstalk e deriva de calibração;
- mapeamento e profundidade adicionais após transpilar.

| Representação | Contém ruído de shots? | Contém ruído físico? | Uso principal |
|---|---:|---:|---|
| `Statevector` | não | não | raciocínio e teste ideal |
| Aer ideal + shots | sim | não | estatística de medição |
| Aer + `NoiseModel` | sim | simulado | estudo controlado de robustez |
| QPU real | sim | sim | validação experimental |
""")

md(r"""
### 🧒 Ruído = palco imperfeito e câmera imperfeita

Imagine uma dança executada em um palco que treme e filmada por uma câmera que às vezes troca a etiqueta `0` por `1`.

- **palco/execução:** relaxação, perda de fase, erro de portas, crosstalk e deriva;
- **câmera/leitura:** erro ao converter o estado físico em bit clássico;
- **poucas fotos:** incerteza de shots, mesmo sem falha física.

**🔬 Tradução científica:** ruído de estado e de portas atua antes da medição, enquanto o erro de leitura altera a distribuição observada condicionada ao resultado ideal. Shots finitos acrescentam variância amostral, não um canal físico no circuito.

**⚠️ Onde a analogia falha:** canais quânticos podem causar decoerência e alterar termos fora da diagonal da matriz de densidade; uma câmera clássica defeituosa não representa toda essa dinâmica.

**Atividade:** na célula 4.2, zere primeiro `ReadoutError` e varie apenas o erro `CX`; depois faça o contrário. Mude um fator por vez, repita com seeds diferentes e compare intervalos — não apenas um histograma bonito.
""")

code(r"""
# @title 4.2 — Bell ideal × Bell com ruído controlado
from qiskit_aer.noise import NoiseModel, ReadoutError, depolarizing_error

modelo_ruido = NoiseModel()
modelo_ruido.add_all_qubit_quantum_error(depolarizing_error(0.01, 1), ["h"])
modelo_ruido.add_all_qubit_quantum_error(depolarizing_error(0.03, 2), ["cx"])
modelo_ruido.add_all_qubit_readout_error(
    ReadoutError([[0.97, 0.03], [0.04, 0.96]])
)

sim_ruidoso = AerSimulator(noise_model=modelo_ruido)
qc_bell_ruido_t = transpile(qc_bell_medida, sim_ruidoso)
counts_ruido = sim_ruidoso.run(
    qc_bell_ruido_t, shots=SHOTS, seed_simulator=SEED
).result().get_counts()

display(plot_histogram(
    [counts_bell, counts_ruido],
    legend=["ideal", "ruidoso"],
    title="Efeito de portas e leitura imperfeitas"
))

def taxa_erros_bell(counts):
    total = sum(counts.values())
    return (counts.get("01", 0) + counts.get("10", 0)) / total

erro_ideal = taxa_erros_bell(counts_bell)
erro_ruidoso = taxa_erros_bell(counts_ruido)
print(f"Resultados anticorrelacionados — ideal: {erro_ideal:.3%}")
print(f"Resultados anticorrelacionados — ruído: {erro_ruidoso:.3%}")

assert erro_ideal == 0.0
assert set(counts_ruido) <= {"00", "01", "10", "11"}
print("✅ Ruído introduzido de forma explícita e auditável.")
""")

md(r"""
### Exercício 4 — desenho experimental

Altere separadamente:

1. apenas o erro de leitura;
2. apenas o erro da porta `CX`;
3. os dois juntos.

Registre a taxa de `01` + `10` e responda:

- os efeitos parecem aditivos?
- a conclusão muda com 256 versus 8.192 shots?
- qual variável é manipulada, qual é resposta e quais devem permanecer controladas?

> Esta é a passagem de “executar código” para “fazer pesquisa”: isolar fatores, repetir, quantificar incerteza e documentar decisões.
""")

md(r"""
# Módulo 5 — Como a computação quântica pode ajudar a pesquisa em IA?

## Resposta curta e honesta

A computação quântica **não acelera automaticamente** redes neurais, não substitui GPU e não transforma um conjunto de dados comum em vantagem quântica. Ela pode ser útil quando um subproblema possui estrutura compatível com estados, amostragem, otimização ou simulação quântica e quando o custo de codificar/ler os dados não elimina o benefício.

### Quatro interfaces de pesquisa

| Interface | Papel do circuito quântico | Pergunta científica |
|---|---|---|
| aprendizado de dados quânticos | processar estados/medições nativamente | como inferir fases, Hamiltonianos ou propriedades? |
| kernel quântico | calcular similaridades em espaço de Hilbert | o mapa separa classes que kernels clássicos não separam bem? |
| circuito variacional/QNN | atuar como modelo parametrizado | expressividade e generalização compensam ruído/custo? |
| amostragem/otimização | gerar amostras ou explorar paisagens | existe estrutura aproveitável e benchmark verificável? |

### Arquitetura híbrida mais comum

1. dados e pré-processamento clássicos;
2. codificação em um circuito parametrizado;
3. execução em simulador ou QPU;
4. medição de probabilidades/valores esperados;
5. otimização e decisão clássicas.

O gargalo frequentemente está na codificação, no número de shots, no ruído, na fila do hardware e na ausência de comparação justa.
""")

md(r"""
## 🧒 Parada leiga 5 — um mapa especial para descobrir vizinhos

Imagine pontos desenhados em uma folha. Talvez vermelho e azul estejam embaralhados. Um **feature map** é como dobrar a folha seguindo uma regra: pontos antes distantes podem ficar próximos, e pontos antes misturados podem se separar. O **kernel** é uma régua que mede sem precisar abrir totalmente essa nova geometria.

**🔬 Tradução científica:** o circuito $U_\phi(x)$ prepara $|\phi(x)\rangle$ e o kernel de fidelidade calcula $K(x,z)=|\langle\phi(x)|\phi(z)\rangle|^2$. A matriz $K$ alimenta um método clássico, aqui um SVM com kernel pré-computado.

**⚠️ Onde a analogia falha:** o mapa quântico não “vê” automaticamente a classe correta e não aprende sozinho neste experimento. O circuito fornece uma geometria; o SVM clássico ajusta a fronteira. Dobrar a folha também esconde custos reais: codificação, avaliações $O(n^2)$, shots, ruído e acesso à QPU.

### Experiência de papel antes do código

1. Desenhe dois arcos intercalados, como o conjunto `make_moons`, usando duas cores.
2. Tente separá-los com uma régua reta: este é o desafio de um modelo linear.
3. Curve ou dobre mentalmente a folha e pergunte quais pares deveriam ser considerados semelhantes.
4. Escreva **antes** do benchmark: “minha hipótese é que o mapa ZZ preservará vizinhança de classe melhor que ____ porque ____”.
5. Depois, confronte a hipótese com alinhamento kernel–alvo, posto efetivo, desempenho, incerteza e custo. Uma acurácia isolada não valida a história.
""")

md(r"""
## Conceitos de QML que o pesquisador deve distinguir

### 1. Codificação de dados

- **Angle encoding:** cada variável controla uma rotação; custo simples, número de variáveis relacionado ao número de qubits/camadas.
- **Basis encoding:** dados binários viram estados da base computacional.
- **Amplitude encoding:** pode representar muitos valores em amplitudes, mas preparar o estado pode ser caro e a leitura não recupera todos os valores de uma vez.

### 2. Feature map quântico

Um circuito $U_\phi(x)$ mapeia a observação clássica $x$ para $|\phi(x)\rangle$. A escolha do mapa é uma hipótese de modelagem, equivalente a escolher uma representação.

### 3. Kernel quântico

$$K_{ij}=|\langle\phi(x_i)|\phi(x_j)\rangle|^2.$$

O circuito estima similaridades; um algoritmo clássico, como SVM, usa a matriz.

### 4. Circuito variacional

Possui parâmetros treináveis $\theta$. Um otimizador clássico ajusta $\theta$ a partir de medições. Desafios: muitos shots, ruído, custo de gradiente e **barren plateaus**.
""")

md(r"""
## Portão de decisão: este problema é um bom candidato?

Marque “sim”, “não” ou “ainda não sei”. Quanto mais respostas “não”, mais o estudo deve ser apresentado como investigação metodológica, não promessa de ganho.

| Questão | Por que importa? |
|---|---|
| os dados são quânticos ou simulam um sistema quântico? | evita custo de converter dados clássicos |
| há hipótese explícita sobre o feature map? | reduz busca arbitrária por bons resultados |
| existem baselines clássicos fortes e ajustados? | impede comparação com alvo artificialmente fraco |
| o particionamento e o pré-processamento são idênticos? | evita vazamento e confusão experimental |
| custo de circuitos, shots e tempo é registrado? | acurácia isolada não mede utilidade |
| o resultado se repete em várias sementes? | uma execução pode ser acaso |
| existe conjunto de teste externo ou validação aninhada? | estima generalização |
| a afirmação corresponde à evidência? | prova de conceito não é vantagem quântica |

### Escala do statevector

Um estado puro de $n$ qubits possui $2^n$ amplitudes complexas. Em precisão dupla complexa (16 bytes por amplitude), a memória idealizada cresce como $16\cdot2^n$ bytes, sem contar overhead.
""")

code(r"""
# @title 5.1 — Por que a simulação clássica escala exponencialmente?
qubits = np.arange(1, 41)
memoria_gib = 16 * (2.0 ** qubits) / (1024 ** 3)
df_memoria = pd.DataFrame({"qubits": qubits, "statevector_GiB": memoria_gib})

display(df_memoria[df_memoria["qubits"].isin([10, 20, 25, 30, 35, 40])])

plt.semilogy(qubits, memoria_gib, lw=2, color="#0891b2")
plt.axhline(16, ls="--", color="gray", label="16 GiB")
plt.axhline(128, ls=":", color="black", label="128 GiB")
plt.xlabel("número de qubits")
plt.ylabel("memória idealizada do statevector (GiB, log)")
plt.title("Custo clássico de armazenar 2ⁿ amplitudes")
plt.legend()
plt.show()

assert np.isclose(df_memoria.loc[df_memoria.qubits == 30, "statevector_GiB"].item(), 16.0)
print("✅ Aproximadamente 30 qubits já exigem 16 GiB só para amplitudes.")
""")

md(r"""
# Módulo 6 — Projeto aplicado: kernel quântico para classificação

## Pergunta

Um mapa de características ZZ seguido de SVM produz classificação competitiva no `make_moons` quando comparado, sob o mesmo protocolo, com regressão logística e SVM de kernel RBF?

## Desenho mínimo

- **Dados:** duas classes, duas variáveis, ruído controlado.
- **Divisão:** treino/teste estratificados.
- **Transformação:** ajustada somente no treino; intervalo $[0,\pi]$ para rotações.
- **Baselines:** regressão logística e SVM-RBF.
- **Modelo quântico:** `ZZFeatureMap` + fidelidade + SVM com kernel pré-calculado.
- **Desfechos:** acurácia, acurácia balanceada, F1, matriz de confusão, custo do kernel.
- **Controles:** mesma amostra, semente e conjunto de teste.

> O conjunto é pequeno para manter o Colab didático. O objetivo é aprender o protocolo, não provar vantagem.
""")

code(r"""
# @title 6.1 — Dados, split sem vazamento e visualização
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

X_total, y_total = make_moons(n_samples=120, noise=0.20, random_state=SEED)
X_treino_full, X_teste_full, y_treino_full, y_teste_full = train_test_split(
    X_total,
    y_total,
    test_size=0.30,
    stratify=y_total,
    random_state=SEED,
)

n_treino = 32 if MODO_RAPIDO else 64
n_teste = 16 if MODO_RAPIDO else 32

X_treino_raw, _, y_treino, _ = train_test_split(
    X_treino_full,
    y_treino_full,
    train_size=n_treino,
    stratify=y_treino_full,
    random_state=SEED,
)
X_teste_raw, _, y_teste, _ = train_test_split(
    X_teste_full,
    y_teste_full,
    train_size=n_teste,
    stratify=y_teste_full,
    random_state=SEED,
)

# Regra anti-vazamento: fit apenas no treino.
escalador = MinMaxScaler(feature_range=(0, np.pi))
X_treino = escalador.fit_transform(X_treino_raw)
X_teste = escalador.transform(X_teste_raw)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(X_treino_raw[:, 0], X_treino_raw[:, 1], c=y_treino, cmap="coolwarm", edgecolor="k")
ax[0].set_title("Treino — espaço original")
ax[1].scatter(X_treino[:, 0], X_treino[:, 1], c=y_treino, cmap="coolwarm", edgecolor="k")
ax[1].set_title("Treino — ângulos em [0, π]")
for eixo in ax:
    eixo.set_xlabel("x₁")
    eixo.set_ylabel("x₂")
plt.tight_layout()
plt.show()

assert len(set(y_treino)) == 2 and len(set(y_teste)) == 2
assert X_treino.shape[1] == 2
assert np.all(X_treino >= -1e-12) and np.all(X_treino <= np.pi + 1e-12)
print(f"✅ Treino: {len(X_treino)} | teste: {len(X_teste)} | sem fit no teste.")
""")

code(r"""
# @title 6.2 — Baselines clássicos sob o mesmo protocolo
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.svm import SVC

def calcular_metricas(nome, y_true, y_pred, custo_s=None):
    return {
        "modelo": nome,
        "acuracia": accuracy_score(y_true, y_pred),
        "acuracia_balanceada": balanced_accuracy_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
        "tempo_kernel_s": custo_s,
    }

modelo_log = LogisticRegression(max_iter=2000, random_state=SEED)
modelo_rbf = SVC(kernel="rbf", C=1.0, gamma="scale")

modelo_log.fit(X_treino, y_treino)
modelo_rbf.fit(X_treino, y_treino)

pred_log = modelo_log.predict(X_teste)
pred_rbf = modelo_rbf.predict(X_teste)

resultados = [
    calcular_metricas("Regressão logística", y_teste, pred_log),
    calcular_metricas("SVM-RBF", y_teste, pred_rbf),
]

display(pd.DataFrame(resultados))
print("\nRelatório SVM-RBF:\n", classification_report(y_teste, pred_rbf, digits=3))

fig, ax = plt.subplots(1, 2, figsize=(8, 3.5))
sns.heatmap(confusion_matrix(y_teste, pred_log), annot=True, fmt="d", cbar=False, ax=ax[0])
sns.heatmap(confusion_matrix(y_teste, pred_rbf), annot=True, fmt="d", cbar=False, ax=ax[1])
ax[0].set_title("Regressão logística")
ax[1].set_title("SVM-RBF")
for eixo in ax:
    eixo.set_xlabel("predito")
    eixo.set_ylabel("real")
plt.tight_layout()
plt.show()

assert len(pred_log) == len(y_teste) == len(pred_rbf)
print("✅ Baselines registrados antes do modelo quântico.")
""")

md(r"""
## O que o `ZZFeatureMap` faz?

Ele combina:

- portas Hadamard para criar superposições;
- fases dependentes de cada variável;
- interações ZZ dependentes de pares de variáveis;
- entrelaçamento definido pela topologia escolhida.

O circuito não “aprende” sozinho neste experimento. Ele define uma geometria de similaridade. O SVM clássico aprende a fronteira a partir da matriz de kernel.

### Complexidade experimental

Para $n$ amostras de treino, a matriz completa possui $n^2$ entradas. Mesmo explorando simetria, o número de avaliações cresce quadraticamente. Registre tempo, número de circuitos e shots: desempenho sem custo não é benchmark completo.
""")

code(r"""
# @title 6.3 — Construção do feature map e do kernel quântico
from qiskit.circuit.library import zz_feature_map
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_machine_learning.state_fidelities import ComputeUncompute

feature_map = zz_feature_map(
    feature_dimension=2,
    reps=1,
    entanglement="linear",
)

sampler_kernel = StatevectorSampler(default_shots=SHOTS, seed=SEED)
fidelidade = ComputeUncompute(sampler=sampler_kernel)
kernel_quantico = FidelityQuantumKernel(
    fidelity=fidelidade,
    feature_map=feature_map,
    enforce_psd=True,
    evaluate_duplicates="off_diagonal",
)

display(feature_map.draw("mpl"))
print("Qubits:", feature_map.num_qubits)
print("Parâmetros de dados:", feature_map.num_parameters)

assert feature_map.num_qubits == X_treino.shape[1]
print("✅ Dimensão dos dados compatível com o circuito.")
""")

code(r"""
# @title 6.4 — Avaliação das matrizes de kernel (etapa de maior custo)
import time

inicio = time.perf_counter()
K_treino_bruto = kernel_quantico.evaluate(x_vec=X_treino)
K_teste_bruto = kernel_quantico.evaluate(x_vec=X_teste, y_vec=X_treino)
tempo_kernel = time.perf_counter() - inicio

def normalizar_kernel_fidelidade(K_treino_entrada, K_cruzado_entrada=None, eps=1e-12):
    '''Converte uma matriz PSD em matriz de correlação com diagonal unitária.

    Para K_train usa D^(-1/2) K D^(-1/2). Para um kernel cruzado
    K(X_novo, X_train), a autofidelidade teórica das linhas novas é 1; portanto,
    normaliza somente pelas escalas das colunas de treino.
    '''
    Ksim = (np.asarray(K_treino_entrada) + np.asarray(K_treino_entrada).T) / 2
    diagonal = np.diag(Ksim).copy()
    if np.any(~np.isfinite(diagonal)) or np.any(diagonal <= eps):
        raise ValueError("A diagonal do kernel contém valor não finito ou não positivo.")
    escala = np.sqrt(diagonal)
    Kcorr = Ksim / np.outer(escala, escala)
    Kcorr = (Kcorr + Kcorr.T) / 2
    np.fill_diagonal(Kcorr, 1.0)
    if K_cruzado_entrada is None:
        return Kcorr
    Kcross = np.asarray(K_cruzado_entrada) / escala[None, :]
    return Kcorr, Kcross

# enforce_psd repara o espectro global, mas pode deslocar a diagonal. A
# normalização congruente abaixo preserva PSD e restaura k(x,x)=1 sem usar
# rótulos ou dados de teste para ajustar qualquer parâmetro.
K_treino, K_teste = normalizar_kernel_fidelidade(K_treino_bruto, K_teste_bruto)

print("K_treino:", K_treino.shape)
print("K_teste:", K_teste.shape)
print(f"Tempo total de kernel: {tempo_kernel:.2f} s")
print(f"Avaliações lógicas aproximadas: {len(X_treino)**2 + len(X_teste)*len(X_treino):,}")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
sns.heatmap(K_treino, cmap="viridis", vmin=0, vmax=1, ax=ax[0])
sns.heatmap(K_teste, cmap="magma", vmin=0, vmax=1, ax=ax[1])
ax[0].set_title("Kernel quântico — treino × treino")
ax[1].set_title("Kernel quântico — teste × treino")
for eixo in ax:
    eixo.set_xlabel("índice de treino")
    eixo.set_ylabel("índice da linha")
plt.tight_layout()
plt.show()
""")

code(r"""
# @title 6.5 — Diagnóstico geométrico robusto e TDD da matriz
from IPython.display import Markdown

diagonal_max_bruta = np.max(np.abs(np.diag(K_treino_bruto) - 1.0))
simetria_max = np.max(np.abs(K_treino - K_treino.T))
diagonal_max = np.max(np.abs(np.diag(K_treino) - 1.0))
autovalores = np.linalg.eigvalsh((K_treino + K_treino.T) / 2)
menor_autovalor = autovalores.min()

# A diagonal teórica é exatamente 1. O desvio bruto é provocado pela projeção
# PSD global, não constitui estimador adequado de suficiência de shots. Depois da
# normalização de correlação, a identidade deve valer em precisão numérica.
TOL_SIMETRIA = 1e-10
TOL_PSD = 1e-10
TOL_DIAGONAL = 1e-10

y_pm = 2 * y_treino - 1
K_alvo = np.outer(y_pm, y_pm)
alinhamento = np.sum(K_treino * K_alvo) / (
    np.linalg.norm(K_treino, "fro") * np.linalg.norm(K_alvo, "fro")
)

diagnostico_kernel = {
    "assimetria_max": float(simetria_max),
    "desvio_diagonal_bruta_apos_psd": float(diagonal_max_bruta),
    "desvio_diagonal_max": float(diagonal_max),
    "menor_autovalor": float(menor_autovalor),
    "alinhamento_kernel_alvo": float(alinhamento),
    "tolerancia_diagonal": float(TOL_DIAGONAL),
}

status_simetria = "✅ aprovado" if simetria_max <= TOL_SIMETRIA else "❌ revisar"
status_diagonal = "✅ normalizada" if diagonal_max <= TOL_DIAGONAL else "❌ revisar normalização"
status_psd = "✅ aprovado" if menor_autovalor >= -TOL_PSD else "❌ revisar PSD"

tabela_diagnostico = f'''
### Diagnóstico numérico do kernel

| Métrica | Valor observado | Critério | Situação |
|---|---:|---:|:---|
| Assimetria máxima | `{simetria_max:.3e}` | `≤ {TOL_SIMETRIA:.1e}` | {status_simetria} |
| Desvio diagonal bruto após PSD | `{diagonal_max_bruta:.3e}` | diagnóstico | ℹ️ registrado antes da normalização |
| Desvio diagonal normalizado | `{diagonal_max:.3e}` | `≤ {TOL_DIAGONAL:.1e}` | {status_diagonal} |
| Menor autovalor | `{menor_autovalor:.3e}` | `≥ {-TOL_PSD:.1e}` | {status_psd} |
| Alinhamento kernel–alvo | `{alinhamento:.3e}` | informativo | ℹ️ sem aprovação automática |
'''
display(Markdown(tabela_diagnostico))

print(
    "Nota: enforce_psd=True pode deslocar a diagonal. Foi aplicada a transformação "
    "D^(-1/2) K D^(-1/2), que restaura k(xᵢ,xᵢ)=1 e preserva PSD por congruência. "
    "A adequação de shots deve ser avaliada por repetições/seeds e estabilidade dos "
    "elementos fora da diagonal, não pelo desvio diagonal criado pelo reparo PSD."
)

plt.plot(autovalores, marker="o", ms=3)
plt.axhline(0, color="black", lw=1)
plt.title("Espectro da matriz de kernel")
plt.xlabel("índice")
plt.ylabel("autovalor")
plt.show()

assert K_treino.shape == (len(X_treino), len(X_treino))
assert K_teste.shape == (len(X_teste), len(X_treino))
assert simetria_max <= TOL_SIMETRIA, "A matriz perdeu simetria numérica."
assert diagonal_max <= TOL_DIAGONAL, (
    f"A normalização não restaurou a diagonal: {diagonal_max:.3e}."
)
assert menor_autovalor >= -TOL_PSD, "A matriz não é PSD dentro da tolerância numérica."
print("✅ Kernel simétrico, diagonal unitária e espectro PSD aprovados.")
""")

code(r"""
# @title 6.6 — Treino do SVM com kernel quântico e comparação final
modelo_qk = SVC(kernel="precomputed", C=1.0)
modelo_qk.fit(K_treino, y_treino)
pred_qk = modelo_qk.predict(K_teste)

resultados.append(
    calcular_metricas("SVM + kernel quântico", y_teste, pred_qk, tempo_kernel)
)
resultados_df = pd.DataFrame(resultados).sort_values("acuracia", ascending=False)
display(resultados_df.style.format({
    "acuracia": "{:.3f}",
    "acuracia_balanceada": "{:.3f}",
    "f1": "{:.3f}",
    "tempo_kernel_s": "{:.2f}",
}))

print("\nRelatório do kernel quântico:\n", classification_report(y_teste, pred_qk, digits=3))
sns.heatmap(confusion_matrix(y_teste, pred_qk), annot=True, fmt="d", cbar=False, cmap="Purples")
plt.title("SVM + kernel quântico")
plt.xlabel("predito")
plt.ylabel("real")
plt.show()

assert resultados_df["modelo"].nunique() == 3
assert len(pred_qk) == len(y_teste)
print("✅ Comparação concluída sob o mesmo conjunto de teste.")
""")

code(r"""
# @title 6.7 — Incerteza: intervalo bootstrap da acurácia
def intervalo_bootstrap_acuracia(y_true, y_pred, seed=42, n_boot=3000):
    rng = np.random.default_rng(seed)
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    valores = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(y_true), size=len(y_true))
        valores.append(accuracy_score(y_true[idx], y_pred[idx]))
    return np.quantile(valores, [0.025, 0.5, 0.975])

predicoes = {
    "Regressão logística": pred_log,
    "SVM-RBF": pred_rbf,
    "SVM + kernel quântico": pred_qk,
}

intervalos = []
for nome, pred in predicoes.items():
    baixo, mediana, alto = intervalo_bootstrap_acuracia(y_teste, pred, SEED)
    intervalos.append({"modelo": nome, "IC_2.5%": baixo, "mediana": mediana, "IC_97.5%": alto})

intervalos_df = pd.DataFrame(intervalos)
display(intervalos_df.style.format({"IC_2.5%": "{:.3f}", "mediana": "{:.3f}", "IC_97.5%": "{:.3f}"}))

print("Interprete com cautela: o bootstrap quantifica a instabilidade desta pequena amostra;")
print("ele não substitui validação multi-semente, teste externo ou análise de potência.")
""")

md(r"""
# Módulo 6.8 — Gap aplicado: do placar ao portão de evidência

## O problema que faltava resolver

Uma tabela de acurácia ajuda a comparar modelos, mas não responde sozinha à pergunta que orienta a decisão científica: **a diferença observada é estável, relevante e suficiente para justificar o próximo investimento experimental?**

Em QML, esse gap é especialmente perigoso porque:

- experimentos simulados costumam usar amostras pequenas;
- selecionar o melhor concorrente olhando o teste produz viés;
- intervalos isolados de dois modelos não são o intervalo da **diferença pareada**;
- custo, shots e geometria do kernel podem desaparecer atrás de uma única acurácia;
- “venceu nesta execução” não equivale a vantagem quântica.

O painel abaixo funciona como um **assistente de decisão para o pesquisador**. Ele compara o kernel quântico com o `SVM-RBF`, definido **a priori** como baseline não linear de referência; estima a diferença de acurácia por bootstrap pareado; resume custo e posto efetivo; emite um parecer limitado ao protocolo; e lista o próximo experimento necessário.

> O portão não prova vantagem quântica. Sua função é impedir que evidência exploratória seja promovida, por engano, a conclusão forte.
""")

md(r"""
## 🧒 Portão de evidência = semáforo científico

- **🔴 Pare:** um resultado isolado, baseline fraco, vazamento ou custo não registrado.
- **🟡 Avance com cuidado:** sinal pareado exploratório, mas intervalo inclui efeitos irrelevantes ou falta validação externa.
- **🟢 Prossiga para o próximo teste:** critérios pré-especificados foram atendidos; isso autoriza **mais investigação**, não uma manchete definitiva.

**🔬 Tradução científica:** o portão combina comparação pareada, intervalo de incerteza, baseline definido a priori, geometria, custo e regras go/no-go. Cada nível limita quais alegações são permitidas.

**⚠️ Onde a analogia falha:** um semáforo comum decide com três luzes fixas. Evidência científica é gradual, depende do desenho, da validade das hipóteses e pode mudar com replicação. “Verde” aqui nunca significa “vantagem quântica provada”.

**Prática:** antes de rodar 6.8.1, classifique o estudo como vermelho, amarelo ou verde e escreva duas evidências que faltam. Depois compare sua decisão com o painel e explique qualquer mudança.
""")

code(r"""
# @title 6.8.1 — Quantum Evidence Gate: efeito pareado, geometria e custo
from IPython.display import Markdown

BASELINE_REFERENCIA = "SVM-RBF"  # pré-especificado; não escolhido pelo resultado do teste
N_BOOT_PAREADO = 5000

predicoes_classicas = {
    "Regressão logística": pred_log,
    "SVM-RBF": pred_rbf,
}
pred_baseline = np.asarray(predicoes_classicas[BASELINE_REFERENCIA])

def bootstrap_delta_pareado(y_true, pred_candidato, pred_referencia, seed=42, n_boot=5000):
    '''Reamostra as mesmas observações para preservar o pareamento entre modelos.'''
    y_true = np.asarray(y_true)
    pred_candidato = np.asarray(pred_candidato)
    pred_referencia = np.asarray(pred_referencia)
    assert len(y_true) == len(pred_candidato) == len(pred_referencia)

    rng = np.random.default_rng(seed)
    deltas = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        idx = rng.integers(0, len(y_true), size=len(y_true))
        acc_q = accuracy_score(y_true[idx], pred_candidato[idx])
        acc_b = accuracy_score(y_true[idx], pred_referencia[idx])
        deltas[i] = acc_q - acc_b
    return deltas

delta_observado = float(
    accuracy_score(y_teste, pred_qk) - accuracy_score(y_teste, pred_baseline)
)
deltas_boot = bootstrap_delta_pareado(
    y_teste, pred_qk, pred_baseline, seed=SEED, n_boot=N_BOOT_PAREADO
)
ic_delta_baixo, mediana_delta, ic_delta_alto = np.quantile(
    deltas_boot, [0.025, 0.5, 0.975]
)
fracao_delta_positivo = float(np.mean(deltas_boot > 0))

# Posto efetivo entrópico: resumo descritivo de quantas direções espectrais
# contribuem de forma relevante. Não é, isoladamente, um teste de vantagem.
espectro_nao_negativo = np.clip(autovalores, 0.0, None)
pesos_espectrais = espectro_nao_negativo / espectro_nao_negativo.sum()
pesos_positivos = pesos_espectrais[pesos_espectrais > 0]
entropia_espectral = float(-np.sum(pesos_positivos * np.log(pesos_positivos)))
posto_efetivo = float(np.exp(entropia_espectral))
posto_efetivo_relativo = float(posto_efetivo / len(K_treino))

# Estimativa de avaliações únicas: triângulo sem diagonal no treino + teste × treino.
# O backend pode agrupar pubs de modo diferente; por isso, isto é contabilidade lógica.
avaliacoes_fidelidade_estimadas = int(
    len(X_treino) * (len(X_treino) - 1) // 2
    + len(X_teste) * len(X_treino)
)
shots_logicos_estimados = int(avaliacoes_fidelidade_estimadas * SHOTS)

if ic_delta_baixo > 0:
    parecer = "sinal positivo neste protocolo; requer confirmação independente"
elif ic_delta_alto < 0:
    parecer = "baseline clássico favorecido neste protocolo"
else:
    parecer = "inconclusivo: o IC pareado inclui diferença zero"

criterios_evidencia = {
    "baseline_pre_especificado": True,
    "comparacao_pareada": True,
    "ic_exclui_zero_a_favor_qml": bool(ic_delta_baixo > 0),
    "teste_com_ao_menos_30_casos": bool(len(y_teste) >= 30),
    "validacao_multissemente_executada": False,
    "teste_externo_executado": False,
    "custo_quantico_registrado": bool(np.isfinite(tempo_kernel)),
}

recomendacoes = []
if ic_delta_baixo <= 0 <= ic_delta_alto:
    recomendacoes.append(
        "Aumentar o teste e repetir o split em pelo menos 10 sementes; a diferença ainda inclui zero."
    )
if len(y_teste) < 30:
    recomendacoes.append(
        "Reservar um teste maior ou externo; a amostra atual é adequada apenas para exploração."
    )
recomendacoes.append(
    "Ajustar C e hiperparâmetros de ambos os SVMs por validação aninhada, sem tocar no teste final."
)
recomendacoes.append(
    "Executar a escada statevector → shots → ruído → QPU e registrar a degradação do kernel."
)
recomendacoes.append(
    "Relatar o resultado mesmo se for nulo ou negativo; ele restringe hipóteses futuras."
)

status_evidencia = (
    "candidata a confirmação, nunca vantagem demonstrada"
    if ic_delta_baixo > 0
    else "exploratória"
)

portao_evidencia = {
    "baseline_referencia": BASELINE_REFERENCIA,
    "delta_acuracia_qml_menos_baseline": delta_observado,
    "ic95_delta_pareado": [float(ic_delta_baixo), float(ic_delta_alto)],
    "mediana_delta_bootstrap": float(mediana_delta),
    "fracao_reamostragens_delta_positivo": fracao_delta_positivo,
    "n_bootstrap": N_BOOT_PAREADO,
    "n_teste": int(len(y_teste)),
    "posto_efetivo_kernel": posto_efetivo,
    "posto_efetivo_relativo": posto_efetivo_relativo,
    "tempo_kernel_s": float(tempo_kernel),
    "avaliacoes_fidelidade_estimadas": avaliacoes_fidelidade_estimadas,
    "shots_logicos_estimados": shots_logicos_estimados,
    "parecer": parecer,
    "status_evidencia": status_evidencia,
    "criterios": criterios_evidencia,
    "proximos_passos": recomendacoes,
}

linhas_criterios = "\n".join(
    f"| {nome.replace('_', ' ')} | {'✅' if aprovado else '⬜'} |"
    for nome, aprovado in criterios_evidencia.items()
)
linhas_recomendacoes = "\n".join(
    f"{i}. {item}" for i, item in enumerate(recomendacoes, start=1)
)

painel_evidencia = f'''
## Painel de decisão científica

| Pergunta | Resultado |
|---|---:|
| Baseline de referência | **{BASELINE_REFERENCIA}** |
| Δ acurácia QML − baseline | **{delta_observado:+.3f}** |
| IC 95% pareado do Δ | **[{ic_delta_baixo:+.3f}, {ic_delta_alto:+.3f}]** |
| Reamostragens com Δ > 0 | **{fracao_delta_positivo:.1%}** |
| Posto efetivo do kernel | **{posto_efetivo:.2f} / {len(K_treino)}** |
| Tempo para construir kernels | **{tempo_kernel:.2f} s** |
| Avaliações lógicas estimadas | **{avaliacoes_fidelidade_estimadas:,}** |
| Parecer | **{parecer}** |
| Nível atual | **{status_evidencia}** |

### Critérios de progressão

| Critério | Atendido |
|---|:---:|
{linhas_criterios}

### Próximo experimento recomendado

{linhas_recomendacoes}
'''
display(Markdown(painel_evidencia))
""")

code(r"""
# @title 6.8.2 — TDD do portão de evidência
assert len(deltas_boot) == N_BOOT_PAREADO
assert np.all(np.isfinite(deltas_boot))
assert -1.0 <= delta_observado <= 1.0
assert ic_delta_baixo <= mediana_delta <= ic_delta_alto
assert 0.0 <= fracao_delta_positivo <= 1.0
assert 1.0 - 1e-9 <= posto_efetivo <= len(K_treino) + 1e-9
assert portao_evidencia["baseline_referencia"] == BASELINE_REFERENCIA
assert portao_evidencia["status_evidencia"] != "vantagem quântica demonstrada"
print("✅ Portão de evidência consistente: efeito pareado, geometria e custo auditados.")
""")

md(r"""
## Como interpretar sem exagerar

1. **Se o kernel quântico empatar:** ele demonstrou viabilidade, não superioridade.
2. **Se vencer por uma observação:** a diferença pode ser instabilidade do teste pequeno.
3. **Se perder:** isso não refuta QML em geral; refuta ou enfraquece esta configuração neste protocolo.
4. **Se o kernel demorar muito mais:** reporte custo e benefício juntos.
5. **Se o baseline RBF vencer:** é um resultado científico válido e útil.

### Afirmações permitidas por este notebook

- “Implementamos e auditamos um pipeline híbrido de kernel quântico.”
- “Sob esta divisão e estes hiperparâmetros, observamos a métrica X.”
- “São necessárias repetições, ajuste aninhado e hardware real para conclusões mais amplas.”

### Afirmações que os dados ainda não sustentam

- “O modelo quântico é universalmente melhor.”
- “Houve vantagem quântica.”
- “O resultado pequeno garante escalabilidade.”
""")

md(r"""
# Módulo 7 — Transformar o laboratório em protocolo de pesquisa

## Matriz de ablação recomendada

| Fator | Níveis iniciais | Mantido constante |
|---|---|---|
| repetições do feature map | 1, 2, 3 | dados, C, split |
| shots | 512, 2.048, 8.192 | mapa, semente, split |
| entrelaçamento | linear, full | dimensão, reps |
| ruído | ideal, simulado, QPU | circuito lógico |
| tamanho de treino | 32, 64, 128… | distribuição e teste |
| semente | ≥ 10 valores | grade e métricas |

Para uma comparação publicável, faça ajuste de hiperparâmetros **dentro do treino** (validação cruzada aninhada), mantenha o teste final intocado e inclua um orçamento computacional.
""")

code(r"""
# @title 7.1 — Experimentos estendidos opcionais (podem demorar) {display-mode: "form"}
resultados_ablação = []

if not EXECUTAR_EXPERIMENTOS_ESTENDIDOS:
    print("⏭️ Ablações não executadas. Marque EXECUTAR_EXPERIMENTOS_ESTENDIDOS na configuração.")
else:
    for reps in [1, 2]:
        for shots_ab in [512, 2048]:
            fm = zz_feature_map(2, reps=reps, entanglement="linear")
            sampler_ab = StatevectorSampler(default_shots=shots_ab, seed=SEED)
            fidelity_ab = ComputeUncompute(sampler=sampler_ab)
            qk_ab = FidelityQuantumKernel(fidelity=fidelity_ab, feature_map=fm, enforce_psd=True)

            t0 = time.perf_counter()
            Ktr = qk_ab.evaluate(x_vec=X_treino)
            Kte = qk_ab.evaluate(x_vec=X_teste, y_vec=X_treino)
            dt = time.perf_counter() - t0

            clf = SVC(kernel="precomputed", C=1.0).fit(Ktr, y_treino)
            pred = clf.predict(Kte)
            resultados_ablação.append({
                "reps": reps,
                "shots": shots_ab,
                "acuracia": accuracy_score(y_teste, pred),
                "f1": f1_score(y_teste, pred),
                "tempo_s": dt,
            })
            print("Concluído:", resultados_ablação[-1])

    display(pd.DataFrame(resultados_ablação))
""")

md(r"""
## 7.2 — Validação para paper: CV aninhada repetida

Esta etapa implementa a principal recomendação do portão de evidência.

### 🧒 Analogia: escola, treino e envelope lacrado

Pense em três papéis diferentes:

1. **caderno de treino:** ajustar o modelo;
2. **simulado interno:** escolher hiperparâmetros;
3. **prova externa em envelope lacrado:** estimar generalização sem reutilizar as respostas.

Na validação aninhada, cada fold externo vira temporariamente o envelope lacrado, enquanto a validação interna escolhe o modelo usando apenas o restante.

**🔬 Tradução científica:** o laço externo estima o erro de generalização do procedimento completo; o laço interno seleciona hiperparâmetros sem acesso ao fold externo. As diferenças entre modelos são calculadas no mesmo fold, preservando o pareamento.

**⚠️ Onde a analogia falha:** folds reutilizam observações entre iterações e, portanto, não são provas independentes. A inferência deve corrigir dependência e não substitui validação em uma população externa.

Em cada fold externo:

1. um teste externo à seleção é separado primeiro;
2. o escalonador é ajustado somente no treino;
3. `C` — e `gamma`, no RBF — são escolhidos por validação cruzada interna;
4. RBF e kernel quântico usam exatamente o mesmo teste;
5. a unidade da comparação estatística passa a ser a **diferença pareada por fold externo**.

O desenho usa **4 folds × 3 repetições = 12 avaliações externas**, cada uma com 30 casos de teste e seleção interna em 3 folds. Isso substitui a sugestão inicial de dez sementes por uma estrutura mais apropriada para artigo. Para manter o custo viável em Colab, a fidelidade é calculada por statevector e o ruído de shots é emulado por amostragem binomial. Isso **não substitui** Aer com ruído de portas nem hardware real; esses níveis aparecem na seção seguinte.
""")

code(r"""
# @title 7.2 — 4 folds × 3 repetições + seleção interna {display-mode: "form"}
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold, StratifiedKFold
from qiskit_machine_learning.kernels import FidelityStatevectorKernel
from qiskit_machine_learning.utils import algorithm_globals

GRADE_C = [0.1, 1.0, 10.0]
GRADE_GAMMA_RBF = ["scale", "auto"]
N_SPLITS_EXTERNOS = 4
N_REPETICOES_EXTERNAS = 3
N_AVALIACOES_EXTERNAS = N_SPLITS_EXTERNOS * N_REPETICOES_EXTERNAS

validacao_robusta_df = pd.DataFrame()
resumo_validacao_robusta = {}

def ic_bootstrap_media_pareada(valores, seed=42, n_boot=5000):
    valores = np.asarray(valores, dtype=float)
    rng = np.random.default_rng(seed)
    medias = np.empty(n_boot)
    for i in range(n_boot):
        medias[i] = rng.choice(valores, size=len(valores), replace=True).mean()
    return np.quantile(medias, [0.025, 0.5, 0.975])

if not EXECUTAR_VALIDACAO_ROBUSTA:
    print("⏭️ Validação robusta preparada, mas não executada.")
    print("Ative EXECUTAR_VALIDACAO_ROBUSTA na célula 0.1 e execute novamente a partir daqui.")
else:
    linhas_validacao = []
    cv_externa = RepeatedStratifiedKFold(
        n_splits=N_SPLITS_EXTERNOS,
        n_repeats=N_REPETICOES_EXTERNAS,
        random_state=SEED,
    )

    for numero_execucao, (idx_tr, idx_te) in enumerate(
        cv_externa.split(X_total, y_total), start=1
    ):
        seed_run = SEED + numero_execucao * 1009
        repeticao = (numero_execucao - 1) // N_SPLITS_EXTERNOS + 1
        fold_externo = (numero_execucao - 1) % N_SPLITS_EXTERNOS + 1
        algorithm_globals.random_seed = seed_run
        assert set(idx_tr).isdisjoint(set(idx_te)), "Vazamento: treino e teste se sobrepõem."

        Xr_tr_raw, Xr_te_raw = X_total[idx_tr], X_total[idx_te]
        yr_tr, yr_te = y_total[idx_tr], y_total[idx_te]
        scaler_run = MinMaxScaler((0, np.pi)).fit(Xr_tr_raw)
        Xr_tr = scaler_run.transform(Xr_tr_raw)
        Xr_te = scaler_run.transform(Xr_te_raw)

        cv_interna = StratifiedKFold(n_splits=3, shuffle=True, random_state=seed_run)

        busca_rbf = GridSearchCV(
            estimator=SVC(kernel="rbf"),
            param_grid={"C": GRADE_C, "gamma": GRADE_GAMMA_RBF},
            scoring="balanced_accuracy",
            cv=cv_interna,
            n_jobs=-1,
            refit=True,
        )
        busca_rbf.fit(Xr_tr, yr_tr)
        pred_rbf_run = busca_rbf.predict(Xr_te)

        qk_run = FidelityStatevectorKernel(
            feature_map=feature_map,
            shots=SHOTS,
            enforce_psd=True,
        )
        t0_kernel = time.perf_counter()
        Kr_tr = qk_run.evaluate(Xr_tr)
        Kr_te = qk_run.evaluate(Xr_te, Xr_tr)
        tempo_run = time.perf_counter() - t0_kernel

        busca_qk = GridSearchCV(
            estimator=SVC(kernel="precomputed"),
            param_grid={"C": GRADE_C},
            scoring="balanced_accuracy",
            cv=cv_interna,
            n_jobs=1,
            refit=True,
        )
        busca_qk.fit(Kr_tr, yr_tr)
        pred_qk_run = busca_qk.predict(Kr_te)

        acc_rbf_run = accuracy_score(yr_te, pred_rbf_run)
        acc_qk_run = accuracy_score(yr_te, pred_qk_run)
        bac_rbf_run = balanced_accuracy_score(yr_te, pred_rbf_run)
        bac_qk_run = balanced_accuracy_score(yr_te, pred_qk_run)
        f1_rbf_run = f1_score(yr_te, pred_rbf_run)
        f1_qk_run = f1_score(yr_te, pred_qk_run)

        linhas_validacao.append({
            "execucao": numero_execucao,
            "repeticao": repeticao,
            "fold_externo": fold_externo,
            "seed": seed_run,
            "n_treino": len(idx_tr),
            "n_teste": len(idx_te),
            "C_rbf": busca_rbf.best_params_["C"],
            "gamma_rbf": busca_rbf.best_params_["gamma"],
            "C_quantico": busca_qk.best_params_["C"],
            "acuracia_rbf": acc_rbf_run,
            "acuracia_quantica": acc_qk_run,
            "delta_acuracia": acc_qk_run - acc_rbf_run,
            "acuracia_balanceada_rbf": bac_rbf_run,
            "acuracia_balanceada_quantica": bac_qk_run,
            "delta_acuracia_balanceada": bac_qk_run - bac_rbf_run,
            "f1_rbf": f1_rbf_run,
            "f1_quantico": f1_qk_run,
            "delta_f1": f1_qk_run - f1_rbf_run,
            "tempo_kernel_s": tempo_run,
        })
        print(
            f"[{numero_execucao:02d}/{N_AVALIACOES_EXTERNAS}] rep={repeticao} fold={fold_externo} | "
            f"Δacc={acc_qk_run - acc_rbf_run:+.3f} | kernel={tempo_run:.2f}s"
        )

    validacao_robusta_df = pd.DataFrame(linhas_validacao)
    baixo_rob, mediana_rob, alto_rob = ic_bootstrap_media_pareada(
        validacao_robusta_df["delta_acuracia"], seed=SEED
    )

    if baixo_rob > 0:
        parecer_robusto = "sinal positivo repetido; avançar para teste externo e ruído/QPU"
    elif alto_rob < 0:
        parecer_robusto = "baseline RBF favorecido nas repetições"
    else:
        parecer_robusto = "resultado multissemente inconclusivo"

    resumo_validacao_robusta = {
        "n_avaliacoes_externas": int(len(validacao_robusta_df)),
        "n_repeticoes_externas": N_REPETICOES_EXTERNAS,
        "n_folds_externos": N_SPLITS_EXTERNOS,
        "media_delta_acuracia": float(validacao_robusta_df["delta_acuracia"].mean()),
        "desvio_delta_acuracia": float(validacao_robusta_df["delta_acuracia"].std(ddof=1)),
        "ic95_media_delta": [float(baixo_rob), float(alto_rob)],
        "mediana_bootstrap_media_delta": float(mediana_rob),
        "vitorias_qml": int((validacao_robusta_df["delta_acuracia"] > 0).sum()),
        "empates": int((validacao_robusta_df["delta_acuracia"] == 0).sum()),
        "parecer": parecer_robusto,
    }

    portao_evidencia["criterios"]["validacao_multissemente_executada"] = True
    portao_evidencia["validacao_robusta"] = resumo_validacao_robusta
    portao_evidencia["status_evidencia"] = parecer_robusto

    display(validacao_robusta_df.style.format({
        "acuracia_rbf": "{:.3f}",
        "acuracia_quantica": "{:.3f}",
        "delta_acuracia": "{:+.3f}",
        "acuracia_balanceada_rbf": "{:.3f}",
        "acuracia_balanceada_quantica": "{:.3f}",
        "delta_acuracia_balanceada": "{:+.3f}",
        "f1_rbf": "{:.3f}",
        "f1_quantico": "{:.3f}",
        "delta_f1": "{:+.3f}",
        "tempo_kernel_s": "{:.2f}",
    }))

    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(validacao_robusta_df["execucao"], validacao_robusta_df["acuracia_rbf"], "o-", label="SVM-RBF")
    ax[0].plot(validacao_robusta_df["execucao"], validacao_robusta_df["acuracia_quantica"], "o-", label="QML")
    ax[0].set(title="Desempenho por fold externo", xlabel="avaliação externa", ylabel="acurácia", ylim=(0, 1.05))
    ax[0].legend()
    cores_delta = np.where(validacao_robusta_df["delta_acuracia"] > 0, "#6f42c1", "#6c757d")
    ax[1].bar(validacao_robusta_df["execucao"].astype(str), validacao_robusta_df["delta_acuracia"], color=cores_delta)
    ax[1].axhline(0, color="black", lw=1)
    ax[1].set(title="Efeito pareado QML − RBF", xlabel="avaliação externa", ylabel="Δ acurácia")
    plt.tight_layout()
    plt.show()

    display(Markdown(f'''
### Parecer da validação aninhada repetida

- **Δ médio de acurácia:** {resumo_validacao_robusta["media_delta_acuracia"]:+.3f}
- **IC 95% bootstrap da média:** [{baixo_rob:+.3f}, {alto_rob:+.3f}]
- **Vitórias/empates em 12 avaliações:** {resumo_validacao_robusta["vitorias_qml"]}/{resumo_validacao_robusta["empates"]}
- **Parecer:** **{parecer_robusto}**

Mesmo um intervalo positivo não demonstra vantagem computacional: ainda faltam teste externo, custo de escala e hardware.
'''))

    assert len(validacao_robusta_df) == N_AVALIACOES_EXTERNAS == 12
    assert validacao_robusta_df["seed"].nunique() == N_AVALIACOES_EXTERNAS
    assert (validacao_robusta_df["n_teste"] >= 30).all()
    assert validacao_robusta_df["C_rbf"].isin(GRADE_C).all()
    assert validacao_robusta_df["C_quantico"].isin(GRADE_C).all()
    assert np.isfinite(validacao_robusta_df.select_dtypes(include="number")).all().all()
    print("✅ Doze comparações externas concluídas sem usar o teste para escolher hiperparâmetros.")
""")

md(r"""
## 7.2.1 — Inferência estatística compatível com folds dependentes

Folds repetidos compartilham observações; tratá-los como doze experimentos independentes subestima a incerteza. O teste primário usa a correção de Nadeau–Bengio para a variância da diferença entre algoritmos. Como análises de sensibilidade, o notebook inclui permutação exata de sinais, tamanho de efeito pareado, teste de equivalência e ajuste de Holm.

### Regras de interpretação

- **Superioridade:** IC corrigido acima de zero e teste primário unilateral significativo.
- **Equivalência prática:** TOST significativo dentro da margem pré-especificada de ±0,02 em acurácia balanceada.
- **Inconclusivo:** nenhum dos critérios anteriores.
- **Inferioridade:** IC corrigido abaixo de zero.

Não selecione a regra depois de observar os resultados: margem, alfa e desfecho primário já foram congelados no Módulo 0.
""")

code(r"""
# @title 7.2.1 — Teste corrigido, equivalência, permutação e Holm
from itertools import product
from scipy.stats import t as distribuicao_t

ALPHA = PROTOCOLO_PRE_REGISTRADO["alpha"]
MARGEM_EQUIVALENCIA_BAC = PROTOCOLO_PRE_REGISTRADO["margem_equivalencia_bac"]
analise_estatistica_paper = {}
tabela_testes_paper = pd.DataFrame()

def teste_nadeau_bengio(diferencas, proporcao_teste_treino, alternativa="two-sided"):
    d = np.asarray(diferencas, dtype=float)
    n = len(d)
    media = float(d.mean())
    variancia = float(d.var(ddof=1))
    erro_padrao = float(np.sqrt((1 / n + proporcao_teste_treino) * variancia))
    gl = n - 1
    if erro_padrao == 0:
        estatistica = np.inf if media > 0 else (-np.inf if media < 0 else 0.0)
    else:
        estatistica = media / erro_padrao
    if alternativa == "greater":
        p = float(distribuicao_t.sf(estatistica, gl))
    elif alternativa == "less":
        p = float(distribuicao_t.cdf(estatistica, gl))
    else:
        p = float(2 * distribuicao_t.sf(abs(estatistica), gl))
    critico = float(distribuicao_t.ppf(1 - ALPHA / 2, gl))
    ic = [media - critico * erro_padrao, media + critico * erro_padrao]
    return {"media": media, "se_corrigido": erro_padrao, "t": float(estatistica), "gl": gl, "p": p, "ic95": ic}

def teste_permutacao_sinais_exato(diferencas):
    d = np.asarray(diferencas, dtype=float)
    assert len(d) <= 20, "Use Monte Carlo para mais de 20 diferenças."
    sinais = np.asarray(list(product([-1.0, 1.0], repeat=len(d))))
    medias_nulas = (sinais * d).mean(axis=1)
    observado = abs(d.mean())
    return float(np.mean(np.abs(medias_nulas) >= observado - 1e-15))

def p_tost_corrigido(diferencas, margem, proporcao_teste_treino):
    base = teste_nadeau_bengio(diferencas, proporcao_teste_treino)
    media, se, gl = base["media"], base["se_corrigido"], base["gl"]
    if se == 0:
        return 0.0 if abs(media) < margem else 1.0
    t_limite_inferior = (media + margem) / se
    t_limite_superior = (media - margem) / se
    p_inferior = distribuicao_t.sf(t_limite_inferior, gl)
    p_superior = distribuicao_t.cdf(t_limite_superior, gl)
    return float(max(p_inferior, p_superior))

def ajustar_holm(p_valores):
    p = np.asarray(p_valores, dtype=float)
    ordem = np.argsort(p)
    ajustados = np.empty_like(p)
    acumulado = 0.0
    m = len(p)
    for posicao, indice in enumerate(ordem):
        candidato = min(1.0, (m - posicao) * p[indice])
        acumulado = max(acumulado, candidato)
        ajustados[indice] = acumulado
    return ajustados

if validacao_robusta_df.empty:
    print("⏭️ Inferência do paper aguardando a execução da célula 7.2.")
else:
    proporcao_teste_treino = float(
        validacao_robusta_df["n_teste"].iloc[0] / validacao_robusta_df["n_treino"].iloc[0]
    )
    delta_primario = validacao_robusta_df["delta_acuracia_balanceada"].to_numpy()
    teste_primario = teste_nadeau_bengio(
        delta_primario, proporcao_teste_treino, alternativa="greater"
    )
    teste_bilateral = teste_nadeau_bengio(delta_primario, proporcao_teste_treino)
    p_permutacao = teste_permutacao_sinais_exato(delta_primario)
    p_equivalencia = p_tost_corrigido(
        delta_primario, MARGEM_EQUIVALENCIA_BAC, proporcao_teste_treino
    )
    desvio_pareado = float(np.std(delta_primario, ddof=1))
    tamanho_efeito_dz = float(delta_primario.mean() / desvio_pareado) if desvio_pareado > 0 else np.nan

    metricas_secundarias = ["delta_acuracia", "delta_f1"]
    testes_secundarios = [
        teste_nadeau_bengio(validacao_robusta_df[m], proporcao_teste_treino)
        for m in metricas_secundarias
    ]
    p_holm = ajustar_holm([teste["p"] for teste in testes_secundarios])
    tabela_testes_paper = pd.DataFrame([
        {
            "desfecho": "Δ acurácia balanceada (primário)",
            "media": teste_bilateral["media"],
            "ic95_inferior": teste_bilateral["ic95"][0],
            "ic95_superior": teste_bilateral["ic95"][1],
            "p_corrigido": teste_primario["p"],
            "p_holm": teste_primario["p"],
        },
        *[
            {
                "desfecho": metrica,
                "media": teste["media"],
                "ic95_inferior": teste["ic95"][0],
                "ic95_superior": teste["ic95"][1],
                "p_corrigido": teste["p"],
                "p_holm": float(p_ajustado),
            }
            for metrica, teste, p_ajustado in zip(
                metricas_secundarias, testes_secundarios, p_holm
            )
        ],
    ])

    ic_baixo, ic_alto = teste_bilateral["ic95"]
    if ic_baixo > 0 and teste_primario["p"] < ALPHA:
        classificacao_inferencia = "superioridade estatística neste protocolo"
    elif ic_alto < 0:
        classificacao_inferencia = "inferioridade estatística neste protocolo"
    elif p_equivalencia < ALPHA:
        classificacao_inferencia = "equivalência prática dentro da margem pré-especificada"
    else:
        classificacao_inferencia = "inconclusivo"

    analise_estatistica_paper = {
        "desfecho_primario": "delta_acuracia_balanceada",
        "teste": "Nadeau-Bengio corrigido, unilateral",
        "media_delta_bac": float(delta_primario.mean()),
        "ic95_corrigido_bilateral": [float(ic_baixo), float(ic_alto)],
        "p_primario_corrigido": teste_primario["p"],
        "p_permutacao_sinais_sensibilidade": p_permutacao,
        "p_tost_equivalencia": p_equivalencia,
        "margem_equivalencia": MARGEM_EQUIVALENCIA_BAC,
        "tamanho_efeito_dz": tamanho_efeito_dz,
        "classificacao": classificacao_inferencia,
        "nota_dependencia": "erro-padrão inclui correção n_teste/n_treino",
    }
    portao_evidencia["inferencia_paper"] = analise_estatistica_paper
    portao_evidencia["status_evidencia"] = classificacao_inferencia

    display(tabela_testes_paper.style.format({
        "media": "{:+.4f}",
        "ic95_inferior": "{:+.4f}",
        "ic95_superior": "{:+.4f}",
        "p_corrigido": "{:.4g}",
        "p_holm": "{:.4g}",
    }))
    display(Markdown(f'''
### Decisão estatística pré-especificada

- **Desfecho primário:** Δ acurácia balanceada QML − RBF
- **Estimativa:** {delta_primario.mean():+.4f}
- **IC 95% corrigido:** [{ic_baixo:+.4f}, {ic_alto:+.4f}]
- **p unilateral corrigido:** {teste_primario["p"]:.4g}
- **p de equivalência TOST:** {p_equivalencia:.4g}
- **Permutação exata de sinais (sensibilidade):** {p_permutacao:.4g}
- **Tamanho de efeito pareado dz:** {tamanho_efeito_dz:+.3f}
- **Conclusão limitada:** **{classificacao_inferencia}**
'''))

    assert tabela_testes_paper["p_holm"].between(0, 1).all()
    assert 0 <= p_permutacao <= 1 and 0 <= p_equivalencia <= 1
    assert PROTOCOLO_PRE_REGISTRADO["desfecho_primario"] == "delta_acuracia_balanceada"
    print("✅ Inferência corrigida e análises de sensibilidade concluídas.")
""")

md(r"""
## 7.3 — Escada de validade: ideal → shots → ruído → QPU

Uma aplicação não deve saltar diretamente do statevector ideal para uma conclusão sobre hardware. A escada abaixo isola quatro fontes de perda:

| Nível | O que muda | Pergunta respondida |
|---:|---|---|
| 0 | fidelidade exata por statevector | a geometria ideal é útil? |
| 1 | shots finitos | a geometria tolera amostragem? |
| 2 | portas e leitura ruidosas no Aer | o circuito tolera um modelo NISQ controlado? |
| 3 | pares-âncora em QPU | parte da geometria sobrevive no dispositivo atual? |

O nível 3 está no Módulo 8 e permanece desativado por padrão porque envia jobs remotos. A classificação completa só deve ir à QPU depois que os pares-âncora mostrarem fidelidade geométrica aceitável.
""")

code(r"""
# @title 7.3.1 — Níveis 0 e 1: fidelidade exata versus shots
algorithm_globals.random_seed = SEED

inicio_exato = time.perf_counter()
kernel_exato = FidelityStatevectorKernel(
    feature_map=feature_map,
    shots=None,
    enforce_psd=True,
)
K_treino_exato = kernel_exato.evaluate(X_treino)
K_teste_exato = kernel_exato.evaluate(X_teste, X_treino)
tempo_exato = time.perf_counter() - inicio_exato

modelo_exato = SVC(kernel="precomputed", C=1.0).fit(K_treino_exato, y_treino)
pred_exato = modelo_exato.predict(K_teste_exato)

def posto_efetivo_matriz(K):
    eig = np.clip(np.linalg.eigvalsh((K + K.T) / 2), 0.0, None)
    pesos = eig / eig.sum()
    pesos = pesos[pesos > 0]
    return float(np.exp(-np.sum(pesos * np.log(pesos))))

def alinhamento_kernel(K, y):
    y_local = 2 * np.asarray(y) - 1
    alvo = np.outer(y_local, y_local)
    return float(np.sum(K * alvo) / (np.linalg.norm(K, "fro") * np.linalg.norm(alvo, "fro")))

def erro_frobenius_relativo(K_ref, K_obs):
    return float(np.linalg.norm(K_obs - K_ref, "fro") / np.linalg.norm(K_ref, "fro"))

linhas_escada = [
    {
        "nivel": "0 · statevector exato",
        "acuracia": accuracy_score(y_teste, pred_exato),
        "f1": f1_score(y_teste, pred_exato),
        "erro_geometrico_relativo": 0.0,
        "alinhamento": alinhamento_kernel(K_treino_exato, y_treino),
        "posto_efetivo": posto_efetivo_matriz(K_treino_exato),
        "tempo_s": tempo_exato,
    },
    {
        "nivel": f"1 · {SHOTS} shots",
        "acuracia": accuracy_score(y_teste, pred_qk),
        "f1": f1_score(y_teste, pred_qk),
        "erro_geometrico_relativo": erro_frobenius_relativo(K_treino_exato, K_treino),
        "alinhamento": alinhamento_kernel(K_treino, y_treino),
        "posto_efetivo": posto_efetivo_matriz(K_treino),
        "tempo_s": tempo_kernel,
    },
]
escada_kernel_df = pd.DataFrame(linhas_escada)
display(escada_kernel_df.style.format({
    "acuracia": "{:.3f}",
    "f1": "{:.3f}",
    "erro_geometrico_relativo": "{:.3f}",
    "alinhamento": "{:.3f}",
    "posto_efetivo": "{:.2f}",
    "tempo_s": "{:.2f}",
}))

assert np.allclose(np.diag(K_treino_exato), 1.0, atol=1e-10)
assert np.min(np.linalg.eigvalsh(K_treino_exato)) >= -1e-10
assert escada_kernel_df["nivel"].nunique() == 2
print("✅ Referência ideal criada; a degradação por shots agora é mensurável.")
""")

code(r"""
# @title 7.3.2 — Nível 2: kernel sob ruído de portas e leitura no Aer {display-mode: "form"}
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, ReadoutError, depolarizing_error

ERRO_1Q = 0.001  # @param {type:"number"}
ERRO_2Q = 0.010  # @param {type:"number"}
ERRO_LEITURA = 0.020  # @param {type:"number"}

K_treino_ruidoso = None
K_teste_ruidoso = None
resultado_ruido = {}

def circuito_sobreposicao(x, y, mapa):
    parametros = list(mapa.parameters)
    ux = mapa.assign_parameters(dict(zip(parametros, np.asarray(x, dtype=float))))
    uy = mapa.assign_parameters(dict(zip(parametros, np.asarray(y, dtype=float))))
    circuito = QuantumCircuit(mapa.num_qubits)
    circuito.compose(ux, inplace=True)
    circuito.compose(uy.inverse(), inplace=True)
    circuito.measure_all()
    return circuito

def avaliar_kernel_aer(Xa, Xb, mapa, simulador, shots, seed, simetrico=False):
    Xa, Xb = np.asarray(Xa), np.asarray(Xb)
    matriz = np.zeros((len(Xa), len(Xb)), dtype=float)
    pares, circuitos = [], []

    if simetrico:
        assert len(Xa) == len(Xb) and np.allclose(Xa, Xb)
        np.fill_diagonal(matriz, 1.0)
        indices = ((i, j) for i in range(len(Xa)) for j in range(i + 1, len(Xb)))
    else:
        indices = ((i, j) for i in range(len(Xa)) for j in range(len(Xb)))

    for i, j in indices:
        pares.append((i, j))
        circuitos.append(circuito_sobreposicao(Xa[i], Xb[j], mapa))

    circuitos_isa = transpile(
        circuitos,
        simulador,
        optimization_level=1,
        seed_transpiler=seed,
    )
    resultado = simulador.run(
        circuitos_isa,
        shots=shots,
        seed_simulator=seed,
    ).result()
    lista_counts = resultado.get_counts()
    if isinstance(lista_counts, dict):
        lista_counts = [lista_counts]

    zero = "0" * mapa.num_qubits
    for (i, j), counts in zip(pares, lista_counts):
        fidelidade_obs = counts.get(zero, 0) / shots
        matriz[i, j] = fidelidade_obs
        if simetrico:
            matriz[j, i] = fidelidade_obs
    return matriz

def projetar_psd(K):
    Ksim = (K + K.T) / 2
    valores, vetores = np.linalg.eigh(Ksim)
    return (vetores * np.clip(valores, 0.0, None)) @ vetores.T

if not EXECUTAR_ESCADA_RUIDO:
    print("⏭️ Aer ruidoso preparado, mas não executado.")
    print("Ative EXECUTAR_ESCADA_RUIDO na célula 0.1 para materializar o nível 2.")
else:
    assert 0 <= ERRO_1Q < 1 and 0 <= ERRO_2Q < 1 and 0 <= ERRO_LEITURA < 0.5
    modelo_ruido = NoiseModel()
    modelo_ruido.add_all_qubit_quantum_error(
        depolarizing_error(ERRO_1Q, 1), ["rz", "sx", "x"]
    )
    modelo_ruido.add_all_qubit_quantum_error(
        depolarizing_error(ERRO_2Q, 2), ["cx"]
    )
    modelo_ruido.add_all_qubit_readout_error(
        ReadoutError([
            [1 - ERRO_LEITURA, ERRO_LEITURA],
            [ERRO_LEITURA, 1 - ERRO_LEITURA],
        ])
    )
    simulador_ruidoso = AerSimulator(noise_model=modelo_ruido)

    inicio_ruido = time.perf_counter()
    K_treino_ruidoso_bruto = avaliar_kernel_aer(
        X_treino, X_treino, feature_map, simulador_ruidoso, SHOTS, SEED, simetrico=True
    )
    K_treino_ruidoso = projetar_psd(K_treino_ruidoso_bruto)
    K_teste_ruidoso = avaliar_kernel_aer(
        X_teste, X_treino, feature_map, simulador_ruidoso, SHOTS, SEED, simetrico=False
    )
    tempo_ruido = time.perf_counter() - inicio_ruido

    modelo_qk_ruidoso = SVC(kernel="precomputed", C=1.0).fit(K_treino_ruidoso, y_treino)
    pred_qk_ruidoso = modelo_qk_ruidoso.predict(K_teste_ruidoso)
    resultado_ruido = {
        "nivel": "2 · Aer com ruído",
        "acuracia": accuracy_score(y_teste, pred_qk_ruidoso),
        "f1": f1_score(y_teste, pred_qk_ruidoso),
        "erro_geometrico_relativo": erro_frobenius_relativo(K_treino_exato, K_treino_ruidoso),
        "alinhamento": alinhamento_kernel(K_treino_ruidoso, y_treino),
        "posto_efetivo": posto_efetivo_matriz(K_treino_ruidoso),
        "tempo_s": tempo_ruido,
        "erro_1q": ERRO_1Q,
        "erro_2q": ERRO_2Q,
        "erro_leitura": ERRO_LEITURA,
    }
    escada_kernel_df = pd.concat(
        [escada_kernel_df, pd.DataFrame([resultado_ruido])], ignore_index=True
    )
    display(escada_kernel_df.style.format({
        "acuracia": "{:.3f}",
        "f1": "{:.3f}",
        "erro_geometrico_relativo": "{:.3f}",
        "alinhamento": "{:.3f}",
        "posto_efetivo": "{:.2f}",
        "tempo_s": "{:.2f}",
    }))

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    sns.barplot(data=escada_kernel_df, x="nivel", y="acuracia", ax=ax[0], color="#6f42c1")
    sns.barplot(data=escada_kernel_df, x="nivel", y="erro_geometrico_relativo", ax=ax[1], color="#d97706")
    ax[0].set_ylim(0, 1.05)
    ax[0].set_title("Desempenho ao descer a escada")
    ax[1].set_title("Deformação versus kernel ideal")
    for eixo in ax:
        eixo.tick_params(axis="x", rotation=20)
    plt.tight_layout()
    plt.show()

    assert K_treino_ruidoso.shape == K_treino_exato.shape
    assert np.max(np.abs(K_treino_ruidoso - K_treino_ruidoso.T)) < 1e-10
    assert np.min(np.linalg.eigvalsh(K_treino_ruidoso)) >= -1e-8
    print("✅ Nível 2 concluído: perda geométrica e perda preditiva separadas.")
""")

md(r"""
## 7.4 — Aplicações e teste do gap mecanístico

O paper não deve se apoiar apenas em `make_moons`. A suíte abaixo acrescenta três conjuntos públicos do `scikit-learn` e testa uma hipótese mais informativa do que um simples placar: **a geometria que sobrevive aos shots está associada ao efeito preditivo do QML?**

| Aplicação | Papel no estudo | Desfecho | Cuidado de interpretação |
|---|---|---|---|
| `make_moons` | controle sintético não linear | classe geométrica | não representa mundo real |
| Iris binária | classificação biológica simples | espécie | baixa complexidade |
| Wine binário | composição físico-química | classe de vinho | apenas duas das três classes |
| Breast Cancer Wisconsin | teste tabular biomédico | rótulo diagnóstico histórico | **não usar clinicamente** |

Todas as bases são reduzidas para dois componentes **dentro de cada fold de treino**: imputação → padronização → PCA → escala angular. O teste externo nunca participa do ajuste. O limite de 160 observações controla o custo quadrático e deve ser reportado como limitação de validade externa.

### Gap científico candidato

Trabalhos recentes já estudam baselines fortes, espectro, ruído e hardware. O ponto ainda testável aqui é a utilidade de um fluxo integrado de **sobrevivência geométrica + inferência corrigida + custo + regra de progressão**. A formulação deve permanecer “contribuição candidata” até a revisão sistemática final.
""")

code(r"""
# @title 7.4 — Suíte multibase para paper (opcional) {display-mode: "form"}
from sklearn.datasets import load_breast_cancer, load_iris, load_wine
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from scipy.stats import spearmanr

MAX_AMOSTRAS_POR_BASE = 160
resultados_aplicacoes_df = pd.DataFrame()
analise_mecanistica_aplicacoes = {}

def limitar_amostra_estratificada(X, y, maximo, seed):
    X, y = np.asarray(X), np.asarray(y)
    if len(y) <= maximo:
        return X, y
    idx, _ = train_test_split(
        np.arange(len(y)),
        train_size=maximo,
        stratify=y,
        random_state=seed,
    )
    return X[idx], y[idx]

def bases_aplicacao():
    iris = load_iris()
    mascara_iris = iris.target < 2
    vinho = load_wine()
    mascara_vinho = vinho.target < 2
    cancer = load_breast_cancer()
    return {
        "make_moons": (X_total, y_total),
        "iris_binaria": (iris.data[mascara_iris], iris.target[mascara_iris]),
        "wine_binario": (vinho.data[mascara_vinho], vinho.target[mascara_vinho]),
        "breast_cancer_metodologico": (cancer.data, cancer.target),
    }

if not EXECUTAR_SUITE_APLICACOES:
    print("⏭️ Suíte multibase preparada, mas não executada.")
    print("Ative EXECUTAR_SUITE_APLICACOES na célula 0.1 para gerar a Tabela de Aplicações.")
else:
    linhas_aplicacoes = []
    for nome_base, (X_base, y_base) in bases_aplicacao().items():
        X_base, y_base = limitar_amostra_estratificada(
            X_base, y_base, MAX_AMOSTRAS_POR_BASE, SEED
        )
        cv_base = StratifiedKFold(n_splits=4, shuffle=True, random_state=SEED)

        for fold_base, (idx_tr, idx_te) in enumerate(cv_base.split(X_base, y_base), start=1):
            Xb_tr_raw, Xb_te_raw = X_base[idx_tr], X_base[idx_te]
            yb_tr, yb_te = y_base[idx_tr], y_base[idx_te]
            assert set(idx_tr).isdisjoint(set(idx_te))

            preprocessador = Pipeline([
                ("imputador", SimpleImputer(strategy="median")),
                ("padronizador", StandardScaler()),
                ("pca", PCA(n_components=2, random_state=SEED)),
                ("angulo", MinMaxScaler((0, np.pi))),
            ])
            Xb_tr = preprocessador.fit_transform(Xb_tr_raw)
            Xb_te = preprocessador.transform(Xb_te_raw)

            cv_interna_base = StratifiedKFold(
                n_splits=3, shuffle=True, random_state=SEED + fold_base
            )
            rbf_base = GridSearchCV(
                SVC(kernel="rbf"),
                {"C": GRADE_C, "gamma": GRADE_GAMMA_RBF},
                scoring="balanced_accuracy",
                cv=cv_interna_base,
                n_jobs=-1,
            ).fit(Xb_tr, yb_tr)
            pred_rbf_base = rbf_base.predict(Xb_te)

            algorithm_globals.random_seed = SEED + fold_base
            qk_exato_base = FidelityStatevectorKernel(feature_map=feature_map, shots=None)
            qk_shots_base = FidelityStatevectorKernel(
                feature_map=feature_map, shots=SHOTS, enforce_psd=True
            )
            Kb_tr_exato = qk_exato_base.evaluate(Xb_tr)
            t0_base = time.perf_counter()
            Kb_tr = qk_shots_base.evaluate(Xb_tr)
            Kb_te = qk_shots_base.evaluate(Xb_te, Xb_tr)
            tempo_base = time.perf_counter() - t0_base

            qml_base = GridSearchCV(
                SVC(kernel="precomputed"),
                {"C": GRADE_C},
                scoring="balanced_accuracy",
                cv=cv_interna_base,
                n_jobs=1,
            ).fit(Kb_tr, yb_tr)
            pred_qml_base = qml_base.predict(Kb_te)

            bac_rbf_base = balanced_accuracy_score(yb_te, pred_rbf_base)
            bac_qml_base = balanced_accuracy_score(yb_te, pred_qml_base)
            erro_geo_base = erro_frobenius_relativo(Kb_tr_exato, Kb_tr)
            sobrevivencia_geometrica = float(np.clip(1 - erro_geo_base, 0, 1))

            linhas_aplicacoes.append({
                "base": nome_base,
                "fold": fold_base,
                "n_treino": len(yb_tr),
                "n_teste": len(yb_te),
                "C_rbf": rbf_base.best_params_["C"],
                "C_qml": qml_base.best_params_["C"],
                "bac_rbf": bac_rbf_base,
                "bac_qml": bac_qml_base,
                "delta_bac": bac_qml_base - bac_rbf_base,
                "sobrevivencia_geometrica": sobrevivencia_geometrica,
                "erro_frobenius_relativo": erro_geo_base,
                "alinhamento": alinhamento_kernel(Kb_tr, yb_tr),
                "posto_efetivo_relativo": posto_efetivo_matriz(Kb_tr) / len(Kb_tr),
                "tempo_kernel_s": tempo_base,
            })
            print(
                f"{nome_base} | fold {fold_base}/4 | "
                f"ΔBAC={bac_qml_base - bac_rbf_base:+.3f}"
            )

    resultados_aplicacoes_df = pd.DataFrame(linhas_aplicacoes)
    rho_sobrevivencia, p_sobrevivencia = spearmanr(
        resultados_aplicacoes_df["sobrevivencia_geometrica"],
        resultados_aplicacoes_df["delta_bac"],
    )
    rho_alinhamento, p_alinhamento = spearmanr(
        resultados_aplicacoes_df["alinhamento"],
        resultados_aplicacoes_df["delta_bac"],
    )
    analise_mecanistica_aplicacoes = {
        "n_bases": int(resultados_aplicacoes_df["base"].nunique()),
        "n_folds": int(len(resultados_aplicacoes_df)),
        "spearman_sobrevivencia_delta_bac": float(rho_sobrevivencia),
        "p_exploratorio_sobrevivencia": float(p_sobrevivencia),
        "spearman_alinhamento_delta_bac": float(rho_alinhamento),
        "p_exploratorio_alinhamento": float(p_alinhamento),
        "status": "exploratório; folds não são observações totalmente independentes",
    }

    resumo_bases = resultados_aplicacoes_df.groupby("base", as_index=False).agg(
        bac_rbf_media=("bac_rbf", "mean"),
        bac_qml_media=("bac_qml", "mean"),
        delta_bac_media=("delta_bac", "mean"),
        sobrevivencia_media=("sobrevivencia_geometrica", "mean"),
        tempo_kernel_medio_s=("tempo_kernel_s", "mean"),
    )
    display(resumo_bases.style.format({
        "bac_rbf_media": "{:.3f}",
        "bac_qml_media": "{:.3f}",
        "delta_bac_media": "{:+.3f}",
        "sobrevivencia_media": "{:.3f}",
        "tempo_kernel_medio_s": "{:.2f}",
    }))

    sns.scatterplot(
        data=resultados_aplicacoes_df,
        x="sobrevivencia_geometrica",
        y="delta_bac",
        hue="base",
        style="base",
        s=90,
    )
    plt.axhline(0, color="black", lw=1)
    plt.title(f"Hipótese H2 — sobrevivência geométrica × ΔBAC (ρ={rho_sobrevivencia:.2f})")
    plt.show()

    assert resultados_aplicacoes_df["base"].nunique() == 4
    assert len(resultados_aplicacoes_df) == 16
    assert resultados_aplicacoes_df["sobrevivencia_geometrica"].between(0, 1).all()
    print("✅ Quatro aplicações avaliadas; associação mecanística marcada como exploratória.")
""")

md(r"""
## 7.4.1 — Laboratório progressivo: flor → imagem biomédica → geometria controlada

Este laboratório transforma a comparação em uma sequência didática e auditável:

| Etapa | Pergunta simples | Papel científico |
|---|---|---|
| **Iris Setosa × Versicolor** | o pipeline separa duas flores conhecidas? | controle de sanidade em dados tabulares simples |
| **BreastMNIST** | a representação preserva algum sinal em imagens de ultrassom? | teste metodológico em imagem biomédica de baixa resolução |
| **`make_moons`** | o método acompanha uma fronteira curva? | controle sintético da geometria não linear |

**Analogia rigorosa.** Imagine regular um microscópio. O treino ensina a focalizar; a validação escolhe a lente e a intensidade do ruído; o teste é uma lâmina lacrada, aberta uma única vez. Regular o microscópio olhando a lâmina final seria vazamento de teste.

O BreastMNIST combina `normal + benigno` contra `maligno`, preserva o split oficial e é usado **somente para pesquisa metodológica**. O benchmark não é dispositivo médico, não estima risco individual e não sustenta decisão clínica. Fonte: [MedMNIST v2](https://doi.org/10.1038/s41597-022-01721-8).

### Regra de busca sem otimismo

1. ajuste `imputação → padronização → PCA(2) → escala angular` apenas no treino;
2. escolha perfil de ruído e `C` somente pela acurácia balanceada de validação;
3. em empate, prefira menor deformação geométrica e depois menor carga de ruído;
4. congele a escolha e abra o teste uma vez;
5. compare com RBF e kernel quântico exato. Um ganho aparente por ruído é **regularização exploratória**, nunca evidência automática de vantagem quântica.
""")

code(r"""
# @title 7.4.1 — Preparar e visualizar as três aplicações {display-mode: "form"}
from sklearn.datasets import load_iris, make_moons
from sklearn.metrics import balanced_accuracy_score
from medmnist import BreastMNIST

EXECUTAR_LAB_GUIADO = False  # @param {type:"boolean"}
MAX_TREINO_LAB = 24  # @param {type:"integer"}
MAX_VALIDACAO_LAB = 12  # @param {type:"integer"}
MAX_TESTE_LAB = 12  # @param {type:"integer"}
SHOTS_BUSCA_RUIDO = 512  # @param {type:"integer"}

def subamostra_estratificada(X, y, n, seed):
    X, y = np.asarray(X), np.asarray(y, dtype=int).ravel()
    if len(y) <= n:
        return X, y
    idx, _ = train_test_split(
        np.arange(len(y)), train_size=n, stratify=y, random_state=seed
    )
    return X[idx], y[idx]

def dividir_desenvolvimento_teste(X, y, seed):
    X_dev, X_te, y_dev, y_te = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=seed
    )
    X_tr, X_va, y_tr, y_va = train_test_split(
        X_dev, y_dev, test_size=1/3, stratify=y_dev, random_state=seed + 1
    )
    return X_tr, X_va, X_te, y_tr, y_va, y_te

def preparar_angular(X_tr_raw, X_va_raw, X_te_raw):
    preparo = Pipeline([
        ("imputador", SimpleImputer(strategy="median")),
        ("padronizador", StandardScaler()),
        ("pca", PCA(n_components=2, random_state=SEED)),
        ("angulo", MinMaxScaler((0, np.pi))),
    ])
    X_tr = preparo.fit_transform(X_tr_raw)
    return X_tr, preparo.transform(X_va_raw), preparo.transform(X_te_raw), preparo

aplicacoes_guiadas = {}
metadados_aplicacoes_guiadas = {}

if not EXECUTAR_LAB_GUIADO:
    print("⏭️ Laboratório guiado preparado, mas não executado.")
else:
    # 1) Iris: Setosa (0) versus Versicolor (1).
    iris_lab = load_iris()
    m_iris = iris_lab.target < 2
    split_iris = dividir_desenvolvimento_teste(
        iris_lab.data[m_iris], iris_lab.target[m_iris], SEED
    )
    aplicacoes_guiadas["iris_setosa_versicolor"] = split_iris
    metadados_aplicacoes_guiadas["iris_setosa_versicolor"] = {
        "tipo": "tabular", "classes": ["setosa", "versicolor"], "uso_clinico": False
    }

    # 2) BreastMNIST: usa os splits oficiais; imagens 28x28 são achatadas antes do PCA.
    bm_tr = BreastMNIST(split="train", download=True, size=28)
    bm_va = BreastMNIST(split="val", download=True, size=28)
    bm_te = BreastMNIST(split="test", download=True, size=28)
    Xbm_tr, ybm_tr = subamostra_estratificada(
        np.asarray(bm_tr.imgs).reshape(len(bm_tr), -1), bm_tr.labels, MAX_TREINO_LAB, SEED
    )
    Xbm_va, ybm_va = subamostra_estratificada(
        np.asarray(bm_va.imgs).reshape(len(bm_va), -1), bm_va.labels, MAX_VALIDACAO_LAB, SEED + 1
    )
    Xbm_te, ybm_te = subamostra_estratificada(
        np.asarray(bm_te.imgs).reshape(len(bm_te), -1), bm_te.labels, MAX_TESTE_LAB, SEED + 2
    )
    aplicacoes_guiadas["breastmnist_imagens"] = (
        Xbm_tr, Xbm_va, Xbm_te, ybm_tr, ybm_va, ybm_te
    )
    metadados_aplicacoes_guiadas["breastmnist_imagens"] = {
        "tipo": "imagem_ultrassom_28x28",
        "classes": {"0": "maligno", "1": "normal_ou_benigno"},
        "uso_clinico": False,
        "aviso": "benchmark metodológico; proibida interpretação clínica individual",
        "doi": "10.1038/s41597-022-01721-8",
    }

    # 3) Moons: fronteira não linear conhecida.
    Xm, ym = make_moons(n_samples=120, noise=0.18, random_state=SEED)
    aplicacoes_guiadas["make_moons"] = dividir_desenvolvimento_teste(Xm, ym, SEED + 10)
    metadados_aplicacoes_guiadas["make_moons"] = {
        "tipo": "sintetico", "classes": ["lua_0", "lua_1"], "uso_clinico": False
    }

    # Limites iguais para tornar o custo quadrático comparável entre aplicações.
    for nome, (Xtr, Xva, Xte, ytr, yva, yte) in list(aplicacoes_guiadas.items()):
        Xtr, ytr = subamostra_estratificada(Xtr, ytr, MAX_TREINO_LAB, SEED + 20)
        Xva, yva = subamostra_estratificada(Xva, yva, MAX_VALIDACAO_LAB, SEED + 21)
        Xte, yte = subamostra_estratificada(Xte, yte, MAX_TESTE_LAB, SEED + 22)
        aplicacoes_guiadas[nome] = (Xtr, Xva, Xte, ytr, yva, yte)

    fig, ax = plt.subplots(1, 3, figsize=(15, 4))
    Xi, _, _, yi, _, _ = aplicacoes_guiadas["iris_setosa_versicolor"]
    ax[0].scatter(Xi[:, 2], Xi[:, 3], c=yi, cmap="cool", edgecolor="white")
    ax[0].set(xlabel="comprimento da pétala", ylabel="largura da pétala", title="1 · Iris")
    for k in range(min(9, len(bm_tr.imgs))):
        linha, coluna = divmod(k, 3)
        mini = np.asarray(bm_tr.imgs[k]).squeeze()
        x0, x1 = coluna / 3, (coluna + 1) / 3
        y0, y1 = 1 - (linha + 1) / 3, 1 - linha / 3
        ax_in = ax[1].inset_axes([x0, y0, x1 - x0, y1 - y0])
        ax_in.imshow(mini, cmap="gray")
        ax_in.axis("off")
    ax[1].set_title("2 · BreastMNIST (amostras)")
    ax[1].axis("off")
    Xm0, _, _, ym0, _, _ = aplicacoes_guiadas["make_moons"]
    ax[2].scatter(Xm0[:, 0], Xm0[:, 1], c=ym0, cmap="cool", edgecolor="white")
    ax[2].set_title("3 · make_moons")
    plt.tight_layout()
    plt.show()

    assert set(aplicacoes_guiadas) == {
        "iris_setosa_versicolor", "breastmnist_imagens", "make_moons"
    }
    assert metadados_aplicacoes_guiadas["breastmnist_imagens"]["uso_clinico"] is False
    print("✅ Três aplicações prontas; BreastMNIST preserva o teste oficial e uso não clínico.")
""")

code(r"""
# @title 7.4.2 — Selecionar ruído na validação e abrir o teste uma vez {display-mode: "form"}
PERFIS_RUIDO = [
    {"perfil": "shots_sem_ruido", "erro_1q": 0.0, "erro_2q": 0.0, "erro_leitura": 0.0},
    {"perfil": "baixo", "erro_1q": 0.0005, "erro_2q": 0.005, "erro_leitura": 0.010},
    {"perfil": "moderado", "erro_1q": 0.0010, "erro_2q": 0.010, "erro_leitura": 0.020},
    {"perfil": "alto_2q", "erro_1q": 0.0010, "erro_2q": 0.030, "erro_leitura": 0.020},
    {"perfil": "leitura_alta", "erro_1q": 0.0010, "erro_2q": 0.010, "erro_leitura": 0.050},
]

def criar_simulador_ruido(perfil):
    modelo = NoiseModel()
    if perfil["erro_1q"] > 0:
        modelo.add_all_qubit_quantum_error(
            depolarizing_error(perfil["erro_1q"], 1), ["rz", "sx", "x"]
        )
    if perfil["erro_2q"] > 0:
        modelo.add_all_qubit_quantum_error(
            depolarizing_error(perfil["erro_2q"], 2), ["cx"]
        )
    if perfil["erro_leitura"] > 0:
        p = perfil["erro_leitura"]
        modelo.add_all_qubit_readout_error(ReadoutError([[1-p, p], [p, 1-p]]))
    return AerSimulator(noise_model=modelo)

busca_ruido_aplicacoes_df = pd.DataFrame()
parecer_aplicacoes_guiadas_df = pd.DataFrame()
parametros_ruido_selecionados = {}
contador_aberturas_teste = {}

if not EXECUTAR_LAB_GUIADO:
    print("⏭️ Busca de ruído não executada.")
else:
    linhas_busca, linhas_parecer = [], []
    for i_base, (nome, partes) in enumerate(aplicacoes_guiadas.items()):
        Xtr_raw, Xva_raw, Xte_raw, ytr, yva, yte = partes
        Xtr, Xva, Xte, _ = preparar_angular(Xtr_raw, Xva_raw, Xte_raw)

        # Referência exata; o teste ainda não participa de nenhuma escolha.
        qk_ideal = FidelityStatevectorKernel(feature_map=feature_map, shots=None)
        Ktr_ideal = qk_ideal.evaluate(Xtr)
        Kva_ideal = qk_ideal.evaluate(Xva, Xtr)

        candidatos_rbf = []
        for C in GRADE_C:
            for gamma in GRADE_GAMMA_RBF:
                modelo = SVC(kernel="rbf", C=C, gamma=gamma).fit(Xtr, ytr)
                candidatos_rbf.append((balanced_accuracy_score(yva, modelo.predict(Xva)), C, gamma))
        _, C_rbf, gamma_rbf = max(candidatos_rbf, key=lambda z: (z[0], -z[1]))

        candidatos_ideal = []
        for C in GRADE_C:
            modelo = SVC(kernel="precomputed", C=C).fit(Ktr_ideal, ytr)
            candidatos_ideal.append((balanced_accuracy_score(yva, modelo.predict(Kva_ideal)), C))
        _, C_ideal = max(candidatos_ideal, key=lambda z: (z[0], -z[1]))

        for i_perfil, perfil in enumerate(PERFIS_RUIDO):
            sim = criar_simulador_ruido(perfil)
            seed_local = SEED + 100 * i_base + i_perfil
            t0 = time.perf_counter()
            Ktr_bruto = avaliar_kernel_aer(
                Xtr, Xtr, feature_map, sim, SHOTS_BUSCA_RUIDO, seed_local, simetrico=True
            )
            Ktr = projetar_psd(Ktr_bruto)
            Kva = avaliar_kernel_aer(
                Xva, Xtr, feature_map, sim, SHOTS_BUSCA_RUIDO, seed_local, simetrico=False
            )
            erro_geo = erro_frobenius_relativo(Ktr_ideal, Ktr)
            for C in GRADE_C:
                modelo = SVC(kernel="precomputed", C=C).fit(Ktr, ytr)
                bac_va = balanced_accuracy_score(yva, modelo.predict(Kva))
                linhas_busca.append({
                    "aplicacao": nome, "perfil": perfil["perfil"], "C": C,
                    "bac_validacao": bac_va, "erro_geometrico_validacao": erro_geo,
                    "alinhamento_treino": alinhamento_kernel(Ktr, ytr),
                    "erro_1q": perfil["erro_1q"], "erro_2q": perfil["erro_2q"],
                    "erro_leitura": perfil["erro_leitura"],
                    "tempo_busca_s": time.perf_counter() - t0,
                    "conjunto_selecao": "validacao_exclusivamente",
                })

        busca_base = pd.DataFrame(linhas_busca).query("aplicacao == @nome").copy()
        busca_base["carga_ruido"] = (
            busca_base["erro_1q"] + busca_base["erro_2q"] + busca_base["erro_leitura"]
        )
        melhor = busca_base.sort_values(
            ["bac_validacao", "erro_geometrico_validacao", "carga_ruido", "C"],
            ascending=[False, True, True, True],
        ).iloc[0]
        perfil_escolhido = next(p for p in PERFIS_RUIDO if p["perfil"] == melhor["perfil"])
        parametros_ruido_selecionados[nome] = {
            **perfil_escolhido, "C": float(melhor["C"]),
            "criterio": "BAC_validacao; desempate por geometria e carga de ruido",
        }

        # Abertura única do teste, somente depois do congelamento acima.
        contador_aberturas_teste[nome] = contador_aberturas_teste.get(nome, 0) + 1
        Kte_ideal = qk_ideal.evaluate(Xte, Xtr)
        sim_final = criar_simulador_ruido(perfil_escolhido)
        Ktr_final = projetar_psd(avaliar_kernel_aer(
            Xtr, Xtr, feature_map, sim_final, SHOTS_BUSCA_RUIDO,
            SEED + 1000 + i_base, simetrico=True
        ))
        Kte_final = avaliar_kernel_aer(
            Xte, Xtr, feature_map, sim_final, SHOTS_BUSCA_RUIDO,
            SEED + 1000 + i_base, simetrico=False
        )
        pred_final = SVC(kernel="precomputed", C=float(melhor["C"])).fit(Ktr_final, ytr).predict(Kte_final)
        pred_ideal = SVC(kernel="precomputed", C=C_ideal).fit(Ktr_ideal, ytr).predict(Kte_ideal)
        pred_rbf = SVC(kernel="rbf", C=C_rbf, gamma=gamma_rbf).fit(Xtr, ytr).predict(Xte)
        bac_final = balanced_accuracy_score(yte, pred_final)
        bac_ideal = balanced_accuracy_score(yte, pred_ideal)
        bac_rbf = balanced_accuracy_score(yte, pred_rbf)
        delta = bac_final - bac_rbf
        sobrevivencia = float(np.clip(1 - erro_frobenius_relativo(Ktr_ideal, Ktr_final), 0, 1))
        if delta > 0.02 and sobrevivencia >= 0.85:
            decisao = "GO exploratorio para repeticao independente"
        elif delta < -0.02:
            decisao = "NO-GO; baseline classico favorecido"
        else:
            decisao = "equivalencia pratica ou resultado inconclusivo"
        if nome == "breastmnist_imagens":
            decisao += "; sem interpretacao clinica"
        linhas_parecer.append({
            "aplicacao": nome, "perfil_ruido_selecionado": melhor["perfil"],
            "C_selecionado": float(melhor["C"]),
            "bac_validacao_selecao": float(melhor["bac_validacao"]),
            "bac_teste_quantico_ruidoso": bac_final,
            "bac_teste_quantico_exato": bac_ideal, "bac_teste_rbf": bac_rbf,
            "delta_ruidoso_menos_rbf": delta,
            "sobrevivencia_geometrica": sobrevivencia,
            "aberturas_teste": contador_aberturas_teste[nome],
            "parecer": decisao,
        })

    busca_ruido_aplicacoes_df = pd.DataFrame(linhas_busca)
    parecer_aplicacoes_guiadas_df = pd.DataFrame(linhas_parecer)
    display(parecer_aplicacoes_guiadas_df.style.format({
        "bac_validacao_selecao": "{:.3f}", "bac_teste_quantico_ruidoso": "{:.3f}",
        "bac_teste_quantico_exato": "{:.3f}", "bac_teste_rbf": "{:.3f}",
        "delta_ruidoso_menos_rbf": "{:+.3f}", "sobrevivencia_geometrica": "{:.3f}",
    }))

    longo = parecer_aplicacoes_guiadas_df.melt(
        id_vars="aplicacao",
        value_vars=["bac_teste_rbf", "bac_teste_quantico_exato", "bac_teste_quantico_ruidoso"],
        var_name="modelo", value_name="BAC_teste",
    )
    fig, ax = plt.subplots(1, 2, figsize=(14, 4.5))
    sns.barplot(data=longo, x="aplicacao", y="BAC_teste", hue="modelo", ax=ax[0])
    ax[0].set_ylim(0, 1.05); ax[0].tick_params(axis="x", rotation=15)
    ax[0].set_title("Teste aberto uma vez após a seleção")
    sns.barplot(data=parecer_aplicacoes_guiadas_df, x="aplicacao",
                y="sobrevivencia_geometrica", hue="perfil_ruido_selecionado", ax=ax[1])
    ax[1].set_ylim(0, 1.05); ax[1].tick_params(axis="x", rotation=15)
    ax[1].set_title("Geometria preservada pelo perfil escolhido")
    plt.tight_layout(); plt.show()

    assert parecer_aplicacoes_guiadas_df["aplicacao"].nunique() == 3
    assert busca_ruido_aplicacoes_df["conjunto_selecao"].eq("validacao_exclusivamente").all()
    assert parecer_aplicacoes_guiadas_df["aberturas_teste"].eq(1).all()
    assert parecer_aplicacoes_guiadas_df.filter(like="bac_").apply(
        lambda s: s.between(0, 1).all()
    ).all()
    assert parecer_aplicacoes_guiadas_df.query(
        "aplicacao == 'breastmnist_imagens'"
    )["parecer"].str.contains("sem interpretacao clinica").all()
    print("✅ Seleção sem teste, abertura única e parecer auditável concluídos.")
""")

md(r"""
## 7.4.3 — Como escrever o parecer no artigo

- **Iris:** controle de sanidade; desempenho alto não demonstra escalabilidade.
- **BreastMNIST:** evidência metodológica em amostra reduzida e imagem comprimida para dois componentes; não há validade diagnóstica.
- **Moons:** teste de mecanismo geométrico; não há validade externa por ser sintético.
- **Ruído:** relate todos os perfis, inclusive resultados negativos. Um perfil ruidoso selecionado precisa ser repetido com novas seeds e confirmado sob CV aninhada antes de qualquer alegação.
- **QPU:** este laboratório é uma triagem. Pares-âncora só seguem ao hardware depois do OSF e dos portões estatístico, geométrico e de custo; o classificador QPU completo continua sendo a última etapa.
""")

md(r"""
## 7.4.4 — Suíte de baselines fortes e representações justas

Uma comparação publicável precisa responder a duas perguntas diferentes:

1. **Com a mesma representação de dois componentes**, o kernel quântico supera modelos clássicos?
2. **Sem a restrição de dois qubits**, quanto desempenho um pipeline clássico consegue preservar?

O primeiro contraste mede o efeito do kernel. O segundo mede o custo informacional da compressão. Para BreastMNIST, HOG resume bordas e texturas; ele não é um diagnóstico clínico nem substitui validação externa. Todos os modelos são definidos antes da abertura do teste.
""")

code(r"""
# @title 7.4.4 — Baselines fortes, HOG e teto clássico {display-mode: "form"}
from sklearn.base import clone
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import matthews_corrcoef, roc_auc_score
from skimage.feature import hog
from medmnist import PneumoniaMNIST

resultados_baselines_fortes_df = pd.DataFrame()
representacoes_paper = {}
aplicacoes_paper_avancado = dict(aplicacoes_guiadas)
INCLUIR_REPLICACAO_PNEUMONIAMNIST = True  # @param {type:"boolean"}

if EXECUTAR_LAB_GUIADO:
    # A suíte de paper usa o BreastMNIST oficial completo. O teto 24/12/12 vale
    # somente para a escada quântica ruidosa, cujo custo cresce quadraticamente.
    aplicacoes_paper_avancado["breastmnist_imagens"] = (
        np.asarray(bm_tr.imgs).reshape(len(bm_tr), -1),
        np.asarray(bm_va.imgs).reshape(len(bm_va), -1),
        np.asarray(bm_te.imgs).reshape(len(bm_te), -1),
        np.asarray(bm_tr.labels, dtype=int).ravel(),
        np.asarray(bm_va.labels, dtype=int).ravel(),
        np.asarray(bm_te.labels, dtype=int).ravel(),
    )
if EXECUTAR_PAPER_AVANCADO and INCLUIR_REPLICACAO_PNEUMONIAMNIST:
    pm_tr = PneumoniaMNIST(split="train", download=True, size=28)
    pm_va = PneumoniaMNIST(split="val", download=True, size=28)
    pm_te = PneumoniaMNIST(split="test", download=True, size=28)
    aplicacoes_paper_avancado["pneumoniamnist_replicacao"] = (
        np.asarray(pm_tr.imgs).reshape(len(pm_tr), -1),
        np.asarray(pm_va.imgs).reshape(len(pm_va), -1),
        np.asarray(pm_te.imgs).reshape(len(pm_te), -1),
        np.asarray(pm_tr.labels, dtype=int).ravel(),
        np.asarray(pm_va.labels, dtype=int).ravel(),
        np.asarray(pm_te.labels, dtype=int).ravel(),
    )
    metadados_aplicacoes_guiadas["pneumoniamnist_replicacao"] = {
        "tipo": "radiografia_torax_28x28", "uso_clinico": False,
        "aviso": "replicacao metodologica exploratoria; sem interpretacao clinica",
        "doi": "10.1038/s41597-022-01721-8",
    }

def extrair_hog_lote(X_flat):
    imagens = np.asarray(X_flat).reshape(-1, 28, 28)
    return np.asarray([
        hog(img, orientations=9, pixels_per_cell=(7, 7), cells_per_block=(2, 2),
            block_norm="L2-Hys", feature_vector=True)
        for img in imagens
    ])

def metricas_binarias_seguras(y, pred, score=None):
    saida = {
        "BAC": balanced_accuracy_score(y, pred),
        "F1": f1_score(y, pred),
        "MCC": matthews_corrcoef(y, pred),
    }
    saida["AUROC"] = roc_auc_score(y, score) if score is not None else np.nan
    return saida

if not EXECUTAR_PAPER_AVANCADO:
    print("⏭️ Suíte avançada preparada. Ative EXECUTAR_PAPER_AVANCADO após registrar o OSF.")
else:
    assert EXECUTAR_LAB_GUIADO, "Execute primeiro a preparação das aplicações em 7.4.1."
    linhas_baselines = []
    for nome, partes in aplicacoes_paper_avancado.items():
        Xtr_raw, Xva_raw, Xte_raw, ytr, yva, yte = partes
        conjuntos_repr = {"entrada_original": (Xtr_raw, Xva_raw, Xte_raw)}
        if nome in {"breastmnist_imagens", "pneumoniamnist_replicacao"}:
            conjuntos_repr["HOG"] = (
                extrair_hog_lote(Xtr_raw), extrair_hog_lote(Xva_raw), extrair_hog_lote(Xte_raw)
            )

        for representacao, (Rtr, Rva, Rte) in conjuntos_repr.items():
            Xtr2, Xva2, Xte2, preparo2 = preparar_angular(Rtr, Rva, Rte)
            representacoes_paper[(nome, representacao, "2D")] = (
                Xtr2, Xva2, Xte2, ytr, yva, yte
            )
            modelos = {
                "Dummy-estratificado": DummyClassifier(strategy="stratified", random_state=SEED),
                "Logistica": LogisticRegression(C=1.0, max_iter=3000, random_state=SEED),
                "SVM-linear": SVC(kernel="linear", C=1.0, probability=True, random_state=SEED),
                "SVM-RBF": SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=SEED),
                "RandomForest": RandomForestClassifier(
                    n_estimators=400, min_samples_leaf=2, class_weight="balanced",
                    random_state=SEED, n_jobs=-1
                ),
                "HistGradientBoosting": HistGradientBoostingClassifier(
                    max_iter=250, learning_rate=0.05, max_leaf_nodes=15, random_state=SEED
                ),
            }
            for nome_modelo, estimador in modelos.items():
                ajustado = clone(estimador).fit(Xtr2, ytr)
                pred_va, pred_te = ajustado.predict(Xva2), ajustado.predict(Xte2)
                score_va = ajustado.predict_proba(Xva2)[:, 1] if hasattr(ajustado, "predict_proba") else None
                score_te = ajustado.predict_proba(Xte2)[:, 1] if hasattr(ajustado, "predict_proba") else None
                mva, mte = metricas_binarias_seguras(yva, pred_va, score_va), metricas_binarias_seguras(yte, pred_te, score_te)
                linhas_baselines.append({
                    "aplicacao": nome, "representacao": representacao,
                    "dimensao": 2, "modelo": nome_modelo,
                    **{f"validacao_{k}": v for k, v in mva.items()},
                    **{f"teste_{k}": v for k, v in mte.items()},
                    "papel": "comparacao_justa_2D", "teste_aberto_uma_vez": True,
                })

            # Teto clássico: preserva mais dimensões e quantifica o custo da compressão.
            n_comp = min(32, Rtr.shape[1], len(Rtr) - 2)
            teto = Pipeline([
                ("imputador", SimpleImputer(strategy="median")),
                ("padronizador", StandardScaler()),
                ("pca", PCA(n_components=n_comp, random_state=SEED)),
                ("svm", SVC(kernel="rbf", C=1.0, gamma="scale", probability=True, random_state=SEED)),
            ]).fit(Rtr, ytr)
            pred_va, pred_te = teto.predict(Rva), teto.predict(Rte)
            mva = metricas_binarias_seguras(yva, pred_va, teto.predict_proba(Rva)[:, 1])
            mte = metricas_binarias_seguras(yte, pred_te, teto.predict_proba(Rte)[:, 1])
            linhas_baselines.append({
                "aplicacao": nome, "representacao": representacao,
                "dimensao": n_comp, "modelo": "SVM-RBF-teto-classico",
                **{f"validacao_{k}": v for k, v in mva.items()},
                **{f"teste_{k}": v for k, v in mte.items()},
                "papel": "teto_classico_sem_restricao_2_qubits", "teste_aberto_uma_vez": True,
            })

    resultados_baselines_fortes_df = pd.DataFrame(linhas_baselines)
    display(resultados_baselines_fortes_df.sort_values(
        ["aplicacao", "representacao", "teste_BAC"], ascending=[True, True, False]
    ).style.format({c: "{:.3f}" for c in resultados_baselines_fortes_df if "BAC" in c or "F1" in c or "MCC" in c or "AUROC" in c}))
    g = sns.catplot(data=resultados_baselines_fortes_df, x="modelo", y="teste_BAC",
                    col="aplicacao", hue="papel", kind="bar", col_wrap=2,
                    height=4, sharex=False)
    for ax in g.axes.flat: ax.tick_params(axis="x", rotation=75)
    g.fig.subplots_adjust(top=.88); g.fig.suptitle("Baselines fortes e custo da compressão para dois qubits")
    plt.show()
    n_aplicacoes_esperado = 4 if INCLUIR_REPLICACAO_PNEUMONIAMNIST else 3
    assert resultados_baselines_fortes_df["aplicacao"].nunique() == n_aplicacoes_esperado
    assert resultados_baselines_fortes_df["teste_BAC"].between(0, 1).all()
    print("✅ Baselines fortes executados; teto clássico separado da comparação 2D.")
""")

md(r"""
### 7.4.4.1 — Baselines visuais: CNN pequena e embedding congelado

A CNN pequena testa aprendizagem visual direta. A ResNet-18 congelada funciona como extrator de representações: nenhum peso visual é ajustado nas imagens do estudo, e uma regressão logística aprende apenas a camada final.

Para evitar uma comparação enganosa, esses modelos formam um **teto visual clássico**; eles não competem em igualdade de recursos com o circuito de dois qubits. Brier score, erro de calibração e curvas de decisão são diagnósticos metodológicos. BreastMNIST e PneumoniaMNIST permanecem sem uso clínico.
""")

code(r"""
# @title 7.4.4.1 — CNN, ResNet congelada, calibração e decisão {display-mode: "form"}
EPOCAS_CNN = 20
PACIENCIA_CNN = 4
BATCH_DEEP = 64
resultados_deep_imagens_df = pd.DataFrame()
curvas_decisao_imagens_df = pd.DataFrame()
historico_cnn_df = pd.DataFrame()
status_deep_imagens = "nao_executado"
modelos_cnn_treinados = {}

def erro_calibracao_esperado(y, prob, n_bins=10):
    y, prob = np.asarray(y), np.asarray(prob)
    bordas = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for a, b in zip(bordas[:-1], bordas[1:]):
        m = (prob >= a) & (prob < b if b < 1 else prob <= b)
        if m.any():
            ece += m.mean() * abs(y[m].mean() - prob[m].mean())
    return float(ece)

def curva_decisao_binaria(y, prob, limiares=np.arange(.1, 1, .1)):
    y, prob = np.asarray(y), np.asarray(prob)
    linhas = []
    for t in limiares:
        pred = prob >= t
        tp = np.sum(pred & (y == 1)); fp = np.sum(pred & (y == 0))
        linhas.append({"limiar": t, "beneficio_liquido": tp/len(y) - fp/len(y)*(t/(1-t))})
    return pd.DataFrame(linhas)

if not EXECUTAR_BASELINES_DEEP:
    print("⏭️ Baselines deep preparados. Ative somente após OSF e com GPU opcional.")
else:
    try:
        import torch
        import torch.nn as nn
        import torch.nn.functional as F
        from torch.utils.data import DataLoader, TensorDataset
        from torchvision.models import resnet18, ResNet18_Weights

        torch.manual_seed(SEED)
        if torch.cuda.is_available(): torch.cuda.manual_seed_all(SEED)
        torch.use_deterministic_algorithms(True, warn_only=True)
        dispositivo = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        class CNNPequena(nn.Module):
            def __init__(self):
                super().__init__()
                self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
                self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
                self.fc1 = nn.Linear(32*7*7, 64)
                self.fc2 = nn.Linear(64, 1)
            def forward(self, x):
                x = F.max_pool2d(F.relu(self.conv1(x)), 2)
                x = F.max_pool2d(F.relu(self.conv2(x)), 2)
                x = x.flatten(1)
                return self.fc2(F.relu(self.fc1(x))).squeeze(1)

        def tensor_imagens(X):
            X = np.asarray(X, dtype=np.float32).reshape(-1, 1, 28, 28) / 255.0
            return torch.from_numpy(X)

        def probabilidades_cnn(modelo, X):
            modelo.eval(); partes = []
            with torch.no_grad():
                for (xb,) in DataLoader(TensorDataset(tensor_imagens(X)), batch_size=BATCH_DEEP):
                    partes.append(torch.sigmoid(modelo(xb.to(dispositivo))).cpu().numpy())
            return np.concatenate(partes)

        linhas_deep, linhas_hist, linhas_decisao = [], [], []
        bases_imagem = {
            k: v for k, v in aplicacoes_paper_avancado.items()
            if k in {"breastmnist_imagens", "pneumoniamnist_replicacao"}
        }
        if not bases_imagem:
            raise RuntimeError("Ative EXECUTAR_LAB_GUIADO e EXECUTAR_PAPER_AVANCADO para carregar as imagens oficiais.")

        pesos_resnet = ResNet18_Weights.DEFAULT
        extrator = resnet18(weights=pesos_resnet)
        extrator.fc = nn.Identity()
        extrator.eval().to(dispositivo)
        for parametro in extrator.parameters(): parametro.requires_grad = False

        def embeddings_resnet(X):
            saidas = []
            loader = DataLoader(TensorDataset(tensor_imagens(X)), batch_size=BATCH_DEEP)
            with torch.no_grad():
                for (xb,) in loader:
                    xb = F.interpolate(xb, size=(224, 224), mode="bilinear", align_corners=False)
                    xb = xb.repeat(1, 3, 1, 1)
                    xb = (xb - torch.tensor([.485,.456,.406], device=dispositivo)[None,:,None,None]) / torch.tensor([.229,.224,.225], device=dispositivo)[None,:,None,None]
                    saidas.append(extrator(xb.to(dispositivo)).cpu().numpy())
            return np.concatenate(saidas)

        for nome, (Xtr, Xva, Xte, ytr, yva, yte) in bases_imagem.items():
            gerador = torch.Generator().manual_seed(SEED)
            loader = DataLoader(
                TensorDataset(tensor_imagens(Xtr), torch.tensor(ytr, dtype=torch.float32)),
                batch_size=BATCH_DEEP, shuffle=True, generator=gerador
            )
            modelo = CNNPequena().to(dispositivo)
            positivos = max(np.sum(ytr == 1), 1); negativos = max(np.sum(ytr == 0), 1)
            perda_fn = nn.BCEWithLogitsLoss(pos_weight=torch.tensor(negativos/positivos, device=dispositivo))
            otimizador = torch.optim.AdamW(modelo.parameters(), lr=1e-3, weight_decay=1e-4)
            melhor, estado_melhor, espera = np.inf, None, 0
            for epoca in range(1, EPOCAS_CNN + 1):
                modelo.train(); perdas = []
                for xb, yb in loader:
                    xb, yb = xb.to(dispositivo), yb.to(dispositivo)
                    otimizador.zero_grad(); perda = perda_fn(modelo(xb), yb)
                    perda.backward(); otimizador.step(); perdas.append(perda.item())
                pva = probabilidades_cnn(modelo, Xva)
                eps = 1e-7
                perda_va = float(-np.mean(yva*np.log(pva+eps)+(1-yva)*np.log(1-pva+eps)))
                linhas_hist.append({"aplicacao": nome, "epoca": epoca, "perda_treino": np.mean(perdas), "perda_validacao": perda_va})
                if perda_va < melhor - 1e-4:
                    melhor = perda_va; espera = 0
                    estado_melhor = {k: v.detach().cpu().clone() for k, v in modelo.state_dict().items()}
                else:
                    espera += 1
                    if espera >= PACIENCIA_CNN: break
            modelo.load_state_dict(estado_melhor); modelos_cnn_treinados[nome] = modelo.cpu()
            modelo.to(dispositivo)
            pte_cnn = probabilidades_cnn(modelo, Xte); pred_cnn = (pte_cnn >= .5).astype(int)

            Etr, Eva, Ete = embeddings_resnet(Xtr), embeddings_resnet(Xva), embeddings_resnet(Xte)
            candidatos = []
            for C in GRADE_C:
                lr = LogisticRegression(C=C, max_iter=3000, class_weight="balanced", random_state=SEED).fit(Etr, ytr)
                candidatos.append((balanced_accuracy_score(yva, lr.predict(Eva)), C))
            _, Cemb = max(candidatos, key=lambda z: (z[0], -z[1]))
            lr_emb = LogisticRegression(C=Cemb, max_iter=3000, class_weight="balanced", random_state=SEED).fit(Etr, ytr)
            pte_emb = lr_emb.predict_proba(Ete)[:,1]; pred_emb = (pte_emb >= .5).astype(int)

            for modelo_nome, pred, prob in [
                ("CNN_pequena", pred_cnn, pte_cnn),
                ("ResNet18_congelada_logistica", pred_emb, pte_emb),
            ]:
                linhas_deep.append({
                    "aplicacao": nome, "modelo": modelo_nome,
                    "BAC": balanced_accuracy_score(yte, pred), "F1": f1_score(yte, pred),
                    "AUROC": roc_auc_score(yte, prob), "Brier": float(np.mean((prob-yte)**2)),
                    "ECE_10_bins": erro_calibracao_esperado(yte, prob),
                    "uso_clinico": False, "teste_aberto_uma_vez": True,
                })
                dc = curva_decisao_binaria(yte, prob)
                dc["aplicacao"], dc["modelo"] = nome, modelo_nome
                linhas_decisao.extend(dc.to_dict("records"))

        resultados_deep_imagens_df = pd.DataFrame(linhas_deep)
        curvas_decisao_imagens_df = pd.DataFrame(linhas_decisao)
        historico_cnn_df = pd.DataFrame(linhas_hist)
        status_deep_imagens = "concluido_metodologico_sem_uso_clinico"
        display(resultados_deep_imagens_df.style.format({
            "BAC":"{:.3f}", "F1":"{:.3f}", "AUROC":"{:.3f}",
            "Brier":"{:.3f}", "ECE_10_bins":"{:.3f}",
        }))
        sns.lineplot(data=curvas_decisao_imagens_df, x="limiar", y="beneficio_liquido", hue="modelo", style="aplicacao", markers=True)
        plt.axhline(0,color="black",lw=1); plt.title("Curvas de decisão — comparação metodológica, não clínica"); plt.show()
        assert resultados_deep_imagens_df["uso_clinico"].eq(False).all()
    except Exception as erro_deep:
        status_deep_imagens = "falha_registrada"
        resultados_deep_imagens_df = pd.DataFrame([{
            "status": status_deep_imagens, "erro": str(erro_deep), "uso_clinico": False
        }])
        print("⚠️ Baselines deep não concluídos; falha registrada sem fallback silencioso:", erro_deep)
""")

md(r"""
## 7.4.5 — Curvas de aprendizagem e concentração do kernel

Uma acurácia isolada não mostra se o modelo está saturado, subajustado ou melhorando com mais dados. As curvas usam somente treino e validação. O teste oficial não participa. Cada ponto é repetido por subamostragem estratificada.

Os diagnósticos de concentração verificam se quase todos os exemplos estão se tornando artificialmente iguais ou ortogonais no espaço quântico.
""")

code(r"""
# @title 7.4.5 — Curvas, espectro e testes de concentração {display-mode: "form"}
TAMANHOS_CURVA = [24, 48, 96, 192]
REPETICOES_CURVA = 5
resultados_curvas_df = pd.DataFrame()
diagnosticos_concentracao_df = pd.DataFrame()

def diagnosticar_concentracao(K, y):
    K = np.asarray(K); y = np.asarray(y)
    fora = K[~np.eye(len(K), dtype=bool)]
    mesma = y[:, None] == y[None, :]
    intra = K[mesma & ~np.eye(len(K), dtype=bool)]
    inter = K[~mesma]
    eig = np.clip(np.linalg.eigvalsh((K + K.T) / 2), 0, None)
    positivos = eig[eig > 1e-12]
    cond = float(positivos.max() / positivos.min()) if len(positivos) else np.inf
    p = eig / eig.sum() if eig.sum() else np.zeros_like(eig)
    entropia = float(-np.sum(p[p > 0] * np.log(p[p > 0])))
    return {
        "media_offdiag": float(np.mean(fora)), "variancia_offdiag": float(np.var(fora)),
        "media_intra": float(np.mean(intra)), "media_inter": float(np.mean(inter)),
        "separacao_intra_inter": float(np.mean(intra) - np.mean(inter)),
        "condicao_espectral": cond, "entropia_espectral": entropia,
        "posto_efetivo": posto_efetivo_matriz(K),
    }

if not EXECUTAR_CURVAS_APRENDIZAGEM:
    print("⏭️ Curvas preparadas. Ative EXECUTAR_CURVAS_APRENDIZAGEM depois do registro OSF.")
else:
    assert EXECUTAR_LAB_GUIADO
    linhas_curvas, linhas_concentracao = [], []
    for i_base, (nome, partes) in enumerate(aplicacoes_paper_avancado.items()):
        Xtr0, Xva0, _, ytr0, yva0, _ = partes
        Xdev = np.concatenate([Xtr0, Xva0]); ydev = np.concatenate([ytr0, yva0])
        maximo = min(max(TAMANHOS_CURVA), len(ydev))
        tamanhos = sorted(set([n for n in TAMANHOS_CURVA if n <= maximo] + [maximo]))
        for n in tamanhos:
            for rep in range(REPETICOES_CURVA):
                Xsub, ysub = subamostra_estratificada(Xdev, ydev, n, SEED + 1000*i_base + rep)
                Xtr_raw, Xva_raw, ytr, yva = train_test_split(
                    Xsub, ysub, test_size=.25, stratify=ysub, random_state=SEED + rep
                )
                Xtr, Xva, _, _ = preparar_angular(Xtr_raw, Xva_raw, Xva_raw)
                t0 = time.perf_counter()
                rbf = SVC(kernel="rbf", C=1.0, gamma="scale").fit(Xtr, ytr)
                bac_rbf = balanced_accuracy_score(yva, rbf.predict(Xva))
                tempo_rbf = time.perf_counter() - t0
                t0 = time.perf_counter()
                qk = FidelityStatevectorKernel(feature_map=feature_map, shots=None)
                Ktr, Kva = qk.evaluate(Xtr), qk.evaluate(Xva, Xtr)
                qml = SVC(kernel="precomputed", C=1.0).fit(Ktr, ytr)
                bac_qml = balanced_accuracy_score(yva, qml.predict(Kva))
                tempo_qml = time.perf_counter() - t0
                linhas_curvas.extend([
                    {"aplicacao": nome, "n": n, "repeticao": rep, "modelo": "SVM-RBF", "BAC_validacao": bac_rbf, "tempo_s": tempo_rbf},
                    {"aplicacao": nome, "n": n, "repeticao": rep, "modelo": "QML-exato", "BAC_validacao": bac_qml, "tempo_s": tempo_qml},
                ])
                linhas_concentracao.append({"aplicacao": nome, "n": n, "repeticao": rep, **diagnosticar_concentracao(Ktr, ytr)})
    resultados_curvas_df = pd.DataFrame(linhas_curvas)
    diagnosticos_concentracao_df = pd.DataFrame(linhas_concentracao)
    resumo_curvas = resultados_curvas_df.groupby(["aplicacao", "n", "modelo"], as_index=False).agg(
        BAC_media=("BAC_validacao", "mean"), BAC_dp=("BAC_validacao", "std"), tempo_medio_s=("tempo_s", "mean")
    )
    g = sns.relplot(data=resumo_curvas, x="n", y="BAC_media", hue="modelo", col="aplicacao",
                    kind="line", marker="o", facet_kws={"sharex": False}, height=4)
    g.set(ylim=(0, 1.05)); g.fig.subplots_adjust(top=.83); g.fig.suptitle("Curvas de aprendizagem sem abrir o teste")
    plt.show()
    assert resultados_curvas_df["BAC_validacao"].between(0, 1).all()
    assert diagnosticos_concentracao_df["variancia_offdiag"].ge(0).all()
    print("✅ Curvas e concentração calculadas somente no desenvolvimento.")
""")

code(r"""
# @title 7.4.6 — Controles negativos e deslocamento de distribuição {display-mode: "form"}
N_PERMUTACOES_CONTROLE = 50
resultados_generalizacao_df = pd.DataFrame()

if not EXECUTAR_PAPER_AVANCADO:
    print("⏭️ Controles de generalização preparados, mas não executados.")
else:
    linhas_gen = []
    for i_base, (nome, partes) in enumerate(aplicacoes_paper_avancado.items()):
        Xtr_raw, Xva_raw, _, ytr, yva, _ = partes
        Xtr, Xva, _, _ = preparar_angular(Xtr_raw, Xva_raw, Xva_raw)
        qk = FidelityStatevectorKernel(feature_map=feature_map, shots=None)
        Ktr, Kva = qk.evaluate(Xtr), qk.evaluate(Xva, Xtr)
        rng = np.random.default_rng(SEED + i_base)
        for b in range(N_PERMUTACOES_CONTROLE):
            yperm = rng.permutation(ytr)
            for modelo, pred in {
                "RBF_rotulo_permutado": SVC(kernel="rbf", C=1.0).fit(Xtr, yperm).predict(Xva),
                "QML_rotulo_permutado": SVC(kernel="precomputed", C=1.0).fit(Ktr, yperm).predict(Kva),
            }.items():
                linhas_gen.append({"aplicacao": nome, "controle": modelo, "repeticao": b,
                                   "BAC": balanced_accuracy_score(yva, pred)})
        for sigma in [0.00, 0.05, 0.10, 0.20]:
            Xshift = np.clip(Xva + rng.normal(0, sigma, Xva.shape), 0, np.pi)
            Kshift = qk.evaluate(Xshift, Xtr)
            pred_rbf = SVC(kernel="rbf", C=1.0).fit(Xtr, ytr).predict(Xshift)
            pred_qml = SVC(kernel="precomputed", C=1.0).fit(Ktr, ytr).predict(Kshift)
            linhas_gen.extend([
                {"aplicacao": nome, "controle": "RBF_shift", "repeticao": sigma, "BAC": balanced_accuracy_score(yva, pred_rbf)},
                {"aplicacao": nome, "controle": "QML_shift", "repeticao": sigma, "BAC": balanced_accuracy_score(yva, pred_qml)},
            ])
    resultados_generalizacao_df = pd.DataFrame(linhas_gen)
    display(resultados_generalizacao_df.groupby(["aplicacao", "controle"], as_index=False).agg(
        BAC_media=("BAC", "mean"), BAC_dp=("BAC", "std")
    ).style.format({"BAC_media": "{:.3f}", "BAC_dp": "{:.3f}"}))
    assert resultados_generalizacao_df["BAC"].between(0, 1).all()
    print("✅ Controles negativos e perturbações concluídos; interpretar como robustez, não causalidade.")
""")

md(r"""
## 7.4.7 — Ruído aninhado multissemente

Aqui o ruído deixa de ser escolhido por uma única realização favorável. Em cada fold externo:

1. o treino externo é novamente dividido em treino interno e validação;
2. cada perfil é repetido com cinco seeds;
3. escolhe-se a maior BAC média de validação;
4. empates favorecem menor deformação e menor carga de ruído;
5. somente então o fold externo é avaliado.

Assim, o eventual “benefício do ruído” precisa sobreviver a folds e seeds, e não apenas a uma flutuação de shots.
""")

code(r"""
# @title 7.4.7 — Seleção aninhada de ruído com cinco seeds {display-mode: "form"}
SEEDS_RUIDO = [101, 211, 307, 401, 503]
SHOTS_RUIDO_CONFIRMATORIO = 512
N_FOLDS_RUIDO_EXTERNOS = 3
MAX_AMOSTRAS_RUIDO_ANINHADO = 48
resultados_ruido_aninhado_df = pd.DataFrame()
resumo_ruido_aninhado_df = pd.DataFrame()

if not EXECUTAR_RUIDO_ANINHADO:
    print("⏭️ Ruído aninhado preparado. Ative somente depois do registro OSF.")
else:
    assert EXECUTAR_LAB_GUIADO
    linhas_ruido_aninhado = []
    for i_base, (nome, partes) in enumerate(aplicacoes_paper_avancado.items()):
        Xtr0, Xva0, _, ytr0, yva0, _ = partes
        Xdev = np.concatenate([Xtr0, Xva0]); ydev = np.concatenate([ytr0, yva0])
        Xdev, ydev = subamostra_estratificada(
            Xdev, ydev, MAX_AMOSTRAS_RUIDO_ANINHADO, SEED + i_base
        )
        cv_ext = StratifiedKFold(N_FOLDS_RUIDO_EXTERNOS, shuffle=True, random_state=SEED + i_base)
        for fold, (idx_dev, idx_ext) in enumerate(cv_ext.split(Xdev, ydev), start=1):
            Xd_raw, Xe_raw = Xdev[idx_dev], Xdev[idx_ext]
            yd, ye = ydev[idx_dev], ydev[idx_ext]
            idx_in, idx_va = train_test_split(
                np.arange(len(yd)), test_size=.30, stratify=yd, random_state=SEED + fold
            )
            Xin_raw, Xv_raw = Xd_raw[idx_in], Xd_raw[idx_va]
            yin, yv = yd[idx_in], yd[idx_va]
            Xin, Xv, Xe_from_in, preparo_in = preparar_angular(Xin_raw, Xv_raw, Xe_raw)
            qk_ideal = FidelityStatevectorKernel(feature_map=feature_map, shots=None)
            Kin_ideal = qk_ideal.evaluate(Xin)
            candidatos_rbf_validacao = []
            for C_rbf in GRADE_C:
                for gamma_rbf in GRADE_GAMMA_RBF:
                    pred_rbf_v = SVC(kernel="rbf", C=C_rbf, gamma=gamma_rbf).fit(Xin, yin).predict(Xv)
                    candidatos_rbf_validacao.append(
                        balanced_accuracy_score(yv, pred_rbf_v)
                    )
            bac_rbf_validacao = float(max(candidatos_rbf_validacao))
            candidatos = []
            for perfil in PERFIS_RUIDO:
                for seed_ruido in SEEDS_RUIDO:
                    sim = criar_simulador_ruido(perfil)
                    Kin = projetar_psd(avaliar_kernel_aer(
                        Xin, Xin, feature_map, sim, SHOTS_RUIDO_CONFIRMATORIO,
                        seed_ruido + 1000*fold, simetrico=True
                    ))
                    Kv = avaliar_kernel_aer(
                        Xv, Xin, feature_map, sim, SHOTS_RUIDO_CONFIRMATORIO,
                        seed_ruido + 1000*fold, simetrico=False
                    )
                    for C in GRADE_C:
                        pred = SVC(kernel="precomputed", C=C).fit(Kin, yin).predict(Kv)
                        candidatos.append({
                            "perfil": perfil["perfil"], "C": C, "seed_ruido": seed_ruido,
                            "bac_validacao": balanced_accuracy_score(yv, pred),
                            "erro_geometrico": erro_frobenius_relativo(Kin_ideal, Kin),
                            "carga_ruido": perfil["erro_1q"] + perfil["erro_2q"] + perfil["erro_leitura"],
                        })
            cand = pd.DataFrame(candidatos)
            agregado = cand.groupby(["perfil", "C"], as_index=False).agg(
                bac_validacao_media=("bac_validacao", "mean"),
                bac_validacao_dp=("bac_validacao", "std"),
                erro_geometrico_medio=("erro_geometrico", "mean"),
                carga_ruido=("carga_ruido", "first"),
            ).sort_values(
                ["bac_validacao_media", "erro_geometrico_medio", "carga_ruido", "C"],
                ascending=[False, True, True, True]
            )
            escolha = agregado.iloc[0]
            perfil = next(p for p in PERFIS_RUIDO if p["perfil"] == escolha["perfil"])

            # Reajusta o preprocessamento no desenvolvimento externo inteiro.
            Xd, Xe, _, _ = preparar_angular(Xd_raw, Xe_raw, Xe_raw)
            Kd_ideal = FidelityStatevectorKernel(feature_map=feature_map, shots=None).evaluate(Xd)
            t0_rbf = time.perf_counter()
            pred_rbf = SVC(kernel="rbf", C=1.0, gamma="scale").fit(Xd, yd).predict(Xe)
            tempo_rbf = time.perf_counter() - t0_rbf
            bac_rbf = balanced_accuracy_score(ye, pred_rbf)
            for seed_ruido in SEEDS_RUIDO:
                sim = criar_simulador_ruido(perfil)
                t0_q = time.perf_counter()
                Kd = projetar_psd(avaliar_kernel_aer(
                    Xd, Xd, feature_map, sim, SHOTS_RUIDO_CONFIRMATORIO,
                    seed_ruido + 10000*fold, simetrico=True
                ))
                Ke = avaliar_kernel_aer(
                    Xe, Xd, feature_map, sim, SHOTS_RUIDO_CONFIRMATORIO,
                    seed_ruido + 10000*fold, simetrico=False
                )
                pred_q = SVC(kernel="precomputed", C=float(escolha["C"])).fit(Kd, yd).predict(Ke)
                tempo_q = time.perf_counter() - t0_q
                bac_q = balanced_accuracy_score(ye, pred_q)
                n_circuitos = len(Xd)*(len(Xd)-1)//2 + len(Xe)*len(Xd)
                linhas_ruido_aninhado.append({
                    "aplicacao": nome, "fold_externo": fold, "seed_ruido": seed_ruido,
                    "perfil_selecionado": escolha["perfil"], "C_selecionado": float(escolha["C"]),
                    "bac_validacao_media_selecao": float(escolha["bac_validacao_media"]),
                    "bac_validacao_dp_selecao": float(escolha["bac_validacao_dp"]),
                    "bac_rbf_validacao": bac_rbf_validacao,
                    "delta_bac_validacao": float(escolha["bac_validacao_media"] - bac_rbf_validacao),
                    "sobrevivencia_geometrica_validacao": float(np.clip(1-escolha["erro_geometrico_medio"],0,1)),
                    "bac_rbf_externo": bac_rbf, "bac_qml_externo": bac_q,
                    "delta_bac": bac_q - bac_rbf,
                    "sobrevivencia_geometrica": float(np.clip(1-erro_frobenius_relativo(Kd_ideal, Kd), 0, 1)),
                    "tempo_qml_s": tempo_q, "tempo_rbf_s": tempo_rbf,
                    "custo_logico": n_circuitos*SHOTS_RUIDO_CONFIRMATORIO,
                    "selecao_sem_fold_externo": True,
                })
            print(f"{nome} | fold {fold}/{N_FOLDS_RUIDO_EXTERNOS} | perfil={escolha['perfil']}")

    resultados_ruido_aninhado_df = pd.DataFrame(linhas_ruido_aninhado)
    resumo_ruido_aninhado_df = resultados_ruido_aninhado_df.groupby(
        ["aplicacao", "fold_externo", "perfil_selecionado"], as_index=False
    ).agg(
        bac_qml_media=("bac_qml_externo", "mean"), bac_qml_dp=("bac_qml_externo", "std"),
        bac_validacao_media_selecao=("bac_validacao_media_selecao", "first"),
        bac_validacao_dp_selecao=("bac_validacao_dp_selecao", "first"),
        bac_rbf_validacao=("bac_rbf_validacao", "first"),
        delta_bac_validacao=("delta_bac_validacao", "first"),
        sobrevivencia_geometrica_validacao=("sobrevivencia_geometrica_validacao", "first"),
        bac_rbf=("bac_rbf_externo", "first"), delta_bac=("delta_bac", "mean"),
        sobrevivencia_geometrica=("sobrevivencia_geometrica", "mean"),
        custo_logico=("custo_logico", "first"), tempo_qml_s=("tempo_qml_s", "mean"),
        tempo_rbf_s=("tempo_rbf_s", "first"),
    )
    display(resumo_ruido_aninhado_df.style.format({
        "bac_qml_media": "{:.3f}", "bac_qml_dp": "{:.3f}", "bac_rbf": "{:.3f}",
        "delta_bac": "{:+.3f}", "sobrevivencia_geometrica": "{:.3f}"
    }))
    assert resultados_ruido_aninhado_df["selecao_sem_fold_externo"].all()
    assert resultados_ruido_aninhado_df.groupby(["aplicacao", "fold_externo"])["seed_ruido"].nunique().eq(len(SEEDS_RUIDO)).all()
    print("✅ Ruído escolhido na validação interna e replicado em cinco seeds externas.")
""")

md(r"""
## 7.4.8 — Modelo multinível e Quantum Utility Score em desenvolvimento

Folds e seeds da mesma aplicação compartilham dados e não são observações independentes. O modelo abaixo usa intercepto aleatório por aplicação e apresenta uma regressão com erros agrupados como sensibilidade.

O **QUS** combina efeito de validação, geometria de validação, reprodutibilidade e custo. Ele é calculado antes de consultar o fold externo; em seguida, esse fold avalia discriminação e calibração sem reajustar pesos. A validação final continua reservada a novas bases e à QPU.
""")

code(r"""
# @title 7.4.8 — Efeitos mistos, sensibilidade por cluster e QUS {display-mode: "form"}
import statsmodels.formula.api as smf

resultado_modelo_multinivel = {}
tabela_qus_df = pd.DataFrame()
calibracao_qus_df = pd.DataFrame()
resultado_validacao_qus = {}

if resultados_ruido_aninhado_df.empty:
    print("⏭️ Modelo multinível e QUS aguardam a execução de 7.4.7.")
else:
    dados_modelo = resumo_ruido_aninhado_df.copy()
    dados_modelo["log_custo"] = np.log1p(dados_modelo["custo_logico"])
    formula = "delta_bac ~ sobrevivencia_geometrica + log_custo"
    try:
        ajuste_misto = smf.mixedlm(formula, dados_modelo, groups=dados_modelo["aplicacao"]).fit(
            reml=True, method="lbfgs", disp=False
        )
        resultado_modelo_multinivel = {
            "modelo": "MixedLM; intercepto aleatorio por aplicacao",
            "beta_sobrevivencia": float(ajuste_misto.params["sobrevivencia_geometrica"]),
            "se_sobrevivencia": float(ajuste_misto.bse["sobrevivencia_geometrica"]),
            "p_sobrevivencia": float(ajuste_misto.pvalues["sobrevivencia_geometrica"]),
            "convergiu": bool(ajuste_misto.converged),
            "status": f"exploratorio; {dados_modelo['aplicacao'].nunique()} aplicacoes",
        }
    except Exception as erro_misto:
        resultado_modelo_multinivel = {
            "modelo": "MixedLM não estimável",
            "convergiu": False, "erro": str(erro_misto),
            "status": "reportar falha sem substituir silenciosamente o modelo",
        }
    try:
        ajuste_cluster = smf.ols(formula, dados_modelo).fit(
            cov_type="cluster", cov_kwds={"groups": dados_modelo["aplicacao"]}
        )
        resultado_modelo_multinivel["sensibilidade_cluster"] = {
            "beta_sobrevivencia": float(ajuste_cluster.params["sobrevivencia_geometrica"]),
            "se_sobrevivencia": float(ajuste_cluster.bse["sobrevivencia_geometrica"]),
            "p_sobrevivencia": float(ajuste_cluster.pvalues["sobrevivencia_geometrica"]),
            "aviso": f"p aproximado instavel com {dados_modelo['aplicacao'].nunique()} clusters",
        }
    except Exception as erro_cluster:
        resultado_modelo_multinivel["sensibilidade_cluster"] = {
            "erro": str(erro_cluster),
            "aviso": "sensibilidade nao estimavel; manter resultado como ausente",
        }

    tabela_qus_df = dados_modelo.copy()
    tabela_qus_df["reprodutibilidade"] = np.exp(
        -tabela_qus_df["bac_validacao_dp_selecao"].fillna(0) / MARGEM_EQUIVALENCIA_BAC
    )
    tabela_qus_df["razao_custo"] = (
        tabela_qus_df["tempo_qml_s"] / tabela_qus_df["tempo_rbf_s"].clip(lower=1e-9)
    )
    efeito_normalizado = np.clip(
        (tabela_qus_df["delta_bac_validacao"] + MARGEM_EQUIVALENCIA_BAC) /
        (2*MARGEM_EQUIVALENCIA_BAC), 0, 1
    )
    tabela_qus_df["QUS_prospectivo"] = (
        tabela_qus_df["sobrevivencia_geometrica_validacao"] * efeito_normalizado *
        tabela_qus_df["reprodutibilidade"] /
        (1 + np.log1p(tabela_qus_df["razao_custo"]))
    )
    tabela_qus_df["utilidade_preservada_fold_externo"] = (
        (tabela_qus_df["delta_bac"] >= -MARGEM_EQUIVALENCIA_BAC)
        & (tabela_qus_df["sobrevivencia_geometrica"] >= 0.85)
    ).astype(int)
    y_qus = tabela_qus_df["utilidade_preservada_fold_externo"]
    p_qus = tabela_qus_df["QUS_prospectivo"].clip(0,1)
    auc_qus = roc_auc_score(y_qus,p_qus) if y_qus.nunique()==2 else np.nan
    brier_qus = float(np.mean((p_qus-y_qus)**2))
    rng_qus=np.random.default_rng(SEED); auc_boot=[]
    for _ in range(3000):
        idx=rng_qus.integers(0,len(y_qus),len(y_qus)); yb=y_qus.iloc[idx]; pb=p_qus.iloc[idx]
        if yb.nunique()==2: auc_boot.append(roc_auc_score(yb,pb))
    ic_auc=np.quantile(auc_boot,[.025,.975]) if auc_boot else [np.nan,np.nan]
    resultado_validacao_qus={
        "validacao":"prospectiva_no_fold_externo_sem_reajuste_de_pesos",
        "AUROC":float(auc_qus) if np.isfinite(auc_qus) else None,
        "IC95_bootstrap_AUROC":[float(ic_auc[0]),float(ic_auc[1])] if np.isfinite(ic_auc).all() else None,
        "Brier":brier_qus,
        "n_aplicacoes":int(tabela_qus_df["aplicacao"].nunique()),
        "validacao_hardware":"pendente",
        "regra":"nao reajustar formula ou limiar com estes folds",
    }
    bins=pd.cut(p_qus,bins=[-1e-12,.02,.05,.10,.20,1],include_lowest=True,duplicates="drop")
    calibracao_qus_df=tabela_qus_df.assign(faixa_QUS=bins.astype(str)).groupby(
        "faixa_QUS",as_index=False,observed=True
    ).agg(QUS_medio=("QUS_prospectivo","mean"),taxa_utilidade=("utilidade_preservada_fold_externo","mean"),n=("aplicacao","size"))
    tabela_qus_df["status_QUS"] = "validacao_tecnica_externa_concluida_hardware_pendente"
    display(pd.Series(resultado_modelo_multinivel, name="resultado").to_frame())
    display(tabela_qus_df.style.format({
        "delta_bac_validacao": "{:+.3f}", "delta_bac": "{:+.3f}",
        "sobrevivencia_geometrica_validacao": "{:.3f}", "sobrevivencia_geometrica": "{:.3f}",
        "reprodutibilidade": "{:.3f}", "razao_custo": "{:.1f}",
        "QUS_prospectivo": "{:.4f}",
    }))
    display(pd.Series(resultado_validacao_qus,name="valor").to_frame())
    display(calibracao_qus_df)
    assert tabela_qus_df["QUS_prospectivo"].between(0, 1).all()
    assert tabela_qus_df["status_QUS"].eq("validacao_tecnica_externa_concluida_hardware_pendente").all()
    componentes_qus={"delta_bac_validacao","sobrevivencia_geometrica_validacao","bac_validacao_dp_selecao","razao_custo"}
    assert componentes_qus.isdisjoint({"delta_bac","bac_qml_media","bac_qml_externo","bac_rbf_externo"})
    print("✅ QUS calculado sem o fold externo; validação técnica concluída e hardware pendente.")
""")

md(r"""
## 7.4.9 — Benchmark ampliado com dez ou mais bases

Folds adicionais da mesma base não substituem novas aplicações. Por isso, esta etapa amplia a unidade de generalização:

- sete bases locais ou sintéticas garantem que o código continue reprodutível sem rede;
- cinco bases OpenML possuem IDs fixos, cache e registro de proveniência;
- falhas de download são registradas e **nunca** substituídas silenciosamente;
- a expressão “benchmark 10+ bases” somente é autorizada se pelo menos dez bases forem efetivamente avaliadas;
- `Z`, `ZZ` e `Pauli` participam da seleção interna; o fold externo não escolhe o mapa.

O limite de 96 observações por base controla o custo quadrático e deve aparecer nas limitações.
""")

code(r"""
# @title 7.4.9 — Catálogo 10+ bases e seleção aninhada de feature map {display-mode: "form"}
from sklearn.datasets import (
    fetch_openml, load_breast_cancer, load_digits, load_wine,
    make_circles, make_classification,
)
from sklearn.preprocessing import LabelEncoder
from qiskit.circuit.library import z_feature_map, pauli_feature_map

MAX_AMOSTRAS_BENCHMARK = 96
N_FOLDS_BENCHMARK = 3
MIN_BASES_PARA_ALEGACAO = 10
resultados_benchmark_ampliado_df = pd.DataFrame()
catalogo_bases_ampliado_df = pd.DataFrame()
status_benchmark_ampliado = "nao_executado"

def checksum_base(X, y):
    Xc = np.ascontiguousarray(np.asarray(X, dtype=np.float64))
    yc = np.ascontiguousarray(np.asarray(y, dtype=np.int64))
    return hashlib.sha256(Xc.tobytes() + yc.tobytes()).hexdigest()

def registrar_base_local():
    iris = load_iris(); mi = iris.target < 2
    wine = load_wine(); mw = wine.target < 2
    bc = load_breast_cancer()
    dig = load_digits(); mdig = np.isin(dig.target, [3, 8])
    Xm, ym = make_moons(n_samples=240, noise=.20, random_state=SEED)
    Xc, yc = make_circles(n_samples=240, noise=.10, factor=.45, random_state=SEED)
    Xs, ys = make_classification(
        n_samples=240, n_features=12, n_informative=5, n_redundant=3,
        class_sep=.8, flip_y=.05, random_state=SEED
    )
    return {
        "iris_setosa_versicolor": (iris.data[mi], iris.target[mi], "sklearn", "biologico_simples"),
        "wine_binario": (wine.data[mw], wine.target[mw], "sklearn", "fisico_quimico"),
        "breast_cancer_wisconsin": (bc.data, bc.target, "sklearn", "biomedico_tabular_nao_clinico"),
        "digits_3_vs_8": (dig.data[mdig], (dig.target[mdig] == 8).astype(int), "sklearn", "imagem_8x8"),
        "make_moons": (Xm, ym, "sintetico_seed_42", "geometria_curva"),
        "make_circles": (Xc, yc, "sintetico_seed_42", "geometria_radial"),
        "make_classification": (Xs, ys, "sintetico_seed_42", "alta_dimensao_controlada"),
    }

OPENML_FIXO = {
    "sonar": 40,
    "ionosphere": 59,
    "diabetes_pima": 37,
    "spambase": 44,
    "banknote_authentication": 1462,
    "blood_transfusion": 1464,
}

def carregar_openml_numerico(nome, data_id):
    lote = fetch_openml(data_id=data_id, as_frame=True, parser="auto")
    Xdf = lote.data.select_dtypes(include="number")
    if Xdf.shape[1] < 2:
        raise ValueError("menos de duas colunas numéricas")
    y = LabelEncoder().fit_transform(lote.target.astype(str))
    if len(np.unique(y)) != 2:
        raise ValueError("alvo não binário")
    return Xdf.to_numpy(float), y

if not EXECUTAR_BENCHMARK_AMPLIADO:
    print("⏭️ Benchmark ampliado preparado. Ative-o somente depois do registro OSF.")
else:
    bases = registrar_base_local()
    catalogo = []
    for nome, data_id in OPENML_FIXO.items():
        try:
            Xo, yo = carregar_openml_numerico(nome, data_id)
            bases[nome] = (Xo, yo, f"OpenML data_id={data_id}", "externo_publico")
            catalogo.append({"base": nome, "fonte": "OpenML", "data_id": data_id, "status": "carregada", "erro": ""})
        except Exception as erro:
            catalogo.append({"base": nome, "fonte": "OpenML", "data_id": data_id, "status": "falha_registrada", "erro": str(erro)})

    mapas_candidatos = {
        "Z_reps1": z_feature_map(feature_dimension=2, reps=1),
        "ZZ_linear_reps1": zz_feature_map(feature_dimension=2, reps=1, entanglement="linear"),
        "ZZ_full_reps2": zz_feature_map(feature_dimension=2, reps=2, entanglement="full"),
        "Pauli_Z_ZZ": pauli_feature_map(feature_dimension=2, reps=1, paulis=["Z", "ZZ"]),
    }
    linhas_benchmark = []
    for i_base, (nome, (X0, y0, fonte, dominio)) in enumerate(bases.items()):
        X0, y0 = subamostra_estratificada(X0, y0, MAX_AMOSTRAS_BENCHMARK, SEED + i_base)
        catalogo.append({
            "base": nome, "fonte": fonte, "data_id": OPENML_FIXO.get(nome),
            "status": "incluida", "erro": "", "n": len(y0), "p": np.asarray(X0).shape[1],
            "dominio": dominio, "checksum_sha256": checksum_base(X0, y0),
        })
        cv_ext = StratifiedKFold(N_FOLDS_BENCHMARK, shuffle=True, random_state=SEED + i_base)
        for fold, (itr, ite) in enumerate(cv_ext.split(X0, y0), start=1):
            Xtr_raw, Xte_raw, ytr, yte = X0[itr], X0[ite], y0[itr], y0[ite]
            Xtr, Xte, _, _ = preparar_angular(Xtr_raw, Xte_raw, Xte_raw)
            cv_int = StratifiedKFold(3, shuffle=True, random_state=SEED + fold)

            classicos = {
                "SVM-linear": (SVC(kernel="linear"), {"C": GRADE_C}),
                "SVM-RBF": (SVC(kernel="rbf"), {"C": GRADE_C, "gamma": GRADE_GAMMA_RBF}),
            }
            for modelo_nome, (est, grade) in classicos.items():
                busca = GridSearchCV(est, grade, scoring="balanced_accuracy", cv=cv_int, n_jobs=-1).fit(Xtr, ytr)
                linhas_benchmark.append({
                    "base": nome, "dominio": dominio, "fold": fold, "modelo": modelo_nome,
                    "feature_map": "nao_aplicavel", "BAC": balanced_accuracy_score(yte, busca.predict(Xte)),
                    "selecionado_internamente": True, "n_treino": len(ytr), "n_teste": len(yte),
                })

            candidatos_q = []
            kernels_cache = {}
            for mapa_nome, mapa in mapas_candidatos.items():
                qk = FidelityStatevectorKernel(feature_map=mapa, shots=None)
                Ktr = qk.evaluate(Xtr); Kte = qk.evaluate(Xte, Xtr)
                kernels_cache[mapa_nome] = (Ktr, Kte)
                busca_q = GridSearchCV(
                    SVC(kernel="precomputed"), {"C": GRADE_C},
                    scoring="balanced_accuracy", cv=cv_int, n_jobs=1
                ).fit(Ktr, ytr)
                candidatos_q.append({
                    "mapa": mapa_nome, "C": busca_q.best_params_["C"],
                    "BAC_interna": busca_q.best_score_,
                    "entropia": diagnosticar_concentracao(Ktr, ytr)["entropia_espectral"],
                })
            escolhido = pd.DataFrame(candidatos_q).sort_values(
                ["BAC_interna", "entropia", "mapa"], ascending=[False, True, True]
            ).iloc[0]
            Ktr, Kte = kernels_cache[escolhido["mapa"]]
            pred = SVC(kernel="precomputed", C=float(escolhido["C"])).fit(Ktr, ytr).predict(Kte)
            linhas_benchmark.append({
                "base": nome, "dominio": dominio, "fold": fold, "modelo": "QML",
                "feature_map": escolhido["mapa"], "BAC": balanced_accuracy_score(yte, pred),
                "selecionado_internamente": True, "n_treino": len(ytr), "n_teste": len(yte),
                **{f"kernel_{k}": v for k, v in diagnosticar_concentracao(Ktr, ytr).items()},
            })
            print(f"{nome} | fold {fold}/{N_FOLDS_BENCHMARK} | mapa={escolhido['mapa']}")

    resultados_benchmark_ampliado_df = pd.DataFrame(linhas_benchmark)
    catalogo_bases_ampliado_df = pd.DataFrame(catalogo)
    n_bases_avaliadas = resultados_benchmark_ampliado_df["base"].nunique()
    status_benchmark_ampliado = (
        "apto_para_alegacao_10_mais_bases" if n_bases_avaliadas >= MIN_BASES_PARA_ALEGACAO
        else "incompleto_nao_alegar_validade_ampliada"
    )
    display(catalogo_bases_ampliado_df)
    display(resultados_benchmark_ampliado_df.groupby(["base", "modelo"], as_index=False).agg(
        BAC_media=("BAC", "mean"), BAC_dp=("BAC", "std")
    ).style.format({"BAC_media": "{:.3f}", "BAC_dp": "{:.3f}"}))
    print("Status:", status_benchmark_ampliado, "| bases avaliadas:", n_bases_avaliadas)
    assert resultados_benchmark_ampliado_df["BAC"].between(0, 1).all()
    assert resultados_benchmark_ampliado_df["selecionado_internamente"].all()
""")

md(r"""
## 7.4.10 — Nyström e aquisição ativa sob o mesmo orçamento

Esta é a comparação de eficiência central. Cada estratégia recebe o mesmo total de shots lógicos:

| Estratégia | O que mede | Como escolhe |
|---|---|---|
| matriz uniforme | todos os pares | shots iguais por par |
| Nyström aleatório | colunas-landmark | sorteio estratificado pela seed |
| Nyström leverage | colunas-landmark | leverage scores do RBF de treino |
| aquisição ativa | landmarks de fronteira | margem do RBF + variância do piloto |

Leverage, margem e alocação usam somente treino. O teste é medido depois de congelar landmarks e shots. O simulador abaixo reproduz estatística binomial de fidelidade; a mesma lista de pares pode ser enviada futuramente à QPU.
""")

code(r"""
# @title 7.4.10 — Eficiência por shot: completo × Nyström × ativo {display-mode: "form"}
ORCAMENTO_SHOTS_AQUISICAO = 200_000
N_LANDMARKS = 8
SHOTS_PILOTO_ATIVO = 32
SEEDS_AQUISICAO = [17, 29, 43, 61, 79]
MAX_TREINO_AQUISICAO = 48
MAX_TESTE_AQUISICAO = 16
resultados_aquisicao_ativa_df = pd.DataFrame()
planos_medicao_aquisicao_df = pd.DataFrame()

def alocar_inteiros(total, pesos, minimo=1):
    pesos = np.asarray(pesos, dtype=float).ravel()
    n = len(pesos)
    if total < n*minimo: raise ValueError("orçamento menor que o mínimo por circuito")
    pesos = np.clip(pesos, 0, None)
    pesos = np.ones(n) if pesos.sum() == 0 else pesos
    restante = total - n*minimo
    bruto = restante * pesos/pesos.sum()
    aloc = np.full(n, minimo, dtype=int) + np.floor(bruto).astype(int)
    sobra = total - aloc.sum()
    if sobra: aloc[np.argsort(-(bruto-np.floor(bruto)))[:sobra]] += 1
    assert aloc.sum() == total
    return aloc

def medir_vetor_fidelidades(probabilidades, shots, rng):
    p = np.clip(np.asarray(probabilidades, dtype=float), 0, 1)
    s = np.asarray(shots, dtype=int)
    return rng.binomial(s, p)/s

def medir_kernel_completo(Ktr, Kte, orcamento, rng):
    n, nt = len(Ktr), len(Kte)
    pares = [(i,j) for i in range(n) for j in range(i+1,n)]
    total_circuitos = len(pares) + nt*n
    shots = alocar_inteiros(orcamento, np.ones(total_circuitos), minimo=1)
    out_tr = np.eye(n); cursor = 0
    probs_tr = [Ktr[i,j] for i,j in pares]
    obs_tr = medir_vetor_fidelidades(probs_tr, shots[:len(pares)], rng)
    for (i,j), valor in zip(pares, obs_tr): out_tr[i,j]=out_tr[j,i]=valor
    cursor = len(pares)
    out_te = medir_vetor_fidelidades(Kte.ravel(), shots[cursor:], rng).reshape(nt,n)
    out_tr = projetar_psd(out_tr)
    out_tr, out_te = normalizar_kernel_fidelidade(out_tr, out_te)
    return out_tr, out_te, shots

def escolher_landmarks_leverage(X, m):
    Krbf = np.exp(-np.square(np.linalg.norm(X[:,None,:]-X[None,:,:], axis=2)))
    _, U = np.linalg.eigh((Krbf+Krbf.T)/2)
    lev = np.sum(U[:,-min(m,len(U)): ]**2, axis=1)
    return np.argsort(-lev)[:m]

def escolher_landmarks_fronteira(X, y, m):
    modelo = SVC(kernel="rbf", C=1.0).fit(X,y)
    margem = np.abs(modelo.decision_function(X))
    escolhidos=[]
    for classe in np.unique(y):
        candidatos=np.where(y==classe)[0]
        escolhidos.extend(candidatos[np.argsort(margem[candidatos])[:max(1,m//2)]].tolist())
    if len(escolhidos)<m:
        escolhidos.extend([i for i in np.argsort(margem) if i not in escolhidos][:m-len(escolhidos)])
    return np.asarray(escolhidos[:m],dtype=int), margem

def medir_nystrom(Ktr, Kte, landmarks, orcamento, rng, ativo=False, margem=None):
    n, nt, m = len(Ktr), len(Kte), len(landmarks)
    probs = np.concatenate([Ktr[:,landmarks].ravel(), Kte[:,landmarks].ravel()])
    n_circ = len(probs)
    if ativo:
        piloto = np.full(n_circ, SHOTS_PILOTO_ATIVO, dtype=int)
        if piloto.sum() >= orcamento: raise ValueError("orçamento insuficiente para o piloto ativo")
        obs_piloto = medir_vetor_fidelidades(probs, piloto, rng)
        variancia = np.sqrt(obs_piloto*(1-obs_piloto)+1/(4*SHOTS_PILOTO_ATIVO))
        sens_tr = 1/(1+np.repeat(margem, m))
        sens_te = np.ones(nt*m)
        pesos = variancia*np.concatenate([sens_tr,sens_te])
        extra = alocar_inteiros(orcamento-piloto.sum(), pesos, minimo=0)
        shots = piloto+extra
    else:
        shots = alocar_inteiros(orcamento, np.ones(n_circ), minimo=1)
    Ctr_obs = medir_vetor_fidelidades(probs[:n*m], shots[:n*m], rng).reshape(n,m)
    Cte_obs = medir_vetor_fidelidades(probs[n*m:], shots[n*m:], rng).reshape(nt,m)
    W = (Ctr_obs[landmarks,:] + Ctr_obs[landmarks,:].T)/2
    W = projetar_psd(W) + 1e-8*np.eye(m)
    Wpinv = np.linalg.pinv(W, rcond=1e-8)
    Kaprox = projetar_psd(Ctr_obs@Wpinv@Ctr_obs.T) + 1e-10*np.eye(n)
    Kaprox_te = Cte_obs@Wpinv@Ctr_obs.T
    Kaprox, Kaprox_te = normalizar_kernel_fidelidade(Kaprox, Kaprox_te)
    return Kaprox, Kaprox_te, shots

if not EXECUTAR_AQUISICAO_ATIVA:
    print("⏭️ Aquisição ativa preparada. Ative somente após o registro OSF.")
else:
    assert EXECUTAR_LAB_GUIADO
    linhas, planos = [], []
    for i_base,(nome,partes) in enumerate(aplicacoes_guiadas.items()):
        Xtr0,Xva0,Xte0,ytr0,yva0,yte0=partes
        Xdev=np.concatenate([Xtr0,Xva0]); ydev=np.concatenate([ytr0,yva0])
        Xdev,ydev=subamostra_estratificada(Xdev,ydev,MAX_TREINO_AQUISICAO,SEED+i_base)
        Xte0,yte0=subamostra_estratificada(Xte0,yte0,MAX_TESTE_AQUISICAO,SEED+100+i_base)
        Xtr,Xte,_,_=preparar_angular(Xdev,Xte0,Xte0)
        qk=FidelityStatevectorKernel(feature_map=feature_map,shots=None)
        Kideal,Kideal_te=qk.evaluate(Xtr),qk.evaluate(Xte,Xtr)
        m=min(N_LANDMARKS,len(Xtr)//3)
        lev=escolher_landmarks_leverage(Xtr,m)
        front,margem=escolher_landmarks_fronteira(Xtr,ydev,m)
        for seed_aq in SEEDS_AQUISICAO:
            estrategias={
                "matriz_uniforme": None,
                "nystrom_aleatorio": np.random.default_rng(seed_aq).choice(len(Xtr),m,replace=False),
                "nystrom_leverage_rbf": lev,
                "aquisicao_ativa_fronteira": front,
            }
            for estrategia,landmarks in estrategias.items():
                rng=np.random.default_rng(seed_aq+1000*i_base)
                if estrategia=="matriz_uniforme":
                    Kobs,Kobs_te,shots=medir_kernel_completo(Kideal,Kideal_te,ORCAMENTO_SHOTS_AQUISICAO,rng)
                    landmarks_txt="todos"
                else:
                    Kobs,Kobs_te,shots=medir_nystrom(
                        Kideal,Kideal_te,np.asarray(landmarks),ORCAMENTO_SHOTS_AQUISICAO,rng,
                        ativo=estrategia=="aquisicao_ativa_fronteira",margem=margem
                    )
                    landmarks_txt=",".join(map(str,landmarks))
                pred=SVC(kernel="precomputed",C=1.0).fit(Kobs,ydev).predict(Kobs_te)
                bac=balanced_accuracy_score(yte0,pred)
                erro=erro_frobenius_relativo(Kideal,Kobs); sobreviv=float(np.clip(1-erro,0,1))
                eficiencia=float((bac*sobreviv)/np.log1p(ORCAMENTO_SHOTS_AQUISICAO))
                linhas.append({
                    "aplicacao":nome,"seed":seed_aq,"estrategia":estrategia,
                    "BAC":bac,"erro_geometrico":erro,"sobrevivencia_geometrica":sobreviv,
                    "orcamento_shots":int(shots.sum()),"n_circuitos":len(shots),
                    "shots_min":int(shots.min()),"shots_mediana":float(np.median(shots)),
                    "shots_max":int(shots.max()),"eficiencia_BAC_geometria_logshot":eficiencia,
                    "selecao_sem_teste":True,
                })
                planos.append({"aplicacao":nome,"seed":seed_aq,"estrategia":estrategia,"landmarks":landmarks_txt,"shots_total":int(shots.sum())})
    resultados_aquisicao_ativa_df=pd.DataFrame(linhas)
    planos_medicao_aquisicao_df=pd.DataFrame(planos)
    display(resultados_aquisicao_ativa_df.groupby(["aplicacao","estrategia"],as_index=False).agg(
        BAC_media=("BAC","mean"),sobrevivencia_media=("sobrevivencia_geometrica","mean"),
        eficiencia_media=("eficiencia_BAC_geometria_logshot","mean")
    ).style.format({"BAC_media":"{:.3f}","sobrevivencia_media":"{:.3f}","eficiencia_media":"{:.5f}"}))
    assert resultados_aquisicao_ativa_df.groupby(["aplicacao","seed"])["orcamento_shots"].nunique().eq(1).all()
    assert resultados_aquisicao_ativa_df["selecao_sem_teste"].all()
    print("✅ Estratégias comparadas sob orçamento idêntico e sem seleção pelo teste.")
""")

md(r"""
## 7.5 — Adaptador seguro para dados próprios

Requisitos: alvo binário, ao menos duas variáveis numéricas e unidade de análise definida. O adaptador trata ausências, reduz dimensionalidade e escala dados **apenas após o split**.

- Use split temporal quando o objetivo prevê o futuro.
- Exclua identificadores, variáveis pós-desfecho e proxies de vazamento.
- Em saúde, educação ou dados pessoais: anonimize, documente consentimento/base legal, avalie subgrupos e não transforme o resultado em decisão automática de alto impacto.
- O pipeline aceita somente variáveis numéricas nesta edição; categorias exigem codificação dentro de cada fold.
""")

code(r"""
# @title 7.5 — CSV real: preparação e benchmark sem vazamento {display-mode: "form"}
USAR_CSV_PROPRIO = False  # @param {type:"boolean"}
COLUNA_ALVO = "alvo"  # @param {type:"string"}
COLUNAS_EXCLUIR = "id"  # @param {type:"string"}
TIPO_SPLIT = "estratificado"  # @param ["estratificado", "temporal"]
COLUNA_TEMPO = "data"  # @param {type:"string"}

resultado_aplicacao_csv = {}
dados_aplicacao_preparados = {}

if not USAR_CSV_PROPRIO:
    print("⏭️ Adaptador CSV desativado. Ative somente após definir alvo, split e exclusões.")
else:
    from google.colab import files
    from sklearn.preprocessing import LabelEncoder

    enviados = files.upload()
    assert len(enviados) == 1, "Envie um CSV por execução."
    nome_csv = next(iter(enviados))
    dados_proprios = pd.read_csv(nome_csv)
    assert COLUNA_ALVO in dados_proprios.columns, f"Alvo ausente: {COLUNA_ALVO}"

    exclusoes = [c.strip() for c in COLUNAS_EXCLUIR.split(",") if c.strip()]
    colunas_numericas = dados_proprios.select_dtypes(include="number").columns.tolist()
    colunas_features = [
        c for c in colunas_numericas if c != COLUNA_ALVO and c not in exclusoes
    ]
    assert len(colunas_features) >= 2, "São necessárias ao menos duas variáveis numéricas."

    dados_modelo = dados_proprios.dropna(subset=[COLUNA_ALVO]).copy()
    if len(dados_modelo) > MAX_AMOSTRAS_POR_BASE and TIPO_SPLIT != "temporal":
        dados_modelo, _ = train_test_split(
            dados_modelo,
            train_size=MAX_AMOSTRAS_POR_BASE,
            stratify=dados_modelo[COLUNA_ALVO],
            random_state=SEED,
        )
    codificador_alvo = LabelEncoder()
    y_proprio = codificador_alvo.fit_transform(dados_modelo[COLUNA_ALVO])
    assert len(np.unique(y_proprio)) == 2, "Este protocolo requer alvo binário."

    if TIPO_SPLIT == "temporal":
        assert COLUNA_TEMPO in dados_modelo.columns, f"Coluna temporal ausente: {COLUNA_TEMPO}"
        ordem = pd.to_datetime(dados_modelo[COLUNA_TEMPO], errors="raise").sort_values().index
        dados_modelo = dados_modelo.loc[ordem]
        if len(dados_modelo) > MAX_AMOSTRAS_POR_BASE:
            dados_modelo = dados_modelo.iloc[-MAX_AMOSTRAS_POR_BASE:].copy()
        y_proprio = codificador_alvo.transform(dados_modelo[COLUNA_ALVO])
        corte = int(0.75 * len(dados_modelo))
        idx_tr_local = np.arange(corte)
        idx_te_local = np.arange(corte, len(dados_modelo))
    else:
        idx_tr_local, idx_te_local = train_test_split(
            np.arange(len(dados_modelo)),
            test_size=0.25,
            stratify=y_proprio,
            random_state=SEED,
        )

    X_proprio_raw = dados_modelo[colunas_features].to_numpy(dtype=float)
    Xp_tr_raw, Xp_te_raw = X_proprio_raw[idx_tr_local], X_proprio_raw[idx_te_local]
    yp_tr, yp_te = y_proprio[idx_tr_local], y_proprio[idx_te_local]
    assert set(idx_tr_local).isdisjoint(set(idx_te_local))
    assert len(np.unique(yp_tr)) == len(np.unique(yp_te)) == 2

    preprocessador_csv = Pipeline([
        ("imputador", SimpleImputer(strategy="median")),
        ("padronizador", StandardScaler()),
        ("pca", PCA(n_components=2, random_state=SEED)),
        ("angulo", MinMaxScaler((0, np.pi))),
    ])
    Xp_tr = preprocessador_csv.fit_transform(Xp_tr_raw)
    Xp_te = preprocessador_csv.transform(Xp_te_raw)

    cv_csv = StratifiedKFold(n_splits=3, shuffle=True, random_state=SEED)
    busca_rbf_csv = GridSearchCV(
        SVC(kernel="rbf"),
        {"C": GRADE_C, "gamma": GRADE_GAMMA_RBF},
        scoring="balanced_accuracy",
        cv=cv_csv,
        n_jobs=-1,
    ).fit(Xp_tr, yp_tr)
    pred_rbf_csv = busca_rbf_csv.predict(Xp_te)

    qk_csv = FidelityStatevectorKernel(feature_map=feature_map, shots=SHOTS, enforce_psd=True)
    Kp_tr = qk_csv.evaluate(Xp_tr)
    Kp_te = qk_csv.evaluate(Xp_te, Xp_tr)
    busca_qml_csv = GridSearchCV(
        SVC(kernel="precomputed"),
        {"C": GRADE_C},
        scoring="balanced_accuracy",
        cv=cv_csv,
        n_jobs=1,
    ).fit(Kp_tr, yp_tr)
    pred_qml_csv = busca_qml_csv.predict(Kp_te)

    bac_rbf_csv = balanced_accuracy_score(yp_te, pred_rbf_csv)
    bac_qml_csv = balanced_accuracy_score(yp_te, pred_qml_csv)
    resultado_aplicacao_csv = {
        "arquivo": nome_csv,
        "tipo_split": TIPO_SPLIT,
        "n_treino": int(len(yp_tr)),
        "n_teste": int(len(yp_te)),
        "n_features_originais": int(len(colunas_features)),
        "n_componentes_quanticos": 2,
        "bac_rbf": float(bac_rbf_csv),
        "bac_qml": float(bac_qml_csv),
        "delta_bac": float(bac_qml_csv - bac_rbf_csv),
        "C_rbf": busca_rbf_csv.best_params_["C"],
        "C_qml": busca_qml_csv.best_params_["C"],
        "classes": [str(c) for c in codificador_alvo.classes_],
        "aviso": "resultado exploratório; requer CV aninhada e governança de dados",
    }
    dados_aplicacao_preparados = {
        "X_treino": Xp_tr,
        "X_teste": Xp_te,
        "y_treino": yp_tr,
        "y_teste": yp_te,
    }
    display(pd.Series(resultado_aplicacao_csv, name="valor").to_frame())

    assert Xp_tr.shape[1] == Xp_te.shape[1] == 2
    assert np.all((Xp_tr >= -1e-12) & (Xp_tr <= np.pi + 1e-12))
    print("✅ Aplicação CSV executada com preprocessing ajustado somente no treino.")
""")

code(r"""
# @title 7.6 — Exportar pacote de resultados e manuscrito {display-mode: "form"}
BAIXAR_PACOTE_AO_FINAL = False  # @param {type:"boolean"}
import shutil
from pathlib import Path

pasta_resultados = Path("resultados_quantum_ia")
pasta_resultados.mkdir(exist_ok=True)

resultados_df.to_csv(pasta_resultados / "comparacao_modelos.csv", index=False)
intervalos_df.to_csv(pasta_resultados / "intervalos_bootstrap.csv", index=False)
pd.DataFrame([diagnostico_kernel]).to_csv(pasta_resultados / "diagnostico_kernel.csv", index=False)
np.savez_compressed(
    pasta_resultados / "matrizes_e_split.npz",
    X_treino=X_treino,
    X_teste=X_teste,
    y_treino=y_treino,
    y_teste=y_teste,
    K_treino_bruto_apos_psd=K_treino_bruto,
    K_teste_bruto_apos_psd=K_teste_bruto,
    K_treino=K_treino,
    K_teste=K_teste,
)

config_experimento = {
    "pesquisador": NOME_PESQUISADOR,
    "projeto": PROJETO,
    "seed": SEED,
    "shots": SHOTS,
    "modo_rapido": MODO_RAPIDO,
    "n_treino": len(X_treino),
    "n_teste": len(X_teste),
    "feature_map": "ZZFeatureMap",
    "feature_map_reps": 1,
    "entanglement": "linear",
    "C_svm": 1.0,
    "tempo_kernel_s": tempo_kernel,
    "alinhamento_kernel_alvo": alinhamento,
    "desvio_diagonal_bruta_apos_psd": float(diagonal_max_bruta),
    "normalizacao_kernel": "D^(-1/2) K D^(-1/2)",
    "tolerancia_diagonal": TOL_DIAGONAL,
    "hash_protocolo": HASH_PROTOCOLO,
    "osf_registration_url": OSF_REGISTRATION_URL,
    "status_gate_osf": STATUS_GATE_OSF,
    "url_osf_validada_sintaticamente": URL_OSF_VALIDA,
    "data_corte_literatura": DATA_CORTE_LITERATURA,
    "validacao_robusta_executada": not validacao_robusta_df.empty,
    "escada_ruido_executada": K_treino_ruidoso is not None,
    "suite_aplicacoes_executada": not resultados_aplicacoes_df.empty,
    "lab_guiado_executado": not parecer_aplicacoes_guiadas_df.empty,
    "lab_guiado_selecao": "validacao_exclusivamente",
    "lab_guiado_teste_aberto_uma_vez": bool(
        not parecer_aplicacoes_guiadas_df.empty
        and parecer_aplicacoes_guiadas_df["aberturas_teste"].eq(1).all()
    ),
    "breastmnist_uso_clinico": False,
    "pneumoniamnist_uso_clinico": False,
    "paper_avancado_executado": not resultados_baselines_fortes_df.empty,
    "curvas_aprendizagem_executadas": not resultados_curvas_df.empty,
    "ruido_aninhado_executado": not resultados_ruido_aninhado_df.empty,
    "modelo_multinivel_executado": bool(resultado_modelo_multinivel),
    "qus_status": (
        "validacao_tecnica_externa_hardware_pendente" if not tabela_qus_df.empty else "aguardando_execucao"
    ),
    "benchmark_ampliado_status": status_benchmark_ampliado,
    "baselines_deep_status": status_deep_imagens,
    "aquisicao_ativa_executada": not resultados_aquisicao_ativa_df.empty,
    "versoes": VERSOES,
}

with open(pasta_resultados / "configuracao.json", "w", encoding="utf-8") as f:
    json.dump(config_experimento, f, ensure_ascii=False, indent=2)

with open(pasta_resultados / "portao_evidencia.json", "w", encoding="utf-8") as f:
    json.dump(portao_evidencia, f, ensure_ascii=False, indent=2)

with open(pasta_resultados / "protocolo_pre_registrado.json", "w", encoding="utf-8") as f:
    json.dump(PROTOCOLO_PRE_REGISTRADO, f, ensure_ascii=False, indent=2)
(pasta_resultados / "protocolo_sha256.txt").write_text(
    HASH_PROTOCOLO + "\n", encoding="utf-8"
)
shutil.copy2(pasta_osf / "protocolo_osf.md", pasta_resultados / "protocolo_osf.md")
shutil.copy2(
    pasta_osf / "manifesto_pre_registro.json",
    pasta_resultados / "manifesto_pre_registro.json",
)
for nome_anexo_osf in [
    "formulario_osf_preenchido.md",
    "formulario_osf_campos.json",
    "dicionario_variaveis_osf.csv",
]:
    shutil.copy2(pasta_osf / nome_anexo_osf, pasta_resultados / nome_anexo_osf)

escada_kernel_df.to_csv(pasta_resultados / "escada_validade_kernel.csv", index=False)

# Materiais didáticos também são artefatos versionáveis: permitem auditar se a
# divulgação preserva a tradução formal e explicita onde cada analogia falha.
catalogo_analogias_df = pd.DataFrame([
    {"conceito": conceito, **conteudo}
    for conceito, conteudo in ANALOGIAS_RIGOROSAS.items()
])
catalogo_analogias_df.to_csv(
    pasta_resultados / "catalogo_analogias_rigorosas.csv", index=False
)
with open(pasta_resultados / "mapas_mentais.json", "w", encoding="utf-8") as f:
    json.dump(MAPAS_DIDATICOS, f, ensure_ascii=False, indent=2)

if resultados_ablação:
    pd.DataFrame(resultados_ablação).to_csv(pasta_resultados / "ablacoes.csv", index=False)
if not validacao_robusta_df.empty:
    validacao_robusta_df.to_csv(pasta_resultados / "validacao_aninhada_repetida.csv", index=False)
if not tabela_testes_paper.empty:
    tabela_testes_paper.to_csv(pasta_resultados / "tabela_testes_estatisticos.csv", index=False)
    with open(pasta_resultados / "analise_estatistica_paper.json", "w", encoding="utf-8") as f:
        json.dump(analise_estatistica_paper, f, ensure_ascii=False, indent=2)
if not resultados_aplicacoes_df.empty:
    resultados_aplicacoes_df.to_csv(pasta_resultados / "suite_aplicacoes_folds.csv", index=False)
    with open(pasta_resultados / "analise_mecanistica_aplicacoes.json", "w", encoding="utf-8") as f:
        json.dump(analise_mecanistica_aplicacoes, f, ensure_ascii=False, indent=2)
if not busca_ruido_aplicacoes_df.empty:
    busca_ruido_aplicacoes_df.to_csv(
        pasta_resultados / "busca_ruido_aplicacoes.csv", index=False
    )
if not parecer_aplicacoes_guiadas_df.empty:
    parecer_aplicacoes_guiadas_df.to_csv(
        pasta_resultados / "parecer_aplicacoes_guiadas.csv", index=False
    )
    with open(
        pasta_resultados / "parametros_ruido_selecionados.json", "w", encoding="utf-8"
    ) as f:
        json.dump(parametros_ruido_selecionados, f, ensure_ascii=False, indent=2)
if not resultados_baselines_fortes_df.empty:
    resultados_baselines_fortes_df.to_csv(
        pasta_resultados / "baselines_fortes_representacoes.csv", index=False
    )
if not resultados_curvas_df.empty:
    resultados_curvas_df.to_csv(pasta_resultados / "curvas_aprendizagem.csv", index=False)
    diagnosticos_concentracao_df.to_csv(
        pasta_resultados / "diagnosticos_concentracao_kernel.csv", index=False
    )
if not resultados_generalizacao_df.empty:
    resultados_generalizacao_df.to_csv(
        pasta_resultados / "controles_generalizacao.csv", index=False
    )
if not resultados_ruido_aninhado_df.empty:
    resultados_ruido_aninhado_df.to_csv(
        pasta_resultados / "ruido_aninhado_multissemente.csv", index=False
    )
    resumo_ruido_aninhado_df.to_csv(
        pasta_resultados / "resumo_ruido_aninhado.csv", index=False
    )
if resultado_modelo_multinivel:
    with open(pasta_resultados / "modelo_multinivel.json", "w", encoding="utf-8") as f:
        json.dump(resultado_modelo_multinivel, f, ensure_ascii=False, indent=2)
if not tabela_qus_df.empty:
    tabela_qus_df.to_csv(
        pasta_resultados / "qus_prospectivo_validacao_tecnica.csv", index=False
    )
    calibracao_qus_df.to_csv(pasta_resultados / "calibracao_qus.csv",index=False)
    with open(pasta_resultados / "validacao_qus.json","w",encoding="utf-8") as f:
        json.dump(resultado_validacao_qus,f,ensure_ascii=False,indent=2)
if not resultados_deep_imagens_df.empty:
    resultados_deep_imagens_df.to_csv(pasta_resultados / "baselines_deep_imagens.csv",index=False)
if not curvas_decisao_imagens_df.empty:
    curvas_decisao_imagens_df.to_csv(pasta_resultados / "curvas_decisao_imagens.csv",index=False)
if not historico_cnn_df.empty:
    historico_cnn_df.to_csv(pasta_resultados / "historico_treino_cnn.csv",index=False)
if modelos_cnn_treinados:
    import torch
    torch.save(
        {nome:modelo.state_dict() for nome,modelo in modelos_cnn_treinados.items()},
        pasta_resultados / "pesos_cnn_pequena.pt"
    )
if not resultados_benchmark_ampliado_df.empty:
    resultados_benchmark_ampliado_df.to_csv(pasta_resultados / "benchmark_ampliado_10mais.csv",index=False)
    catalogo_bases_ampliado_df.to_csv(pasta_resultados / "catalogo_bases_ampliado.csv",index=False)
if not resultados_aquisicao_ativa_df.empty:
    resultados_aquisicao_ativa_df.to_csv(pasta_resultados / "aquisicao_ativa_orcamento_igual.csv",index=False)
    planos_medicao_aquisicao_df.to_csv(pasta_resultados / "planos_medicao_aquisicao.csv",index=False)
if resultado_aplicacao_csv:
    with open(pasta_resultados / "resultado_aplicacao_csv.json", "w", encoding="utf-8") as f:
        json.dump(resultado_aplicacao_csv, f, ensure_ascii=False, indent=2)

matriz_novidade = pd.DataFrame([
    {
        "fonte": "Bowles, Ahmed e Schuld (2024)",
        "status": "preprint",
        "contribuicao_existente": "benchmarking rigoroso, baselines fortes e crítica a alegações simplistas",
        "sobreposicao_com_este_protocolo": "justiça de comparação e controle de alegações",
        "lacuna_residual_aparente": "não estabelece a sequência operacional multietapa usada neste Evidence Gate",
        "implicacao": "reduz a novidade de qualquer contribuição baseada apenas em benchmark",
        "identificador": "10.48550/arXiv.2403.07059",
    },
    {
        "fonte": "Heyraud et al. (2022)",
        "status": "publicado",
        "contribuicao_existente": "efeito do ruído, espectro e posto efetivo em máquinas de kernel quântico",
        "sobreposicao_com_este_protocolo": "deformação geométrica e diagnóstico espectral",
        "lacuna_residual_aparente": "transformar diagnóstico geométrico em regra pré-especificada de progressão",
        "implicacao": "posto efetivo não pode ser reivindicado como contribuição original",
        "identificador": "10.1103/PhysRevA.106.052421",
    },
    {
        "fonte": "Sahin et al. (2025)",
        "status": "preprint",
        "contribuicao_existente": "KTA e Nyström para reduzir avaliações, com testes sob ruído coerente e despolarizante",
        "sobreposicao_com_este_protocolo": "custo, KTA e robustez ao ruído",
        "lacuna_residual_aparente": "não combina inferência pareada corrigida, equivalência e progressão ideal→QPU",
        "implicacao": "qualquer alegação de eficiência deve comparar também aproximação Nyström",
        "identificador": "10.48550/arXiv.2502.08225",
    },
    {
        "fonte": "Yin et al. (2025)",
        "status": "publicado",
        "contribuicao_existente": "demonstração experimental de kernel fotônico com comparação a kernels clássicos",
        "sobreposicao_com_este_protocolo": "validação em hardware e diferença geométrica",
        "lacuna_residual_aparente": "plataforma e tarefas construídas diferem do fluxo tabular IBM/Qiskit aqui avaliado",
        "implicacao": "vantagem experimental já foi mostrada em contexto fotônico específico; não generalizar",
        "identificador": "10.1038/s41566-025-01682-5",
    },
    {
        "fonte": "Kakavand, Strohmeyer e Schlotter (2026)",
        "status": "preprint",
        "contribuicao_existente": "970 experimentos, CV aninhada, espectro, custo e validação IBM em nove bases",
        "sobreposicao_com_este_protocolo": "sobreposição forte em desenho, baselines, espectro, custo e hardware",
        "lacuna_residual_aparente": "avaliar uma regra prospectiva que condicione QPU ao conjunto inferência+geometria+custo",
        "implicacao": "a novidade não pode ser 'benchmark rigoroso com hardware'; deve ser a regra decisória pré-registrada",
        "identificador": "10.48550/arXiv.2604.18837",
    },
    {
        "fonte": "AQKA (2026)",
        "status": "preprint",
        "contribuicao_existente": "aquisição ativa de pares e alocação de shots orientada por sensibilidade em hardware IBM",
        "sobreposicao_com_este_protocolo": "pares-âncora, orçamento de shots e progressão para hardware",
        "lacuna_residual_aparente": "o Evidence Gate avalia se deve avançar; AQKA otimiza como medir após avançar",
        "implicacao": "âncoras uniformes são baseline mínimo; AQKA/Nyström devem constar como extensões de custo",
        "identificador": "10.48550/arXiv.2605.14672",
    },
    {
        "fonte": "Nadeau e Bengio (2003)",
        "status": "publicado",
        "contribuicao_existente": "inferência corrigida para estimativas dependentes de erro de generalização",
        "sobreposicao_com_este_protocolo": "erro-padrão corrigido em CV repetida",
        "lacuna_residual_aparente": "aplicação integrada ao fluxo de decisão QML",
        "implicacao": "a correção estatística é adaptação metodológica, não novidade teórica",
        "identificador": "10.1023/A:1024068626366",
    },
    {
        "fonte": "Contribuição candidata deste estudo",
        "status": "hipótese pré-registrável",
        "contribuicao_existente": "não aplicável; contribuição ainda será testada",
        "sobreposicao_com_este_protocolo": "Evidence Gate prospectivo e sequencial",
        "lacuna_residual_aparente": (
            "utilidade de uma regra go/no-go pré-especificada que integra efeito pareado corrigido, "
            "equivalência, sobrevivência geométrica, custo e pares-âncora antes do classificador QPU"
        ),
        "implicacao": (
            "formular como contribuição candidata; não usar 'primeiro' sem revisão sistemática, "
            "dupla triagem e atualização na data de submissão"
        ),
        "identificador": "OSF/DOI a preencher após registro",
    },
])
matriz_novidade["data_corte_busca"] = DATA_CORTE_LITERATURA
matriz_novidade.to_csv(pasta_resultados / "matriz_auditoria_novidade.csv", index=False)

metodos_paper = f'''
# Métodos — versão gerada automaticamente

## Desenho

Estudo computacional comparativo, pré-especificado pelo hash `{HASH_PROTOCOLO}`. O desfecho primário foi a diferença pareada de acurácia balanceada entre um SVM com kernel quântico de fidelidade e um SVM-RBF. A seleção de hiperparâmetros ocorreu exclusivamente nos dados de desenvolvimento.

## Validação

Foi definida validação cruzada aninhada repetida com quatro folds externos e três repetições (12 avaliações externas). Em cada fold externo, a transformação imputação–padronização–PCA–escala angular foi ajustada apenas no treino. A seleção interna utilizou três folds estratificados, `C ∈ {GRADE_C}` para ambos os SVMs e `gamma ∈ {GRADE_GAMMA_RBF}` para o RBF.

## Kernel quântico

O mapa ZZ utilizou dois qubits, uma repetição e entrelaçamento linear. A matriz foi avaliada em referência exata, {SHOTS} shots, ruído Aer e, opcionalmente, pares-âncora em QPU. Foram registrados alinhamento kernel–alvo, posto efetivo, erro de Frobenius relativo, variância fora da diagonal, separação intra/interclasse, condição e entropia espectral, tempo e avaliações lógicas. A matriz reparada como PSD foi normalizada por D^(-1/2)KD^(-1/2), preservando o espectro não negativo e restaurando diagonal unitária.

## Baselines, imagens e curvas

Foram pré-especificados Dummy estratificado, regressão logística, SVM linear, SVM-RBF, Random Forest e HistGradientBoosting na mesma representação bidimensional. Para imagens, HOG foi comparado à entrada vetorizada; um SVM-RBF com até 32 componentes, uma CNN pequena e uma ResNet-18 congelada atuaram como tetos clássicos e não como contrastes quânticos de recursos equivalentes. Foram registrados Brier, ECE e curvas de decisão sem interpretação clínica. Curvas de aprendizagem foram repetidas nos dados de desenvolvimento, sem consulta ao teste.

## Ruído e generalização

Perfis de ruído foram selecionados dentro de cada fold por BAC média em cinco seeds, com desempate por menor deformação e carga. O fold externo foi avaliado somente depois do congelamento. Permutações de rótulos e perturbações angulares funcionaram como controles negativos e de deslocamento.

## Validade externa e eficiência de medição

O benchmark ampliado reuniu sete bases locais/sintéticas e seis fontes OpenML com IDs fixos, checksums e registro explícito de falhas; somente execuções com dez ou mais bases autorizam a alegação ampliada. Z, ZZ linear, ZZ full e Pauli participaram da seleção interna. Matriz completa, Nyström aleatório, Nyström por leverage scores e aquisição ativa foram comparados com o mesmo total de shots lógicos. Landmarks e alocação foram definidos sem o teste.

## Estatística

O teste primário unilateral utilizou a correção de Nadeau–Bengio para dependência entre folds (α={ALPHA}). O IC bilateral de 95%, a permutação exata de sinais, o tamanho de efeito pareado dz e TOST com margem ±{MARGEM_EQUIVALENCIA_BAC:.2f} foram análises pré-especificadas. Desfechos secundários receberam ajuste de Holm. A hipótese mecanística ampliada utilizou efeitos mistos com intercepto por aplicação e regressão agrupada como sensibilidade. O QUS foi calculado apenas com validação interna e confrontado, sem reajuste, com utilidade preservada no fold externo; validação em hardware permaneceu pendente.

## Limites

Simulação em pequena escala, apenas três aplicações principais, compressão para dois componentes, custo quadrático do kernel, poucos clusters para o modelo multinível, QUS ainda não validado e ausência de validade clínica/operacional direta.
'''
(pasta_resultados / "paper_metodos.md").write_text(metodos_paper.strip() + "\n", encoding="utf-8")

if analise_estatistica_paper:
    ic_paper = analise_estatistica_paper["ic95_corrigido_bilateral"]
    resultados_paper = f'''
# Resultados — rascunho automático

Na validação aninhada repetida, a diferença média do desfecho primário foi de {analise_estatistica_paper["media_delta_bac"]:+.4f}, com IC95% corrigido [{ic_paper[0]:+.4f}; {ic_paper[1]:+.4f}] e p unilateral corrigido de {analise_estatistica_paper["p_primario_corrigido"]:.4g}. O teste de equivalência apresentou p={analise_estatistica_paper["p_tost_equivalencia"]:.4g}. A classificação pré-especificada foi: **{analise_estatistica_paper["classificacao"]}**.

Este texto descreve somente o protocolo executado. Complete a análise multibase, a escada de ruído, os intervalos, tabelas e limitações antes da submissão.
'''
else:
    resultados_paper = '''
# Resultados — aguardando execução confirmatória

Ative `EXECUTAR_VALIDACAO_ROBUSTA`, execute o notebook integralmente e regenere o pacote. Não preencha conclusões antes da análise pré-especificada.
'''
(pasta_resultados / "paper_resultados.md").write_text(resultados_paper.strip() + "\n", encoding="utf-8")

regras_alegacao = '''
# Auditoria de alegações

- Não afirmar “primeiro estudo” sem revisão sistemática atualizada e estratégia de busca anexada.
- Não afirmar “vantagem quântica” a partir de acurácia em simulador.
- Distinguir superioridade preditiva, equivalência prática, sobrevivência geométrica e vantagem computacional.
- Reportar resultados nulos e negativos.
- Identificar como exploratória qualquer análise não congelada no protocolo.
- Preservar custos, seeds/folds, versões, matrizes e código.
'''
(pasta_resultados / "auditoria_alegacoes.md").write_text(
    regras_alegacao.strip() + "\n", encoding="utf-8"
)

referencias_abnt = '''
BOWLES, Joseph; AHMED, Shahnawaz; SCHULD, Maria. Better than classical? The subtle art of benchmarking quantum machine learning models. arXiv, 2024. DOI: 10.48550/arXiv.2403.07059.

HEYRAUD, Valentin et al. Noisy quantum kernel machines. Physical Review A, v. 106, art. 052421, 2022. DOI: 10.1103/PhysRevA.106.052421.

KAKAVAND, Siavash; STROHMEYER, Christoph; SCHLOTTER, Michael. Benchmarking Quantum Kernel Support Vector Machines Against Classical Baselines on Tabular Data: A Rigorous Empirical Study with Hardware Validation. arXiv, 2026. DOI: 10.48550/arXiv.2604.18837.

SAHIN, Enes et al. Quantum-Efficient Kernel Target Alignment. arXiv, 2025. DOI: 10.48550/arXiv.2502.08225.

YIN, Zhenghao et al. Experimental quantum-enhanced kernel-based machine learning on a photonic processor. Nature Photonics, v. 19, p. 1020–1027, 2025. DOI: 10.1038/s41566-025-01682-5.

ACTIVE QUANTUM KERNEL ACQUISITION UNDER A SHOT BUDGET. arXiv, 2026. DOI: 10.48550/arXiv.2605.14672.

NADEAU, Claude; BENGIO, Yoshua. Inference for the Generalization Error. Machine Learning, v. 52, n. 3, p. 239–281, 2003. DOI: 10.1023/A:1024068626366.

YANG, Jiancheng et al. MedMNIST v2: A large-scale lightweight benchmark for 2D and 3D biomedical image classification. Scientific Data, v. 10, art. 41, 2023. DOI: 10.1038/s41597-022-01721-8.

GIL-FUSTER, Elies; EISERT, Jens; BRAVO-PRIETO, Carlos. Understanding quantum machine learning also requires rethinking generalization. Nature Communications, v. 15, art. 2277, 2024. DOI: 10.1038/s41467-024-45882-z.

INCUDINI, Marco et al. Mitigating exponential concentration in covariant quantum kernels for subspace and real-world data. npj Quantum Information, 2025. DOI: 10.1038/s41534-025-01154-2.

HUANG, Hsiang-Wei et al. Noise-enhanced quantum kernels on analog quantum computers. arXiv, 2026. DOI: 10.48550/arXiv.2604.12476.

MIROSZEWSKI, Artur et al. Adaptive Measurement Allocation for Learning Kernelized Quantum Models. arXiv, 2026. DOI: 10.48550/arXiv.2605.22275.
'''
(pasta_resultados / "referencias_abnt.md").write_text(
    referencias_abnt.strip() + "\n", encoding="utf-8"
)

# Pacote FAIR/RO-Crate mínimo: ambiente, cartões e checksums dos artefatos.
requirements_lock = "\n".join([
    f"numpy=={np.__version__}", f"pandas=={pd.__version__}",
    f"scikit-learn=={sklearn.__version__}", f"scikit-image=={skimage.__version__}",
    f"statsmodels=={statsmodels.__version__}", f"medmnist=={medmnist.__version__}",
    f"torch=={VERSOES['torch']}", f"torchvision=={VERSOES['torchvision']}",
    f"qiskit=={qiskit.__version__}", f"qiskit-aer=={qiskit_aer.__version__}",
    f"qiskit-machine-learning=={qiskit_machine_learning.__version__}",
]) + "\n"
(pasta_resultados / "requirements_lock.txt").write_text(requirements_lock,encoding="utf-8")

data_cards = '''
# Cartões de dados

- Iris, Wine, Digits e Breast Cancer Wisconsin: distribuições do scikit-learn; verificar a fonte original citada pelo loader.
- make_moons, make_circles e make_classification: controles sintéticos gerados por seed, sem validade externa.
- BreastMNIST e PneumoniaMNIST: MedMNIST v2, imagens 28x28 e splits oficiais; uso exclusivamente metodológico, sem decisão clínica.
- OpenML: IDs fixos, cache e checksum por base; falhas de recuperação permanecem registradas.
- Limites: subamostragem por custo O(n²), compressão angular e representação binária.
'''
(pasta_resultados / "data_cards.md").write_text(data_cards.strip()+"\n",encoding="utf-8")

model_card = '''
# Cartão dos modelos

Finalidade: benchmark metodológico de kernels quânticos e baselines clássicos.
Uso proibido: diagnóstico, prognóstico ou decisão automatizada sobre pessoas.
Desfecho primário: diferença pareada de acurácia balanceada.
Baselines: Dummy, logística, SVM linear/RBF, floresta, boosting, CNN pequena e embedding congelado.
Riscos: amostras pequenas, compressão para dois componentes, concentração, drift de hardware e custo quadrático.
QUS: escore prospectivo em validação técnica; validação QPU permanece pendente.
'''
(pasta_resultados / "model_card.md").write_text(model_card.strip()+"\n",encoding="utf-8")

entidades_ro=[]
for artefato in sorted(pasta_resultados.iterdir()):
    if artefato.is_file() and artefato.name != "ro-crate-metadata.json":
        entidades_ro.append({
            "@id":artefato.name,"@type":"File","name":artefato.name,
            "contentSize":artefato.stat().st_size,
            "sha256":hashlib.sha256(artefato.read_bytes()).hexdigest(),
        })
ro_crate={
    "@context":"https://w3id.org/ro/crate/1.1/context",
    "@graph":[
        {"@id":"ro-crate-metadata.json","@type":"CreativeWork","about":{"@id":"./"},"conformsTo":{"@id":"https://w3id.org/ro/crate/1.1"}},
        {"@id":"./","@type":"Dataset","name":PROTOCOLO_PRE_REGISTRADO["titulo_provisorio"],
         "description":PROTOCOLO_PRE_REGISTRADO["descricao"],"license":"https://creativecommons.org/licenses/by/4.0/",
         "creator":{"@id":"https://osf.io/user/953q4"},"identifier":HASH_PROTOCOLO},
        {"@id":"https://osf.io/user/953q4","@type":"Person","name":"Marcelo Claro Laranjeira"},
        *entidades_ro,
    ],
}
(pasta_resultados / "ro-crate-metadata.json").write_text(
    json.dumps(ro_crate,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"
)

print("Arquivos gerados:")
for caminho in sorted(pasta_resultados.iterdir()):
    print(" -", caminho)

arquivo_zip = shutil.make_archive("resultados_quantum_ia", "zip", root_dir=pasta_resultados)
print("Pacote compactado:", arquivo_zip)

if BAIXAR_PACOTE_AO_FINAL:
    from google.colab import files
    files.download(arquivo_zip)
""")

md(r"""
# Módulo 8 — QPU real IBM Quantum (opcional)

Execute esta seção somente depois de concluir o simulador.

## Onde obter e onde colocar a chave

1. Crie ou acesse sua conta em **[IBM Quantum Platform](https://quantum.cloud.ibm.com/)**.
2. No painel inicial, escolha a conta e a região corretas e crie uma instância. Para o plano gratuito **Open**, use `us-east`.
3. Crie a API key no painel e copie-a imediatamente para um gerenciador de segredos: a chave de 44 caracteres não volta a ser exibida.
4. Se quiser fixar uma instância, abra **Instances**, copie o CRN e guarde-o separadamente.
5. No Google Colab, abra o ícone **🔑 Secrets** na barra lateral esquerda.
6. Crie um segredo com o nome exato **`IBM_QUANTUM_API_KEY`**, cole a chave no valor e habilite o acesso ao notebook.
7. Opcionalmente, crie **`IBM_QUANTUM_INSTANCE_CRN`** para fixar a instância sem escrever o CRN na célula.

Guias oficiais: **[configurar conta e instância](https://quantum.cloud.ibm.com/docs/guides/cloud-setup)** e **[criar/salvar credenciais](https://quantum.cloud.ibm.com/docs/guides/save-credentials)**.

**Nunca cole a chave diretamente em uma célula, saída, arquivo `.ipynb`, GitHub, OSF ou artigo.** A célula 8.2 lê o segredo sem imprimi-lo e autentica somente em memória. O segredo do Colab é a cópia persistente; `save_account()` não é usado no ambiente hospedado.

### Antes de enviar um job

1. crie/configure sua conta IBM Quantum Platform;
2. guarde a chave em recurso secreto — nunca em célula pública;
3. verifique plano, região, fila e orçamento de tempo;
4. transpile para o backend selecionado;
5. registre nome e versão do QPU, horário, calibração, layout, profundidade e shots;
6. use **job mode** no plano Open; sessões podem não estar disponíveis;
7. compare simulador ideal, modelo de ruído e QPU.

O bloco abaixo fica desativado por segurança e para que “Executar tudo” não envie trabalho remoto.
""")

code(r"""
# @title 8.1 — Instalar acesso ao IBM Quantum (opcional) {display-mode: "form"}
INSTALAR_IBM_RUNTIME = False  # @param {type:"boolean"}

if INSTALAR_IBM_RUNTIME:
    import subprocess
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q", "qiskit-ibm-runtime~=0.47.0"
    ])
    print("✅ Runtime instalado. Se necessário, reinicie a sessão.")
else:
    print("⏭️ Instalação opcional não executada.")
""")

code(r"""
# @title 8.2 — Conectar em memória com Colab Secrets, sem expor a chave {display-mode: "form"}
CONFIGURAR_ACESSO_IBM = False  # @param {type:"boolean"}
IBM_INSTANCE_CRN_FALLBACK = "auto"  # @param {type:"string"}
IBM_REGIAO = "us-east"  # @param ["us-east", "eu-de"]
VALIDAR_LISTA_DE_QPUS = True  # @param {type:"boolean"}

service = None
if not CONFIGURAR_ACESSO_IBM:
    print("⏭️ Acesso IBM não configurado. A chave permanece no cofre do Colab.")
    print("ℹ️ Nenhum job remoto foi criado.")
else:
    from google.colab import userdata
    from qiskit_ibm_runtime import QiskitRuntimeService

    def ler_segredo_colab(nome, obrigatorio=False):
        try:
            valor = userdata.get(nome)
        except Exception as exc:
            if obrigatorio:
                raise RuntimeError(
                    f"Crie o segredo {nome} no painel 🔑 Secrets e habilite o acesso."
                ) from exc
            return None
        valor = valor.strip() if isinstance(valor, str) else valor
        if obrigatorio and not valor:
            raise RuntimeError(f"O segredo {nome} está vazio ou sem acesso habilitado.")
        return valor or None

    chave_ibm = ler_segredo_colab("IBM_QUANTUM_API_KEY", obrigatorio=True)
    if len(chave_ibm) != 44:
        raise RuntimeError(
            "Formato inesperado: a documentação atual descreve a API key IBM com 44 caracteres. "
            "Gere uma nova chave no dashboard e atualize IBM_QUANTUM_API_KEY."
        )

    crn_secreto = ler_segredo_colab("IBM_QUANTUM_INSTANCE_CRN", obrigatorio=False)
    instancia = crn_secreto or IBM_INSTANCE_CRN_FALLBACK.strip()
    argumentos = {
        "channel": "ibm_quantum_platform",
        "token": chave_ibm,
    }
    if instancia and instancia.lower() != "auto":
        argumentos["instance"] = instancia
    else:
        argumentos.update({
            "region": IBM_REGIAO,
            "plans_preference": ["open"],
        })

    # Não chama save_account(): o token não é gravado no sistema de arquivos do Colab.
    service = QiskitRuntimeService(**argumentos)
    del argumentos, chave_ibm, crn_secreto, instancia

    print("✅ Autenticação validada em memória, sem imprimir ou gravar a credencial.")
    print("Instância ativa:", service.active_instance())
    if VALIDAR_LISTA_DE_QPUS:
        qpus = service.backends(simulator=False, operational=True)
        print("QPUs operacionais visíveis:", len(qpus))
        print("Backends:", ", ".join(sorted(b.name for b in qpus)) or "nenhum")
    print("🔒 Teste somente de metadados: nenhum circuito foi enviado e nenhum shot foi consumido.")
""")

code(r"""
# @title 8.3 — Executar Bell em QPU real (desativado por padrão) {display-mode: "form"}
EXECUTAR_EM_QPU = False  # @param {type:"boolean"}

if not EXECUTAR_EM_QPU:
    print("⏭️ Nenhum job remoto foi enviado.")
else:
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

    assert service is not None, (
        "Execute primeiro a célula 8.2 com CONFIGURAR_ACESSO_IBM=True. "
        "A credencial é carregada do Colab Secrets somente em memória."
    )
    backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)
    print("Backend selecionado:", backend.name, "| versão:", backend.backend_version)

    bell_qpu = QuantumCircuit(2)
    bell_qpu.h(0)
    bell_qpu.cx(0, 1)
    bell_qpu.measure_all()

    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    bell_isa = pm.run(bell_qpu)
    sampler_qpu = SamplerV2(mode=backend)
    job = sampler_qpu.run([bell_isa], shots=SHOTS)
    print("Job ID:", job.job_id())

    resultado_qpu = job.result()[0]
    counts_qpu = resultado_qpu.data.meas.get_counts()
    display(plot_histogram(counts_qpu, title=f"Bell em {backend.name}"))
    print(counts_qpu)
""")

md(r"""
## 8.3.1 — Gêmeo de ruído baseado na calibração da QPU

Um ruído Aer escolhido manualmente é um experimento controlado; ele não representa necessariamente o dispositivo. Esta célula captura um snapshot do backend, registra erros/durações por instrução e cria um `NoiseModel.from_backend`. O snapshot recebe hash e pode ser comparado entre dias para medir drift.

Criar o snapshot consulta metadados, mas **não envia circuitos**.
""")

code(r"""
# @title 8.3.1 — Snapshot IBM e Aer calibrado, sem enviar job {display-mode: "form"}
CRIAR_SNAPSHOT_CALIBRACAO = False  # @param {type:"boolean"}
BACKEND_SNAPSHOT = "auto"  # @param {type:"string"}

snapshot_calibracao = {}
simulador_calibrado = None
historico_calibracao_df = pd.DataFrame()

if not CRIAR_SNAPSHOT_CALIBRACAO:
    print("⏭️ Snapshot não criado; nenhum acesso remoto adicional foi realizado.")
else:
    from qiskit_ibm_runtime import QiskitRuntimeService
    from qiskit_aer.noise import NoiseModel
    assert service is not None, (
        "Execute primeiro a célula 8.2 com CONFIGURAR_ACESSO_IBM=True."
    )
    backend_cal = (
        service.least_busy(operational=True, simulator=False, min_num_qubits=feature_map.num_qubits)
        if BACKEND_SNAPSHOT.strip().lower() == "auto" else service.backend(BACKEND_SNAPSHOT.strip())
    )
    target = backend_cal.target
    instrucoes = []
    for nome_operacao in sorted(target.operation_names):
        for qargs in target.qargs_for_operation_name(nome_operacao):
            prop = target[nome_operacao].get(qargs)
            instrucoes.append({
                "operacao": nome_operacao, "qubits": list(qargs),
                "erro": None if prop is None or prop.error is None else float(prop.error),
                "duracao_s": None if prop is None or prop.duration is None else float(prop.duration),
            })
    arestas = []
    try: arestas = [list(e) for e in backend_cal.coupling_map.get_edges()]
    except Exception: pass
    snapshot_calibracao = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "backend": backend_cal.name, "backend_version": str(backend_cal.backend_version),
        "num_qubits": int(backend_cal.num_qubits), "dt_s": getattr(target,"dt",None),
        "instrucoes": instrucoes, "arestas_acoplamento": arestas,
        "fonte": "IBM Quantum backend target",
    }
    texto_snapshot=json.dumps(snapshot_calibracao,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    snapshot_calibracao["sha256"]=hashlib.sha256(texto_snapshot.encode()).hexdigest()
    modelo_calibrado=NoiseModel.from_backend(backend_cal)
    simulador_calibrado=AerSimulator(noise_model=modelo_calibrado)
    arquivo_snapshot=Path(f"snapshot_{backend_cal.name}_{snapshot_calibracao['sha256'][:10]}.json")
    arquivo_snapshot.write_text(json.dumps(snapshot_calibracao,ensure_ascii=False,indent=2),encoding="utf-8")
    resumo_snapshot={
        "timestamp_utc":snapshot_calibracao["timestamp_utc"],"backend":backend_cal.name,
        "backend_version":str(backend_cal.backend_version),"sha256":snapshot_calibracao["sha256"],
        "erro_1q_mediano":float(np.nanmedian([x["erro"] for x in instrucoes if len(x["qubits"])==1 and x["erro"] is not None])),
        "erro_2q_mediano":float(np.nanmedian([x["erro"] for x in instrucoes if len(x["qubits"])==2 and x["erro"] is not None])),
    }
    arquivo_hist=Path("historico_snapshots_calibracao.csv")
    anterior=pd.read_csv(arquivo_hist) if arquivo_hist.exists() else pd.DataFrame()
    historico_calibracao_df=pd.concat([anterior,pd.DataFrame([resumo_snapshot])],ignore_index=True).drop_duplicates("sha256")
    historico_calibracao_df.to_csv(arquivo_hist,index=False)
    if "pasta_resultados" in globals():
        shutil.copy2(arquivo_snapshot,pasta_resultados/arquivo_snapshot.name)
        historico_calibracao_df.to_csv(pasta_resultados/"historico_snapshots_calibracao.csv",index=False)
    display(pd.Series(resumo_snapshot,name="valor").to_frame())
    print("✅ Snapshot e Aer calibrado criados sem envio de job:",arquivo_snapshot)
""")

code(r"""
# @title 8.4 — Pares-âncora do kernel em QPU: teste go/no-go {display-mode: "form"}
EXECUTAR_ANCORAS_QPU = False  # @param {type:"boolean"}
SHOTS_QPU = 1024  # @param {type:"slider", min:256, max:8192, step:256}
ID_SESSAO_QPU = "sessao_01_data_backend"  # @param {type:"string"}
N_BOOTSTRAP_ANCORAS = 5000
APLICAR_MITIGACAO_LEITURA = True  # @param {type:"boolean"}

resultado_ancoras_qpu_df = pd.DataFrame()
diagnostico_ancoras_qpu = {}

if not EXECUTAR_ANCORAS_QPU:
    print("⏭️ Âncoras QPU não enviadas. Nenhum custo remoto foi gerado.")
else:
    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
    from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

    assert service is not None, (
        "Execute primeiro a célula 8.2 com CONFIGURAR_ACESSO_IBM=True."
    )
    backend_ancora = service.least_busy(
        operational=True, simulator=False, min_num_qubits=feature_map.num_qubits
    )
    # Amostragem prospectiva: cobre o espectro ideal e inclui pares próximos da
    # fronteira. Não usa o resultado da QPU para escolher os próprios pares.
    candidatos_pares = []
    decisao_treino = np.abs(modelo_qk.decision_function(K_treino))
    for i in range(len(X_treino)):
        for j in range(i + 1, len(X_treino)):
            candidatos_pares.append({
                "i": i, "j": j, "fidelidade_ideal": float(K_treino_exato[i, j]),
                "mesma_classe": bool(y_treino[i] == y_treino[j]),
                "proximidade_fronteira": float(decisao_treino[i] + decisao_treino[j]),
            })
    candidatos_pares_df = pd.DataFrame(candidatos_pares)
    escolhidos = []
    for q in [0.05, 0.25, 0.50, 0.75, 0.95]:
        alvo_q = candidatos_pares_df["fidelidade_ideal"].quantile(q)
        idx = (candidatos_pares_df["fidelidade_ideal"] - alvo_q).abs().idxmin()
        escolhidos.append((int(candidatos_pares_df.loc[idx, "i"]), int(candidatos_pares_df.loc[idx, "j"])))
    for _, linha in candidatos_pares_df.sort_values("proximidade_fronteira").head(5).iterrows():
        escolhidos.append((int(linha["i"]), int(linha["j"])))
    pares_ancora = list(dict.fromkeys(escolhidos))
    assert len(pares_ancora) >= 8, "Número insuficiente de pares-âncora diversos."
    fidelidades_aer_calibrado = {}
    if simulador_calibrado is not None:
        for i,j in pares_ancora:
            fidelidades_aer_calibrado[(i,j)] = float(avaliar_kernel_aer(
                X_treino[[i]], X_treino[[j]], feature_map, simulador_calibrado,
                SHOTS_QPU, SEED+i*100+j, simetrico=False
            )[0,0])
    circuitos_ancora = [
        circuito_sobreposicao(X_treino[i], X_treino[j], feature_map)
        for i, j in pares_ancora
    ]
    pm_ancora = generate_preset_pass_manager(
        backend=backend_ancora, optimization_level=1, seed_transpiler=SEED
    )
    circuitos_ancora_isa = pm_ancora.run(circuitos_ancora)
    circuitos_calibracao_isa = []
    if APLICAR_MITIGACAO_LEITURA:
        circuitos_calibracao = []
        for estado in range(2**feature_map.num_qubits):
            qc_cal = QuantumCircuit(feature_map.num_qubits)
            for q in range(feature_map.num_qubits):
                if (estado >> q) & 1: qc_cal.x(q)
            qc_cal.measure_all(); circuitos_calibracao.append(qc_cal)
        circuitos_calibracao_isa = pm_ancora.run(circuitos_calibracao)
    sampler_ancora = SamplerV2(mode=backend_ancora)
    circuitos_job = list(circuitos_ancora_isa) + list(circuitos_calibracao_isa)
    job_ancora = sampler_ancora.run(circuitos_job, shots=SHOTS_QPU)
    print("Backend:", backend_ancora.name, "| Job ID:", job_ancora.job_id())

    resultados_job = job_ancora.result()
    resultados_qpu = resultados_job[:len(pares_ancora)]
    matriz_atribuicao = None
    if APLICAR_MITIGACAO_LEITURA:
        resultados_cal = resultados_job[len(pares_ancora):]
        dim = 2**feature_map.num_qubits
        matriz_atribuicao = np.zeros((dim,dim))
        for preparado, resultado_cal in enumerate(resultados_cal):
            counts_cal = resultado_cal.data.meas.get_counts()
            for bitstring, quantidade in counts_cal.items():
                observado = int(bitstring.replace(" ",""),2)
                matriz_atribuicao[observado,preparado] += quantidade/SHOTS_QPU
        inversa_atribuicao = np.linalg.pinv(matriz_atribuicao,rcond=1e-6)
    zero_ancora = "0" * feature_map.num_qubits
    linhas_ancora = []
    for (i, j), circuito_isa, resultado_publicacao in zip(
        pares_ancora, circuitos_ancora_isa, resultados_qpu
    ):
        counts = resultado_publicacao.data.meas.get_counts()
        fidelidade_qpu = counts.get(zero_ancora, 0) / SHOTS_QPU
        fidelidade_qpu_mitigada = np.nan
        if matriz_atribuicao is not None:
            p_obs=np.zeros(2**feature_map.num_qubits)
            for bitstring,quantidade in counts.items():
                p_obs[int(bitstring.replace(" ",""),2)] += quantidade/SHOTS_QPU
            p_corr=np.clip(inversa_atribuicao@p_obs,0,None)
            p_corr=p_corr/p_corr.sum() if p_corr.sum()>0 else p_obs
            fidelidade_qpu_mitigada=float(p_corr[0])
        fidelidade_avaliacao = (
            fidelidade_qpu_mitigada if APLICAR_MITIGACAO_LEITURA else fidelidade_qpu
        )
        fidelidade_ideal = float(K_treino_exato[i, j])
        linhas_ancora.append({
            "i": i,
            "j": j,
            "fidelidade_ideal": fidelidade_ideal,
            "fidelidade_qpu": fidelidade_qpu,
            "fidelidade_qpu_mitigada": fidelidade_qpu_mitigada,
            "fidelidade_qpu_avaliacao": fidelidade_avaliacao,
            "fidelidade_aer_calibrado": fidelidades_aer_calibrado.get((i,j), np.nan),
            "erro_absoluto_bruto": abs(fidelidade_qpu - fidelidade_ideal),
            "erro_absoluto": abs(fidelidade_avaliacao - fidelidade_ideal),
            "erro_aer_qpu": (
                abs(fidelidade_avaliacao-fidelidades_aer_calibrado[(i,j)])
                if (i,j) in fidelidades_aer_calibrado else np.nan
            ),
            "backend": backend_ancora.name,
            "backend_version": str(backend_ancora.backend_version),
            "shots": SHOTS_QPU,
            "job_id": job_ancora.job_id(),
            "id_sessao": ID_SESSAO_QPU,
            "mesma_classe": bool(y_treino[i] == y_treino[j]),
            "proximidade_fronteira": float(decisao_treino[i] + decisao_treino[j]),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "profundidade_isa": int(circuito_isa.depth()),
            "portas_2q_isa": int(sum(
                quantidade for porta, quantidade in circuito_isa.count_ops().items()
                if porta in {"cx", "ecr", "cz"}
            )),
            "layout_isa": str(circuito_isa.layout),
            "snapshot_calibracao_sha256": snapshot_calibracao.get("sha256"),
        })

    resultado_ancoras_qpu_df = pd.DataFrame(linhas_ancora)
    arquivo_historico_ancoras = Path("historico_ancoras_qpu.csv")
    if arquivo_historico_ancoras.exists():
        historico_anterior = pd.read_csv(arquivo_historico_ancoras)
        historico_anterior = historico_anterior.query("id_sessao != @ID_SESSAO_QPU")
        historico_ancoras_qpu_df = pd.concat(
            [historico_anterior, resultado_ancoras_qpu_df], ignore_index=True
        )
    else:
        historico_ancoras_qpu_df = resultado_ancoras_qpu_df.copy()
    historico_ancoras_qpu_df.to_csv(arquivo_historico_ancoras, index=False)

    correlacao_ancoras = float(
        resultado_ancoras_qpu_df["fidelidade_ideal"].corr(
            resultado_ancoras_qpu_df["fidelidade_qpu_avaliacao"]
        )
    )
    mae_ancoras = float(resultado_ancoras_qpu_df["erro_absoluto"].mean())
    mae_aer_qpu = (
        float(resultado_ancoras_qpu_df["erro_aer_qpu"].mean())
        if resultado_ancoras_qpu_df["erro_aer_qpu"].notna().any() else None
    )
    rng_boot = np.random.default_rng(SEED)
    correlacoes_boot = []
    for _ in range(N_BOOTSTRAP_ANCORAS):
        idx = rng_boot.integers(0, len(resultado_ancoras_qpu_df), len(resultado_ancoras_qpu_df))
        amostra = resultado_ancoras_qpu_df.iloc[idx]
        if amostra["fidelidade_ideal"].nunique() > 1 and amostra["fidelidade_qpu_avaliacao"].nunique() > 1:
            r_boot = amostra["fidelidade_ideal"].corr(amostra["fidelidade_qpu_avaliacao"])
            if np.isfinite(r_boot):
                correlacoes_boot.append(float(r_boot))
    ic_corr = np.quantile(correlacoes_boot, [0.025, 0.975]) if correlacoes_boot else [np.nan, np.nan]
    n_sessoes = int(historico_ancoras_qpu_df["id_sessao"].nunique())
    estabilidade_sessoes = historico_ancoras_qpu_df.groupby("id_sessao")["erro_absoluto"].mean().std(ddof=1)
    aprovou_ancoras = (
        correlacao_ancoras >= 0.90 and mae_ancoras <= 0.10
        and np.isfinite(ic_corr[0]) and ic_corr[0] >= 0.80
        and n_sessoes >= 2 and np.isfinite(estabilidade_sessoes)
        and estabilidade_sessoes <= 0.05
    )
    diagnostico_ancoras_qpu = {
        "correlacao_pearson_ideal_qpu": correlacao_ancoras,
        "ic95_bootstrap_correlacao": [float(ic_corr[0]), float(ic_corr[1])],
        "mae_fidelidade": mae_ancoras,
        "mae_aer_calibrado_qpu": mae_aer_qpu,
        "mitigacao_leitura_aplicada": APLICAR_MITIGACAO_LEITURA,
        "condicao_matriz_atribuicao": (
            float(np.linalg.cond(matriz_atribuicao)) if matriz_atribuicao is not None else None
        ),
        "n_pares": len(resultado_ancoras_qpu_df),
        "n_sessoes_independentes": n_sessoes,
        "dp_mae_entre_sessoes": float(estabilidade_sessoes) if np.isfinite(estabilidade_sessoes) else None,
        "criterio_exploratorio_go": (
            "r >= 0.90; limite inferior IC95% >= 0.80; MAE <= 0.10; "
            ">=2 sessões; DP do MAE entre sessões <= 0.05"
        ),
        "decisao": (
            "GO para piloto ampliado"
            if aprovou_ancoras
            else "NO-GO: completar sessões ou revisar layout, mitigação, shots ou feature map"
        ),
    }
    display(resultado_ancoras_qpu_df.style.format({
        "fidelidade_ideal": "{:.3f}",
        "fidelidade_qpu": "{:.3f}",
        "fidelidade_qpu_mitigada": "{:.3f}",
        "erro_absoluto": "{:.3f}",
    }))
    display(pd.Series(diagnostico_ancoras_qpu, name="valor").to_frame())

    if "pasta_resultados" in globals():
        resultado_ancoras_qpu_df.to_csv(
            pasta_resultados / "ancoras_kernel_qpu.csv", index=False
        )
        historico_ancoras_qpu_df.to_csv(
            pasta_resultados / "historico_ancoras_qpu.csv", index=False
        )
        with open(pasta_resultados / "diagnostico_ancoras_qpu.json", "w", encoding="utf-8") as f:
            json.dump(diagnostico_ancoras_qpu, f, ensure_ascii=False, indent=2)
        print("Rode novamente a célula 7.6 para incluir as âncoras no ZIP final.")

    assert resultado_ancoras_qpu_df["fidelidade_qpu"].between(0, 1).all()
    assert resultado_ancoras_qpu_df["fidelidade_qpu_avaliacao"].between(0, 1).all()
    assert len(resultado_ancoras_qpu_df) == len(pares_ancora)
    assert resultado_ancoras_qpu_df["fidelidade_ideal"].nunique() >= 5
    print("✅ Âncoras espectrais e de fronteira avaliadas; o classificador completo permanece bloqueado até duas sessões.")
""")

md(r"""
## 8.5 — Classificador completo em QPU: última etapa e duplo bloqueio

Esta célula permanece desligada mesmo quando as âncoras são executadas. Ela exige simultaneamente:

1. CV aninhada completa;
2. suíte multibase completa;
3. nível de ruído Aer completo;
4. decisão **GO** nos pares-âncora, com IC bootstrap e ao menos duas sessões independentes;
5. confirmação explícita do orçamento lógico.

O duplo bloqueio evita que “Executar tudo” envie centenas ou milhares de circuitos por engano.
""")

code(r"""
# @title 8.5 — Classificador QPU completo, bloqueado por evidência e orçamento {display-mode: "form"}
EXECUTAR_CLASSIFICADOR_COMPLETO_QPU = False  # @param {type:"boolean"}
CONFIRMAR_ORCAMENTO_CLASSIFICADOR_QPU = False  # @param {type:"boolean"}
SHOTS_QPU_CLASSIFICADOR = 1024  # @param {type:"slider", min:256, max:8192, step:256}

n_pares_treino_qpu = len(X_treino) * (len(X_treino) - 1) // 2
n_pares_teste_qpu = len(X_teste) * len(X_treino)
avaliacoes_classificador_qpu = n_pares_treino_qpu + n_pares_teste_qpu
shots_logicos_classificador_qpu = avaliacoes_classificador_qpu * SHOTS_QPU_CLASSIFICADOR

print("Avaliações lógicas previstas:", avaliacoes_classificador_qpu)
print("Shots lógicos previstos:", f"{shots_logicos_classificador_qpu:,}")

if not EXECUTAR_CLASSIFICADOR_COMPLETO_QPU:
    print("⏭️ Classificador completo não enviado: esta é deliberadamente a última etapa.")
else:
    assert CONFIRMAR_ORCAMENTO_CLASSIFICADOR_QPU, "Confirme o orçamento lógico antes do envio."
    assert len(validacao_robusta_df) == N_AVALIACOES_EXTERNAS
    assert not resultados_aplicacoes_df.empty
    assert K_treino_ruidoso is not None
    assert diagnostico_ancoras_qpu.get("decisao") == "GO para piloto ampliado", (
        "Pares-âncora não aprovaram a progressão para o classificador completo."
    )
    assert service is not None and "backend_ancora" in globals()

    pares_treino_full = [
        (i, j) for i in range(len(X_treino)) for j in range(i + 1, len(X_treino))
    ]
    pares_teste_full = [
        (i, j) for i in range(len(X_teste)) for j in range(len(X_treino))
    ]
    circuitos_full = [
        circuito_sobreposicao(X_treino[i], X_treino[j], feature_map)
        for i, j in pares_treino_full
    ] + [
        circuito_sobreposicao(X_teste[i], X_treino[j], feature_map)
        for i, j in pares_teste_full
    ]

    pm_full = generate_preset_pass_manager(
        backend=backend_ancora, optimization_level=1, seed_transpiler=SEED
    )
    circuitos_full_isa = pm_full.run(circuitos_full)
    sampler_full = SamplerV2(mode=backend_ancora)
    job_full = sampler_full.run(circuitos_full_isa, shots=SHOTS_QPU_CLASSIFICADOR)
    print("Backend:", backend_ancora.name, "| Job ID:", job_full.job_id())
    resultados_full = job_full.result()

    K_treino_qpu = np.eye(len(X_treino), dtype=float)
    K_teste_qpu = np.zeros((len(X_teste), len(X_treino)), dtype=float)
    zero_full = "0" * feature_map.num_qubits
    cursor_full = 0
    for i, j in pares_treino_full:
        counts = resultados_full[cursor_full].data.meas.get_counts()
        K_treino_qpu[i, j] = K_treino_qpu[j, i] = (
            counts.get(zero_full, 0) / SHOTS_QPU_CLASSIFICADOR
        )
        cursor_full += 1
    for i, j in pares_teste_full:
        counts = resultados_full[cursor_full].data.meas.get_counts()
        K_teste_qpu[i, j] = counts.get(zero_full, 0) / SHOTS_QPU_CLASSIFICADOR
        cursor_full += 1

    K_treino_qpu = projetar_psd(K_treino_qpu)
    modelo_full_qpu = SVC(kernel="precomputed", C=1.0).fit(K_treino_qpu, y_treino)
    pred_full_qpu = modelo_full_qpu.predict(K_teste_qpu)
    resultado_classificador_qpu = {
        "backend": backend_ancora.name,
        "job_id": job_full.job_id(),
        "shots": SHOTS_QPU_CLASSIFICADOR,
        "avaliacoes_logicas": avaliacoes_classificador_qpu,
        "acuracia": float(accuracy_score(y_teste, pred_full_qpu)),
        "acuracia_balanceada": float(balanced_accuracy_score(y_teste, pred_full_qpu)),
        "f1": float(f1_score(y_teste, pred_full_qpu)),
    }
    display(pd.Series(resultado_classificador_qpu, name="resultado").to_frame())
    print("✅ Classificador QPU executado somente após todos os portões anteriores.")
""")

md(r"""
# Problemas comuns e diagnóstico

| Sintoma | Causa provável | Ação |
|---|---|---|
| `ModuleNotFoundError` | instalação não executada/reinício | execute 0.2 e reinicie se solicitado |
| import antigo de `Aer` falha | API desatualizada | use `from qiskit_aer import AerSimulator` |
| desenho `mpl` falha | extras de visualização ausentes | reinstale `qiskit[visualization]` |
| statevector após medição confuso | medição é não unitária | crie cópia sem medição para `Statevector` |
| bitstrings parecem invertidos | convenção little-endian | confira ordem de qubits e registradores |
| kernel demora | crescimento $O(n^2)$ e shots | ative modo rápido e reduza amostra |
| autovalor negativo pequeno | ruído de shots/precisão | documente tolerância e correção PSD |
| resultado muda | sementes ou shots diferentes | fixe e registre todas as fontes aleatórias |
| ótima acurácia suspeita | vazamento ou problema fácil | audite split, duplicatas e baseline |
| QPU rejeita circuito | circuito não está em ISA | transpile para o backend atual |
| acesso remoto falha | credencial/plano/região | valide conta sem expor a chave |

### Roteiro de depuração

1. Leia a última linha do erro.
2. Confirme versões na célula 0.3.
3. Reduza ao menor circuito que falha.
4. Compare `Statevector` ideal com Aer.
5. Verifique dimensões, ordem de qubits, shots e seed.
6. Só depois acrescente ruído ou hardware.
""")

md(r"""
# Dicionário de duas vozes — da explicação infantil ao texto científico

| Se eu contar para uma criança… | No texto científico, escrevo… | Cuidado para não dizer… |
|---|---|---|
| qubit é uma receita de possibilidades | vetor normalizado em um espaço de Hilbert bidimensional | que é um bit clássico indeciso |
| amplitude é uma seta | coeficiente complexo cuja norma quadrada gera probabilidade | que amplitude já é probabilidade |
| fase é o momento da corda de pular | relação angular complexa observável por interferência | que toda fase global é mensurável |
| porta é uma instrução da partitura | operação unitária sobre o estado | que qualquer operação é reversível após medir |
| circuito é a partitura inteira | composição ordenada de canais/portas e medições | que a ordem nunca importa |
| esfera de Bloch é uma bússola | parametrização geométrica de um qubit | que muitos qubits cabem numa esfera comum |
| shot é uma fotografia | repetição de preparação, circuito e medição | que um shot revela o statevector |
| interferência são ondas que somam | soma coerente de amplitudes antes da regra de Born | que a função de onda é água material |
| entrelaçamento é coreografia conjunta | não separabilidade do estado composto | que permite comunicação superluminal |
| ruído é palco/câmera imperfeitos | canais de erro físico e matriz de confusão de leitura | que shots finitos e ruído físico são iguais |
| feature map dobra o mapa | transformação $x\mapsto|\phi(x)\rangle$ | que a transformação conhece os rótulos por magia |
| kernel é uma régua especial | função de similaridade $K(x,z)$ usada por um estimador | que o kernel quântico aprende sozinho |
| CV aninhada é prova em envelope | seleção interna e avaliação externa pareada | que todos os folds são independentes |
| portão de evidência é semáforo | regra pré-especificada de progressão e alegação | que “verde” equivale a verdade definitiva |

## Técnica “ensine de volta”

Escolha um conceito e faça uma explicação de 60 segundos com quatro partes:

1. **história:** use uma imagem concreta sem jargão;
2. **ponte:** diga qual objeto matemático corresponde a cada parte da história;
3. **quebra:** mostre ao menos um ponto em que a analogia deixa de funcionar;
4. **teste:** faça uma previsão numérica ou experimental que poderia estar errada.

### Rubrica de autoavaliação (0–2 por item)

| Critério | 0 | 1 | 2 |
|---|---|---|---|
| clareza | jargão sem explicação | história compreensível | criança consegue recontar |
| rigor | sem definição | definição parcial | equação/objeto correto |
| limite | analogia tratada como realidade | limite vago | falha específica e relevante |
| verificabilidade | só opinião | exemplo qualitativo | previsão testável e resultado |
| honestidade | promete vantagem | inclui ressalva | separa observação, inferência e alegação |

**Meta:** pelo menos 8/10, sem nota zero em rigor ou limite. Se a criança entende a história, mas o cientista rejeita a tradução, a explicação ainda não terminou.
""")

md(r"""
# Desafios de consolidação

## Nível 0

1. Explique, em até 80 palavras, a diferença entre amplitude e probabilidade.
2. Por que dois estados podem ter a mesma distribuição em Z e ainda serem diferentes?
3. O que um shot representa?

## Graduação

4. Demonstre que $H^2=I$.
5. Construa os quatro estados de Bell e escreva testes para suas amplitudes.
6. Meça $|\Phi^+\rangle$ nas bases Z e X; compare as correlações.
7. Varie o erro de `CX` e estime uma curva dose–resposta para bitstrings anticorrelacionados.

## Pesquisa

8. Execute a CV aninhada 4 × 3 e explique por que os folds não são independentes.
9. Compare o teste corrigido, a permutação de sinais e o TOST de equivalência.
10. Compare `linear` e `full` registrando profundidade, número de portas, tempo e desempenho.
11. Teste a hipótese de sobrevivência geométrica nas quatro bases de aplicação.
12. Escreva limitações que incluam compressão para dois componentes, custo, shots, ruído, QPU e validade externa.
""")

md(r"""
# Gabarito conceitual resumido

1. **Amplitude** é um número complexo que participa de interferência; **probabilidade** é o módulo quadrado da amplitude na base de medição.
2. A fase relativa pode diferir. $|+\rangle$ e $|-\rangle$ dão 50/50 em Z, mas resultados opostos após uma Hadamard.
3. Um shot é uma preparação, execução e medição do circuito.
4. Multiplique as matrizes ou observe que Hadamard transforma base Z em X e novamente X em Z.
5. Use combinações de `H`, `CX`, `X` e `Z`; valide as quatro amplitudes.
6. Bell mantém correlações nas bases adequadas, enquanto uma mistura clássica de `00/11` não reproduz todas as coerências.
7. Mantenha shots, seed e leitura constantes; varie apenas a taxa de erro `CX`.
8–12. Não há número único correto: avaliam desenho experimental, justiça da comparação e qualidade da inferência.
""")

code(r"""
# @title Auditoria final — testes de integração do notebook
auditoria = {
    "ambiente_qiskit_2": int(qiskit.__version__.split(".")[0]) == 2,
    "estado_normalizado": np.isclose(np.vdot(psi, psi), 1.0),
    "hadamard_balanceada": np.allclose(np.abs(estado_h_qiskit.data) ** 2, [0.5, 0.5]),
    "bell_correlacionado": set(counts_bell) <= {"00", "11"},
    "interferencia_validada": np.max(np.abs(p0_simulado - p0_teorico)) < 1e-10,
    "split_binario": len(np.unique(y_treino)) == len(np.unique(y_teste)) == 2,
    "kernel_simetrico": simetria_max <= TOL_SIMETRIA,
    "kernel_diagonal_compativel": diagonal_max <= TOL_DIAGONAL,
    "kernel_psd": menor_autovalor >= -TOL_PSD,
    "tres_modelos": resultados_df["modelo"].nunique() == 3,
    "protocolo_congelado": (
        hashlib.sha256(texto_protocolo.encode("utf-8")).hexdigest() == HASH_PROTOCOLO
    ),
    "gate_osf_sem_excecao": STATUS_GATE_OSF in {
        "aguardando_registro", "bloqueado_sem_excecao", "liberado_por_url_registro"
    },
    "gate_osf_nao_executa_sem_url": (
        URL_OSF_VALIDA
        or not any([
            EXECUTAR_VALIDACAO_ROBUSTA, EXECUTAR_ESCADA_RUIDO,
            EXECUTAR_SUITE_APLICACOES, EXECUTAR_PAPER_AVANCADO,
            EXECUTAR_CURVAS_APRENDIZAGEM, EXECUTAR_RUIDO_ANINHADO,
            EXECUTAR_BENCHMARK_AMPLIADO, EXECUTAR_BASELINES_DEEP,
            EXECUTAR_AQUISICAO_ATIVA,
        ])
    ),
    "kernel_exato_referencia": np.allclose(np.diag(K_treino_exato), 1.0, atol=1e-10),
    "escada_validade_criada": escada_kernel_df["nivel"].nunique() >= 2,
    "portao_evidencia_gerado": (
        portao_evidencia["baseline_referencia"] == BASELINE_REFERENCIA
        and len(portao_evidencia["ic95_delta_pareado"]) == 2
    ),
    "cv_aninhada_executada_ou_bloqueada": (
        not EXECUTAR_VALIDACAO_ROBUSTA
        or len(validacao_robusta_df) == N_AVALIACOES_EXTERNAS
    ),
    "suite_aplicacoes_executada": (
        not EXECUTAR_SUITE_APLICACOES
        or (
            not resultados_aplicacoes_df.empty
            and resultados_aplicacoes_df["base"].nunique() == 4
        )
    ),
    "escada_ruido_executada": (
        not EXECUTAR_ESCADA_RUIDO
        or (
            K_treino_ruidoso is not None
            and "2 · Aer com ruído" in set(escada_kernel_df["nivel"])
        )
    ),
    "baselines_fortes_protegidos": (
        not EXECUTAR_PAPER_AVANCADO
        or (
            resultados_baselines_fortes_df["aplicacao"].nunique() == (
                4 if INCLUIR_REPLICACAO_PNEUMONIAMNIST else 3
            )
            and resultados_baselines_fortes_df["papel"].isin([
                "comparacao_justa_2D", "teto_classico_sem_restricao_2_qubits"
            ]).all()
        )
    ),
    "curvas_sem_teste": (
        not EXECUTAR_CURVAS_APRENDIZAGEM
        or (not resultados_curvas_df.empty and resultados_curvas_df["BAC_validacao"].between(0, 1).all())
    ),
    "ruido_aninhado_multissemente": (
        not EXECUTAR_RUIDO_ANINHADO
        or (
            resultados_ruido_aninhado_df["selecao_sem_fold_externo"].all()
            and resultados_ruido_aninhado_df.groupby(
                ["aplicacao", "fold_externo"]
            )["seed_ruido"].nunique().eq(len(SEEDS_RUIDO)).all()
        )
    ),
    "qus_nao_superalegado": (
        tabela_qus_df.empty
        or (
            tabela_qus_df["status_QUS"].eq(
                "validacao_tecnica_externa_concluida_hardware_pendente"
            ).all()
            and resultado_validacao_qus.get("validacao_hardware") == "pendente"
        )
    ),
    "benchmark_10mais_ou_bloqueado": (
        not EXECUTAR_BENCHMARK_AMPLIADO
        or (
            status_benchmark_ampliado == "apto_para_alegacao_10_mais_bases"
            and resultados_benchmark_ampliado_df["base"].nunique() >= MIN_BASES_PARA_ALEGACAO
        )
    ),
    "deep_concluido_ou_bloqueado": (
        not EXECUTAR_BASELINES_DEEP
        or status_deep_imagens == "concluido_metodologico_sem_uso_clinico"
    ),
    "aquisicao_orcamento_igual_ou_bloqueada": (
        not EXECUTAR_AQUISICAO_ATIVA
        or (
            not resultados_aquisicao_ativa_df.empty
            and resultados_aquisicao_ativa_df.groupby(
                ["aplicacao","seed"]
            )["orcamento_shots"].nunique().eq(1).all()
        )
    ),
    "snapshot_calibracao_auditavel": (
        not CRIAR_SNAPSHOT_CALIBRACAO
        or (
            bool(snapshot_calibracao.get("sha256"))
            and simulador_calibrado is not None
        )
    ),
    "matriz_novidade_revisada": (
        len(matriz_novidade) >= 8
        and matriz_novidade["data_corte_busca"].eq(DATA_CORTE_LITERATURA).all()
        and matriz_novidade["implicacao"].str.len().gt(20).all()
    ),
    "sequencia_qpu_protegida": (
        not EXECUTAR_ANCORAS_QPU
        or (
            len(validacao_robusta_df) == N_AVALIACOES_EXTERNAS
            and not resultados_aplicacoes_df.empty
            and K_treino_ruidoso is not None
        )
    ),
    "classificador_qpu_ultima_etapa": (
        not EXECUTAR_CLASSIFICADOR_COMPLETO_QPU
        or (
            CONFIRMAR_ORCAMENTO_CLASSIFICADOR_QPU
            and diagnostico_ancoras_qpu.get("decisao") == "GO para piloto ampliado"
        )
    ),
    "mapas_didaticos": len(MAPAS_DIDATICOS) == 6,
    "analogias_com_limites": (
        len(ANALOGIAS_RIGOROSAS) >= 10
        and all(
            {"crianca", "formal", "limite"} <= set(analogia)
            and all(str(analogia[campo]).strip() for campo in ["crianca", "formal", "limite"])
            for analogia in ANALOGIAS_RIGOROSAS.values()
        )
    ),
    "arquivos_exportados": (pasta_resultados / "configuracao.json").exists(),
    "catalogo_didatico_exportado": all(
        (pasta_resultados / nome).exists()
        for nome in ["catalogo_analogias_rigorosas.csv", "mapas_mentais.json"]
    ),
    "pacote_paper_gerado": all(
        (pasta_resultados / nome).exists()
        for nome in [
            "paper_metodos.md",
            "paper_resultados.md",
            "matriz_auditoria_novidade.csv",
            "auditoria_alegacoes.md",
        ]
    ),
    "pacote_ro_crate_gerado": all(
        (pasta_resultados / nome).exists()
        for nome in ["ro-crate-metadata.json","requirements_lock.txt","data_cards.md","model_card.md"]
    ),
}

auditoria_df = pd.DataFrame({
    "teste": auditoria.keys(),
    "aprovado": auditoria.values(),
})
display(auditoria_df)

assert all(auditoria.values()), "Há ao menos um contrato não satisfeito. Revise a tabela."
print("🎓 Todos os contratos essenciais foram aprovados.")
""")

md(r"""
# Checklist para relatório ou artigo

- [ ] pergunta, hipótese e desfecho foram definidos antes da comparação;
- [ ] protocolo foi pré-registrado externamente e o hash local coincide;
- [ ] critérios de inclusão/exclusão e unidade de análise estão claros;
- [ ] split ocorreu antes de escalonamento, seleção ou PCA;
- [ ] baselines clássicos receberam ajuste comparável;
- [ ] teto clássico e comparação justa em dois componentes foram separados;
- [ ] CNN pequena e embedding congelado foram tratados como teto visual, não como paridade de recursos;
- [ ] Brier, ECE e curvas de decisão foram reportados sem linguagem clínica;
- [ ] pelo menos dez bases foram efetivamente carregadas antes de alegar validade ampliada;
- [ ] feature map foi selecionado somente dentro do fold interno;
- [ ] curvas de aprendizagem foram calculadas sem consultar o teste;
- [ ] permutação de rótulos e deslocamento das entradas foram testados;
- [ ] concentração, separação intra/interclasse e espectro foram auditados;
- [ ] perfis de ruído foram selecionados dentro do fold e repetidos em cinco seeds;
- [ ] QUS foi identificado como índice em desenvolvimento, com validação de hardware ainda pendente;
- [ ] QUS foi calculado sem o fold externo e validado sem reajuste nesse fold;
- [ ] matriz completa, Nyström e aquisição ativa receberam o mesmo orçamento de shots;
- [ ] sementes, shots, versões, backend e tempo foram registrados;
- [ ] feature map, reps, entrelaçamento e hiperparâmetros estão descritos;
- [ ] matriz de kernel foi auditada (simetria, diagonal, PSD, alinhamento);
- [ ] CV aninhada repetida foi executada e a dependência entre folds foi corrigida;
- [ ] superioridade, equivalência e inconclusão foram distinguidas por regras prévias;
- [ ] efeito foi comparado de forma pareada a um baseline definido antes de olhar o teste;
- [ ] portão de evidência separa resultado exploratório, sinal confirmável e alegação forte;
- [ ] custo computacional acompanha as métricas preditivas;
- [ ] resultados negativos e limitações foram preservados;
- [ ] cada analogia possui tradução formal, limite explícito e uma previsão verificável;
- [ ] leitores leigos foram avaliados com a técnica “ensine de volta”, sem simplificar a alegação;
- [ ] análise de novidade foi atualizada até a data da submissão, sem alegação absoluta automática;
- [ ] pares-âncora passaram pelo critério go/no-go antes do classificador completo em QPU;
- [ ] âncoras cobriram espectro e fronteira em pelo menos duas sessões independentes;
- [ ] snapshot IBM e Aer calibrado foram versionados com hash;
- [ ] fidelidades brutas e mitigadas foram preservadas na ablação de leitura;
- [ ] RO-Crate, requirements lock, cartões de dados e modelo foram exportados;
- [ ] “vantagem quântica” só aparece se houver evidência apropriada de escala/custo;
- [ ] código, ambiente e dados permitidos foram versionados.

## Próximo passo recomendado

Registre o protocolo no OSF, ative a CV aninhada repetida e a suíte de aplicações, execute a escada de ruído e revise a matriz de novidade. Somente depois envie pares-âncora à QPU; o classificador completo é a última etapa.
""")

md(r"""
# Referências essenciais — formato ABNT

BOWLES, Joseph; AHMED, Shahnawaz; SCHULD, Maria. Better than classical? The subtle art of benchmarking quantum machine learning models. **arXiv**, 2024. DOI: [10.48550/arXiv.2403.07059](https://doi.org/10.48550/arXiv.2403.07059).

BIAMONTE, Jacob et al. Quantum machine learning. **Nature**, London, v. 549, p. 195–202, 2017. DOI: [10.1038/nature23474](https://doi.org/10.1038/nature23474).

CEREZO, M. et al. Challenges and opportunities in quantum machine learning. **Nature Computational Science**, [s. l.], v. 2, p. 567–576, 2022. DOI: [10.1038/s43588-022-00311-3](https://doi.org/10.1038/s43588-022-00311-3).

HAVLÍČEK, Vojtěch et al. Supervised learning with quantum-enhanced feature spaces. **Nature**, London, v. 567, p. 209–212, 2019. DOI: [10.1038/s41586-019-0980-2](https://doi.org/10.1038/s41586-019-0980-2).

HEYRAUD, Valentin et al. Noisy quantum kernel machines. **Physical Review A**, College Park, v. 106, art. 052421, 2022. DOI: [10.1103/PhysRevA.106.052421](https://doi.org/10.1103/PhysRevA.106.052421).

KAKAVAND, Siavash; STROHMEYER, Christoph; SCHLOTTER, Michael. Benchmarking Quantum Kernel Support Vector Machines Against Classical Baselines on Tabular Data: A Rigorous Empirical Study with Hardware Validation. **arXiv**, 2026. DOI: [10.48550/arXiv.2604.18837](https://doi.org/10.48550/arXiv.2604.18837).

NADEAU, Claude; BENGIO, Yoshua. Inference for the Generalization Error. **Machine Learning**, [s. l.], v. 52, n. 3, p. 239–281, 2003. DOI: [10.1023/A:1024068626366](https://doi.org/10.1023/A:1024068626366).

PRESKILL, John. Quantum computing in the NISQ era and beyond. **Quantum**, [s. l.], v. 2, p. 79, 2018. DOI: [10.22331/q-2018-08-06-79](https://doi.org/10.22331/q-2018-08-06-79).

SCHULD, Maria; KILLORAN, Nathan. Quantum machine learning in feature Hilbert spaces. **Physical Review Letters**, College Park, v. 122, art. 040504, 2019. DOI: [10.1103/PhysRevLett.122.040504](https://doi.org/10.1103/PhysRevLett.122.040504).

## Documentação técnica consultada

- [Qiskit SDK — documentação oficial](https://quantum.cloud.ibm.com/docs/api/qiskit)
- [Qiskit Aer 0.17.1 — simuladores](https://qiskit.github.io/qiskit-aer/)
- [Qiskit Machine Learning 0.9.0](https://qiskit-community.github.io/qiskit-machine-learning/)
- [Tutorial oficial de quantum kernels](https://qiskit-community.github.io/qiskit-machine-learning/tutorials/03_quantum_kernel.html)
- [IBM Quantum Platform — documentação](https://quantum.cloud.ibm.com/docs/)
- [IBM Quantum — criar e salvar credenciais](https://quantum.cloud.ibm.com/docs/guides/save-credentials)
- [OSF Registries — pré-registro](https://help.osf.io/article/330-welcome-to-registrations)

> Última revisão técnica desta edição: 17 ago. 2026. Bibliotecas evoluem; ao atualizar versões, reexecute todos os testes.
""")


notebook = {
    "cells": cells,
    "metadata": {
        "accelerator": "CPU",
        "colab": {
            "authorship_tag": "openai-work-mode",
            "include_colab_link": True,
            "name": OUTPUT.name,
            "provenance": [],
        },
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

OUTPUT.write_text(json.dumps(notebook, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Notebook criado: {OUTPUT} ({len(cells)} células)")
