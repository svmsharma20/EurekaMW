FROM ubuntu

# Let's work here
WORKDIR /opt/app

# Copy the source into the image
COPY . ./

# Install dependencies
RUN apt update && \
apt install -y python-pip && \
pip install Flask pymongo

# This fails. No idea why. I have 0 Python knowledge :)
CMD python -m com.eurekamw_mg.controller.Main
