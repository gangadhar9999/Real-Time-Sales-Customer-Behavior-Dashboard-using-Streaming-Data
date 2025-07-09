#Python Script for Fake Real-Time E-Commerce Data
import random
import json
import time
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# Sample Data
event_types = ['page_view', 'click', 'add_to_cart', 'purchase', 'remove_from_cart']
product_ids = [f'P{str(i).zfill(4)}' for i in range(1, 101)]  # Product IDs P0001 to P0100

def generate_fake_data():
    """Generate a single fake transaction or user event."""
    data = {
        "order_id": fake.uuid4(),                   # Random Order ID
        "user_id": fake.random_int(min=1000, max=9999),  # User ID
        "product_id": random.choice(product_ids),   # Random Product ID
        "timestamp": datetime.utcnow().isoformat(), # Current Timestamp (UTC)
        "amount": round(random.uniform(10, 500), 2),  # Amount between $10 and $500
        "event_type": random.choice(event_types)    # Random Event Type
    }
    return data

# Simulate continuous data stream
def stream_fake_data(batch_size=10, sleep_time=2):
    """Simulate streaming by printing JSON data to console (or write to Kafka)."""
    while True:
        for _ in range(batch_size):
            event = generate_fake_data()
            print(json.dumps(event))  # You can push this to Kafka instead of print
        time.sleep(sleep_time)  # Simulate delay between batches

if __name__ == "__main__":
    stream_fake_data(batch_size=5, sleep_time=3)  # Generates 5 records every 3 seconds
