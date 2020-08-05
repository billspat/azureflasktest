## Azure Flask Test

This is a test of deployment methods to [Azure Web App Service](https://azure.microsoft.com/en-us/services/app-service/web/)

It really doesn't do anything other than test the .env config, and report on which libs are installed
and maybe some aspects of those libs. 

---
Python3

1. create environment however you like, e.g.

```bash
conda create -n azureflasktest pip
conda activate azureflasktest
```

2. install

```
pip install -r requirements.txt
```

3. config env

this step is required as the app needs 

copy .env-example to .env

```
cp .env-example .env
```

edit .env as needed (as of initial commit that's not necessary)

4. run

```
flask run
```

note you may have to start a new shell or clear your env if some vars are already set.   

---

# deploy to Azure

*instructions coming...*

---

August 2020
