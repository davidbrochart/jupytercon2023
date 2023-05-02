```bash
micromamba create -n jupytercon2023
micromamba activate jupytercon2023
micromamba install -c conda-forge jupyter_server

jupyter server
jupyter server extension list
# jupyter_server_terminals

micromamba install -c conda-forge jupyterlab
jupyter server extension list
# jupyter_server_terminals
# jupyter_server_fileid
# jupyter_server_ydoc
# jupyterlab
# nbclassic
jupyter lab

jupyter server extension disable jupyter_server_terminals
jupyter server extension list
jupyter lab
# not able to open a terminal

jupyter lab --ServerApp.jpserver_extensions="jupyter_server_terminals=True"

pip install -e .
http://127.0.0.1:8888/myextension/hello
```
