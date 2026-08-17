# Sobrevivência Geométrica sem Vantagem Preditiva em Kernels Quânticos: Protocolo Aberto e Evidência Piloto

**English title:** Geometric Survival without Predictive Advantage in Quantum Kernels: An Open Protocol and Pilot Evidence

**Autor:** Marcelo Claro Laranjeira  
**Afiliação:** pesquisador independente, Brasil  
**Versão editorial:** 0.1 — 17 ago. 2026  
**Tipo de artigo:** estudo computacional metodológico com resultados exploratórios e negativos  
**Estado científico:** manuscrito para revisão do autor; não contém resultados confirmatórios pós-registro.

> **Nota de transparência:** este manuscrito separa três camadas de evidência: (i) resultados-piloto anteriores ao registro OSF; (ii) execução diagnóstica realizada após a submissão, mas antes da aprovação do embargo; e (iii) análises confirmatórias ainda não executadas. Nenhum resultado das duas primeiras camadas é reclassificado como confirmatório.

## Resumo

Kernels quânticos podem representar dados em espaços de Hilbert de alta dimensão, mas a preservação de sua geometria sob amostragem finita não garante vantagem preditiva sobre métodos clássicos. Este estudo apresenta um protocolo aberto, auditável e orientado por portões de evidência para comparar um SVM com kernel quântico de fidelidade a regressão logística e SVM com kernel radial. O núcleo diagnóstico utilizou o conjunto sintético make_moons, divisão estratificada, pré-processamento ajustado apenas no treino, mapa ZZ com dois qubits, uma repetição e entrelaçamento linear, semente 42 e 2.048 shots. Em 32 observações de treino e 16 de teste, o SVM-RBF obteve acurácia balanceada de 0,875, a regressão logística 0,8125 e o kernel quântico 0,625. A diferença QML–RBF foi −0,25, com IC95% pareado de −0,5625 a 0,0625. A matriz quântica foi simétrica, apresentou diagonal unitária e permaneceu sem autovalores negativos materialmente relevantes; contudo, o alinhamento kernel–alvo foi 0,1097. Statevector e 2.048 shots produziram a mesma acurácia, embora o erro geométrico relativo tenha sido 1,22%. Resultados-piloto multibase anteriores também apresentaram diferenças negativas frente ao RBF. Conclui-se que a estabilidade geométrica observada não implicou utilidade preditiva neste protocolo. A evidência permanece exploratória devido ao teste pequeno, à ausência de validação confirmatória multissemente e à inexistência de execução em QPU. O protocolo disponibilizado impede alegações de vantagem antes de validação aninhada, replicação independente e análise explícita de custo.

**Palavras-chave:** aprendizado de máquina quântico; kernel quântico; ciência aberta; validação aninhada; resultado negativo.

## Abstract

Quantum kernels can represent data in high-dimensional Hilbert spaces, but preservation of their geometry under finite sampling does not ensure predictive advantage over classical methods. We present an open, auditable, evidence-gated protocol comparing a fidelity quantum-kernel SVM with logistic regression and a radial-basis-function SVM. The diagnostic core used make_moons data, stratified splitting, train-only preprocessing, a two-qubit ZZ feature map with one repetition and linear entanglement, seed 42, and 2,048 shots. With 32 training and 16 test observations, balanced accuracy was 0.875 for the RBF-SVM, 0.8125 for logistic regression, and 0.625 for the quantum-kernel SVM. The paired QML–RBF difference was −0.25, with a 95% interval from −0.5625 to 0.0625. The quantum kernel was symmetric, had a unit diagonal, and showed no materially negative eigenvalue; nevertheless, target alignment was only 0.1097. Statevector and finite-shot evaluation achieved identical accuracy, despite a 1.22% relative geometric error. Earlier preregistration pilot benchmarks also yielded negative differences against the RBF baseline. Thus, observed geometric stability did not translate into predictive utility under this protocol. Evidence remains exploratory because of the small test set, the absence of confirmatory multi-seed validation, and the lack of QPU execution. The released workflow blocks advantage claims until nested validation, independent replication, and explicit resource accounting are completed.

