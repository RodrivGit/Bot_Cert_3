from robocorp.tasks import task
from RPA.HTTP import HTTP
from RPA.JSON import JSON

@task
def produce_traffic_data():
    """
    Produce traffic data work items.
    """
    print("produce")
    download_traffic_data()

@task
def consume_traffic_data():
    """
    Consumes traffic data work items.
    """
    print("consume")

def download_traffic_data():
    http = HTTP()
    http.download(
        url="https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json",
        target_file="output/traffic.json",
        overwrite=True
    )

def filter_traffic_data():
    """
    Function to filter traffic data using the requirements
    """
    values = JSON().load_json_from_file("output/traffic.json")
    
filter_traffic_data()
