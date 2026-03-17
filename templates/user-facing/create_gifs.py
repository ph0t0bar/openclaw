from PIL import Image, ImageDraw
import math

# Create animated GIF for progress bar (welcome email)
# Apple-style smooth animation with your colors

frames = []
width, height = 160, 6
duration = 40  # 40 frames for ~1.3s loop

for i in range(duration):
    # Create frame with white background (transparent in email)
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Background track - subtle gray
    draw.rounded_rectangle([0, 0, width, height], radius=3, fill=(45, 42, 38, 25))
    
    # Animated progress indicator
    # Apple-style: smooth ease-out motion
    progress = i / duration
    # Ease-out cubic
    eased = 1 - math.pow(1 - progress, 3)
    
    bar_width = 48
    max_x = width - bar_width
    x = int(eased * max_x)
    
    # Your warm color palette - cycling through
    colors = [
        (224, 167, 148),   # #e0a794 terracotta
        (196, 164, 132),   # #C4A484 caramel  
        (249, 216, 204),   # #f9d8cc peach
        (253, 233, 224),   # #fde9e0 blush
    ]
    color_idx = (i // 10) % len(colors)
    bar_color = colors[color_idx]
    
    # Draw progress bar with rounded ends (Apple style)
    draw.rounded_rectangle([x, 0, x + bar_width, height], radius=3, fill=bar_color)
    
    frames.append(img)

# Save as GIF
frames[0].save(
    '/root/.openclaw/workspace/templates/user-facing/progress-bar.gif',
    save_all=True,
    append_images=frames[1:],
    duration=33,  # ~30fps
    loop=0,
    optimize=True
)

print("Created: progress-bar.gif")