**Keywords:** quantum machine learning; quantum kernel; open science; nested validation; negative result.

---

## 1 Introdução

O aprendizado de máquina quântico propõe usar circuitos quânticos para codificar, transformar ou classificar dados, com a expectativa de que certos espaços de representação sejam difíceis de reproduzir classicamente (BIAMONTE et al., 2017; HAVLÍČEK et al., 2019). Em métodos de kernel, um circuito parametrizado pelos dados define um mapa de características e a fidelidade entre estados atua como medida de similaridade. O treinamento do classificador pode permanecer clássico, enquanto o dispositivo quântico — ou seu simulador — fornece a matriz de kernel (SCHULD; KILLORAN, 2019).

A existência de um espaço de características grande, entretanto, não constitui por si só evidência de vantagem. Dados clássicos podem permitir que modelos clássicos aprendam funções cuja avaliação direta parece difícil, reduzindo a separação prática entre abordagens (HUANG et al., 2021). Além disso, mapas excessivamente expressivos podem produzir concentração exponencial dos elementos do kernel, tornando as amostras quase indistinguíveis e prejudicando a capacidade de generalização (THANASILP et al., 2024). Mesmo demonstrações experimentais recentes reforçam a necessidade de comparar desempenho, custo, escala e controles clássicos, em vez de tratar a execução quântica como desfecho suficiente (YIN et al., 2025).

Três problemas metodológicos são recorrentes. Primeiro, hiperparâmetros podem ser escolhidos depois de observar o teste, produzindo viés otimista. Segundo, diferenças entre algoritmos são frequentemente calculadas sobre folds dependentes como se fossem observações independentes. Terceiro, a estabilidade geométrica do kernel pode ser confundida com utilidade preditiva. A validação aninhada reduz o viés associado à seleção de modelos (VARMA; SIMON, 2006), enquanto procedimentos corrigidos para reamostragem reconhecem a dependência entre partições (NADEAU; BENGIO, 2003).

O presente trabalho transforma essas restrições em um fluxo operacional com portões de evidência. A contribuição principal não é alegar superioridade quântica, mas oferecer um protocolo que permita detectar quando a evidência é insuficiente, nula ou desfavorável. Resultados negativos são preservados porque delimitam hipóteses futuras e reduzem o risco de publicação seletiva.

## 2 Objetivos e perguntas de pesquisa

### 2.1 Objetivo geral

Avaliar se a geometria produzida por um kernel quântico de fidelidade permanece estável sob amostragem finita e se essa estabilidade se traduz em desempenho preditivo superior ao de baselines clássicos sob o mesmo particionamento de dados.

### 2.2 Objetivos específicos

1. Comparar regressão logística, SVM-RBF e SVM com kernel quântico sobre as mesmas observações.
2. Auditar simetria, diagonal, semidefinitude positiva, alinhamento e posto efetivo do kernel.
3. Quantificar a deformação entre statevector e avaliação com shots.
4. Registrar custo temporal, número de avaliações de fidelidade e shots lógicos.
5. Impedir inferência confirmatória quando o registro, o tamanho amostral ou a validação não satisfizerem os critérios pré-especificados.
6. Preservar resultados nulos ou negativos com proveniência explícita.

### 2.3 Hipóteses

**H1 — desempenho primário.** A diferença de acurácia balanceada entre o kernel quântico e o SVM-RBF é positiva.

**H2 — mecanismo geométrico.** Maior sobrevivência da geometria entre statevector, shots, ruído e QPU está associada a menor degradação preditiva.

**H3 — custo.** Qualquer ganho preditivo deve permanecer relevante depois de documentados tempo, avaliações de fidelidade e shots lógicos.

No presente manuscrito, H1–H3 permanecem hipóteses confirmatórias não testadas. Os resultados apresentados são diagnósticos ou pilotos.

## 3 Materiais e métodos

### 3.1 Desenho e governança

Foi construído um estudo computacional comparativo em notebook Google Colab. O código-fonte, o gerador do notebook, o protocolo, os resultados-piloto e o histórico analítico são públicos no GitHub. O projeto associado e o registro estão no OSF. A submissão do registro ocorreu em 17 ago. 2026; a aprovação do embargo permanecia pendente durante a execução diagnóstica aqui descrita.

