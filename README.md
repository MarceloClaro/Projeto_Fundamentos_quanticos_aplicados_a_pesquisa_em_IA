# Projeto: Fundamentos Quânticos Aplicados à Pesquisa em IA

<div align="center">

![Quantum Lab](https://img.shields.io/badge/Quantum-Research%20Lab-cyan?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Qiskit](https://img.shields.io/badge/Qiskit-2.3+-purple?style=flat-square)
![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=flat-square)

**Do primeiro qubit a um protocolo de Quantum Machine Learning pré-registrável, auditável e orientado à evidência**

</div>

---

## 📋 Visão Geral

Este projeto é uma trilha de pesquisa educacional completa em **Física Quântica, Computação Quântica e Inteligência Artificial**. Ele transforma conceitos quânticos abstratos em um **experimento de IA reproduzível**, comparável com métodos clássicos e cientificamente rigoroso.

### 🎯 Pergunta Central

> Como transformar conceitos quânticos em um experimento de IA reproduzível, comparável com métodos clássicos e cientificamente honesto?

---

## 📚 Objetivo Pedagógico

Ao terminar esta trilha, você será capaz de:

1. **Explicar** os princípios essenciais da física quântica sem depender de jargão
2. **Representar** estados com notação de Dirac, vetores e probabilidades
3. **Construir** circuitos, visualizar a esfera de Bloch e interpretar medições
4. **Distinguir** superposição, interferência, correlação e entrelaçamento
5. **Simular** ruído e compreender limitações de dispositivos NISQ
6. **Explicar** onde a computação quântica pode — e onde ainda não consegue — ajudar a IA
7. **Comparar** regressão logística, SVM clássico e kernel quântico no mesmo protocolo
8. **Transformar** métricas em um parecer de evidência com próximos passos auditáveis
9. **Executar** validação aninhada, equivalência e análise mecanística multibase
10. **Exportar** resultados, protocolo, métodos e achados para um paper reproduzível

---

## 🗺️ Mapa Conceitual

| Módulo | Pergunta Orientadora | Evidência Produzida |
|---:|---|---|
| **0** | Como manter o experimento reproduzível? | Manifesto de ambiente e sementes |
| **1** | O que torna um fenômeno quântico? | Amplitudes complexas e regra de Born |
| **2** | Como programar e medir um qubit? | Circuitos, Statevector, Bloch e shots |
| **3** | O que é entrelaçamento? | Estado de Bell, entropia e correlações |
| **4** | Como interferência e ruído alteram resultados? | Curva de interferência e modelo NISQ |
| **5** | Onde a computação quântica entra em IA? | Mapa de decisão e arquitetura híbrida |
| **6** | O kernel quântico melhora este problema? | Benchmark, incerteza pareada e portão de evidência |
| **7** | Como transformar laboratório em pesquisa? | Ablações, validação robusta, escada de ruído e aplicações |
| **8** | Como migrar para hardware real com responsabilidade? | Bell e âncoras de kernel opcionais em QPU |

---

## 🛤️ Rotas de Aprendizagem

| Rota | Módulos | Tempo | Produto |
|---|---:|---:|---|
| **Leitura leiga** | Mapas + paradas 🧒 | 45–70 min | Intuição, analogias e vocabulário |
| **Essencial** | 0–3 | 70–100 min | Fundamentos, qubit, medição e Bell |
| **Aplicada** | 0–6 | 3–4 h | Comparação clássica × quântica e portão de evidência |
| **Pesquisa** | 0–8 | 1–2 dias | CV aninhada repetida, escada de ruído, aplicações e paper |

---

## 🧭 Legenda Pedagógica

- **🌱 Nível 0:** Intuição e linguagem simples
- **🧒 Explique a uma criança:** História concreta antes da fórmula
- **🧠 Mapa mental:** Relações entre ideias, não uma lista para decorar
- **🎓 Graduação:** Matemática e implementação
- **🔬 Pesquisa:** Hipótese, controles, limitações e reprodutibilidade
- **✅ TDD:** Teste automático do resultado esperado
- **⚠️ Onde a analogia falha:** Limite obrigatório para preservar rigor
- **🧭 Pare e interprete:** Não avance antes de explicar o gráfico com suas palavras

---

## 📦 Stack Tecnológico

| Componente | Versão | Propósito |
|---|---|---|
| **Python** | 3.10+ | Linguagem base |
| **Qiskit** | 2.3.x | Circuitos e estados quânticos |
| **Qiskit Aer** | 0.17.x | Simulação eficiente com ruído |
| **Qiskit Machine Learning** | 0.9.x | Kernels e algoritmos híbridos |
| **scikit-learn** | 1.5+ | Baselines e métricas |
| **Matplotlib/Seaborn** | Recente | Visualização |
| **NumPy/Pandas** | Recente | Computação numérica |

---

## 🔬 Contrato Científico (SDD)

### Requisitos Funcionais

1. Executar em uma sessão limpa do Google Colab
2. Gerar resultados determinísticos (sempre que simulador permitir)
3. Separar treino e teste **antes** de ajustar transformações
4. Comparar modelos sobre as mesmas observações
5. Produzir métricas, figuras e arquivos exportáveis
6. Não declarar vantagem quântica sem ganho comprovado
7. Toda analogia apresenta sua tradução formal e limites

### Critérios de Aceitação

- ✅ Estados normalizados: ∑ᵢ |αᵢ|² = 1
- ✅ Porta Hadamard em |0⟩: P(0) = P(1) = 0,5 (ideal)
- ✅ Bell ideal: somente `00` e `11` (sem ruído)
- ✅ Kernel: matriz simétrica, diagonal ≈ 1
- ✅ Resultados: ≥3 modelos, métricas comparáveis
- ✅ Inferência: teste pareado contra baseline pré-especificado

---

## 🧪 Hipóteses do Estudo

### Hipótese Primária (H1)
> Um kernel quântico baseado em mapa de características ZZ consegue separar o conjunto sintético `make_moons` com desempenho mensurável.

**Desfecho:** BAC (Balanced Accuracy) do kernel quântico > BAC do SVM-RBF

### Hipótese Mecanística (H2)
> Maior sobrevivência da geometria do kernel entre statevector → shots → ruído está associada a menor degradação preditiva.

**Método:** Correlação de Spearman entre sobrevivência geométrica e desempenho

### Hipótese Exploratória (H3)
> Perfis de ruído do Aer selecionados apenas na validação podem atuar como gatilhos de parada.

---

## 📊 Método das Três Camadas

Cada conceito difícil pode ser lido em três níveis, sem contradição:

1. **🖼️ Imagem concreta:** Algo que uma criança consegue imaginar
2. **📐 Tradução científica:** O conceito correto, com símbolos quando necessário
3. **⚠️ Limite da imagem:** Onde a analogia deixa de representar a física

> **Regra de ouro:** Um resultado quântico só é cientificamente interessante quando comparado a baselines clássicos fortes, sob o mesmo particionamento de dados e sem vazamento de informação.

---

## 🚀 Como Executar

### 1. Preparar o Ambiente

```bash
# Clone o repositório
git clone https://github.com/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA.git
cd Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA

# (Opcional) Crie um virtual environment
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2. Executar no Google Colab

Abra o notebook diretamente no Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA/blob/main/Projeto_Fundamentos_quânticos_aplicados_à_pesquisa_em_IA.ipynb)

### 3. Configurar Parâmetros

Na célula 0.1, defina:

```python
NOME_PESQUISADOR = "Seu Nome"
PROJETO = "Seu Título de Projeto"
SEED = 42
SHOTS = 5888
MODO_RAPIDO = False
EXECUTAR_VALIDACAO_ROBUSTA = True
EXECUTAR_ESCADA_RUIDO = True
```

### 4. Configurar IBM Quantum com segurança (opcional)

1. Crie a API key no [IBM Quantum Platform](https://quantum.cloud.ibm.com/).
2. No Colab, abra **🔑 Secrets** e crie `IBM_QUANTUM_API_KEY`.
3. Opcionalmente, crie `IBM_QUANTUM_INSTANCE_CRN`.
4. Execute a célula 8.2 com `CONFIGURAR_ACESSO_IBM = True`.

A autenticação ocorre somente em memória. A chave não é gravada no notebook, no repositório ou nas saídas, e a validação inicial não envia circuitos nem consome shots.

### 5. Executar Células

Execute as células na ordem usando **Ambiente de execução → Executar tudo** após ler os avisos.

---

## 📈 Orçamento Computacional Estimado

| Etapa | Avaliações Lógicas | Shots Lógicos | Tempo Esperado |
|---|---:|---:|---|
| Núcleo didático | 4.064 | 23,928,832 | ~5-10 min |
| CV aninhada 4×3 | 80.460 | 473,748,480 | ~30-60 min |
| Escada com ruído | 4.064 | 23,928,832 | ~15-30 min |

---

## 📄 Saídas do Projeto

- ✅ Manifesto de ambiente e versões congeladas
- ✅ Circuitos quânticos visualizados
- ✅ Matriz de kernel com diagnósticos
- ✅ Comparação de métricas (BAC, F1, acurácia)
- ✅ Análise de incerteza pareada
- ✅ Portões de evidência geométrica
- ✅ Protocolo para exportação OSF
- ✅ Gerador reproduzível `build_quantum_notebook.py`
- ✅ Figuras e tabelas para paper

---

## 📊 Resultados atuais

O notebook principal é mantido limpo para reprodução. Os resultados já executados foram preservados separadamente e classificados como **piloto anterior ao pré-registro**:

- [Resumo científico dos resultados atuais](RESULTADOS_ATUAIS.md)
- [Notebook piloto executado com todas as saídas](resultados/notebook_executado_piloto_2026-08-16.ipynb)

No snapshot observado, os baselines clássicos superaram o kernel quântico no desfecho principal. Não houve execução em QPU e não há alegação de vantagem quântica.

---

## 🔗 Pré-Registro e Reprodutibilidade

Este projeto segue boas práticas de **ciência aberta**:

- ✅ [Registro permanente OSF 9yuvr](https://osf.io/9yuvr/overview), aprovado e embargado até 16 ago. 2027
- ✅ [Projeto associado OSF kqs2w](https://osf.io/kqs2w)
- ✅ Conteúdo confirmatório congelado; revisões posteriores permanecem versionadas
- ✅ SHA-256 do protocolo documentado
- ✅ Seeds e versões fixadas
- ✅ Validação cruzada aninhada para seleção de hiperparâmetros
- ✅ Análise de sensibilidade e testes de equivalência
- ✅ Exportação para OSF-ready

---

## 👤 Autor

**Prof. Marcelo Claro Laranjeira**  
Pesquisa em Inteligência Artificial, Educação e Computação Quântica

- 🔗 GitHub: [MarceloClaro](https://github.com/MarceloClaro)
- 📊 OSF: [osf.io/user/953q4](https://osf.io/user/953q4)

---

## 📜 Licença

- **Protocolo, texto, tabelas e figuras:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Código:** [MIT License](https://opensource.org/licenses/MIT)

---

## 🎓 Referências e Leitura Recomendada

### Fundamentos de Computação Quântica
- Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
- Qiskit Documentation: https://qiskit.org/documentation/

### Quantum Machine Learning
- Schuld, M., & Killoran, N. (2022). Quantum machine learning in feature Hilbert spaces. *Nature Communications*, 13(1), 4615.
- Cerezo, M., et al. (2021). Variational quantum algorithms. *Nature Reviews Physics*, 3(9), 625-644.

### Metodologia Científica Reproduzível
- Nosek, B. A., et al. (2015). Promoting an open research culture. *Science*, 348(6239), 1422-1425.
- Open Science Framework: https://osf.io/

---

## ❓ Perguntas Frequentes

### P: Preciso de conhecimento prévio de física quântica?
**R:** Não! Álgebra linear e Python são introduzidos conforme surgem.

### P: Posso executar isso em uma máquina local?
**R:** Sim, mas Google Colab com GPU é recomendado para simulations grandes.

### P: Como pré-registrar este projeto?
**R:** Copie o conteúdo do manifesto (célula 0.5) para [OSF](https://osf.io/) antes de executar a análise.

### P: E se eu quiser usar hardware quântico real?
**R:** O Módulo 8 fornece âncoras prospectivas e portões go/no-go. Use o [IBM Quantum Platform](https://quantum.cloud.ibm.com/) e mantenha a API key exclusivamente no Colab Secrets.

---

## 🤝 Contribuições

Correções, sugestões e pull requests são bem-vindos! Por favor:

1. Abra uma [issue](https://github.com/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA/issues)
2. Descreva a melhoria ou problema
3. Submeta um pull request com testes

---

## 📞 Suporte

Para dúvidas ou problemas:

- 📧 Abra uma [discussão](https://github.com/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA/discussions)
- 🐛 [Reporte um bug](https://github.com/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA/issues)
- 📖 Consulte a [documentação Qiskit](https://qiskit.org/documentation/)

---

<div align="center">

**Edição: Agosto de 2026**  
**Ambiente-alvo:** Google Colab • Python 3 • Qiskit 2.3 • Qiskit Aer 0.17 • Qiskit ML 0.9

Made with ❤️ for quantum research and reproducible science

</div>
