import sys
import json
from client import HotStuffEngine

def main():
    hs = HotStuffEngine(node_id=1)
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "propose":
            h, _ = hs.propose_block(params.get("command"))
            res = {"block_hash": h, "view": hs.current_view}
        elif method == "update_qc":
            c = hs.update_high_qc(params.get("qc"), params.get("block_hash"))
            res = {"committed": c, "new_view": hs.current_view}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
