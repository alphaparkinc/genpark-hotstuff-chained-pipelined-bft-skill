from client import HotStuffEngine

def main():
    print("=== Testing HotStuff Chained BFT Engine ===")
    hs = HotStuffEngine(node_id=1)
    b1_h, _ = hs.propose_block("CMD_1")
    hs.update_high_qc("QC_1", b1_h)
    b2_h, _ = hs.propose_block("CMD_2")
    hs.update_high_qc("QC_2", b2_h)
    b3_h, _ = hs.propose_block("CMD_3")
    committed = hs.update_high_qc("QC_3", b3_h)

    print("Three-chain commit status:", committed)
    assert committed
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
