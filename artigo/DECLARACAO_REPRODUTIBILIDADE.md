# Declaração de reprodutibilidade computacional

## Identificação

- Projeto: Fundamentos Quânticos Aplicados à Pesquisa em IA
- Autor responsável: Marcelo Claro Laranjeira
- Data da execução diagnóstica: 17 ago. 2026
- Registro OSF: https://osf.io/9yuvr/overview
- Projeto OSF: https://osf.io/kqs2w/
- Classificação: diagnóstico pós-submissão, não confirmatório

## Ambiente observado

| Componente | Versão |
|---|---|
| Python | 3.12.13 |
| Qiskit | 2.3.1 |
| Qiskit Aer | 0.17.2 |
| Qiskit Machine Learning | 0.9.0 |
| NumPy | 2.0.2 |
| pandas | 2.2.2 |
| scikit-learn | 1.6.1 |
| scikit-image | 0.25.2 |
| statsmodels | 0.14.6 |
| MedMNIST | 3.0.2 |
| PyTorch | 2.11.0+cpu |
| torchvision | 0.26.0+cpu |

## Parâmetros canônicos

- SEED = 42
- SHOTS = 2048
- mapa ZZ: 2 qubits, 1 repetição, entrelaçamento linear
- treino diagnóstico: 32
- teste diagnóstico: 16
- reamostragens bootstrap: 5.000
- QPU: desativada
- módulos confirmatórios: desativados enquanto o registro aguarda aprovação

## Regras de integridade

1. O split é feito antes do ajuste da transformação.
2. O escalonador é ajustado apenas no treino.
3. Modelos recebem as mesmas observações de teste.
4. O baseline primário é o SVM-RBF.
5. Resultados-piloto não são reclassificados como confirmatórios.
6. Matrizes são auditadas quanto a simetria, diagonal e espectro.
7. Custo de fidelidade, shots e tempo é relatado.
8. A QPU permanece bloqueada até aprovação dos portões.

## Artefatos

| Arquivo | Função |
|---|---|
| artigo/MANUSCRITO.md | manuscrito científico |
| artigo/DECLARACAO_REPRODUTIBILIDADE.md | ambiente e regras de reprodução |
| artigo/CHECKLIST_SUBMISSAO.md | pendências editoriais e científicas |
| resultados/resumo_diagnostico_2048shots_2026-08-17.json | dados estruturados da execução |
| RESULTADOS_ATUAIS.md | histórico humano dos resultados |
| WIKI_CIENTIFICA.md | protocolo, governança e auditoria |
| build_quantum_notebook.py | gerador reprodutível |
| notebook principal | execução didática e científica |

## Procedimento de reprodução

1. Abrir uma sessão limpa do Colab.
2. Executar a instalação do ambiente.
3. Validar as versões exibidas pelo notebook.
4. Manter o URL OSF vazio e módulos confirmatórios desativados enquanto o registro estiver pendente.
5. Executar o núcleo com seed 42 e 2.048 shots.
6. Confirmar que os 36 testes de integração foram aprovados.
7. Comparar o JSON produzido com o snapshot versionado.
8. Registrar qualquer divergência de versão, tempo ou métrica; não substituir silenciosamente o snapshot.

## Critérios para execução confirmatória

A fase confirmatória exige aprovação do registro, URL inserida, ambiente limpo, validação externa 4×3, seleção interna em três folds, teste estatístico corrigido para dependência, registro de falhas e publicação de resultados nulos.

## Divergência de licença

O arquivo LICENSE vigente usa Apache-2.0, enquanto o registro menciona MIT para o código original. Até harmonização formal, o repositório deve declarar Apache-2.0 como licença operacional e documentar a divergência em todas as versões do manuscrito.
