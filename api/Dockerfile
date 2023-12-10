FROM python:3.10.12

# # Create the log directory and set permissions
# RUN mkdir -p /var/log/uwsgi && \
#     chown -R www-data:www-data /var/log/uwsgi

# # Set user permissions or switch to the appropriate user
# USER www-data

COPY requirements.txt .

RUN apt-get update && apt-get install -y uwsgi

RUN pip install -r requirements.txt

#RUN python -c "import nltk; nltk.download('omw/1.4'); nltk.download('wordnet')"

COPY . .

#EXPOSE 5001


CMD [ "uwsgi", "app.ini" ]
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]