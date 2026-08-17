# Portões de Evidência Geométrica para Kernels Quânticos Reprodutíveis sob Ruído e Custo

**Documentação científica versionada — espelho expandido da Wiki OSF**  
**Autor e pesquisador responsável:** Marcelo Claro Laranjeira  
**Versão desta página:** 1.1 — 17 de agosto de 2026  
**Natureza:** estudo computacional pré-registrado, metodológico e não clínico

> **Estado verificável em 17/08/2026:** o projeto OSF está público; o pré-registro foi submetido em 17/08/2026 e permanece com o estado **Pending embargo approval**, com embargo previsto até 16/08/2027. A análise confirmatória ainda não foi iniciada, em conformidade com a regra prospectiva do protocolo. Resultados anteriores ao registro são exclusivamente pilotos de depuração e não constituem evidência confirmatória.

---

## 1. Resumo executivo

Este projeto investiga, de forma prospectiva, falsificável e reprodutível, se um classificador SVM com kernel quântico de fidelidade preserva utilidade preditiva sob amostragem finita, ruído e restrições de custo, quando comparado a baselines clássicos fortes. O foco não é procurar uma “vantagem quântica” a qualquer custo, mas determinar em quais condições a geometria do kernel sobrevive à transição do statevector ideal para shots, ruído simulado e, condicionalmente, hardware quântico real.

A estratégia central é um **Evidence Gate**: cada etapa precisa satisfazer critérios de integridade, geometria, desempenho, estabilidade e custo antes de avançar. O desenho separa rigorosamente seleção e avaliação, utiliza validação cruzada aninhada, preserva os splits oficiais quando existentes, registra seeds e hashes, reporta resultados nulos e impede que o conjunto externo seja usado para escolher modelos.

A comparação principal é entre SVC com kernel quântico pré-computado e SVC-RBF. Para contextualizar o desempenho, o estudo inclui Dummy, regressão logística, SVM linear, SVM-RBF, Random Forest e HistGradientBoosting. A comparação justa em duas dimensões é reportada separadamente do teto clássico com até 32 componentes, evitando confundir paridade de representação com capacidade máxima dos modelos clássicos.

---

## 2. Identificadores, rastreabilidade e escopo

