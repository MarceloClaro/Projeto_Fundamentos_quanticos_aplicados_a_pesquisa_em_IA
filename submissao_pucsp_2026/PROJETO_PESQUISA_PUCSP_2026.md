# PROJETO DE PESQUISA — 7º CONGRESSO DE INTELIGÊNCIA ARTIFICIAL DA PUC-SP — 2026

## Título

**Portões de Evidência para Kernels Quânticos Reprodutíveis sob Ruído e Custo**

## Grupo de Trabalho proposto

**GT 1 — Tecnologias de IA**

## Dados da equipe

**Pesquisador responsável pelo desenvolvimento técnico-científico já documentado no repositório:**  
Marcelo Claro Laranjeira.

**Coordenação formal da submissão PUC:**  
**PENDENTE DE PREENCHIMENTO — requisito eliminatório do edital.** O coordenador da proposta deverá possuir vínculo formal com PUC-SP, PUC-Campinas ou PUC-Rio.

**Demais integrantes:**  
**PENDENTE DE PREENCHIMENTO.** A composição final deverá observar a exigência de maioria de alunos e/ou professores da PUC-SP, PUC-Campinas ou PUC-Rio.

> Nota de integridade: este arquivo não atribui vínculo institucional não documentado a nenhum integrante.

---

## Resumo

Este projeto propõe validar, de forma prospectiva, auditável e reprodutível, um protocolo de avaliação de kernels quânticos de fidelidade aplicados à aprendizagem de máquina supervisionada sob amostragem finita, ruído e restrições explícitas de custo computacional. A investigação parte de uma infraestrutura científica já implementada e pré-registrada, com código aberto, documentação de governança analítica, separação entre resultados exploratórios e confirmação, controle de vazamento de informação, validação cruzada aninhada e critérios de progressão por portões de evidência. O objetivo central não é presumir vantagem quântica, mas determinar em quais condições a geometria do kernel permanece informativa e se essa preservação se traduz, ou não, em utilidade preditiva comparável a baselines clássicos fortes. A comparação primária utilizará SVM com kernel quântico de fidelidade e SVM-RBF, com análise complementar de regressão logística, SVM linear, Random Forest e HistGradientBoosting. Serão avaliados acurácia balanceada, contraste pareado de desempenho, alinhamento kernel–alvo, posto efetivo, erro geométrico, sobrevivência geométrica, estabilidade espectral, tempo de execução e custo em avaliações de circuitos e shots. O desenho prevê validação externa repetida, seleção interna independente, análise de sensibilidade, controle de múltiplas comparações e transferência condicional para hardware quântico apenas quando critérios geométricos, preditivos e de custo forem satisfeitos. O produto esperado é um benchmark aberto e auditável para distinguir estabilidade geométrica de utilidade preditiva em Quantum Machine Learning, incluindo resultados positivos, nulos ou negativos.

---

## 1. Introdução

A aprendizagem de máquina quântica (Quantum Machine Learning — QML) investiga formas de codificar dados clássicos em circuitos quânticos e explorar espaços de características de alta dimensionalidade. Entre suas abordagens, os kernels quânticos ganharam destaque por permitirem representar similaridades entre observações a partir da fidelidade entre estados quânticos, mantendo compatibilidade com classificadores clássicos baseados em métodos de kernel.

Trabalhos fundamentais demonstraram que espaços de características quânticas podem oferecer representações expressivas para problemas supervisionados (HAVLÍČEK et al., 2019; SCHULD; KILLORAN, 2019). Entretanto, expressividade geométrica não implica, por si só, vantagem preditiva. A literatura posterior passou a destacar limitações associadas à concentração exponencial, disponibilidade e estrutura dos dados, custo de medição e dificuldade de demonstrar ganhos robustos sobre baselines clássicos fortes (HUANG et al., 2021; THANASILP et al., 2024).

