import settings

def frame_height(percentage):
    return (settings.HEIGHT * percentage / 100)

def frame_width(percentage):
    return (settings.WIDTH * percentage / 100)