A governança distingue:

- **piloto pré-registro:** resultados produzidos durante desenvolvimento e depuração;
- **diagnóstico pós-submissão:** execução usada para validar integridade, ambiente e parâmetros, sem inferência confirmatória;
- **confirmatório:** execução futura, em ambiente limpo, somente após liberação do registro e congelamento dos artefatos.

### 3.2 Dados e particionamento do núcleo diagnóstico

O núcleo utilizou make_moons com 120 observações, ruído 0,20 e semente 42. A divisão inicial treino–teste foi estratificada, com 30% destinados ao conjunto de teste. Para o modo diagnóstico rápido, foram selecionadas 32 observações de treino e 16 de teste, preservando o balanceamento de classes.

A transformação MinMax para o intervalo [0, π] foi ajustada exclusivamente no treino e aplicada ao teste sem novo ajuste. Essa ordem impede vazamento direto de informação do teste para a representação.

### 3.3 Modelos clássicos

Foram ajustados:

- regressão logística, máximo de 2.000 iterações;
- SVM-RBF com C=1 e gamma definido pela regra scale.

A versão confirmatória do protocolo amplia os controles para Dummy estratificado, SVM linear, Random Forest e HistGradientBoosting. A seleção de C em {0,1; 1; 10} e gamma em {scale; auto} ocorrerá apenas em validação interna.

### 3.4 Kernel quântico

O mapa de características ZZ utilizou:

- duas características e dois qubits;
- uma repetição;
- entrelaçamento linear;
- fidelidade Compute–Uncompute;
- semente 42;
- 2.048 shots;
- avaliação de duplicatas fora da diagonal;
- reparo semidefinido positivo quando necessário.

O classificador foi um SVM com kernel pré-calculado. A matriz de treino tinha dimensão 32×32 e a matriz teste–treino 16×32.

### 3.5 Diagnósticos geométricos

Foram registrados:

\[
\text{assimetria}=\max_{i,j}|K_{ij}-K_{ji}|,
\]

\[
\text{desvio diagonal}=\max_i|K_{ii}-1|,
\]

o menor autovalor, o alinhamento kernel–alvo, o posto efetivo e o erro de Frobenius relativo contra a referência statevector. Autovalores negativos com magnitude compatível com precisão numérica foram tratados como erro de arredondamento, não como violação material da condição PSD.

### 3.6 Desfechos e inferência

O desfecho primário é a diferença pareada de acurácia balanceada:

\[
\Delta BAC = BAC_{QML}-BAC_{RBF}.
\]

A execução diagnóstica utilizou 5.000 reamostragens bootstrap pareadas para descrever a incerteza. Como o teste continha apenas 16 casos e não houve repetição multissemente confirmatória, o intervalo não foi usado para declaração de superioridade ou inferioridade universal.

O protocolo confirmatório prevê quatro folds externos, três repetições, seleção interna em três folds, teste unilateral primário com correção de Nadeau–Bengio, IC bilateral de 95%, permutação de sinais, tamanho de efeito pareado, TOST com margem pré-especificada e ajuste de Holm para desfechos secundários.

### 3.7 Escada de validade e custo

A escada prevista é:

1. statevector exato;
2. amostragem finita;
3. Aer com ruído de portas e leitura;
4. pares-âncora em QPU;
5. classificador completo em QPU, somente se os portões anteriores forem aprovados.

Foram registrados tempo do kernel, avaliações lógicas de fidelidade e shots lógicos estimados. A QPU permaneceu bloqueada.

### 3.8 Ambiente computacional

A execução diagnóstica usou Python 3.12.13, NumPy 2.0.2, pandas 2.2.2, scikit-learn 1.6.1, Qiskit 2.3.1, Qiskit Aer 0.17.2 e Qiskit Machine Learning 0.9.0 em Linux x86_64. O notebook aprovou 36 testes de integração.

### 3.9 Considerações éticas

