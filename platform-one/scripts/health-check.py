#!/usr/bin/env python3
"""
Health Check Script for Platform-One
Verifies the status of all services in the orchestration system.
"""

import asyncio
import httpx
import sys
import json
from datetime import datetime
import argparse

SERVICES = {
    "platform-one": "http://localhost:8001/health",
    "cnpj-qa-training": "http://localhost:8000/health",
    "fabrica-backend": "http://localhost:3000/health",
    "fabrica-frontend": "http://localhost:5173",
}

async def check_service_health(service_name: str, url: str) -> dict:
    """Check health of a single service"""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            start_time = asyncio.get_event_loop().time()
            response = await client.get(url)
            response_time = asyncio.get_event_loop().time() - start_time

            if response.status_code == 200:
                return {
                    "name": service_name,
                    "status": "healthy",
                    "response_time": round(response_time * 1000, 2),  # ms
                    "timestamp": datetime.utcnow().isoformat()
                }
            else:
                return {
                    "name": service_name,
                    "status": "unhealthy",
                    "error": f"HTTP {response.status_code}",
                    "timestamp": datetime.utcnow().isoformat()
                }
    except Exception as e:
        return {
            "name": service_name,
            "status": "error",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }

async def check_all_services() -> dict:
    """Check health of all services"""
    tasks = []
    for service_name, url in SERVICES.items():
        tasks.append(check_service_health(service_name, url))

    results = await asyncio.gather(*tasks, return_exceptions=True)

    health_status = {}
    all_healthy = True

    for i, service_name in enumerate(SERVICES.keys()):
        if isinstance(results[i], Exception):
            health_status[service_name] = {
                "name": service_name,
                "status": "error",
                "error": str(results[i])
            }
            all_healthy = False
        else:
            health_status[service_name] = results[i]
            if results[i]["status"] != "healthy":
                all_healthy = False

    return {
        "overall_status": "healthy" if all_healthy else "degraded",
        "timestamp": datetime.utcnow().isoformat(),
        "services": health_status
    }

def print_health_report(health_data: dict):
    """Print a formatted health report"""
    print("🏥 Platform-One Health Check Report")
    print("=" * 50)
    print(f"Overall Status: {'✅ HEALTHY' if health_data['overall_status'] == 'healthy' else '⚠️  DEGRADED'}")
    print(f"Timestamp: {health_data['timestamp']}")
    print()

    for service_name, service_data in health_data["services"].items():
        status_icon = {
            "healthy": "✅",
            "unhealthy": "⚠️ ",
            "error": "❌"
        }.get(service_data["status"], "❓")

        print(f"{status_icon} {service_name}")
        print(f"   Status: {service_data['status']}")

        if "response_time" in service_data:
            print(f"   Response Time: {service_data['response_time']}ms")

        if "error" in service_data:
            print(f"   Error: {service_data['error']}")

        print()

async def main():
    parser = argparse.ArgumentParser(description="Platform-One Health Check")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--exit-code", action="store_true", help="Exit with code based on health status")

    args = parser.parse_args()

    try:
        health_data = await check_all_services()

        if args.json:
            print(json.dumps(health_data, indent=2))
        else:
            print_health_report(health_data)

        # Exit with appropriate code
        if args.exit_code:
            sys.exit(0 if health_data["overall_status"] == "healthy" else 1)

    except Exception as e:
        print(f"❌ Health check failed: {e}", file=sys.stderr)
        if args.exit_code:
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())