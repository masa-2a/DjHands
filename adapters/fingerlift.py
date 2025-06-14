
# Usage: returns whether that finger is pointed up or not (true or false)
# landmarks -> list of all finger landmarks from mediapipes handlandmarker
# tip_index, mcp_index -> index in landmarks list
# threshold -> room for error for the areas where they are equal
def is_finger_lifted(tip_y: int, mcp_y:int, threshold: float = 0.0) -> bool:
     return tip_y < mcp_y