Além disso, resultados obtidos em simulação ideal podem sofrer alterações quando submetidos a shots finitos, ruído de portas, erros de leitura, transpilações e restrições de hardware. Nesses cenários, a matriz de kernel pode manter aparente estabilidade global e ainda assim não produzir ganho preditivo. A distinção entre preservação geométrica e utilidade estatística é, portanto, um problema metodológico central.

O presente projeto adota uma perspectiva baseada em ciência aberta e em governança de evidências. Em vez de buscar uma demonstração favorável de “vantagem quântica”, o protocolo determina previamente em quais condições uma configuração pode avançar da simulação ideal para shots, ruído e, eventualmente, hardware real. Essa estratégia reduz o risco de seleção pós-hoc de modelos, hiperparâmetros ou regimes de execução.

O repositório que fundamenta esta proposta contém protocolo versionado, projeto OSF, pré-registro, notebook reproduzível, gerador programático, dados estruturados de diagnóstico, testes automatizados e manuscrito metodológico. A execução confirmatória permanece separada dos resultados exploratórios, o que permite que a proposta do Congresso seja desenvolvida sobre uma base científica já auditável sem reclassificar pilotos como confirmação.

---

## 2. Justificativa e motivação

O avanço do QML exige protocolos capazes de responder não apenas se um modelo quântico alcança determinado desempenho, mas se esse desempenho permanece estável sob condições realistas, resiste à comparação justa com modelos clássicos e justifica seu custo computacional.

Há três lacunas metodológicas que motivam a proposta.

A primeira é a tendência de interpretar propriedades geométricas favoráveis da matriz de kernel como evidência indireta de utilidade preditiva. Uma matriz aproximadamente simétrica, normalizada e sem autovalores negativos relevantes pode ainda apresentar baixo alinhamento com os rótulos ou não superar um kernel clássico.

A segunda é o risco de viés produzido por seleção e avaliação no mesmo conjunto de dados. Por esse motivo, o protocolo utiliza validação cruzada aninhada, ajusta todo pré-processamento apenas no treino e mantém o fold externo lacrado até que a seleção interna esteja concluída. A importância dessa separação é consistente com a literatura sobre viés de estimativa em seleção de modelos (VARMA; SIMON, 2006).

A terceira é a necessidade de incorporar custo ao julgamento de utilidade. Em kernels quânticos, o número de avaliações de fidelidade e shots pode crescer rapidamente. Assim, ganho preditivo, estabilidade geométrica e orçamento computacional devem ser analisados conjuntamente.

Os resultados exploratórios já preservados no repositório mostraram direção desfavorável ao kernel quântico em diferentes cenários piloto, sem sustentação de vantagem quântica. Esses resultados não serão usados como confirmação; ao contrário, reforçam a necessidade de um protocolo prospectivo capaz de preservar resultados nulos ou negativos e de impedir alegações fortes a partir de uma única divisão de dados, uma única seed ou uma única configuração.

A relevância científica do projeto está, portanto, em transformar a avaliação de kernels quânticos em um processo de decisão auditável, com critérios explícitos de integridade, geometria, desempenho, estabilidade e custo. A relevância tecnológica decorre da implementação executável em Qiskit e Qiskit Aer, com possibilidade condicional de transferência para hardware quântico real. A relevância para ciência aberta decorre da integração entre GitHub, OSF, pré-registro, artefatos versionados e documentação de reprodutibilidade.

---

## 3. Problema e pergunta de pesquisa

### Problema

A preservação da geometria de um kernel quântico sob shots finitos e ruído não garante que essa representação produza utilidade preditiva superior ou equivalente a baselines clássicos fortes.

### Pergunta principal

**Sob seleção interna justa e avaliação externa repetida, em quais condições um kernel quântico de fidelidade preserva geometria e utilidade preditiva suficientes para justificar progressão de statevector para shots, ruído e hardware quântico real?**

### Hipótese confirmatória primária

**H1:** a média pareada de ΔBAC = BAC_QML − BAC_RBF é maior que zero.

### Hipótese mecanística

