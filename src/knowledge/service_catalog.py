from src.models.schemas import Service


SERVICE_CATALOG = [
    Service(
        service_id="video-streaming-001",
        name="Low Latency Video Streaming",
        capabilities=[
            "video_streaming",
            "low_latency"
        ],
        domain="automotive",
        properties={
            "latency": "10ms",
            "bandwidth": "100Mbps",
            "availability": "99.99%"
        }
    ),

    Service(
        service_id="video-streaming-002",
        name="Standard Video Streaming",
        capabilities=[
            "video_streaming"
        ],
        domain="generic",
        properties={
            "latency": "50ms",
            "bandwidth": "50Mbps",
            "availability": "99.9%"
        }
    ),

    Service(
        service_id="object-detection-001",
        name="Edge Object Detection",
        capabilities=[
            "object_detection",
            "edge_ai"
        ],
        domain="automotive",
        properties={
            "latency": "15ms",
            "compute": "GPU"
        }
    ),

    Service(
        service_id="edge-compute-001",
        name="Automotive Edge Compute",
        capabilities=[
            "edge_compute",
            "low_latency"
        ],
        domain="automotive",
        properties={
            "latency": "5ms",
            "cpu": "16",
            "memory": "32GB"
        }
    )
]


def get_service_catalog() -> list[Service]:
    return SERVICE_CATALOG