# ベースイメージはDebianを使用（軽量でカスタマイズ性が高い）
FROM debian:bookworm

# PyPyのパスを環境変数として設定
ENV PYPY_HOME=/opt/pypy3.10 \
    PATH="/usr/local/pypy3.10/bin:$PATH"

# 必要なツールとgcc, Pythonのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates \
    gnupg \
    gcc-12 \
    python3 \
    python3.11-venv \
    python3-pip \
    vim \
    procps \
    tree \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# PyPy 3.10 のインストール
RUN wget https://downloads.python.org/pypy/pypy3.10-v7.3.12-linux64.tar.bz2 && \
    tar -xjf pypy3.10-v7.3.12-linux64.tar.bz2 && \
    mv pypy3.10-v7.3.12-linux64 $PYPY_HOME && \
    ln -s $PYPY_HOME/bin/pypy3 /usr/local/bin/pypy3 && \
    rm pypy3.10-v7.3.12-linux64.tar.bz2


# online-judge-toolsとPythonで使うその他のライブラリのインストール
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip3 install online-judge-tools black

# 仮想環境を開き、シェルを上書きする
CMD ["/bin/bash", "-c", ". /venv/bin/activate && exec bash"]