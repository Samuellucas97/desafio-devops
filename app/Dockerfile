FROM python:3.7.4 as builder

WORKDIR /opt/app

COPY requirements.txt .  

RUN pip install --no-cache-dir -r requirements.txt        

################

FROM python:3.7.4-alpine 

COPY --from=builder /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/       
COPY ./api.py . 

EXPOSE 5000

CMD ["gunicorn", "--log-level", "debug", "api:app"]