- **Projeto OSF editável:** [https://osf.io/kqs2w/](https://osf.io/kqs2w/)
- **Pré-registro associado:** [https://osf.io/9yuvr/](https://osf.io/9yuvr/)
- **Perfil do pesquisador:** [https://osf.io/user/953q4](https://osf.io/user/953q4)
- **Arquivos do projeto:** [https://osf.io/kqs2w/files](https://osf.io/kqs2w/files)
- **Repositório de desenvolvimento:** [Projeto Fundamentos quânticos aplicados à pesquisa em IA](https://github.com/MarceloClaro/Projeto_Fundamentos_quanticos_aplicados_a_pesquisa_em_IA)
- **Seed canônica:** 42, com derivações determinísticas documentadas
- **Shots de referência:** 2.048, salvo análise pré-especificada da escada de shots
- **Hash SHA-256 do protocolo canônico:** `40661c466d7a8f2fb25d30c53fe48aeb742b2bd9a9c24e71b4fc2c71f98e80c5`
- **Licença do registro e da documentação:** CC BY 4.0
- **Licença atual do código neste repositório:** Apache License 2.0
- **Data de corte bibliográfico declarada:** 16/08/2026

O registro congelado é a fonte normativa para as análises confirmatórias. O arquivo `LICENSE` deste repositório contém Apache License 2.0; como o texto do pré-registro menciona MIT para o código original, a divergência de licenciamento permanece explicitamente registrada e deverá ser harmonizada antes da versão científica final. Esta Wiki é documentação viva: esclarece o protocolo, registra o andamento e orienta a reprodução, mas não altera retroativamente hipóteses, critérios ou decisões já pré-especificadas.

---

## 3. Problema científico

Kernels quânticos codificam dados clássicos em estados quânticos e medem similaridades por meio da fidelidade entre esses estados. Em condições ideais, uma matriz de kernel pode parecer informativa; contudo, shots finitos, ruído de portas, erro de leitura, transpilações e custo quadrático podem deformar sua geometria.

Assim, a pergunta cientificamente relevante não é apenas “o classificador acerta?”, mas:

1. a matriz estimada permanece aproximadamente simétrica e semidefinida positiva;
2. a estrutura intra e interclasse é preservada;
3. a degradação geométrica prediz a perda de desempenho;
4. o eventual ganho resiste a validação externa repetida;
5. o resultado permanece útil sob um orçamento comparável de circuitos e shots;
6. a evidência reaparece em sessões independentes de QPU antes do classificador completo.

### Explicação autodidática

- **Kernel:** função que transforma pares de observações em uma medida de similaridade.
- **Kernel quântico:** similaridade estimada após codificar as observações em circuitos quânticos.
- **Shot:** uma execução amostral do circuito. Mais shots reduzem a incerteza amostral, mas elevam o custo.
- **Geometria do kernel:** padrão global de proximidades representado pela matriz de similaridades.
- **BAC:** acurácia balanceada; calcula a média do desempenho por classe e reduz distorções em bases desbalanceadas.
- **Portão de evidência:** critério decidido antes da avaliação que determina se a próxima etapa é justificável.

---

## 4. Perguntas e hipóteses

### H1 — hipótese confirmatória primária

Sob seleção interna justa e avaliação externa repetida, a média pareada de

**ΔBAC = BAC_QML − BAC_RBF**

é maior que zero.

### H2 — sobrevivência geométrica

A associação entre sobrevivência geométrica do kernel e ΔBAC é positiva: matrizes que preservam melhor sua estrutura ideal devem sofrer menor degradação preditiva.

### H3 — ruído como regularizador, exploratória

Um perfil de ruído selecionado exclusivamente na validação pode atuar como regularizador. Qualquer aparente superioridade deverá reaparecer em repetição independente antes de receber interpretação substantiva.

### H4 — robustez multinível

A associação entre sobrevivência geométrica e ΔBAC permanece positiva em modelo multinível que controla aplicação e custo.

### H5 — Quantum Utility Score, exploratória

O Quantum Utility Score, calculado sem consultar o fold externo, pode discriminar configurações que preservam utilidade no teste e, futuramente, na QPU. O índice permanece exploratório e ainda não validado.

### H6 — alocação eficiente de orçamento

Sob orçamento idêntico, Nyström orientado por leverage scores ou aquisição ativa preserva maior combinação de BAC e geometria por shot do que a medição uniforme.

---

## 5. Desenho do estudo

O estudo é uma simulação computacional supervisionada, sem inferência causal e sem intervenção em participantes humanos.

| Aplicação | Tipo | Tamanho/limite | Papel no estudo |
|---|---|---:|---|
| Iris Setosa–Versicolor | tabular, binária | 100 observações elegíveis | caso controlado e didático |
| make_moons | sintética, binária | 120; noise=0,18; seed=42 | fronteira não linear conhecida |
| BreastMNIST v2 | imagens 28×28 | população oficial de 780; laboratório limitado a 24 treino, 12 validação e 12 teste | aplicação metodológica com splits oficiais |
| PneumoniaMNIST | imagens 28×28 | splits oficiais | replicação externa exploratória |
| Suíte multibase | públicas e sintéticas | pelo menos 10 bases; teto de 160 observações por base | validade externa e análise hierárquica |

BreastMNIST e PneumoniaMNIST são usados exclusivamente para avaliação metodológica. Nenhum resultado será interpretado como diagnóstico, prognóstico ou recomendação clínica.

---

## 6. Prevenção de vazamento de informação

Todo pré-processamento é ajustado **somente no conjunto de treino** de cada partição:

1. verificação de integridade, classes e valores ausentes;
2. imputação pela mediana, quando necessária, ajustada apenas no treino;
3. padronização com `StandardScaler`;
4. redução por PCA;
5. reescala para `[0, π]` com `MinMaxScaler`;
6. transformação da validação e do teste com os parâmetros aprendidos no treino;
7. construção das matrizes de kernel após o congelamento das transformações.

Imagens 28×28 são vetorizadas no pipeline quântico. HOG é usado somente nos baselines de imagem previamente definidos. Rótulos nunca são imputados. O fold externo permanece lacrado até a conclusão da seleção interna.

---

## 7. Modelos e política de comparação justa

### 7.1 Faixa A — comparação representacional justa em 2D

Os modelos clássico e quântico recebem a mesma representação bidimensional, produzida dentro de cada fold. Esta faixa responde se o kernel quântico agrega informação quando o orçamento de representação é comparável.

### 7.2 Faixa B — teto clássico separado

Modelos clássicos são também avaliados com até 32 componentes, quando aplicável. Essa faixa estima o teto clássico prático e é reportada separadamente. Um resultado favorável ao QML em 2D não será apresentado como superioridade sobre o melhor modelo clássico de maior dimensionalidade.

### 7.3 Baselines

- Dummy estratificado ou majoritário, conforme definição registrada;
- regressão logística;
- SVM linear;
- SVM com kernel RBF;
- Random Forest;
- HistGradientBoosting;
- HOG e modelos de imagem pré-especificados;
- CNN pequena, embedding congelado, calibração e curvas de decisão somente nos módulos indicados e com rótulo confirmatório ou exploratório explícito.

### 7.4 Modelo quântico

O modelo principal utiliza SVC com matriz de kernel quântico de fidelidade pré-computada, baseada em codificação ZZ. O kernel de treino observado é preservado em sua forma bruta para auditoria; quando necessário, é simetrizado e projetado no cone PSD antes do ajuste do SVM. A magnitude da correção é sempre reportada.

---

## 8. Validação e seleção de hiperparâmetros

A análise principal utiliza validação cruzada aninhada e estratificada:

- **nível externo:** 4 folds × 3 repetições;
- **nível interno:** 3 folds;
- **critério de seleção:** acurácia balanceada média;
- **SVM:** `C ∈ {0,1; 1; 10}`;
- **RBF:** `gamma ∈ {scale, auto}`;
- **perfil de ruído:** selecionado apenas na validação interna;
- **teste externo:** aberto uma única vez por configuração selecionada.

Os folds externos não são tratados como replicações independentes. Seeds, repetições, folds, hiperparâmetros, perfil de ruído, tempos e custos são exportados para permitir reconstrução integral da decisão.

---

## 9. Desfechos e diagnósticos

### 9.1 Desfecho primário

- acurácia balanceada (BAC);
- contraste pareado ΔBAC entre QML e SVM-RBF.

### 9.2 Desfechos secundários

- acurácia;
- F1;
- calibração, quando aplicável;
- curvas de decisão nos módulos de imagem pré-especificados.

### 9.3 Geometria do kernel

- alinhamento kernel–alvo;
- posto efetivo;
- erro relativo de Frobenius;
- sobrevivência geométrica;
- variância fora da diagonal;
- separação intra/interclasse;
- condição espectral;
- entropia espectral;
- lacuna efetiva;
- simetria, diagonal e espectro PSD.

As definições principais são:

- **Erro geométrico:** `||K_obs − K_ideal||F / ||K_ideal||F`;
- **Sobrevivência:** `clip(1 − erro geométrico, 0, 1)`;
- **Alinhamento:** produto interno de Frobenius entre `K` e `yyᵀ`, normalizado pelas normas;
- **Posto efetivo:** `exp(−Σ p_i log p_i)`, com `p_i = λ_i / Σλ`.

### 9.4 Custo

- tempo total e por etapa;
- número de avaliações de circuitos;
- shots lógicos;
- custo por entrada da matriz;
- custo por unidade de BAC e de sobrevivência;
- uso de pares-âncora, Nyström e aquisição ativa.

---

## 10. Plano estatístico

A inferência primária utiliza teste t unilateral com correção de Nadeau–Bengio sobre as diferenças pareadas dos folds externos. Serão reportados:

- média de ΔBAC;
- intervalo de confiança corrigido de 95%;
- tamanho de efeito pareado `d_z`;
- valor de `p`;
- distribuição por aplicação, repetição e fold.

Análises de sensibilidade:

- permutação exata de sinais;
- TOST com margem de equivalência de ±0,02 BAC;
- correção de Holm para desfechos secundários;
- correlação de Spearman para H2;
- modelo de efeitos mistos com intercepto aleatório por aplicação para H4;
- regressão com erros robustos por cluster como sensibilidade;
- controles negativos por permutação de rótulos e deslocamento das entradas.

### Critérios de interpretação

- **superioridade:** ΔBAC estimado positivo e `p` corrigido < 0,05;
- **equivalência prática:** satisfeita pelo TOST com margem ±0,02;
- **resultado nulo:** ausência de evidência suficiente, reportada sem reclassificação;
- **inconclusivo:** incerteza ampla ou falha de precisão;
- **GO exploratório no laboratório:** ΔBAC > 0,02 e sobrevivência ≥ 0,85;
- **NO-GO exploratório:** ΔBAC < −0,02;
- **demais casos:** equivalência prática ou inconclusão, conforme os intervalos.

Não será alegada vantagem quântica com uma única amostra, um único split, uma única seed ou apenas significância nominal.

---

## 11. Escada ideal → shots → ruído → QPU

A ordem de execução é obrigatória:

1. statevector exato;
2. amostragem com shots finitos;
3. cinco perfis de ruído no Qiskit Aer;
4. pares-âncora em QPU, se os portões forem satisfeitos;
5. repetição dos pares-âncora em uma segunda sessão independente;
6. classificador QPU completo somente por último.

### Perfis de ruído pré-especificados

| Perfil | erro 1Q | erro 2Q | erro de leitura |
|---|---:|---:|---:|
| Controle | 0 | 0 | 0 |
| Baixo | 0,0005 | 0,005 | 0,01 |
| Moderado | 0,001 | 0,01 | 0,02 |
| Alto-2Q | 0,001 | 0,03 | 0,02 |
| Leitura-alta | 0,001 | 0,01 | 0,05 |

### Portão para hardware real

A etapa de pares-âncora só avança quando:

- correlação ideal–QPU ≥ 0,90;
- MAE ≤ 0,10;
- custo documentado e viável;
- testes de integridade aprovados.

O classificador QPU completo exige que os critérios reapareçam em **duas sessões independentes**. Credenciais e tokens IBM Quantum nunca são armazenados no notebook, GitHub ou OSF; devem existir somente como segredo temporário do ambiente de execução.

---

## 12. Portões de evidência

### Portão 0 — integridade

Falha imediata quando houver classe ausente, sobreposição entre splits, NaN/Inf não tratado, formato incompatível, matriz inválida ou custo acima do orçamento documentado.

### Portão 1 — validade geométrica

Exige auditoria de simetria, diagonal, PSD, erro de Frobenius, alinhamento, posto efetivo e separação intra/interclasse.

### Portão 2 — validade preditiva

A seleção ocorre apenas internamente. O teste externo não pode retroalimentar hiperparâmetros, perfil de ruído ou escolha de mapa.

### Portão 3 — estabilidade

O sinal do efeito, a sobrevivência geométrica e os diagnósticos devem ser avaliados entre seeds, folds, repetições e aplicações.

### Portão 4 — custo

Desempenho e geometria são avaliados conjuntamente ao orçamento de circuitos, shots e tempo.

### Portão 5 — transferência para QPU

Hardware real é uma etapa condicional, nunca um requisito para fabricar um resultado favorável.

O estudo não interrompe uma execução por desempenho favorável ou desfavorável. Paradas antecipadas são permitidas apenas por falha técnica, integridade ou orçamento pré-especificado.

---

## 13. Estado atual e resultados disponíveis

### 13.1 Resultado confirmatório

**Ainda não há resultado confirmatório.** Essa ausência é deliberada e metodologicamente correta: o protocolo determina que a execução limpa comece somente após a conclusão do registro e a verificação dos hashes.

### 13.2 Evidência piloto anterior ao registro

Antes do pré-registro foram realizadas apenas atividades de preparação:

- inspeção das bases públicas;
- execução de exemplos didáticos;
- depuração do pipeline;
- observação de frequências sob diferentes números de shots;
- observação de desvio diagonal aproximado de 0,006 em teste piloto.

Esses valores não entram na inferência, não serão combinados com estimativas confirmatórias e não podem sustentar conclusão sobre superioridade. Servem apenas para verificar funcionamento, dimensionar custo e congelar decisões técnicas.

### 13.3 Estado operacional

- protocolo e critérios congelados;
- pacote de pré-registro gerado;
- arquivos centrais depositados;
- checksums publicados;
- pré-registro submetido em 17/08/2026;
- aprovação do embargo ainda pendente;
- CV aninhada confirmatória ainda não iniciada;
- experimentos Aer confirmatórios ainda não iniciados;
- pares-âncora e classificador QPU ainda não executados.

---

## 14. Arquivos depositados

1. **`trilha_quantum_ia_pesquisador_colab.ipynb`** — notebook Colab autodidático e executável;
2. **`build_quantum_notebook.py`** — fonte de construção e manutenção do notebook;
3. **`pre_registro_osf.zip`** — protocolo, formulário e artefatos de congelamento;
4. **`formulario_osf_preenchido.md`** — conteúdo completo do pré-registro;
5. **`dicionario_variaveis_osf.csv`** — nomes, tipos e significado das variáveis;
6. **`CHECKSUMS.sha256`** — verificação criptográfica dos arquivos centrais.

Os arquivos devem ser verificados pelos checksums antes de qualquer execução confirmatória. A cópia registrada não deve ser substituída; atualizações operacionais devem receber nova versão e registro explícito de alterações.

---

## 15. Como reproduzir o estudo

1. Acesse os arquivos do projeto OSF.
2. Baixe o notebook e o arquivo `CHECKSUMS.sha256`.
3. Verifique os hashes antes da execução.
4. Abra o notebook em um ambiente Colab limpo.
5. Execute a célula de instalação e registre versões de Python, Qiskit 2.x, Qiskit Aer, scikit-learn, NumPy, pandas e dependências.
6. Mantenha `SEED=42` e as derivações determinísticas.
7. Na cópia de execução, preencha `OSF_REGISTRATION_URL` com a URL permanente do registro `https://osf.io/9yuvr/`; não altere o snapshot registrado.
8. Execute primeiro os testes automáticos de integridade.
9. Rode a CV aninhada e exporte todos os folds, seeds, hiperparâmetros e métricas.
10. Execute a suíte multibase.
11. Prossiga para a escada de shots e os perfis Aer somente após aprovação dos portões anteriores.
12. Considere QPU apenas quando os critérios geométricos e de custo forem satisfeitos.
13. Armazene matrizes brutas, matrizes corrigidas, tempos, contagens de circuitos e logs.
14. Publique resultados positivos, nulos, equivalentes e inconclusivos.
15. Registre toda divergência do plano como desvio pós-registro, com data, motivo e impacto.

### Saídas mínimas de auditoria

Cada linha de resultado deve permitir identificar aplicação, seed, repetição, fold externo, fold interno, regime de execução, perfil de ruído, modelo, hiperparâmetros, número de shots, BAC, acurácia, F1, alinhamento, posto efetivo, erro geométrico, sobrevivência, tempo e custo lógico.

---

## 16. Controle de qualidade e testes automáticos

O notebook incorpora verificações equivalentes a SDD/TDD para assegurar que:

- os splits não se sobrepõem;
- todas as classes previstas estão presentes;
- não há NaN ou infinito inesperado;
- as formas das matrizes são consistentes;
- a matriz de treino é quadrada;
- simetria e diagonal permanecem dentro das tolerâncias;
- autovalores e correção PSD são registrados;
- kernels de treino e teste têm dimensões compatíveis;
- o pré-processamento não acessa o fold externo;
- seeds e parâmetros são serializados;
- falhas geram registro explícito, nunca exclusão silenciosa.

Uma execução reprovada por integridade pode ser repetida com a mesma seed após correção técnica documentada. Não se troca a seed para buscar resultado mais favorável.

---

## 17. Governança analítica

As análises são classificadas antes da interpretação:

- **confirmatórias:** H1, critérios primários e procedimentos congelados;
- **mecanísticas pré-especificadas:** sobrevivência geométrica, H2 e H4;
- **exploratórias:** H3, H5, comparações adicionais, ablações não centrais e módulos clínicos proibidos de interpretação assistencial;
- **desvios:** qualquer mudança pós-registro, sempre datada e separada da análise original.

O projeto adota relatório completo, incluindo falhas técnicas, resultados negativos e custos. Escolhas pós-hoc não substituem a análise confirmatória.

---

## 18. Limitações previstas

- custo `O(n²)` para matrizes de kernel;
- tamanhos reduzidos nos laboratórios de imagem por orçamento de shots;
- ausência de cálculo prospectivo de poder para alguns contrastes;
- ruído Aer não reproduz integralmente drift e correlações de uma QPU real;
- resultados dependem do mapa de características e da representação escolhida;
- múltiplas aplicações aumentam a complexidade inferencial;
- benchmarks públicos não representam todos os cenários reais;
- eventual significância estatística não implica relevância prática;
- eventual desempenho em BreastMNIST ou PneumoniaMNIST não implica validade clínica.

O tamanho amostral não será aumentado depois de observar significância. Incerteza, intervalos e sensibilidade serão priorizados sobre conclusões dicotômicas.

---

## 19. Princípios de ciência aberta

- protocolo prospectivo e versionado;
- hashes criptográficos;
- notebook executável;
- dicionário de variáveis;
- ambientes e versões registrados;
- separação entre piloto e confirmação;
- divulgação de resultados nulos;
- custos e desvios documentados;
- dados de terceiros mantidos sob suas licenças originais;
- código do repositório atualmente regido pelo arquivo `LICENSE` Apache 2.0;
- divergência Apache 2.0 × menção MIT no pré-registro declarada, sem alteração silenciosa;
- nenhuma credencial ou token em repositórios públicos;
- proibição de reivindicar ineditismo, benefício clínico ou vantagem quântica antes da evidência.

---

## 20. Roteiro de execução

- [x] estruturar notebook autodidático;
- [x] implementar baselines fortes;
- [x] separar comparação justa 2D do teto clássico de até 32 componentes;
- [x] congelar protocolo e hipóteses;
- [x] gerar checksums e pacote OSF;
- [x] depositar os arquivos centrais;
- [x] submeter o pré-registro;
- [ ] obter aprovação do embargo;
- [ ] executar CV aninhada confirmatória;
- [ ] executar suíte multibase;
- [ ] executar escada ideal → shots → ruído Aer;
- [ ] avaliar pares-âncora em duas sessões QPU, se houver GO;
- [ ] executar classificador QPU completo, se todos os portões forem satisfeitos;
- [ ] publicar relatório final, resultados, custos e desvios.

---

## 21. Citação sugerida

LARANJEIRA, Marcelo Claro. **Portões de evidência geométrica para kernels quânticos reprodutíveis sob ruído e custo**. OSF, 2026. Disponível em: [https://osf.io/kqs2w/](https://osf.io/kqs2w/). Acesso em: 17 ago. 2026.

---

## 22. Nota de interpretação responsável

Este projeto mede evidência, não promessa tecnológica. Um resultado nulo, equivalente ou desfavorável ao kernel quântico é cientificamente informativo. A progressão até hardware real depende da preservação geométrica, da estabilidade entre repetições e do custo. A conclusão deverá refletir a força real dos dados, sem transformar viabilidade computacional em vantagem quântica e sem transformar benchmark metodológico em aplicação clínica.


---

## Apêndice A — Resultados-piloto preservados no GitHub

> **Classificação:** resultados exploratórios e de depuração anteriores à execução confirmatória. Eles não testam formalmente o protocolo pós-registro e não podem ser usados para declarar vantagem quântica.

O snapshot executado em 16/08/2026 contém 101 células, 106 saídas armazenadas e nenhum erro de execução. O notebook integral está em [`resultados/notebook_executado_piloto_2026-08-16.ipynb`](resultados/notebook_executado_piloto_2026-08-16.ipynb), e o relatório auditável está em [`RESULTADOS_ATUAIS.md`](RESULTADOS_ATUAIS.md).

### A.1 Comparação principal do piloto

| Modelo | Acurácia | BAC | F1 | Tempo do kernel |
|---|---:|---:|---:|---:|
| Regressão logística | 0,906 | 0,906 | 0,914 | — |
| SVM-RBF | 0,906 | 0,906 | 0,914 | — |
| SVM + kernel quântico | 0,656 | 0,656 | 0,667 | 140,80 s |

O contraste piloto foi ΔBAC = −0,2250, com IC95% corrigido [−0,3221; −0,1279]. O sinal favoreceu o SVM-RBF. Esse achado é negativo e informativo, mas permanece condicionado à pequena amostra e ao caráter pré-registro da execução.

### A.2 Escada de validade do piloto

| Nível | BAC/acurácia observada | Erro geométrico | Alinhamento | Posto efetivo |
|---|---:|---:|---:|---:|
| Statevector exato | 0,688 | 0,000 | 0,078 | 9,00 |
| 5.888 shots | 0,656 | 0,007 | 0,077 | 9,16 |
| Aer com ruído moderado | 0,656 | 0,053 | 0,077 | 11,63 |

A execução piloto usou 5.888 shots e é preservada sem reescrita. A execução confirmatória deverá usar o parâmetro canônico de 2.048 shots, além da escada pré-especificada. Isso impede que um valor escolhido antes do registro seja silenciosamente confundido com o protocolo final.

### A.3 Suíte multibase piloto

| Base | BAC RBF | BAC QML | ΔBAC | Sobrevivência geométrica |
|---|---:|---:|---:|---:|
| Breast Cancer metodológico | 0,917 | 0,843 | −0,073 | 0,990 |
| Iris binária | 1,000 | 0,833 | −0,167 | 0,984 |
| make_moons | 0,958 | 0,758 | −0,200 | 0,986 |
| Wine binário | 0,898 | 0,820 | −0,078 | 0,988 |

Todos os valores médios de ΔBAC foram negativos. A elevada sobrevivência geométrica não garantiu superioridade preditiva, reforçando a necessidade de avaliar conjuntamente geometria, desempenho e custo.

### A.4 Parecer responsável

Os resultados-piloto não sustentam vantagem quântica e bloquearam, de maneira metodologicamente coerente, qualquer avanço automático para o classificador completo em QPU. A próxima evidência válida deverá provir de execução limpa pós-registro, CV aninhada repetida, dependência entre folds corrigida e replicação independente.

---

## Apêndice B — Mapa dos artefatos GitHub

| Artefato | Função |
|---|---|
| [`README.md`](README.md) | entrada pedagógica e instruções rápidas |
| [`WIKI_CIENTIFICA.md`](WIKI_CIENTIFICA.md) | protocolo explicado, governança e auditoria |
| [`RESULTADOS_ATUAIS.md`](RESULTADOS_ATUAIS.md) | resultados-piloto detalhados |
| [notebook principal](Projeto_Fundamentos_quânticos_aplicados_à_pesquisa_em_IA.ipynb) | execução limpa e autodidática |
| [`build_quantum_notebook.py`](build_quantum_notebook.py) | gerador reprodutível do notebook |
| [notebook piloto](resultados/notebook_executado_piloto_2026-08-16.ipynb) | snapshot imutável das saídas anteriores ao registro |
| [`LICENSE`](LICENSE) | licença vigente no repositório |

---

## 23. Pacote editorial para artigo científico

Em 17/08/2026 foi criada a versão 0.1 de um manuscrito metodológico, reprodutível e orientado a resultados negativos.

### 23.1 Artefatos

| Artefato | Finalidade |
|---|---|
| [MANUSCRITO.md](artigo/MANUSCRITO.md) | artigo completo em estrutura IMRaD |
| [DECLARACAO_REPRODUTIBILIDADE.md](artigo/DECLARACAO_REPRODUTIBILIDADE.md) | ambiente, parâmetros e procedimento |
| [CHECKLIST_SUBMISSAO.md](artigo/CHECKLIST_SUBMISSAO.md) | itens concluídos e pendentes |
| [JSON diagnóstico](resultados/resumo_diagnostico_2048shots_2026-08-17.json) | resultados legíveis por máquina |
| [CITATION.cff](CITATION.cff) | metadados de citação |

### 23.2 Tese científica atual

A validade numérica e a sobrevivência geométrica de um kernel quântico não implicam vantagem preditiva. No diagnóstico de 2.048 shots, o kernel permaneceu simétrico, unitário na diagonal e efetivamente PSD; entretanto, alcançou BAC 0,625 contra 0,875 do SVM-RBF. O alinhamento kernel–alvo foi 0,10975.

### 23.3 Status editorial

A versão atual pode ser divulgada como **preprint metodológico com resultados exploratórios negativos**. Não pode ser apresentada como confirmação de H1–H6 enquanto permanecerem pendentes:

1. aprovação do registro;
2. execução limpa confirmatória;
3. CV aninhada 4×3;
4. análise corrigida para dependência;
5. validação externa;
6. replicação independente;
7. harmonização da licença;
8. confirmação de afiliação, ORCID, financiamento e conflitos.

### 23.4 Princípio de publicação

Resultados nulos, inconclusivos ou negativos devem ser publicados com a mesma rastreabilidade dos resultados positivos. A QPU permanece uma etapa posterior, condicionada ao portão científico e não ao interesse demonstrativo.

