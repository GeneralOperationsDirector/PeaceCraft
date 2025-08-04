# trust.py
def adjust_trust_level(current, npc_reply):
    if "sorry" in npc_reply.lower() or "understand" in npc_reply.lower():
        return min(100, current + 5)
    elif "blame" in npc_reply.lower() or "refuse" in npc_reply.lower():
        return max(0, current - 5)
    return current
