from src.server.sync_tcp import run_tcp_server


def main():
    print("Starting redispy-db...")
    run_tcp_server()


if __name__ == "__main__":
    main()
