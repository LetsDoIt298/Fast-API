# Fast-API 

This repository helps to understand how to execute GET and POST method.

# Requiremnets
* Python 3.6 or above
* Conda installed in system
* PostMan for API testing

# Steps for execution using python
* Step1 -> Open VS code or the desired IDE
* Step2 -> Create an envirnoment by executing the below command => 'conda create -p <envirnmoment_name> python==<Python_version> -y'
* Step3 -> Create requirements.txt include fastapi, uvicorn in it
* Step4 -> Install requiremnt file, run following command i terminal => pip install -r requirements.txt
* Step5 -> Now, select main file which you want to execute.
* Let's say chosen file is main1
* Step6 -> Run following command in terminal=> uvicorn main1:app --reload
* Step7 -> Now open Postman
* Step8 -> Since api is GET therefoe select GET in PostMan. and paste http://127.0.0.1:8000 and click Send in PostMan.

