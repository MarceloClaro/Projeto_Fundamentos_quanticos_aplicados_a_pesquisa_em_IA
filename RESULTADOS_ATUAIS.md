# Resultados atuais — snapshot piloto

📘 Para o protocolo completo, consulte a [Wiki científica e reprodutível](WIKI_CIENTIFICA.md).

> **Classificação de evidência:** resultados exploratórios e de depuração produzidos antes da análise confirmatória registrada. Este documento preserva o estado observado sem convertê-lo em confirmação de hipótese, vantagem quântica ou evidência clínica.

## Proveniência e integridade

- Fonte: notebook executado anteriormente na branch `main`.
- Blob Git original: `2749d6fe1e1c141fceca7c581ac426ecd53db6d9`.
- Estado preservado: 101 células, 106 saídas e nenhum erro de execução armazenado.
- Registro confirmatório: [OSF 9yuvr](https://osf.io/9yuvr/overview), submetido em 17/08/2026; aprovação do embargo pendente, com término previsto para 16/08/2027.
- Snapshot completo: `resultados/notebook_executado_piloto_2026-08-16.ipynb`.
- Hardware real: **não executado**; não há resultado de QPU neste snapshot.
- O piloto preservado usou 5.888 shots; a execução confirmatória deve usar 2.048 shots como referência canônica e reportar separadamente a escada pré-especificada.

## 1. Diagnóstico numérico do kernel

| Métrica | Valor observado | Critério/uso | Situação |
|---|---:|---:|:---|
| Assimetria máxima | `0.000e+00` | `≤ 1.0e-10` | aprovado |
| Desvio diagonal bruto após reparo PSD | `2.036e-02` | diagnóstico | registrado antes da normalização |
| Desvio diagonal normalizado | `0.000e+00` | `≤ 1.0e-10` | aprovado após normalização |
| Menor autovalor | `-2.794e-15` | `≥ -1.0e-10` | aprovado dentro da precisão numérica |
| Alinhamento kernel–alvo | `7.708e-02` | informativo | sem aprovação automática |

O reparo com `enforce_psd=True` deslocou a diagonal. A transformação por congruência

\[
K_{\mathrm{norm}}=D^{-1/2}KD^{-1/2}
\]

restaurou `k(xᵢ,xᵢ)=1` sem introduzir autovalor negativo relevante. A adequação de shots deve ser julgada pela estabilidade multissemente dos elementos fora da diagonal, e não pelo desvio intermediário causado pelo reparo PSD.

## 2. Comparação principal no conjunto de teste

| Modelo | Acurácia | BAC | F1 | Tempo do kernel (s) |
|---|---:|---:|---:|---:|
| Regressão logística | 0,906 | 0,906 | 0,914 | — |
| SVM-RBF | 0,906 | 0,906 | 0,914 | — |
| SVM + kernel quântico | 0,656 | 0,656 | 0,667 | 140,80 |

### Intervalos bootstrap observados

| Modelo | IC 2,5% | Mediana | IC 97,5% |
|---|---:|---:|---:|
| Regressão logística | 0,812 | 0,906 | 1,000 |
| SVM-RBF | 0,781 | 0,906 | 1,000 |
| SVM + kernel quântico | 0,500 | 0,656 | 0,812 |

O bootstrap descreve a instabilidade desta amostra pequena; não substitui validação externa, análise de potência ou repetição independente.

## 3. Inferência pareada piloto

| Desfecho | Média | IC95% corrigido | p corrigido | p Holm |
|---|---:|---:|---:|---:|
| ΔBAC QML − RBF | -0,2250 | [-0,3221; -0,1279] | 0,9998 | 0,9998 |
| Δ acurácia | -0,2250 | [-0,3221; -0,1279] | 0,0003442 | 0,0006884 |
| ΔF1 | -0,2078 | [-0,3484; -0,0672] | 0,007707 | 0,007707 |

Indicadores adicionais do desfecho primário: `p_TOST=0,9996`, permutação exata de sinais `p=0,0004883` e tamanho de efeito pareado `d_z=-3,292`.

**Conclusão limitada ao protocolo piloto:** o resultado observado favoreceu o SVM-RBF e foi classificado como inferioridade do QML neste protocolo. Isso é um resultado negativo informativo, não uma conclusão universal sobre kernels quânticos.

## 4. Escada de validade

| Nível | Acurácia | F1 | Erro geométrico relativo | Alinhamento | Posto efetivo | Tempo (s) |
|---|---:|---:|---:|---:|---:|---:|
| Statevector exato | 0,688 | 0,667 | 0,000 | 0,078 | 9,00 | 0,14 |
| 5.888 shots | 0,656 | 0,667 | 0,007 | 0,077 | 9,16 | 140,80 |
| Aer com ruído | 0,656 | 0,645 | 0,053 | 0,077 | 11,63 | 85,98 |

No nível Aer foram usados, no snapshot, `erro_1q=0,001`, `erro_2q=0,010` e `erro_leitura=0,020`. A geometria degradou mais sob ruído que sob amostragem finita, enquanto a BAC permaneceu em 0,656 entre shots e Aer.

## 5. Suíte multibase

| Base | BAC RBF | BAC QML | ΔBAC | Sobrevivência geométrica | Tempo médio do kernel (s) |
|---|---:|---:|---:|---:|---:|
| Breast Cancer metodológico | 0,917 | 0,843 | -0,073 | 0,990 | 1,94 |
| Iris binária | 1,000 | 0,833 | -0,167 | 0,984 | 0,80 |
| make_moons | 0,958 | 0,758 | -0,200 | 0,986 | 1,17 |
| Wine binário | 0,898 | 0,820 | -0,078 | 0,988 | 1,13 |

Os quatro valores médios de ΔBAC foram negativos. A sobrevivência geométrica elevada, isoladamente, não garantiu superioridade preditiva.

## 6. Aplicações guiadas e seleção de ruído

| Aplicação | Perfil selecionado | C | BAC QML ruidoso | BAC QML exato | BAC RBF | ΔBAC ruidoso − RBF | Sobrevivência | Parecer |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Iris Setosa–Versicolor | baixo | 10,0 | 0,500 | 0,417 | 1,000 | -0,500 | 0,951 | NO-GO; baseline clássico favorecido |
| BreastMNIST | shots sem ruído | 0,1 | 0,500 | 0,500 | 0,500 | 0,000 | 0,965 | equivalência prática ou inconclusão; sem interpretação clínica |
| make_moons | leitura alta | 0,1 | 0,500 | 0,500 | 0,833 | -0,333 | 0,904 | NO-GO; baseline clássico favorecido |

O perfil e `C` foram escolhidos na validação e o teste foi aberto uma vez. O resultado de BreastMNIST não demonstra utilidade clínica e não autoriza inferência diagnóstica.

## 7. Estado dos portões

| Etapa | Estado atual |
|---|---|
| Kernel simétrico, normalizado e PSD | concluído no piloto |
| Comparação com baselines clássicos | concluída no piloto |
| Inferência pareada e sensibilidades | concluídas no piloto |
| Escada statevector → shots → Aer | concluída no piloto |
| Suíte multibase piloto | concluída |
| CV confirmatória pós-registro | pendente de execução limpa |
| Replicação independente | pendente |
| Pares-âncora em duas sessões QPU | não executados |
| Classificador completo em QPU | bloqueado pelos portões anteriores |

## Parecer científico atual

Os resultados preservados **não sustentam vantagem quântica**. Eles mostram que a geometria do kernel pode sobreviver parcialmente a shots e ruído sem produzir ganho preditivo, um achado metodologicamente relevante para evitar selecionar configurações apenas por fidelidade geométrica. A próxima evidência válida deve vir de execução pós-registro, ambiente limpo, CV aninhada repetida, correção da dependência entre folds e replicação independente. Somente depois devem ser considerados pares-âncora em QPU.

---

## 8. Snapshot diagnóstico de 2.048 shots — 17/08/2026

> **Classificação:** execução diagnóstica posterior à submissão do registro, realizada antes da aprovação do embargo. Não constitui análise confirmatória.

### 8.1 Ambiente

Python 3.12.13; Qiskit 2.3.1; Qiskit Aer 0.17.2; Qiskit Machine Learning 0.9.0; scikit-learn 1.6.1; seed 42; 2.048 shots.

### 8.2 Amostra e modelos

- treino: 32;
- teste: 16;
- duas classes balanceadas;
- QPU desativada;
- módulos confirmatórios e extensos desativados.

| Modelo | Acurácia | BAC | F1 | Tempo do kernel |
|---|---:|---:|---:|---:|
| SVM-RBF | 0,8750 | 0,8750 | 0,8889 | — |
| Regressão logística | 0,8125 | 0,8125 | 0,8421 | — |
| SVM + kernel quântico | 0,6250 | 0,6250 | 0,5000 | 8,60 s |

### 8.3 Inferência descritiva

- ΔBAC QML–RBF: −0,25;
- IC95% pareado: [−0,5625; 0,0625];
- mediana bootstrap: −0,25;
- fração de 5.000 reamostragens com Δ positivo: 0,0424;
- parecer: inconclusivo porque o intervalo inclui zero;
- direção pontual: desfavorável ao QML.

### 8.4 Kernel e escada de validade

| Diagnóstico | Valor |
|---|---:|
| Assimetria máxima | 0 |
| Desvio diagonal | 0 |
| Menor autovalor | −7,81×10⁻¹⁶ |
| Alinhamento kernel–alvo | 0,10975 |
| Posto efetivo | 8,926 |
| Posto efetivo relativo | 0,2789 |
| Erro geométrico de 2.048 shots | 0,01216 |
| Avaliações de fidelidade estimadas | 1.008 |
| Shots lógicos estimados | 2.064.384 |

Statevector e 2.048 shots produziram acurácia 0,625 e F1 0,500. Portanto, a amostragem finita alterou discretamente a matriz, mas não explica a ausência de ganho preditivo.

### 8.5 Auditoria

Os 36 testes de integração foram aprovados. O resumo foi validado como JSON estrito, sem NaN, e está em [resultados/resumo_diagnostico_2048shots_2026-08-17.json](resultados/resumo_diagnostico_2048shots_2026-08-17.json).

### 8.6 Relação com o piloto anterior

O piloto de 5.888 shots permanece preservado e não foi sobrescrito. Os dois snapshots são metodologicamente distintos e não devem ser combinados como réplicas independentes. Ambos apresentam direção desfavorável ao QML, mas somente uma execução confirmatória futura poderá testar formalmente as hipóteses registradas.

