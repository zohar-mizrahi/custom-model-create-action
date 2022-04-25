FROM python:3.9-slim

COPY src/ /opt/action
RUN pip install -r /opt/action/requirements.txt

ENTRYPOINT ["/opt/action/entrypoint.sh"]
