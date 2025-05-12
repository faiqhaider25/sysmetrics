import argparse
import uvicorn
from syspulse.server import app

def main():
    parser = argparse.ArgumentParser(description="SysPulse - System Monitoring Tool")
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind the server to")
    parser.add_argument("--remote", action="store_true", help="Allow remote access (binds to 0.0.0.0)")
    
    args = parser.parse_args()
    
    host = "0.0.0.0" if args.remote else args.host
    print(f"Starting SysPulse server on {host}:{args.port}")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run(app, host=host, port=args.port)

if __name__ == "__main__":
    main() 