O núcleo utiliza dados sintéticos e benchmarks públicos. Não houve recrutamento, intervenção, identificação de participantes ou decisão clínica. Aplicações com MedMNIST são estritamente metodológicas e não autorizam interpretação diagnóstica. A necessidade de revisão ética deve ser reavaliada antes de qualquer uso de dados locais, identificáveis ou prospectivos.

## 4 Resultados

### 4.1 Desempenho diagnóstico com 2.048 shots

| Modelo | Acurácia | BAC | F1 | Tempo do kernel |
|---|---:|---:|---:|---:|
| SVM-RBF | 0,8750 | 0,8750 | 0,8889 | — |
| Regressão logística | 0,8125 | 0,8125 | 0,8421 | — |
| SVM + kernel quântico | 0,6250 | 0,6250 | 0,5000 | 8,60 s |

A estimativa pontual de ΔBAC QML–RBF foi −0,25. O IC95% pareado foi [−0,5625; 0,0625], a mediana bootstrap foi −0,25 e 4,24% das reamostragens produziram diferença positiva. O intervalo inclui zero, impedindo conclusão confirmatória, mas a direção pontual foi desfavorável ao QML.

### 4.2 Integridade e geometria do kernel

| Diagnóstico | Resultado |
|---|---:|
| Forma da matriz de treino | 32×32 |
| Forma teste–treino | 16×32 |
| Assimetria máxima | 0 |
| Desvio diagonal máximo | 0 |
| Menor autovalor | −7,81×10⁻¹⁶ |
| Alinhamento kernel–alvo | 0,10975 |
| Posto efetivo | 8,926 |
| Posto efetivo relativo | 0,2789 |

A magnitude do menor autovalor é compatível com erro numérico. Portanto, a matriz foi considerada PSD na tolerância adotada. O alinhamento baixo sugere que a geometria induzida pelo circuito não estava fortemente alinhada aos rótulos deste split.

### 4.3 Statevector versus shots

| Nível | Acurácia | F1 | Erro geométrico relativo | Alinhamento | Posto efetivo | Tempo |
|---|---:|---:|---:|---:|---:|---:|
| Statevector | 0,625 | 0,500 | 0 | 0,10888 | 8,625 | 0,12 s |
| 2.048 shots | 0,625 | 0,500 | 0,01216 | 0,10975 | 8,926 | 8,60 s |

A amostragem finita alterou discretamente a geometria, mas não modificou a classificação. Isso indica que, neste split, a ausência de ganho não pode ser atribuída principalmente ao número de shots.

### 4.4 Custo registrado

Foram estimadas 1.008 avaliações de fidelidade e 2.064.384 shots lógicos. O custo temporal foi aproximadamente 75 vezes maior que a referência statevector do núcleo, sem melhora preditiva.

### 4.5 Evidência piloto anterior ao registro

O snapshot piloto anterior usou 5.888 shots e amostra maior no núcleo. O SVM-RBF obteve BAC 0,906, enquanto o kernel quântico alcançou 0,656. Uma suíte multibase também apresentou diferenças negativas:

| Base | BAC RBF | BAC QML | ΔBAC |
|---|---:|---:|---:|
| Breast Cancer metodológico | 0,917 | 0,843 | −0,073 |
| Iris binária | 1,000 | 0,833 | −0,167 |
| make_moons | 0,958 | 0,758 | −0,200 |
| Wine binário | 0,898 | 0,820 | −0,078 |

Esses resultados não são independentes da fase de desenvolvimento e não devem ser combinados em metanálise. Sua função é documentar que a direção negativa não apareceu apenas na execução diagnóstica de 2.048 shots.

### 4.6 Portão de evidência

O portão classificou o resultado como **exploratório e inconclusivo** porque:

- o IC pareado inclui zero;
- o teste possui menos de 30 casos;
- não houve validação multissemente confirmatória;
- não houve teste externo confirmatório;
- a QPU não foi executada.

Foram aprovados os controles de baseline pré-especificado, comparação pareada e registro de custo.

## 5 Discussão

