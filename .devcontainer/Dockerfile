# ベースイメージはDebianを使用（軽量でカスタマイズ性が高い）
FROM debian:bookworm

# PyPyのパスを環境変数として設定
ENV PYPY_HOME=/opt/pypy3.10 \
    PATH="/usr/local/pypy3.10/bin:/opt/pypy3.10/bin:$PATH"

# 必要なツールとgccのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    dpkg \
    libicu72 \
    ca-certificates \
    gnupg \
    gcc-12 \
    git \
    vim \
    procps \
    tree

# PyPy 3.10 のインストール
RUN wget https://downloads.python.org/pypy/pypy3.10-v7.3.12-linux64.tar.bz2 && \
    tar -xjf pypy3.10-v7.3.12-linux64.tar.bz2 && \
    mv pypy3.10-v7.3.12-linux64 $PYPY_HOME && \
    ln -s $PYPY_HOME/bin/pypy3 /usr/local/bin/pypy3 && \
    rm pypy3.10-v7.3.12-linux64.tar.bz2


# pip
RUN pypy3 -m ensurepip && \
    pypy3 -m pip install -U pip wheel

# powershellのインストール
RUN wget https://github.com/PowerShell/PowerShell/releases/download/v7.4.7/powershell-lts_7.4.7-1.deb_amd64.deb && \
    dpkg -i powershell-lts_7.4.7-1.deb_amd64.deb && \
    apt-get install -f -y && \
    rm powershell-lts_7.4.7-1.deb_amd64.deb

# online-judge-toolsとPythonで使うその他のライブラリのインストール
RUN pypy3 -m pip install online-judge-tools black


RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# 仮想環境を開き、シェルを上書きする
CMD ["/bin/bash"]