**H2:** maior sobrevivência geométrica do kernel está associada a menor degradação preditiva.

### Hipóteses exploratórias

**H3:** um perfil de ruído selecionado exclusivamente na validação interna pode atuar como regularizador.

**H4:** a associação entre sobrevivência geométrica e ΔBAC permanece positiva em análise multinível que controle aplicação e custo.

**H5:** um índice exploratório de utilidade quântica pode discriminar configurações que preservem utilidade sem consultar o fold externo.

**H6:** sob orçamento idêntico, estratégias de amostragem mais eficientes podem preservar maior combinação de desempenho e geometria por shot do que a medição uniforme.

---

## 4. Objetivos

### 4.1 Objetivo geral

Desenvolver e validar um protocolo reprodutível, pré-especificado e auditável para avaliar kernels quânticos de fidelidade sob amostragem finita, ruído e custo computacional, comparando-os com baselines clássicos fortes e condicionando a progressão para hardware real ao cumprimento de portões de evidência.

### 4.2 Objetivos específicos

1. Implementar comparação padronizada entre SVM com kernel quântico de fidelidade e SVM-RBF sob os mesmos dados, partições e transformações.
2. Mensurar o impacto de shots finitos e perfis de ruído sobre a geometria da matriz de kernel.
3. Quantificar a associação entre sobrevivência geométrica e desempenho preditivo.
4. Executar validação cruzada aninhada com seleção interna e avaliação externa repetida.
5. Comparar o modelo quântico com baselines clássicos adicionais em regime de representação controlada e em teto clássico separado.
6. Avaliar custo em tempo, avaliações de circuitos, shots lógicos e custo por unidade de desempenho.
7. Implementar controles negativos e análises de sensibilidade para detectar resultados espúrios.
8. Definir critérios de GO/NO-GO para progressão de statevector para shots, Aer com ruído e QPU.
9. Preservar e publicar resultados positivos, nulos, equivalentes, inconclusivos ou negativos.
10. Produzir um pacote aberto contendo código, protocolo, matrizes, logs, métricas, hashes e documentação de reprodução.

---

## 5. Metodologia

### 5.1 Delineamento

Estudo computacional supervisionado, metodológico e não clínico, com comparação de classificadores em bases sintéticas, tabulares e de imagem de pequeno porte já definidas no protocolo. Não haverá intervenção em participantes humanos.

### 5.2 Bases e aplicações

O protocolo contempla:

- Iris Setosa–Versicolor;
- make_moons com fronteira não linear conhecida;
- BreastMNIST v2 em uso exclusivamente metodológico;
- PneumoniaMNIST como replicação externa exploratória;
- suíte multibase de conjuntos públicos e sintéticos para análise de validade externa.

Os conjuntos biomédicos serão tratados apenas como benchmarks metodológicos, sem interpretação diagnóstica ou clínica.

### 5.3 Prevenção de vazamento de informação

Em cada partição, todo pré-processamento será ajustado somente no conjunto de treino:

1. inspeção de integridade, classes e valores ausentes;
2. imputação, quando necessária, ajustada apenas no treino;
3. padronização;
4. redução dimensional por PCA;
5. reescala para [0, π];
6. aplicação das transformações aprendidas à validação e ao teste;
7. construção do kernel somente após congelamento das transformações.

O fold externo não poderá ser utilizado para selecionar hiperparâmetros, perfil de ruído ou mapa de características.

### 5.4 Modelos

#### Modelo quântico principal

SVC com matriz de kernel quântico de fidelidade pré-computada, baseada em codificação ZZ.

A matriz bruta será preservada para auditoria. Quando necessário, será simetrizada e projetada no cone semidefinido positivo, com magnitude da correção documentada.

#### Baseline primário

SVM com kernel RBF.

#### Baselines adicionais

- Dummy;
- regressão logística;
- SVM linear;
- Random Forest;
- HistGradientBoosting.