O principal achado é uma dissociação entre estabilidade geométrica e utilidade preditiva. A matriz permaneceu simétrica, unitária na diagonal e efetivamente PSD; a passagem de statevector para 2.048 shots introduziu apenas 1,22% de erro geométrico relativo. Apesar disso, o QML permaneceu 0,25 ponto de BAC abaixo do SVM-RBF.

Essa dissociação é compatível com a literatura que distingue espaço de representação, capacidade de generalização e vantagem operacional. Um kernel pode ser matematicamente válido e estável sem estar alinhado à tarefa. Neste estudo, o alinhamento kernel–alvo de aproximadamente 0,11 oferece uma explicação mecanística mais plausível que a simples escassez de shots. A coincidência de desempenho entre statevector e shots reforça essa interpretação.

Os resultados não demonstram que kernels quânticos sejam universalmente inferiores. O experimento utiliza dois qubits, um mapa ZZ raso e bases pequenas. Existem tarefas artificialmente construídas e configurações experimentais em que separações podem surgir (HAVLÍČEK et al., 2019; LIU; ARUNACHALAM; TEMME, 2021). O que os dados mostram é mais restrito: para as representações, amostras e controles avaliados, a estabilidade geométrica não foi suficiente para superar um baseline clássico forte.

A contribuição metodológica é o uso de portões que impedem progressão automática para hardware. Executar uma QPU após um resultado desfavorável em simuladores, sem hipótese mecanística adicional, elevaria custo sem corrigir o baixo alinhamento observado. Pares-âncora em duas sessões de hardware só serão considerados depois que a execução confirmatória demonstrar estabilidade multissemente, utilidade preditiva ou uma pergunta específica sobre degradação física.

O custo também deve integrar qualquer alegação. O núcleo exigiu mais de dois milhões de shots lógicos estimados para uma matriz pequena. Mesmo que a execução física não reproduza exatamente essa contabilidade, a ordem quadrática das avaliações do kernel permanece um limite prático. Estratégias como Nyström, landmarks selecionados sem consulta ao teste e alocação adaptativa de shots devem ser comparadas sob orçamento idêntico.

## 6 Limitações

1. O teste diagnóstico contém apenas 16 observações.
2. O conjunto make_moons é sintético e não fornece validade externa.
3. Os resultados multibase são pilotos anteriores ao registro.
4. O mapa ZZ tem somente dois qubits e uma repetição.
5. A execução atual não avaliou ruído Aer, deriva temporal ou hardware real.
6. O bootstrap de um único teste não substitui repetição multissemente.
7. O mesmo ecossistema de código participou do desenvolvimento e da avaliação piloto.
8. Ainda não há replicação por equipe independente.
9. A licença registrada para o código deve ser harmonizada com a licença Apache 2.0 vigente no repositório antes da versão final do artigo.
10. A afiliação, o ORCID, o financiamento e a declaração de conflitos exigem confirmação do autor antes da submissão.

## 7 Conclusão

A preservação da geometria do kernel entre statevector e 2.048 shots não produziu vantagem preditiva neste estudo. O SVM-RBF apresentou o melhor desempenho, enquanto o kernel quântico manteve a mesma acurácia na referência exata e na avaliação com shots. A matriz quântica foi numericamente válida, porém pouco alinhada aos rótulos.

O resultado negativo é cientificamente útil: ele mostra que fidelidade geométrica, validade numérica e execução quântica não devem ser tratadas como substitutos de generalização, comparação clássica e análise de custo. O protocolo aberto preserva essa evidência sem convertê-la em conclusão universal e bloqueia alegações confirmatórias até que validação aninhada, replicação e critérios OSF sejam cumpridos.

## Declarações

### Disponibilidade de dados e código

Código, notebooks, protocolo, resultados e histórico analítico estão disponíveis em:

- GitHub: https://github.com/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA
- Projeto OSF: https://osf.io/kqs2w/
- Registro OSF: https://osf.io/9yuvr/overview

### Contribuições dos autores — CRediT

**Marcelo Claro Laranjeira:** conceituação; metodologia; software; validação; análise formal; investigação; curadoria de dados; visualização; redação do rascunho; revisão e edição; administração do projeto.

### Financiamento

Não informado. **Confirmação do autor necessária antes da submissão.**

