# 好心情 Python API client for stable-diffusion-webui



<div align="center">  
<h4>
｜<a href="#安装"> 安装 </a>
｜<a href="#启动"> 启动 </a>
</h4>
</div>


本库包含stable-diffusion-webui API相关功能。

## 安装

 pip install -r requirements.txt


## 启动

### FastAPI方式启动HTTP服务

```shell
uvicorn main:app --reload --host=0.0.0.0 --port=32102
```


### 在Linux服务器运行

```shell

nohup uvicorn main:app --reload --host=0.0.0.0 --port=32102 > uvicorn.log 2>&1 &

```

