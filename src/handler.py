"""Request handler for cedarline-exporter."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "cedarline-exporter"}
