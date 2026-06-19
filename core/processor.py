from core.brain import process as brain_process


def process(command: str):
    """
    Wrapper for backward compatibility.
    All command handling is done in brain.py
    """
    return brain_process(command)