### Conflitos de interesse

Declaração ainda não fornecida. **Confirmação do autor necessária antes da submissão.**

### Uso de inteligência artificial

Ferramentas de IA foram utilizadas como apoio à organização editorial, revisão de consistência e documentação. O autor permanece responsável por código, resultados, interpretações, referências e versão submetida. A declaração deverá ser adaptada à política do periódico escolhido.

## Referências

BIAMONTE, J. et al. Quantum machine learning. **Nature**, London, v. 549, p. 195–202, 2017. DOI: https://doi.org/10.1038/nature23474.

HAVLÍČEK, V. et al. Supervised learning with quantum-enhanced feature spaces. **Nature**, London, v. 567, p. 209–212, 2019. DOI: https://doi.org/10.1038/s41586-019-0980-2.

HUANG, H.-Y. et al. Power of data in quantum machine learning. **Nature Communications**, London, v. 12, art. 2631, 2021. DOI: https://doi.org/10.1038/s41467-021-22539-9.

LIU, Y.; ARUNACHALAM, S.; TEMME, K. A rigorous and robust quantum speed-up in supervised machine learning. **Nature Physics**, London, v. 17, p. 1013–1017, 2021. DOI: https://doi.org/10.1038/s41567-021-01287-z.

NADEAU, C.; BENGIO, Y. Inference for the generalization error. **Machine Learning**, Dordrecht, v. 52, n. 3, p. 239–281, 2003. DOI: https://doi.org/10.1023/A:1024068626366.

QISKIT CONTRIBUTORS. Qiskit: an open-source framework for quantum computing. **Zenodo**, 2019. DOI: https://doi.org/10.5281/zenodo.2562111.

SCHULD, M.; KILLORAN, N. Quantum machine learning in feature Hilbert spaces. **Physical Review Letters**, College Park, v. 122, art. 040504, 2019. DOI: https://doi.org/10.1103/PhysRevLett.122.040504.

THANASILP, S.; WANG, S.; CEREZO, M.; HOLMES, Z. Exponential concentration in quantum kernel methods. **Nature Communications**, London, v. 15, art. 5200, 2024. DOI: https://doi.org/10.1038/s41467-024-49287-w.

VARMA, S.; SIMON, R. Bias in error estimation when using cross-validation for model selection. **BMC Bioinformatics**, London, v. 7, art. 91, 2006. DOI: https://doi.org/10.1186/1471-2105-7-91.

YANG, J. et al. MedMNIST v2: a large-scale lightweight benchmark for 2D and 3D biomedical image classification. **Scientific Data**, London, v. 10, art. 41, 2023. DOI: https://doi.org/10.1038/s41597-022-01721-8.

YIN, Z. et al. Experimental quantum-enhanced kernel-based machine learning. **Nature Photonics**, London, 2025. DOI: https://doi.org/10.1038/s41566-025-01682-5.

---

## Apêndice A — Critérios mínimos para a versão confirmatória

| Critério | Exigência |
|---|---|
| Registro OSF | aprovado e URL inserida no notebook |
| Ambiente | sessão limpa, versões e hash registrados |
| Validação | 4 folds externos × 3 repetições |
| Seleção interna | 3 folds, sem acesso ao teste |
| Teste por fold | aproximadamente 30 casos |
| Baseline primário | SVM-RBF |
| Inferência | Nadeau–Bengio, IC95%, sinais, efeito, TOST |
| Sensibilidade | múltiplas sementes e representações |
| Ruído | statevector → shots → Aer |
| QPU | somente após portões anteriores |
| Replicação | execução independente |
| Relato | publicar também resultado nulo ou negativo |

## Apêndice B — Alterações necessárias antes da submissão

1. Aprovar título, resumo e palavras-chave.
2. Informar afiliação institucional e ORCID, se existentes.
3. Confirmar financiamento e conflitos de interesse.
4. Selecionar o periódico e adaptar extensão/estilo.
5. Inserir figuras exportadas em resolução editorial.
6. Executar a fase confirmatória somente após liberação do registro.
7. Congelar versão, gerar DOI e atualizar a referência do software.
