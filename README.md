# nlp100

<http://www.cl.ecei.tohoku.ac.jp/nlp100/>

> ## 言語処理100本ノック 2015
>
> 言語処理100本ノックは，実践的な課題に取り組みながら，プログラミング，データ分析，研究のスキルを楽しく習得することを目指した問題集です
>
> - 実用的でワクワクするような題材を厳選しました
> - 言語処理に加えて，統計や機械学習などの周辺分野にも親しめます
> - 研究やデータ分析の進め方，作法，スキルを修得できます
> - 問題を解くのに必要なデータ・コーパスを配布しています
> - 言語はPythonを想定していますが，他の言語にも対応しています

## 環境

Python 3.8.1 を利用する。

### pyenv, virtualenv での環境構築方法

```bash
pyenv install 3.8.1
pyenv virtualenv 3.8.1 nlp100
pyenv local nlp100
```

## コマンド

```bash
# Install Dependencies
pipenv install
# Install Dependencies for develop
pipenv install --dev
# Test
pipenv run test
# Lint
pipenv run lint
# Format
pipenv run format
```
