# 15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

## Usage

```bash
$ python tail.py -h
usage: tail.py [-h] [-n number] file

display the last part of a file

positional arguments:
  file

optional arguments:
  -h, --help  show this help message and exit
  -n number   The location is number lines. The default
              starting location is ``-n 10'', or the last
              10 lines of the input.
```