A comparação representacional em duas dimensões será reportada separadamente do teto clássico com dimensionalidade ampliada, evitando que diferenças de capacidade representacional sejam confundidas com efeito do kernel.

### 5.5 Validação

A análise principal utilizará validação cruzada aninhada e estratificada:

- nível externo: 4 folds × 3 repetições;
- nível interno: 3 folds;
- critério principal de seleção: acurácia balanceada média;
- C do SVM: {0,1; 1; 10};
- gamma do RBF: {scale, auto};
- perfil de ruído: escolhido apenas na validação interna;
- teste externo: aberto uma única vez após seleção.

Os folds externos serão tratados como avaliações dependentes, não como replicações independentes.

### 5.6 Regimes de execução

A progressão seguirá a sequência:

1. statevector exato;
2. shots finitos;
3. perfis de ruído no Qiskit Aer;
4. pares-âncora em QPU, se aprovados os portões;
5. repetição em segunda sessão independente de QPU;
6. classificador completo em QPU apenas por último.

A transferência para QPU será condicional e não será usada para fabricar um resultado favorável.

### 5.7 Perfis de ruído

Serão usados os perfis pré-especificados no protocolo:

| Perfil | Erro 1Q | Erro 2Q | Erro de leitura |
|---|---:|---:|---:|
| Controle | 0 | 0 | 0 |
| Baixo | 0,0005 | 0,005 | 0,01 |
| Moderado | 0,001 | 0,01 | 0,02 |
| Alto-2Q | 0,001 | 0,03 | 0,02 |
| Leitura-alta | 0,001 | 0,01 | 0,05 |

### 5.8 Desfechos

#### Primário

- acurácia balanceada;
- ΔBAC entre QML e SVM-RBF.

#### Secundários

- acurácia;
- F1;
- calibração, quando aplicável.

#### Geometria do kernel

- alinhamento kernel–alvo;
- posto efetivo;
- erro relativo de Frobenius;
- sobrevivência geométrica;
- variância fora da diagonal;
- separação intra/interclasse;
- condição e entropia espectral;
- simetria, diagonal e espectro PSD.

#### Custo

- tempo total e por etapa;
- número de avaliações de circuitos;
- shots lógicos;
- custo por entrada da matriz;
- custo por unidade de BAC e sobrevivência geométrica.

### 5.9 Plano estatístico

A inferência primária seguirá o protocolo pré-especificado:

- média de ΔBAC;
- intervalo de confiança de 95%;
- tamanho de efeito pareado;
- teste com correção de Nadeau–Bengio para dependência entre folds;
- permutação de sinais como análise de sensibilidade;
- TOST com margem de equivalência de ±0,02 BAC;
- correção de Holm para desfechos secundários;
- correlação de Spearman para H2;
- modelo de efeitos mistos para H4;
- controles negativos por permutação de rótulos e deslocamento das entradas.

Não será alegada vantagem quântica com uma única amostra, um único split, uma única seed ou apenas significância nominal.

### 5.10 Portões de evidência

**Portão 0 — Integridade:** classes, splits, NaN/Inf, formas e orçamento.

**Portão 1 — Validade geométrica:** simetria, diagonal, PSD, erro de Frobenius, alinhamento e posto efetivo.

**Portão 2 — Validade preditiva:** seleção apenas internamente; fold externo lacrado.

**Portão 3 — Estabilidade:** avaliação entre seeds, folds, repetições e aplicações.

**Portão 4 — Custo:** desempenho e geometria interpretados conjuntamente ao orçamento.

**Portão 5 — QPU:** hardware real somente após cumprimento dos critérios anteriores.

### 5.11 Reprodutibilidade e ciência aberta

O projeto utilizará:

- repositório GitHub público;
- projeto OSF e pré-registro associado;
- seed canônica 42;
- 2.048 shots como referência;
- logs de ambiente;
- matrizes brutas e corrigidas;
- hashes de arquivos;
- notebook reproduzível;
- gerador programático do notebook;
- testes automatizados;
- resultados legíveis por máquina;
- documentação explícita de desvios pós-registro.

