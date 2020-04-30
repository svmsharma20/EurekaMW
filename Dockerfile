FROM ubuntu

# Let's work here
WORKDIR /opt/app

# Copy the source into the image
COPY . ./

# Install dependencies
RUN apt update && \
apt install -y curl python3 python3-pip && \
pip3 install flask pymongo requests

# Our app runs at 5000
EXPOSE 5000

# Check if our app is running
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=10 \
    CMD curl http://localhost:5000

# Start EurekaMW!
CMD python3 -m com.eurekamw_mg.controller.Main
