# FastAPI + pytorch
利用 FastAPI 快速建立 inference api

## Docker
### Dockerfile-fastapi
From tiangolo/uvicorn-gunicorn-fastapi:python3.10
- python-multipart
- Pillow
- requests
- transformers
### Dockerfile-pytroch
- torch
- torchvision
- torchaudio
## 安裝
訓練完的模型放在 model 目錄，make build 建立 docker image
### 啟動
```shell
make run
```
### 開發模式
```shell
make dev
```
### 開發方式
```shell
vim app/main.py
修改完要進入 container 重跑 app
docker exec -it ai-service bash
kill -HUP 1
```
### Call API
```shell
curl --request POST --url http://localhost/predict -F file=@assets/zespri-1.jpg
```
### 壓力測試
```shell
make stress
make stress-loop
```
## 打包 docker image
Setup MODEL and APP_TAG in the Makefile
```shell
make build
```
### Docs
http://localhost/docs