Os resultados exploratórios anteriores serão mantidos separados da análise confirmatória.

---

## 6. Cronograma de execução — 12 meses

| Etapa | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Auditoria final do protocolo e ambiente | X | X | | | | | | | | | | |
| Congelamento de dependências e artefatos | X | X | | | | | | | | | | |
| Execução confirmatória multibase | | X | X | X | | | | | | | | |
| Validação aninhada e inferência | | | X | X | X | | | | | | | |
| Escada statevector → shots | | | | X | X | | | | | | | |
| Perfis de ruído Aer | | | | | X | X | X | | | | | |
| Análise de custo e ablações | | | | | | X | X | X | | | | |
| Replicação independente | | | | | | | X | X | X | | | |
| Pares-âncora QPU, se elegíveis | | | | | | | | X | X | | | |
| Segunda sessão QPU, se elegível | | | | | | | | | X | X | | |
| Consolidação, artigo e pacote FAIR | | | | | | | | | | X | X | |
| Relatório final, dados e apresentação | | | | | | | | | | | X | X |

---

## 7. Resultados esperados e impactos

O projeto não condiciona sucesso científico à obtenção de desempenho superior do kernel quântico. Os resultados esperados são metodológicos e verificáveis.

Espera-se:

1. um benchmark reprodutível de comparação entre kernel quântico e baselines clássicos;
2. uma quantificação da relação entre preservação geométrica e utilidade preditiva;
3. critérios operacionais para decidir quando shots ou ruído tornam uma configuração inviável;
4. uma análise explícita de custo por desempenho;
5. evidência sobre quando a transferência para QPU é justificável e quando deve ser interrompida;
6. um pacote aberto e versionado para reprodução por terceiros;
7. documentação de resultados positivos, nulos, equivalentes ou negativos sem seleção narrativa;
8. material científico reutilizável em ensino de QML, validação de IA e ciência aberta.

### Impacto científico

A contribuição central será um protocolo que trate geometria, desempenho, estabilidade e custo como dimensões conjuntas de evidência, reduzindo a probabilidade de alegações de vantagem baseadas em comparações frágeis.

### Impacto tecnológico

O projeto produzirá infraestrutura executável em Qiskit/Qiskit Aer, com testes automatizados e progressão condicional para hardware real.

### Impacto formativo

O protocolo e os notebooks poderão ser usados em atividades de formação em inteligência artificial, computação quântica, validação de modelos e pesquisa reprodutível.

### Impacto em ciência aberta

A integração entre GitHub, OSF, pré-registro, hashes, código e dados estruturados favorece auditoria externa e reutilização científica.

---

## 8. Estado atual do projeto

A infraestrutura científica já existente inclui:

- protocolo versionado;
- projeto OSF e pré-registro;
- código público;
- notebook e gerador reproduzível;
- critérios de integridade e portões de evidência;
- resultados exploratórios preservados;
- testes automatizados;
- declaração de reprodutibilidade;
- manuscrito metodológico;
- metadados de citação.

Os resultados atuais são classificados como exploratórios/diagnósticos e não serão reclassificados como confirmação. A fase confirmatória deverá obedecer ao estado vigente do registro e às regras de governança documentadas no projeto.

---

## 9. Referências

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

## 10. Itens obrigatórios ainda pendentes antes da submissão

1. Confirmar o **coordenador com vínculo formal PUC-SP, PUC-Campinas ou PUC-Rio**.
2. Confirmar que a **maioria da equipe** é composta por alunos e/ou professores dessas instituições.
3. Inserir afiliações e dados completos da equipe.
4. Verificar o estado atual do pré-registro OSF antes de descrever a fase confirmatória como liberada.
5. Harmonizar a divergência de licença MIT/Apache já documentada no projeto.
6. Converter esta versão para o formato final de submissão, mantendo o limite máximo de 15 páginas.
7. Realizar auditoria final de referências, DOI, ortografia e paginação.
