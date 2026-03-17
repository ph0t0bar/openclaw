from PIL import Image, ImageDraw
import math

# Create animated GIF for checkmark draw (first drop email)
# Apple-style smooth stroke animation

frames = []
size = 120
padding = 10
duration = 45  # frames

for i in range(duration):
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    center = size // 2
    radius = (size - padding * 2) // 2
    
    # Background circle (subtle)
    draw.ellipse([padding, padding, size-padding, size-padding], 
                 outline=(45, 42, 38, 30), width=2)
    
    # Animation progress
    progress = i / duration
    
    # Circle draw animation (first 40% of frames)
    if progress < 0.4:
        circle_progress = progress / 0.4
        # Ease out
        eased = 1 - math.pow(1 - circle_progress, 3)
        arc_length = int(360 * eased)
        
        # Draw partial arc
        for angle in range(0, arc_length, 2):
            rad = math.radians(angle - 90)
            x = center + radius * math.cos(rad)
            y = center + radius * math.sin(rad)
            draw.ellipse([x-1, y-1, x+1, y+1], fill=(250, 254, 250, 255))
    else:
        # Full circle
        draw.ellipse([padding, padding, size-padding, size-padding], 
                     outline=(250, 254, 250, 255), width=2)
    
    # Checkmark draw animation (starts at 50%)
    if progress > 0.5:
        check_progress = (progress - 0.5) / 0.5
        eased = 1 - math.pow(1 - check_progress, 2)
        
        # Checkmark points
        p1 = (center - 20, center + 5)
        p2 = (center - 8, center + 18)
        p3 = (center + 22, center - 18)
        
        # Draw checkmark segments
        if eased < 0.5:
            # First segment (p1 to p2)
            seg_progress = eased * 2
            x = p1[0] + (p2[0] - p1[0]) * seg_progress
            y = p1[1] + (p2[1] - p1[1]) * seg_progress
            draw.line([p1, (x, y)], fill=(250, 254, 250, 255), width=3)
        else:
            # Full first segment + partial second
            draw.line([p1, p2], fill=(250, 254, 250, 255), width=3)
            seg_progress = (eased - 0.5) * 2
            x = p2[0] + (p3[0] - p2[0]) * seg_progress
            y = p2[1] + (p3[1] - p2[1]) * seg_progress
            draw.line([p2, (x, y)], fill=(250, 254, 250, 255), width=3)
    
    frames.append(img)

# Save
frames[0].save(
    '/root/.openclaw/workspace/templates/user-facing/checkmark-draw.gif',
    save_all=True,
    append_images=frames[1:],
    duration=33,
    loop=0,
    optimize=True
)

print("Created: checkmark-draw.gif")
