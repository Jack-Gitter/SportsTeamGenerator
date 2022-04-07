FROM amazon/aws-lambda-python:3.8
    
# Copy function code
COPY threePointShooters.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt

CMD ["ppg.findppg"]