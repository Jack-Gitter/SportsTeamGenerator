FROM amazon/aws-lambda-python:3.8
    
# Copy function code
COPY ws.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

CMD ["ws.findws"]