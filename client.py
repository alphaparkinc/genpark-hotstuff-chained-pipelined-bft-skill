class HotStuffBlock:
    def __init__(self, parent_hash, view, command):
        self.parent_hash = parent_hash
        self.view = view
        self.command = command
        self.qc = None

class HotStuffEngine:
    """
    HotStuff Chained BFT Engine simplifying multi-phase commits
    into a uniform pipelined block chain.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.current_view = 1
        self.high_qc = "GENESIS_QC"
        self.blocks = {}
        self.committed = []

    def propose_block(self, command):
        blk = HotStuffBlock(parent_hash=self.high_qc, view=self.current_view, command=command)
        blk_hash = f"BLOCK_{self.current_view}_{command}"
        self.blocks[blk_hash] = blk
        return blk_hash, blk

    def update_high_qc(self, qc, block_hash):
        self.high_qc = qc
        self.current_view += 1
        if len(self.blocks) >= 3:
            self.committed.append(block_hash)
            return True
        return False
