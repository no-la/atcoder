# ベースイメージはDebianを使用（軽量でカスタマイズ性が高い）
FROM debian:bullseye

# PyPyのパスを環境変数として設定
ENV PYPY_HOME=/opt/pypy3.10 \
    PATH="/usr/local/pypy3.10/bin:$PATH"

# 必要なツールとgccのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates \
    gnupg \
    gcc-12 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# PyPy 3.10 のインストール
RUN wget https://downloads.python.org/pypy/pypy3.10-v7.3.12-linux64.tar.bz2 && \
    tar -xjf pypy3.10-v7.3.12-linux64.tar.bz2 && \
    mv pypy3.10-v7.3.12-linux64 $PYPY_HOME && \
    ln -s $PYPY_HOME/bin/pypy3 /usr/local/bin/pypy3 && \
    rm pypy3.10-v7.3.12-linux64.tar.bz2

# PyPy 用のpipインストール
RUN pypy3 -m ensurepip && \
    pypy3 -m pip install -U pip wheel

# online-judge-toolsのインストール
RUN pypy3 -m pip install online-judge-tools

# デフォルトのシェル
CMD ["/bin/bash"]
